# Workstation implementation status

M0-M12 remains incomplete. Source implementation, hosted controls, native QEMU
execution and deferred physical/manual gates remain separate. Previous status
is preserved in `status-history/pre-sdk31-codec-promotion-v1/`.

## Accepted private integration

`prototypes/native-signal-actions-sdk29-v1/working` contains Kernel875 / OS477,
SDK31. Dirty top-level repositories are preserved. Required next predecessor is
`prototypes/native-child-siginfo-codec-integration-v1/promotion-v1.json`, SHA256
`e9a57bbf29c0c79e2c0601a34cf949c4eb69803d6b30b66b5893da11783a1ac7`. Complete869/475 backups and post-promotion source checks passed.

Typed trusted child-exit payloads and common128-byte target siginfo encoding are
implemented across nine frame policies/ten Kernel profiles. SDK31 is mandatory
for the changed public layout. The OS rejects older ABI artifacts and checks
exact architecture, mode, compiler and hashes. Shared collector checks preserve
continuous inherited wait ownership across image transitions.

Fresh evidence includes20 Debug/Release SDK rows, ten private standalone boots,
one ordinary SDK build/boot, five distro links/ten boots,22 inherited native
signal qualifiers/44 commands, and separate hosted/layout/independent controls.
All22 native receipts replay through the final strict OS477V4 collectors. The
ordinary distro exercises the existing prelinked GUI, not an isolated desktop.

Ten Kernel profiles remain x86_64, i386, aarch64, arm32, rv64, rv32, loongarch64,
mips, mips64 and ppc. Distribution userland stays x86_64, aarch64, rv64 and
loongarch64. Qualification fixtures do not expand that distribution matrix.
Production caught signals remain disabled.

## Active child-exit lifecycle implementation

Automatic SIGCHLD and deferred autoreap follow the accepted codec prerequisite.
The active private candidate adds creator/replacement thread lineage, saved
leader notification cause, cleanup-gated completion and checked safe-boundary
reaping. It is not yet accepted or natively qualified. CPU-time accounting and
broader production signal support remain open.

Two selected Linux6.13.4 x86 boots cover21 reference cases, including18 policy
cases and three leader-first cases. Notification retains leader17 while wait
reports final group23 or SIGTERM15. Newer host behavior differs; binary/source
provenance and cross-architecture Linux equivalence are not established. These
external observations are not Obfuscation execution.

## Inherited bounded storage qualification (SDK30)

Credential-aware journalled chmod covers regular files and allocated ordinary
directories on an explicit maintained-noatime side mount. Retained readable
directory handles remain enumerable after chmod0000; fresh open, path search and
fchdir check current permissions. Namespace, allocations, payload and unrelated
metadata remain unchanged. Reserved inodes/root and symlinks are unsupported;
maintenance-only update remains regular-file-only.

- Twenty fresh architecture/mode SDK builds and ten private standalone boots pass.
- Thirty native directory scenarios pass373,338 public checks,120 mutations,
  1,320 writes and1,140 FLUSH. Thirty independent Linux readonly checks pass.
- Sixty completion-boundary cuts on x86_64/i386/MIPS pass, followed by120 native
  recovery/clean boots (507,960 public checks) and60 independent Linux recoveries.
- Five ordinary distro links/ten boots plus the ordinary signals-off x86 Debug
  SDK boot pass. These exercise the existing prelinked GUI and nonjournalled root.
- Final Kernel hosted/sanitizer/inherited checks, independent source review,
  2,675 collector controls and independent normal native/Linux replay pass.
  Root replayed the complete recovery evidence separately.

All32 changed/new paths were promoted. Kernel candidates1..3 exposed an inherited
cache-generation regression; final v4 avoids the redundant pre-prepare read.
Earlier successes on defective candidates remain diagnostic only. Initial archive
naming, partial image preparation and empty-directory promotion refusal remain
retained with their successful successors.

Three historical MIPS regular-file recovery FLUSH timeouts remain unresolved.
A12-second host fdatasync delay reproduced a timeout, but no production transport
fix or historical cause is claimed. This successful directory campaign does not
close that issue. Whole-completion cuts do not cover torn writes, reordering,
volatile cache or physical power loss. A clean-image FLUSH can complete without
a host sync call. Default journalled root and full M4 remain open.

## Milestone gates

