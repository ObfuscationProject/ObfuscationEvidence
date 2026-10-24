# M0-M12 coverage audit

Audit timestamp: 2026-09-23T09:26:54.384673+00:00

All thirteen milestone completion gates remain open. SDK20 provides substantial executed filesystem, ABI, memory and clock subsets, but the full target requires missing resource/thread/signal/IPC/durability/network/service/desktop/SMP mechanisms. Repeating metadata adapters alone cannot close the dependency graph. This audit performs no builds or guest execution and does not promote any requirement.

## Evidence boundary

The current shared ledger is `2026-09-21.23` / `seed-inventory`: 90 requirements, 163 tests, zero attached execution receipts; its four normative inventories are partial. State counts are {'planned': 33, 'native-partial': 50, 'implemented': 1, 'model-only': 6}. These counts are not a completion percentage.

The shared progress document reports delivered SDK/module20, native UAPI0.6.0. It records all-ten Debug/Release execution for bounded slices and separate hosted/Linux references. This audit inspected concrete source and selected top-level evidence status, but did not recursively rehash or rerun that qualification. The selected SDK20 six-layout receipt explicitly says privileged device execution, not user execution. The two Linux reference boots do not establish physical hardware, SMP or complete Linux build provenance.

SDK21 candidate V2 currently records **failed**; its retained command file has 351 command records. A failed candidate is not shared delivery. The chmod archive states it is unexported and has no actual chmod user execution. Root integration may continue after this audit snapshot; new evidence must remain separately identified.

`gate-mapping.json` contains exact plan exit text, individual missing clauses, source paths/lines/hashes, selected evidence hashes and ledger requirement IDs. `source-ledger.json`, `source-progress.md` and `plan-README.md` retain the audited inputs. Source references identify observed implementation, not proof of every claimed runtime behavior.

## Milestone findings

### M0: Specification baseline

Plan exit gate: Every requirement has owner, semantics source, dependencies and a planned test; ten ABI profiles have explicit qualification gaps

Versioned seed ledger, validation tooling, ten ABI tuples and explicit SDK identity validation exist. Four normative inventories are partial; the source ledger attaches zero execution receipts.

- **M0.exit.1 — partial**: Every requirement has an owner and semantics source. Expand seed requirements to every Issue 8 clause/interface/utility/option, selected RFC MUST/SHOULD, exact ext4 format feature and permitted combination; preserve authoritative versions and ownership.
- **M0.exit.2 — partial**: Every requirement has dependencies and a planned acceptance test. Create the missing normative rows and tests; mapping a subsystem summary to one test does not cover its constituent requirements.
- **M0.exit.3 — partial**: Ten ABI profiles have explicit qualification gaps. Complete per-profile syscall/errno/flag/ELF/TLS/signal/struct inventories and authenticated source pin provenance. Existing bootstrap tuple tables remain valid subsets.

Source anchors: `ObfuscationOS/docs/plans/README.md:192`, `ObfuscationOS/docs/plans/contracts/ledger.json:1`, `ObfuscationOS/tools/plan_ledger.py:305`, `ObfuscationOS/tools/kernel_sdk.py:1`.

### M1: Resource foundation

Plan exit gate: Ten native guests run allocation/map/unmap/protection/pressure/timer tests without corrupting kernel or peers; document real hardware restrictions

Actual bounded anonymous VM, eager fork, guarded copies, native process-frame ownership, calibrated clock/sleep/poll/select subsets execute. Bounded firmware-qualified pools and explicit fallbacks remain; object allocation and synchronized general waits are absent.

- **M1.exit.1 — partial**: Ten native guests execute allocation/map/unmap/protection/pressure tests. Replace fixed per-process/global metadata limits with policy-backed object/frame allocation; qualify quotas/reclaim, pin/reference ownership and rollback using real physical frames on retained platforms.
- **M1.exit.2 — partial**: Timer/wait tests cannot corrupt kernel or peers. Unify typed generation-safe completion, predicate registration and cancellation; add IRQ-safe save/restore locking, timer queue lifecycle, real thread waits and no lost wakeups. Current boot-CPU scanning is a narrower contract.
- **M1.exit.3 — partial**: Locking/atomics/FPU context and hardware restrictions are qualified. Per-profile nested IRQ state, atomic widths/orders, FPU/SIMD isolation and save/restore need dedicated native evidence; document unavailable instruction/protection/platform features without dropping profiles.

