# Workstation implementation status

M0–M12 remains incomplete. Accepted source is separate from candidate code,
automated evidence, and deferred physical/manual gates. Historical checkpoints
are retained in `status-history/pre-native-recovery-v1/`.

## Accepted integration

`prototypes/native-signal-actions-sdk29-v1/working` contains Kernel867 / OS456,
SDK30. The dirty top-level repositories remain preserved. Required next
predecessor: `prototypes/native-journalled-mode-integration-v1/promotion-v1.json`, SHA256
`9de1d0be7ecd286e3e9d7a9cc9f213189395b4beaa96ca8440d0a79d8d74f7e0`.
The receipt's `after` inventories define the accepted source.

Accepted signal waits pass twenty SDK rows, twenty native commands across ten
profiles / 4,840 cases, and twenty-two inherited x86 commands / 2,824 cases.
Hosted runtime checks, codec models and parser controls are separate evidence.
Production signals remain disabled.

Ten Kernel profiles remain: x86_64, i386, aarch64, arm32, rv64, rv32, loongarch64,
mips, mips64 and ppc. The distribution userland matrix remains x86_64, aarch64,
rv64 and loongarch64; additional qualification fixtures do not expand support.

## Accepted journalled chmod slice

Kernel867 / SDK30 implements credential-aware regular-inode chmod on an explicit
maintained-noatime side mount. A public class layout change requires SDK30.
OS456 integrates strict SDK validation, normal/cut/recovery fixtures, disk oracles
and Linux tools. All 97 changed/new paths were promoted after exact qualification;
the prior Kernel865 / OS439 source is retained under the promotion backup.

- Twenty SDK30 architecture/mode builds and ten private Debug boots pass, plus
  one ordinary Debug SDK build/boot with private signal delivery disabled.
- SDK30 inherited x86 tests pass 22 commands / 2,824 cases; fresh all-ten signal
  waits pass 20 commands / 4,840 cases.
- Thirty native chmod scenarios across ten architectures pass 3,007 C checks,
  120 mutations, 1,320 writes and 1,140 flushes. Thirty independent Linux readonly
  mounts and e2fsck checks pass.
- Sixty software completion-boundary cuts on x86_64/i386/MIPS and sixty Linux
  recoveries pass. Three additional executions qualify the separately named cut
  tools while preserving the normal fixture unchanged.
- Sixty native recovery + clean-remount pairs pass (120 boots). Six serialized
  MIPS repeat boots and six boots starting from retained timeout disks also pass.
  Each accepted recovery/read probe performs 4,168 public checks.
- Five ordinary distro links and ten simplefs/ext4 boots pass across four Release
  profiles and x86 Debug. This exercises the existing prelinked GUI and default
  nonjournalled ext4 root; it is not an isolated desktop or journalled root.
- Exact OS449 tools pass 54 unittest suites / 533 methods plus 1,250 explicit
  raw-image model checks. Those449 files remain unchanged in456. New source
  additions are bound to their own native campaigns and independent review.
- Independent recovery collector review passes98 controls (97 reject,1 permitted
  unrelated line). The Linux comparator's length/head defects were closed with
  sixty retained-output replays and79 controls (76 reject,3 valid).

Retained failures include35 preboot image-lock refusals,3 actual MIPS recovery
flush timeouts,4 successful exploratory phases preceding failed pairs, and the
initial unittest discovery mistake. The timeout failures preceded mount/user
publication. Their exact disks recover and remount successfully, including two
clean-looking disks left after failed final flushes. The existing five-second
monotonic timeout mechanism's root cause remains unresolved; retries do not
establish concurrent transport stability.

Native recovery uses an exclusive bounded session and an explicit exported
recovery operation before mount/cache publication. `mount()` itself requires a
clean journal. Whole-completion cuts do not model volatile cache loss, torn writes,
reordering or physical power loss. Write CRC alone is not a unique fingerprint
for complete checksummed superblocks; exact final disks and pinned implementation
provide additional evidence. Hosted, native QEMU and physical results remain
separate. Default-root adoption, broader mutations and full M4 remain open.

## Active candidate: directory mode and retained enumeration

Ordinary-directory journalled chmod and retained readable directory enumeration
are implemented in isolated candidates. The inherited cache-generation regression
is repaired in Kernel869 candidate-v4; source review and all inherited gates pass.
Fresh20SDK builds,30native+30Linux scenarios and5distro links/10boots pass. All
previous defective-candidate guests remain diagnostic only. The exact full60cut,
120native-recovery/clean and60Linux recovery campaign is running. Accepted
Kernel867/OS456 remains unchanged until the final binding and guarded promotion.

A separate host-timing experiment reproduces the existing MIPS timeout with a
12-second delayed host fdatasync; historical cause remains unresolved. A successful
FLUSH from fresh QEMU can occur without a host sync call. Existing software-cut
claims are limited to the guest block interface and complete file bytes.

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