| Milestone | Status | Main remaining gate |
| --- | --- | --- |
| M0 contracts | Open | Complete normative requirements, utilities, options and qualification inventories |
| M1 resources | Open | General resource policy, mapping/lifetime breadth and pressure qualification |
| M2 common objects | Open | Complete paths/credentials, descriptor IPC, TTY/PTY and concurrent lifetimes |
| M3 libc substrate | Active | Remaining signals/thread/ABI semantics, production integration and all-ten musl acceptance |
| M4 durable root | Active | Broader journalled mutation, default root, transport reliability and durability profile |
| M5 POSIX userland | Open | Shared musl/loader, mappings/cache, job control, cancellation and mandatory semantics |
| M6 networking | Open | NIC-to-user sockets, IPv4/IPv6 interoperability, robust transports, DNS and TLS clients |
| M7 services | Open | Persistent supervision, accounts/sessions, service recovery and consistent shutdown |
| M8 graphics | Open | Isolated compositor/clients, shared buffers, seat/input ownership, fonts/toolkit and terminal |
| M9 desktop | Open | Persistent application workflows, installer/recovery and accessibility |
| M10 ext4 breadth | Open | Advertised advanced features/combinations with independent round trips |
| M11 execution breadth | Open; physical acceptance deferred | SMP, module execution/unload, IRQ/DMA/hotplug and reference machines |
| M12 release | Open; manual acceptance deferred | Mandatory gaps, reproducible artifacts, automated workflows and retained human checks |

The user deferred physical acceptance and human desktop workflows. Continue
implementation and automation without requesting those resources again.

## Automatic child-exit lifecycle candidate (unpromoted)

Accepted source remains Kernel875 / OS477, SDK31, at the predecessor above.
The user deferred M11 physical and M12 human desktop acceptance; do not ask
again. Continue implementation and automated qualification.

- Kernel885V2: `native-child-exit-runtime-v1/candidate-v2/ObfuscationKernel`,
  inventory `51f291480cb89d19e359de55ca377bf2902cad239f4dde16ab92e98b89a17f8e`.
  Author handoff `73fe37968d5295052872e67cfccd8855bbd7fe3e3d32713d2e87d870d35f8b29`.
  Automatic SIGCHLD policy, saved leader cause, creator/replacement lineage,
  checked deferred reaping and failure barriers. ABI stays31; production signal
  flags remain off. Administrative infrastructure kills are outside this scope.
- Author14,090 hosted lifecycle,364 actual-runtime-with-mock-backends and3,511
  inherited checks passed; independent57 helper checks. These are not native
  execution. All76 existing public layout values match across ten toolchains.
- `native-child-exit-runtime-build-v1/matrix-v1/result.json`: all20 fresh
  Debug/Release SDK rows passed; ten private standalone Debug boots. Root
  session78640 completed and polled. Ordinary signals-off x86 Debug build/boot
  at `native-child-exit-runtime-distro-v1/sdk-x86-debug-v1` also passed.
- Guest implements18 isolated policy/coalescing/kill/fork/exec cases,40 process
  completions and12 exact128-byte siginfo records per command. OS487V1 first
  x86 execution ran both commands but failed its incorrect minimum41 lease
  assertion. Actual live-leader exec reuses its canonical lease, proven by
  runtime.cpp and native_entry_stacks.hpp, so correct count is40. Original
  failed `native-x86-v1` receipt/serial is retained. Its executed=false field
  was pre-acceptance bookkeeping, not evidence of a preboot failure.
- Corrected OS487V4: `native-child-exit-integration-v1/candidate-os-v4/ObfuscationOS`,
  inventory `a31139021a43a72dfc32b26f4b49be2aa0d905576c0633519a9c5b231dca0d21`.
  Fifteen new hosted methods pass. V4 binds successful native WAITs to unique
  preceding owned completions, requires the exact shell-to-main blocking wait
  and rejects extra guest blocking waits (the pinned guest uses WNOHANG).
  It rejects captured faults and rejected entries. Qualifier receipts separate
  observed guest PASS markers from final native_execution_accepted.
- `replay-x86-v4.json`, SHA256
  `3cce7abda9ffe2c77a6f2d72b70e9f81cdb66053d4ab255ac2be0836bb25f1cf`:
  retained two real x86 commands pass V4; two balanced39-lease mutations fail.
  This is replay, not new execution. Earlier V1-V3 collector review false
  admissions remain at `native-child-exit-collector-review-v1`; V4 independent
  review is ongoing, so no promotion is authorized by these provisional runs.
- Root running sessions:90575 all-ten fresh policy matrix (`policy-matrix-v1`);
  32799 ordinary five-link/ten-boot distro matrix. At this checkpoint x86_64,
  i386, aarch64, arm32 policy rows passed. Check receipts/poll before proceeding;
  do not launch duplicates. Root sessions22830/45951 completed and were polled.
- Agent child_signal_codec_review owns independent new lineage/leader-first/
  real_blocked-vs-ppoll guest work at `native-child-exit-lineage-guest-v1`.
  Agent pipe_signal_guest owns separate legacy collector migration; inherited
  frame/wait/process/directed collectors need typed EXIT/REAP handling before
  regressions against this producer. Never skip unvalidated diagnostic lines.

No current candidate closes M0-M12, full signals/POSIX, networking, services,
desktop, SMP or physical qualification. Next promotion must still match
`native-child-siginfo-codec-integration-v1/promotion-v1.json`, SHA256
`e9a57bbf29c0c79e2c0601a34cf949c4eb69803d6b30b66b5893da11783a1ac7`.