Source anchors: `ObfuscationKernel/include/ok/user/native_page_pool.hpp:1`, `ObfuscationKernel/include/ok/boot/qemu_process_memory.hpp:1`, `ObfuscationKernel/src/user/runtime.cpp:1669`, `ObfuscationKernel/include/ok/sched/deadline.hpp:9`, `ObfuscationKernel/src/user/runtime.cpp:70`, `ObfuscationKernel/src/sched/scheduler.cpp:1091`, `ObfuscationOS/docs/plans/ARCHITECTURE_SDK.md:56`, `ObfuscationOS/apps/posix-check/main.c:1`.

### M2: Common OS objects

Plan exit gate: Relative exec works from a renamed cwd; open/unlink/rename races preserve identity; PTY child and IPC peers terminate/wake correctly

Shared object-based resolver, retained cwd/dirfd, symlinks, open descriptions, dup/fork sharing, pipes and partial credentials are implemented and have native subset tests. Native AF_UNIX rights and TTY/PTY lifecycle are not present.

- **M2.exit.1 — subset-evidenced**: Relative exec works from a renamed cwd. Retain this passing behavior while replacing fixed lifetimes; extend through mount cover/unmount and permission changes. This clause does not qualify all of M2.
- **M2.exit.2 — partial**: Open/unlink/rename races preserve identity. Add synchronized mount/inode/dentry lifetime and concurrent namespace semantics; existing serialized identity checks do not establish races.
- **M2.exit.3 — unimplemented**: PTY child and IPC peers terminate and wake correctly. Implement TTY/PTY/termios plus signal-dependent lifecycle, AF_UNIX/socketpair, SCM_RIGHTS, peer credentials, close/exit wakeup and descriptor-reference ownership.

Source anchors: `ObfuscationKernel/src/fs/vfs.cpp:1`, `ObfuscationKernel/src/posix/fd.cpp:1`, `ObfuscationKernel/include/ok/sched/resources.hpp:1`, `ObfuscationKernel/src/sched/scheduler.cpp:1091`, `ObfuscationOS/docs/plans/POSIX_MUSL.md:829`, `ObfuscationOS/apps/posix-check/main.c:1`.

### M3: Libc substrate

Plan exit gate: Each architecture executes musl-linked file/process/thread/signal/clock tests; 32-bit time64/off64 and endian layouts pass golden vectors

Static musl startup/single-thread TLS, files/processes/clock subsets execute on all ten historical qualified SDK20 profiles. Actual runtime selects threads()[0]; no general native clone threads, signals or futex substrate.

- **M3.exit.1 — partial**: Each architecture executes musl-linked file/process/thread/signal/clock tests. Implement real thread selection/stacks/TLS/sharing, clone flag ordering, thread-group exec/exit, futex wait/wake/robust exit, signals/sigreturn/restart/cancellation, then execute actual pthread/signal workloads.
- **M3.exit.2 — partial**: 32-bit time64/off64 and endian layouts pass golden vectors and execution. Existing bounded time/ABI codecs do not cover complete stat/TTY/signal/IPC structures; wide offsets remain restricted on 32-bit paths. Complete all required layouts and native negative cases.
- **M3.exit.3 — partial**: Auxv/static musl semantics include qualified startup entropy. Implement source-qualified CSPRNG/readiness and startup entropy; exercise allocator/stdio/math/headers under defined FPU ABI and resource pressure, retaining native personality regressions.

Source anchors: `ObfuscationKernel/include/ok/user/linux_bootstrap.hpp:1`, `ObfuscationKernel/include/ok/abi/linux_profile_data.hpp:1`, `ObfuscationKernel/include/ok/sched/scheduler.hpp:68`, `ObfuscationKernel/src/user/runtime.cpp:1669`, `ObfuscationOS/scripts/test_musl_userland.py:1`, `ObfuscationOS/docs/plans/IMPLEMENTATION_PROGRESS.md:7`.

### M4: Durable default root

Plan exit gate: Linux-created image boots, mutates, power-fails, replays, and passes Linux/e2fsck checks; fsync claims tested through actual FLUSH ordering

