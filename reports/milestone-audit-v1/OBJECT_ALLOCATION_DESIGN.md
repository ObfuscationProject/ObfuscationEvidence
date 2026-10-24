# Next M1 mechanism: page-backed fallible Kernel objects

Status: bounded implementation proposal after the wait-registration slice.
No allocator implementation or execution is claimed by this document.

Implement a real typed object pool whose storage comes from the authoritative
native physical-page owner, and migrate actual pending poll/select objects to
it. This makes the first heap consumer execute during ordinary user syscalls,
exposes allocation/refund failures at a useful boundary, and provides stable
object locations for later wait queues/threads. It must not be another model
slab over an unrelated static byte array.

## Observed source and remaining gap

Exact inspected inputs are hashed in `object-allocation-source-pins.json`.
These anchors refer to shared SDK20-era source, not the moving wait prototype.

| Source | Current mechanism and implication |
| --- | --- |
| `ObfuscationKernel/docs/DEVELOPMENT.md:28` | Kernel-owned fallible object allocation is already permitted. No new approval or implicit hosted heap is needed. |
| `ObfuscationKernel/include/ok/driver/abi.hpp:226` and `src/driver/abi.cpp:284` | Existing `OkSlabAllocator` is sixteen fixed 256-byte slots. It does not consume production frames, enforce typed construction or prove caller lifetimes. Preserve its existing model tests. |
| `ObfuscationKernel/include/ok/memory/memory.hpp:124` and `src/memory/memory.cpp:149` | `FrameAllocator` owns physical index/address/generation and returns `Result<PhysicalFrame>`. It is bounded and serialized; backing is not automatically a C++ virtual address. |
| `ObfuscationKernel/include/ok/user/native_page_pool.hpp:10` | `NativePagePool` owns exact physical handles, retirement pins and deferred release. It is the currently authoritative registry for actual native pages. It currently conflates all allocations with user page accounting. |
| `ObfuscationKernel/include/ok/boot/qemu_process_memory.hpp:6` | Current source selects seven firmware-qualified process-pool profiles (including ARM32) and three explicit linker fallbacks. Historical six/four evidence must not be relabeled. |
| `ObfuscationKernel/include/ok/boot/qemu_runtime_frames.hpp:11` | Qualified memory is constrained to established supervisor apertures, with different x86/ARM/PPC bounds. Object storage cannot bypass this by reinterpreting arbitrary physical frame numbers. |
| `ObfuscationKernel/src/user/runtime.cpp:43,212,281,1631` | Native pool activates only after hardware backend initialization; existing user backing is zeroed before mapping. Put object-pool activation after this handoff, never in early model `MemoryManager` initialization. |
| `ObfuscationKernel/src/user/runtime.cpp:70,86,88,1447` | `PollWait` objects occupy a fixed global array and are selected/scanned by PID. They already own copied arguments and descriptor pins; they are a concrete first object consumer. |
| `ObfuscationKernel/include/ok/core/fixed.hpp:144` | `StaticVector::erase_at` moves later entries. General PCB/TCB allocation needs a larger stable-reference redesign; avoid changing it in this first object-pool slice. |

## Proposed implementation ownership and files

1. `include/ok/memory/object_pool.hpp`: constrained typed page-backed pool with
   opaque generation handles; static dispatch to a page-storage provider.
2. `include/ok/user/native_page_pool.hpp`: introduce explicit user/object page
   purposes and kernel-page leases without permitting metadata pages to enter a
   user mapping. Existing user allocation methods remain checked wrappers.
3. `src/user/runtime.cpp`: instantiate `ObjectPool<PollWait, Provider, Limit>`,
   replace the fixed PollWait array with a bounded stable handle index, and
   allocate/release through real begin/cancel/finish readiness paths.
4. Tests remain split into hosted allocator faults, target Kernel object checks,
   and OS-owned user poll/select/pressure execution through a fresh SDK.

The hot allocator algorithm uses templates/concepts. A slab page is one current
4096-byte backing page. `T` must fit one page with alignment no greater than the
page size and be nothrow constructible/destructible. Oversized/overaligned types
are rejected by constraints; multi-page allocations are a later capability.
Use explicit in-place object lifetime (`std::construct_at`/`destroy_at` or an
already-qualified placement facility), with no global `operator new`, implicit
allocation, exception or hosted runtime dependency. Verify emitted imports on
all ten compilers before accepting the construction mechanism.

## Interface and state

```cpp
struct ObjectHandle {
    const void *pool; // Kernel-internal identity, never a userspace record
    u32 page_slot;
    u32 object_slot;
    u64 generation;
};
struct ObjectLimits { usize max_objects; usize max_backing_pages; };

template<class P>
concept ObjectPageProvider = requires(P provider, typename P::Lease lease) {
    { provider.allocate_kernel_page() }; // Result<Lease>, mapped byte span
    { provider.release_kernel_page(lease) }; // Status; exact opaque ownership
};

template<class T, ObjectPageProvider P, usize MaximumPages>
class ObjectPool {
    Result<ObjectHandle> create(/* bounded nothrow constructor arguments */);
    Result<T *> resolve(ObjectHandle); // borrow within serialized operation
    Status destroy(ObjectHandle);     // caller has drained external references
    Status trim_empty_pages();        // no implicit I/O or reclaim recursion
    ObjectAccounting accounting() const;
};
```

