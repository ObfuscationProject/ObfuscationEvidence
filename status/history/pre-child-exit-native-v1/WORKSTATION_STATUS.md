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