Real Virtio nonjournalled ext4 subset, narrow JBD2 recovery/metadata transactions, canonical bounded buffers and opt-in maintained timestamps exist. Readonly mounted namespace with internal metadata maintenance is not a general journalled root writer.

- **M4.exit.1 — partial**: Linux-created modern ext4 image boots and mutates. Complete S1/S2 reader/group/checksum/64-bit/htree/extent and lifetime foundations; route ordinary namespace, allocation, extent, xattr/ACL and orphan mutations through one mounted transaction owner.
- **M4.exit.2 — partial**: Power-fail image replays and passes Linux/e2fsck. Expand bounded whole-operation metadata fixtures to real mounted file/create/rename/unlink/truncate workloads, journal wrap/revoke/orphans and every commit/checkpoint interruption; maintain genuine failure-media captures.
- **M4.exit.3 — partial**: fsync ordering is verified through actual FLUSH. Trace ordered data/journal commit/home checkpoint/clean publication and device flush under failures for the default writer; existing synchronous subset flush evidence cannot establish general crash consistency.

Source anchors: `ObfuscationOS/docs/plans/STORAGE_EXT4.md:560`, `ObfuscationKernel/src/fs/ext4_fs.cpp:1`, `ObfuscationKernel/include/ok/fs/ext4_owned_transaction.hpp:1`, `ObfuscationKernel/include/ok/fs/ext4_completion.hpp:1`, `ObfuscationKernel/include/ok/fs/metadata_buffers.hpp:1`, `ObfuscationKernel/include/ok/fs/ext4_mounted_metadata.hpp:1`, `ObfuscationOS/drivers/virtio/block.cpp:1`, `ObfuscationOS/docs/plans/IMPLEMENTATION_PROGRESS.md:7`.

### M5: Useful POSIX userland

Plan exit gate: Shared applications, dlopen/TLS, pthread cancellation, shell pipelines/redirection/jobs and designated POSIX suites execute in guests

Small native shell/pipelines and static musl subset exist. Dynamic ELF admission is restricted and file/shared mappings, general pthread/signal semantics and conforming shell/job control remain open.

- **M5.exit.1 — unimplemented**: Shared applications and dlopen/TLS execute. Implement PT_INTERP/ET_DYN, file/private/shared mapping and coherent cache, architecture relocations, loader paths, TLS DSOs, constructors, RELRO and safe unload.
- **M5.exit.2 — unimplemented**: pthread cancellation executes correctly. Complete M3 signals/futex/thread lifecycle then public cancellation points, cleanup, robust/process-shared synchronization and loader/thread interaction.
- **M5.exit.3 — partial**: Shell pipelines/redirection/jobs execute with required utilities. Port pinned shell and utility set after sessions/process groups/TTY/signals; implement required utilities, locale/text behavior and designated shell clauses.
- **M5.exit.4 — unimplemented**: Designated POSIX suites execute in guests. Select versioned suites and clause mapping, report unsupported options truthfully through headers/sysconf/pathconf/getconf; close mandatory deviations instead of passing stubs.

Source anchors: `ObfuscationKernel/include/ok/user/linux_bootstrap.hpp:1`, `ObfuscationKernel/src/user/runtime.cpp:1669`, `ObfuscationOS/docs/plans/POSIX_MUSL.md:829`, `ObfuscationOS/apps/init/main.c:24`, `ObfuscationOS/scripts/test_musl_userland.py:1`.

### M6: Connected host

Plan exit gate: Guest-to-host and guest-to-guest applications run over actual NICs under loss/reordering; DNS and HTTP/TLS clients work without debug transport

Loopback/debug network and device/service records are models. No observed real user socket to OS-owned NIC Internet host path qualifies this gate.

- **M6.exit.1 — unimplemented**: Guest-host and guest-guest apps exchange actual NIC traffic. Implement OS Virtio NIC transport with IRQ/DMA/completion ownership on all ten, canonical socket descriptors/events, Ethernet/ARP/IP/UDP/TCP and route control; verify independent capture/peer bytes.
- **M6.exit.2 — unimplemented**: Loss/reordering and host protocol requirements pass. Implement full TCP lifecycle/congestion/RTO/flow control, IPv6/ND/RA/DAD/PMTU/multicast/fragment behavior and hostile packet/pressure suites with real socket calls.
- **M6.exit.3 — unimplemented**: DNS and HTTP/TLS clients work without debug transport. Provide resolver configuration/DNS UDP+TCP, time and CSPRNG trust prerequisites, DHCP/IPv6 configuration and pinned client ports; debug channel or synthetic receive does not count.