The pool owns the page lease and slot table, not the object consumer. A pool-wide
monotonic generation prevents ABA when an empty slab is returned and reacquired;
per-slab generation initialized from zero would be unsafe. Foreign-pool handles
must also fail: either include an opaque pool identity in the typed handle or
require an opaque owner reference in every resolve/destroy operation. A naked
`{slot,generation}` that happens to match another pool is insufficient.

State path: `unbacked -> backing-acquired -> initialized-empty -> occupied ->
initialized-empty -> released`. New page/slot publication is last, after checked
layout, page acquisition, zeroing and object construction. Every pre-publication
failure returns the page or retains an explicitly quarantined lease if its
release fails. Occupied objects never move. Destroy validates owner/slot/
generation before touching bytes and calls the destructor exactly once after
the caller has drained timers/descriptors/other references. Record all counters
before/after faults; a failed release cannot increment free-page accounting.

Do not perform synchronization by storing another boolean. This first pool is
serialized on the boot CPU and rejects IRQ/secondary-CPU callers by contract.
Add IRQ-safe allocation contexts, per-CPU caches and SMP locks only with their
separate saved-IRQ-state/lifetime qualification.

## Physical ownership, mapping and limits

Do not create a second `FrameAllocator` over the same managed ranges, and do not
call `FrameAllocator::allocate` directly behind `NativePagePool`'s ownership
registry. Extend one authoritative page registry with a purpose tag and opaque
kernel lease carrying the retained allocator/index/generation. User releases,
quarantine pins and `owns_pool_page` must reject a kernel-object lease. Before
building any native page table, validate that every user frame has the user
purpose; object page addresses must never be accepted merely because a physical
address is in the global pool.

Use only already-qualified supervisor-accessible backing. Keep the existing
MIPS address translation contract; never assume `PhysicalFrame.address` is a
portable dereferenceable pointer outside this provider. Object metadata and
backing must remain outside user-accessible PTEs on all retained profiles.

Set explicit separate counts for user pages, kernel-object pages, retained pins,
quarantine and free pages; their sum must equal physical ownership accounting.
Current `used_count()` derives from total frame use, so it cannot silently remain
labeled user-only after this change. Update diagnostic/parser semantics and exact
receipt version together.

Reserve enough pages for the declared bounded active wait capacity, derived from
`sizeof(PollWait)`, alignment and per-page slot overhead. Prevent ordinary user
mmap/brk from consuming that reserve. Declare the resulting user quota explicitly
instead of pretending the old 1024-page capacity is unchanged. Empty slabs may
return to the object reserve. Ordinary pool failure returns ENOMEM before wait
publication; cleanup must allocate nothing. No cache reclaim, global OOM killer
or general heap claim is included in this slice.

## Concrete first consumer transaction

`begin_readiness_wait` first admits an object under the process wait limit, then
copies the frozen request, retains descriptions, arms the deadline and registers
the scheduler ticket. If any stage fails, unwind retained descriptions and the
object lease exactly once, preserving the primary syscall error. Do not publish
a pointer to a partly initialized wait.

Keep an owner/thread-to-object-handle index for bounded lookup. That index is
metadata only; the actual `PollWait` bytes must reside in allocated slab pages.
Readiness scanning may iterate stable handles. Cancel/timeout/exit removes the
index entry and source membership before destroying the object. Capture the
next handle before a callback can reclaim the current slab, or collect completed
handles and destroy them after the scan. Never keep an unpinned raw pointer after
releasing the object. The generation-safe wait ticket and object handle protect
different lifetimes and both must be validated.

## Acceptance that proves a mechanism

- Hosted real allocator code with an aligned page provider: layout/alignment,
  zeroing, exact object construction/destruction counts, wrong/foreign/stale
  handles, max generation, live-limit/page-limit failure, backing exhaustion,
  rollback and page-return/quarantine failure; reuse the actual object type.
- Existing native page pool/VM rollback tests plus purpose separation: user
  map/release/pin paths reject object pages; object release rejects user leases;
  no live user page and slab share a frame. Preserve prior mapping quarantine.
- All-ten freestanding C++23/xmake builds: no accidental hosted allocation or
  runtime imports. Debug Kernel checks write/read aligned objects in actual
  provider-backed pages after hardware initialization and return them.
- OS native/musl guests issue real poll/select waits through the allocated
  records; verify descriptor/timeout outputs, cancellation/exit, pressure ENOMEM
  without leaks, later successful reuse, and pending child wakeup when ordinary
  user allocation reaches its declared quota. Record allocator page/object
  counts with command/source/SDK identities.
- In a separate privileged target fixture, inspect the active user mappings and
  assert object backing is supervisor-only. Where the backend has no direct PTE
  walker, use its real user-range check plus a child attempted load from the
  corresponding protected mapping, with architecture address rules explicit.
  Do not turn a metadata list assertion into a universal isolation claim.
- Exact fresh Kernel producer/SDK-only OS consumer and all-ten Debug/Release
  regressions; preserve separate model, privileged Kernel, actual user and
  physical/SMP scopes. No physical or SMP claim is expected here.

This is a first real object allocator and consumer, not completion of M1.
Runtime-sized VM/process metadata, general typed allocations, quotas/reclaim,
shared/file mappings, full address-space references and remote TLB retirement
follow. Once proven, migrate stable open descriptions and thread/process objects
one owner at a time rather than rewriting every fixed array at once.
