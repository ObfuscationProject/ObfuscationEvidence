# Workstation implementation status

M0–M12 remains incomplete. Accepted source is separate from candidate code,
automated evidence, and deferred physical/manual gates. Historical checkpoints
are retained in `status-history/pre-native-recovery-v1/`.

## Accepted integration

`prototypes/native-signal-actions-sdk29-v1/working` contains Kernel865 / OS439,
SDK29. The dirty top-level repositories remain preserved. Required next
predecessor: `prototypes/native-signal-wait-merge-v1/promotion-v1.json`, SHA256
`a19d5a4d351f9b5f17a9e4f91af51e1aaa6a2a3240b5029a2d52fae6e3f0dc65`.
The receipt's `after` inventories define the accepted source.

Accepted signal waits pass twenty SDK rows, twenty native commands across ten
profiles / 4,840 cases, and twenty-two inherited x86 commands / 2,824 cases.
Hosted runtime checks, codec models and parser controls are separate evidence.
Production signals remain disabled.

Ten Kernel profiles remain: x86_64, i386, aarch64, arm32, rv64, rv32, loongarch64,
mips, mips64 and ppc. The distribution userland matrix remains x86_64, aarch64,
rv64 and loongarch64; additional qualification fixtures do not expand support.

## Active journalled chmod slice

Frozen Kernel867 / SDK30 implements credential-aware regular-inode chmod on an
explicit maintained-noatime side mount. A public class layout change requires
SDK30. Frozen OS449 combines strict SDK30 migration, existing waits, new guests,
disk oracles and Linux tools. Neither candidate has been promoted.

- All twenty SDK30 architecture/mode builds and ten private Debug boots pass.
- SDK30 inherited x86 tests pass 22 commands / 2,824 cases; fresh all-ten signal
  waits pass 20 commands / 4,840 cases.
- Thirty native chmod scenarios across ten architectures pass 3,007 C checks,
  120 mutations, 1,320 writes and 1,140 flushes. Thirty independent Linux
  readonly mounts and e2fsck checks pass.
- Sixty software completion-boundary cuts pass on x86_64, i386 and MIPS.
  Sixty independent Linux recoveries retain old inodes for cuts 1–10 and recover
  new inodes for cuts 11–20. Complete disk, size, head and checksum checks pass.
- Exact OS449 passes 54 unittest suites / 533 methods and a separately invoked
  raw-image model / 1,250 checks. The initial mistake of including that standalone
  model in unittest discovery (zero tests, exit 5) is preserved and reconciled.
- Normal guest, recovery and tool bindings have passed read-only replay in
  `prototypes/native-journalled-mode-integration-v1/`.

Native ObfuscationOS second-boot recovery and another clean remount are being
implemented on cloned cut disks. An exclusively owned exported recovery call
precedes mount publication; `mount()` does not itself recover a dirty journal.
Independent review has closed both Linux comparator findings (length and head)
with sixty retained-output replays and 79 controls; final sealing is in progress.

Whole-completion cuts do not model volatile cache loss, torn writes, reordering
or physical power loss. Hosted models, QEMU execution and physical evidence remain
separate. Default-root adoption and broader filesystem operations remain open.

## Milestone gates

| Milestone | Status | Main remaining gate |
| --- | --- | --- |
| M0 contracts | Open | Complete normative requirements, utilities, options and qualification inventories |
| M1 resources | Open | General resource policy, mapping/lifetime breadth and pressure qualification |
| M2 common objects | Open | Complete paths/credentials, descriptor IPC, TTY/PTY and concurrent lifetimes |
| M3 libc substrate | Active | Remaining signals/thread/ABI semantics, production integration and all-ten musl acceptance |
| M4 durable root | Active | Native public-path recovery, broader journalled mutation, default root and durability profile |
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