Source anchors: `ObfuscationOS/docs/plans/NETWORK_SERVICES.md:587`, `ObfuscationKernel/include/ok/net/net.hpp:85`, `ObfuscationKernel/include/ok/sched/resources.hpp:1`, `ObfuscationKernel/src/user/runtime.cpp:70`.

### M7: Managed system

Plan exit gate: Boot without test mode, crash/restart services, recover dependency failure, reap orphans, rotate logs and shut down/reboot with disk consistency

/init launches acceptance or one shell and returns when it ends. Parent-zero kernel reaping/service models are not persistent user PID1 supervision.

- **M7.exit.1 — unimplemented**: Normal boot runs persistent PID1 with dependency/readiness management. Designate user PID1/reparenting/init-death semantics; implement foreground service manifests, authenticated per-launch readiness, generation-safe process control, privileges and resource limits.
- **M7.exit.2 — unimplemented**: Crash/restart/dependency failures and orphan reaping recover. Implement real signals/process control/wait-any/SIGCHLD, service restart bounds/backoff, orphan and zombie policy; execute failures on all ten.
- **M7.exit.3 — unimplemented**: Required services/accounts/sessions and log rotation work. Implement listed log/dev/network/resolver/time/storage/account/login/session/seat/job/update services with versioned credential-checked IPC and durable configs.
- **M7.exit.4 — unimplemented**: Shutdown/reboot preserves consistency. Stop sessions/units in reverse dependency order, TERM/KILL with deadlines, drain logs/I/O, sync/unmount and device quiesce; record sync failure honestly and retain rescue.

Source anchors: `ObfuscationOS/apps/init/main.c:24`, `ObfuscationOS/docs/plans/NETWORK_SERVICES.md:587`, `ObfuscationKernel/include/ok/sched/scheduler.hpp:68`, `ObfuscationKernel/include/ok/sched/resources.hpp:1`.

### M8: Isolated graphics

Plan exit gate: Separate user compositor and two clients draw concurrently; killing one client cannot read peer buffers or stop input; kernel rescue survives

Prelinked OS kernel extension draws desktop views; kernel buffer slots are not isolated shared mappings. Existing visual/model tests remain useful regression fixtures.

- **M8.exit.1 — unimplemented**: Separate user compositor and two clients draw concurrently. Provide display/input FDs, revocable seat leases and owned buffers; implement AF_UNIX rights/shared file mappings then pinned Wayland software compositor and two real client processes.
- **M8.exit.2 — unimplemented**: Client kill cannot expose peer buffers or stop input. Enforce page/FD/lease generations, buffer/presentation lifetimes, guarded truncated SHM access, protocol bounds and distinct credentials/address spaces; execute malicious client/death tests.
- **M8.exit.3 — partial**: Kernel rescue survives and text/PTY foundations work. Keep boot/rescue diagnostics; add exclusive display owner transitions, scalable fonts/shaping/toolkit/input, PTY terminal, CJK/RTL and keyboard focus tests.

Source anchors: `ObfuscationOS/docs/plans/DESKTOP_APPS.md:289`, `ObfuscationOS/modules/system-gui/system_gui_runtime.cpp:1`, `ObfuscationKernel/include/ok/gui/desktop.hpp:1`, `ObfuscationKernel/src/user/runtime.cpp:1669`, `ObfuscationOS/docs/plans/NETWORK_SERVICES.md:587`.

### M9: Daily desktop

Plan exit gate: Scripted and human novice workflows pass: login, network, file copy/save/reopen, package install/rollback, lock and clean shutdown

Existing attractive app views are in-kernel extension views. They do not qualify user login, durable documents, networking, installation or accessibility workflows.

- **M9.exit.1 — unimplemented**: Novice login/network/file-copy/save/reopen workflows pass. Implement independent Files/Editor/Settings/Tasks/Logs/Network/Terminal applications atop actual IPC, permissions, coherent files and durable root; supply error/loading/offline/full-disk states.
- **M9.exit.2 — unimplemented**: Package install/rollback, lock and clean shutdown work. Add trusted package metadata/verification, durable staged install/update/rollback and installer/recovery media; qualified accounts/seat lock/revoke and shutdown required.
- **M9.exit.3 — unimplemented**: Accessibility/persistent preferences and human workflows qualify. Implement keyboard-only navigation, UTF-8/CJK input, scaling and accessibility interfaces; execute scripted acceptance and record real human novice/screen-reader workflows.

