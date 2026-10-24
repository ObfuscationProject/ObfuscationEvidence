# Generation-safe wait ownership: bounded implementation design

Status: proposed integration design, not an exported API or completed M1.
Owner: ObfuscationKernel. OS owns real user probes and SDK-only consumer fixtures.

The existing runtime stores `PollWait` by PID, scans readiness on each main-loop
step, and separately completes `DeadlineWait`. Scheduler pipe/child/console
waits use reason/key scans. `block_current` and the native runtime still primarily
select the first thread. A slot/key describes where to look; it does not prove
that an asynchronous completion belongs to the current registration. This is the
small cross-cutting foundation to implement before native threads and device
callbacks expand the possible interleavings.

## Deliverable and boundary

The first deliverable provides one exactly-once, generation-safe wait owner,
then integrates current pipe/child/console/sleep/poll/select registrations into
it. Preserve copied request data, retained open-description references, absolute
monotonic deadlines and existing result encoding. Registration and completion
remain serialized on the boot CPU until a real IRQ/SMP locking adapter passes
its separate acceptance. Existing loop scanning may remain as the bounded
notification producer; this change does not promise an interrupt-driven idle
scheduler or elimination of polling.

Do not move OS policy into Kernel. Do not add virtual interfaces for wait state
transitions. New exported ThreadControlBlock/SDK structures require a new exact
SDK generation; do not reuse the frozen SDK21 identity.

## Small primitive to implement first

```cpp
enum class WaitCompletion : u8 { none, ready, timeout, cancelled };
struct WaitTicket { u64 owner, thread, generation; };
class WaitRegistration {
  Result<WaitTicket> arm(u64 owner, u64 thread);
  bool pending(WaitTicket) const;
  bool complete(WaitTicket, WaitCompletion);
  bool cancel();
  WaitTicket ticket() const;
  bool active() const;
  WaitCompletion completion() const;
};
```

Each long-lived record owns its monotonic generation. Arm rejects zero identity,
an already-active record and generation exhaustion before changing state.
Completion requires the exact owner/thread/generation triple and a terminal
reason; only its first caller succeeds. Cancel transitions the active record to
cancelled; repeating cancellation is harmless. A completed ticket remains
inspectable; the next successful arm increments generation and resets completion
to none. Generation never wraps. This primitive owns no raw pointer or resource,
executes no callback, copies no user bytes and supplies no memory ordering. It
is valid only inside the caller's documented synchronization domain.

Exclusive relocation may preserve the sole authoritative record and its ticket.
The primitive must not be duplicated into a second authoritative owner or
reconstructed/reset while external tickets may still exist. Scheduler process/thread identities must not repeat within that lifetime;
otherwise a separate record/incarnation generation is required. Teardown must
cancel/drain all callbacks before destroying the record. A pair of separate
records with the same identities is not made unique by local generation alone;
the scheduler owns the one authoritative record for each live thread.

## Integration shape

- Scheduler resolves `(pid, tid)` on each operation rather than retaining a raw
  TCB pointer across process-array compaction. `register_current_wait` associates
  reason/key and the exact ticket; `complete_wait` verifies the ticket before
  changing runnable state. Existing `wake_waiters` is a producer of current
  matching tickets, never an authority to complete a future registration.
- Sleep and poll keep the scheduler ticket alongside their current copied
  request and deadline record. Every ready/timeout/exit path claims the same
  registration. A stale timer or description event cannot wake a new wait after
  cancellation/rearm. A timer scan is permitted; stale scan results must fail.
- Existing pipe/read/write dispatch may retain its bounded continuation/retry
  contract initially. General blocking must later retain typed operation state
  rather than re-running arbitrary user requests. Do not silently claim that
  the primitive converts existing retry paths into full continuation semantics.
- Exit/exec cancels the registration, removes source/timer membership, releases
  each retained pin exactly once, then reclaims process state. A canceled exit
  path never copies results to user memory. Completed ordinary calls revalidate
  their output address space and copy only after leaving internal locks.

## Registration, source ownership and synchronization follow-up

For general event queues, preflight stable wait slots and source memberships
before publishing anything. Use generation-bearing source identities for
open descriptions/pipes/devices, not bare FD numbers. Record source readiness
sequence and subscribe/recheck its predicate inside the same source lock.
Condition mutation publishes the new sequence and wake claim under that lock;
this closes the check-before-park window. A completion occurring before `park`
causes park to return already-completed rather than overwrite the terminal state.

Define a single acquisition order before adding multiple locks: source/object
lock, wait-state lock, then runnable publication; move callbacks/copyout outside
all of them. The exact order must match the scheduler's eventual runqueue design,
so no existing locks may be acquired backwards. A multi-source poll must either
use a stable sorted source order or staged per-source membership with complete
unwind, plus one completion owner. Memory allocation, I/O, user copies and
sleeping while holding an IRQ-safe spinlock are prohibited.

The current architecture facade has enable/disable interrupt calls, while its
SpinLock does not preserve IRQ state. Adding IRQ producers therefore requires a
separate architecture-selected save-disable-restore contract, with nested IRQ
state tests on all ten retained profiles. Acquire/release atomics or hosted
thread tests alone do not establish real SMP safety. Secondary CPUs remain
outside this first integration's contract.

## Acceptance and failure tests

1. Primitive hosted tests: valid arm, exact identity, zero identity, duplicate
   arm, stale owner/thread/generation, duplicate completion, cancel/rearm,
   cancel-inactive, invalid completion kind and generation exhaustion. Verify
   every refusal leaves ticket/state/outcome unchanged. Run ASan/UBSan and ten
   freestanding C++23 target builds through xmake; these are model/build evidence.
2. Scheduler hosted tests: multiple modeled threads, current-thread identity,
   ready-vs-timeout/exit winner, cancellation before park, registration reuse,
   wrong process/thread, child/pipe reason isolation and independent waits.
   Model interleavings are not native thread execution.
3. Kernel debug checks execute the primitive on boot to ensure target compiler
   behavior. Label them kernel checks; they do not execute user-mode waits.
4. Native user tests: parent blocks in pipe read while child writes/exits; poll
   holds descriptions across duplicate/close/reuse; real sleep timeout and
   poll/select timeout complete once; zero/infinite timeouts preserve behavior;
   realtime change leaves monotonic deadline unchanged. Preserve existing actual
   native/musl tests and add stale-ticket diagnostics only through a bounded
   privileged fixture, without an unsafe public test syscall.
5. Every changed final source requires standalone Kernel, fresh exact SDK export,
   SDK-only OS consumer, all-ten Debug/Release native/musl regressions and retained
   commands/artifact identities. No frozen live qualification source is edited.

The successful result is an executed wait ownership foundation. Full signals,
futexes, pthreads, IRQ workers, native SMP and physical platforms require their
own code and evidence. M1 and M3 remain incomplete after this bounded delivery.
