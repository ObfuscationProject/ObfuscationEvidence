# Workstation implementation status

M0-M12 remains incomplete. Accepted source, candidate implementations, model tests,
native QEMU evidence and deferred physical/manual gates are recorded separately.
Prior status is retained in `status-history/pre-directory-promotion-v1/`.

## Accepted integration

`prototypes/native-signal-actions-sdk29-v1/working` contains Kernel869 / OS475,
SDK30. The dirty top-level repositories remain preserved. Required predecessor:
`prototypes/native-journalled-directory-mode-integration-v1/promotion-v1.json`,
SHA256 `0dea0d2569f373283b7baa3fdf480b1407b07d4bbcdaf121f6340eb022f625de`.
Its `after` inventories define the accepted source. The complete867/456 previous
source is backed up. Source inventories were reverified after promotion.

Ten Kernel profiles remain: x86_64, i386, aarch64, arm32, rv64, rv32, loongarch64,
mips, mips64 and ppc. The distribution userland matrix remains x86_64, aarch64,
rv64 and loongarch64; qualification fixtures do not expand distribution support.
Production caught signals remain disabled.

## Accepted bounded storage qualification

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

## Active child-exit signals implementation

The design for automatic SIGCHLD and deferred autoreap is sealed, including18
host policy cases and all-ten external musl layouts. One selected Linux6.13.4
x86_64 QEMU boot confirmed three leader-first cases: notification retains leader
status17 while wait reports final group status23 or SIGTERM15. The newer WSL2
host differs; binary provenance and cross-architecture Linux behavior are not
implied. These reference runs are not Obfuscation execution.

The next private candidate adds a trusted typed child payload and a shared
128-byte siginfo encoder, with SDK31 migration and independent codec review.
Follow-on work adds actual notification, creator-parent thread lineage and
non-erasing detach before safe-boundary autoreap. No child-exit implementation is
yet promoted. CPU-time accounting and broader production integration remain open.

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