Source anchors: `ObfuscationOS/docs/plans/DESKTOP_APPS.md:289`, `ObfuscationOS/modules/system-gui/system_gui_runtime.cpp:1`, `ObfuscationOS/apps/init/main.c:24`.

### M10: Ext4 breadth

Plan exit gate: Every advertised read/write/replay profile round-trips with pinned Linux/e2fsprogs; unsupported combinations are explicitly rejected

Explicit subset/modern metadata profiles reject unsupported combinations. Advanced feature requirements remain planned in the ledger.

- **M10.exit.1 — unimplemented**: Every advertised read/write/replay profile round-trips with pinned references. Implement and qualify S7 legacy mappings, larger blocks/inline/ea_inode/large directories, quota/project, external journals, fscrypt, verity, casefold, bigalloc, MMP, fast commit and online growth as selected by full feature matrix.
- **M10.exit.2 — partial**: Unsupported combinations are explicitly rejected. Expand exact per-bit/version/read/write/replay/tool combination table and corruption tests; do not describe safe current rejection as implemented advanced functionality.
- **M10.exit.3 — unimplemented**: Mixed profiles preserve recovery/resource/security semantics. Exercise two-device failure, crypto/key/cache lifetime, Unicode policy, cluster allocation, simultaneous-mount fencing and fast/full commit crossover after their specific dependencies.

Source anchors: `ObfuscationOS/docs/plans/STORAGE_EXT4.md:560`, `ObfuscationKernel/src/fs/ext4_fs.cpp:1`, `ObfuscationKernel/include/ok/fs/ext4_owned_transaction.hpp:1`, `ObfuscationKernel/include/ok/fs/ext4_mounted_metadata.hpp:1`.

### M11: Execution breadth

Plan exit gate: Module code truly relocates/executes; no use-after-unload; concurrent filesystem/socket/GUI stress passes; hardware evidence is separate from QEMU

SMP topology/lock records and prelinked module metadata are foundations/models. Current qualified runtime and maintained metadata are serialized on boot CPU.

- **M11.exit.1 — unimplemented**: Native module relocates and executes new code. Implement bounded immutable ET_REL capture, exact SDK/compiler validation, per-arch relocation, W^X/cache finalization, initialization/unwind and real exported service call.
- **M11.exit.2 — unimplemented**: No use-after-unload with callbacks/IRQ/DMA/work. Reference/pin module dependencies and active resources; stop publication, drain timers/work/IRQs/DMA and workers, reject EBUSY if not quiescent, then unmap; exercise repeated load/unload.
- **M11.exit.3 — unimplemented**: Real SMP/TLB and concurrent filesystem/socket/GUI stress passes. Implement secondary startup/IPI/per-CPU execution, complete thread scheduling, atomics/lock ranks, remote TLB retirement and concurrent ownership; hosted spinlocks/topology do not prove it.
- **M11.exit.4 — unimplemented**: Physical reference machines have separate evidence. Select explicit platform matrix and record actual boot/storage/NIC/display/input/IRQ/DMA/reset/hotplug behavior; QEMU evidence never substitutes for named machines.

Source anchors: `ObfuscationOS/docs/plans/ARCHITECTURE_SDK.md:56`, `ObfuscationKernel/include/ok/smp/smp.hpp:90`, `ObfuscationKernel/include/ok/sched/scheduler.hpp:68`, `ObfuscationKernel/src/core/module.cpp:1`, `ObfuscationOS/drivers/virtio/block.cpp:1`.

### M12: Full target

Plan exit gate: No mandatory or selected-profile gaps; ten architectures pass the applicable user ABI/product gates; scope and remaining outside-profile limitations are published

Strict SDK producer/consumer pipeline and many preserved subset receipts exist. No complete normative ledger, ten-profile workstation qualification or recoverable product release exists.

- **M12.exit.1 — unimplemented**: No mandatory/selected-profile gaps. Close all exact inventories, code semantics and acceptance gates; preview waivers cannot mark M12 complete.
- **M12.exit.2 — partial**: Ten architectures pass applicable user ABI and product gates in Debug/Release. Preserve ten profiles and existing qualified subsets while qualifying final exact sources/artifacts; physical platform selection is separate, and failed candidate matrices remain failed.
- **M12.exit.3 — partial**: Reproducible artifacts/documentation/recovery and published scope. Produce matched reproducible SDK/sysroot/packages/install/recovery sets, update interruption evidence, release diagnostics and accurate capability/limitation table; repair stale docs and bind evidence to final source.

Source anchors: `ObfuscationOS/docs/plans/README.md:192`, `ObfuscationOS/docs/plans/contracts/ledger.json:1`, `ObfuscationOS/docs/plans/IMPLEMENTATION_PROGRESS.md:7`, `ObfuscationOS/tools/kernel_sdk.py:1`.

## Executable dependency order

1. Finish the current SDK21 integration as a bounded independent delivery; retain failed attempts. In parallel finish M0 normative inventories with verified source pins. Do not broaden the stat/chmod slice into an M1-M12 completion claim.
2. Land P04 generation-safe wait ownership described in `WAIT_FOUNDATION_DESIGN.md`, with real existing pipe/sleep/poll continuations. In parallel advance P02 fallible object/frame allocation and stable process/address-space ownership; bounded native buffers must have explicit limits until replaced.
3. Use those lifetimes to enable real runnable native threads and shared address spaces, architecture TLS/FPU context, clone/clear-child-tid and futex basics. Add per-profile signals/sigreturn/restart before pthread cancellation, supervisor kill and TTY job control.
4. Complete M2 shared file/socket/TTY objects, AF_UNIX/SCM_RIGHTS and namespace locking. Drive static musl pthread/process/signal acceptance through all ten profiles; then introduce dynamic ELF/file mappings/coherent page cache and complete shell/utility/locale semantics.
5. In parallel with libc, extend the existing private ext4 transaction owner into the ordinary mounted writer, including allocation/extent/directory/orphan paths and default-root recovery. Do not enable the new image format before fault/FLUSH/Linux checks pass.
6. After waits/FD/IRQ/DMA lifetimes exist, bring up an actual OS-owned NIC and independent peer capture, then native UDP/TCP and dual-stack configuration/resolver/time/security packages. Separately implement persistent user PID1 with real supervision and authenticated IPC.
7. After shared mappings/AF_UNIX and lifecycle work, introduce user display/input descriptors and a two-client software Wayland vertical slice, then greeter/session, toolkit/PTY and real daily applications.
8. Continue SMP and runtime module work from the foundation stage, not as an afterthought. Qualify advanced ext4 combinations only after their writer/crypto/quota/fencing dependencies. Close release ledger and physical/human workflows last; no emulator substitution for these gates.

## Documentation drift and audit limits

- `ObfuscationKernel/docs/NATIVE_VM.md` still says backing only comes from the linker-reserved arena. The later process-frame implementation and ledger document firmware-qualified pools plus explicit fallbacks. Retain the historic evidence labels and rewrite the current contract around current source.
- `ObfuscationKernel/docs/NATIVE_WAITS.md` still lists select/ppoll/pselect as unimplemented, while later bounded Linux adapters and progress record those subsets. Their nonnull signal-mask/SMP limitations remain; update the distinction rather than claiming complete interfaces.
- Some original ledger limitation strings still mention old ABI generations or pre-integration gaps. Requirement identities and evidence source snapshots must be preserved while updating current capability descriptions.
- This is a bounded source audit, not formal certification or a security audit. It does not infer absence solely from names: the strongest missing-work evidence is the explicit planned ledger plus inspected runtime/initial process/network/GUI ownership. No physical machine or real SMP receipt was supplied by the audited shared progress.

## Recommended bounded feature

Implement `P04.wait-registration-v1` next. It replaces separate wait completion ownership in the existing native runtime with one tested state machine and addresses the dependency shared by threads, IPC, socket events, service supervision and graphics. It is independently implementable on the current serialized boot CPU and gives useful executed behavior before full pthreads. Its acceptance explicitly remains a subset of M1 and does not claim SMP. See `WAIT_FOUNDATION_DESIGN.md` for interface, ownership, transitions, races and native test gates.
