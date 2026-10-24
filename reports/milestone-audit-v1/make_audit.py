#!/usr/bin/env python3
"""Generate a bounded read-only milestone coverage audit from current source."""
import hashlib, json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path('/media/data1/Project/System/ObfuscationProject')
OUT=ROOT/'build/milestone-audit-v1'
PLAN='ObfuscationOS/docs/plans/'
ledger=json.loads((ROOT/PLAN/'contracts/ledger.json').read_text())
refs={}
def ref(path, needle=None):
    full=ROOT/path
    lines=full.read_text(errors='replace').splitlines()
    line=next((i+1 for i,s in enumerate(lines) if needle and needle in s),1)
    key=f'{path}:{line}'
    refs[key]={'path':path,'line':line,'sha256':hashlib.sha256(full.read_bytes()).hexdigest(),'needle':needle}
    return key
R={
 'plan':ref(PLAN+'README.md','## 6. Milestones'),
 'progress':ref(PLAN+'IMPLEMENTATION_PROGRESS.md','## ABI 20'),
 'ledger':ref(PLAN+'contracts/ledger.json'),
 'contracts':ref('ObfuscationOS/tools/plan_ledger.py','if args.command == "gate-m0":'),
 'arch':ref(PLAN+'ARCHITECTURE_SDK.md','## A03.'),
 'posix':ref(PLAN+'POSIX_MUSL.md','## 7.'),
 'storage':ref(PLAN+'STORAGE_EXT4.md','## 10.'),
 'network':ref(PLAN+'NETWORK_SERVICES.md','## 10.'),
 'desktop':ref(PLAN+'DESKTOP_APPS.md','## G08.'),
 'frames':ref('ObfuscationKernel/include/ok/user/native_page_pool.hpp'),
 'firmware':ref('ObfuscationKernel/include/ok/boot/qemu_process_memory.hpp'),
 'vm':ref('ObfuscationKernel/src/user/runtime.cpp','bool step(Kernel &kernel)'),
 'wait':ref('ObfuscationKernel/include/ok/sched/deadline.hpp','class DeadlineWait'),
 'poll':ref('ObfuscationKernel/src/user/runtime.cpp','struct PollWait'),
 'schedwait':ref('ObfuscationKernel/src/sched/scheduler.cpp','Status SchedulerState::block_current'),
 'sleepdoc':ref('ObfuscationKernel/docs/NATIVE_WAITS.md','Readiness is rescanned'),
 'vmdoc':ref('ObfuscationKernel/docs/NATIVE_VM.md','Backing remains'),
 'path':ref('ObfuscationKernel/src/fs/vfs.cpp'),
 'fd':ref('ObfuscationKernel/src/posix/fd.cpp'),
 'resources':ref('ObfuscationKernel/include/ok/sched/resources.hpp'),
 'sched':ref('ObfuscationKernel/include/ok/sched/scheduler.hpp','struct ThreadControlBlock'),
 'linux':ref('ObfuscationKernel/include/ok/user/linux_bootstrap.hpp'),
 'linuxdata':ref('ObfuscationKernel/include/ok/abi/linux_profile_data.hpp'),
 'native':ref('ObfuscationOS/apps/posix-check/main.c'),
 'musl':ref('ObfuscationOS/scripts/test_musl_userland.py'),
 'sdk':ref('ObfuscationOS/tools/kernel_sdk.py'),
 'ext4':ref('ObfuscationKernel/src/fs/ext4_fs.cpp'),
 'journal':ref('ObfuscationKernel/include/ok/fs/ext4_owned_transaction.hpp'),
 'completion':ref('ObfuscationKernel/include/ok/fs/ext4_completion.hpp'),
 'buffers':ref('ObfuscationKernel/include/ok/fs/metadata_buffers.hpp'),
 'mounted':ref('ObfuscationKernel/include/ok/fs/ext4_mounted_metadata.hpp'),
 'block':ref('ObfuscationOS/drivers/virtio/block.cpp'),
 'netmodel':ref('ObfuscationKernel/include/ok/net/net.hpp','class VirtioNetDevice'),
 'init':ref('ObfuscationOS/apps/init/main.c','int main'),
 'gui':ref('ObfuscationOS/modules/system-gui/system_gui_runtime.cpp'),
 'guibuffers':ref('ObfuscationKernel/include/ok/gui/desktop.hpp'),
 'modules':ref('ObfuscationKernel/src/core/module.cpp'),
 'smp':ref('ObfuscationKernel/include/ok/smp/smp.hpp','class SpinLock'),
 'instructions':ref('ObfuscationKernel/include/ok/arch/arch.hpp','enable_interrupts'),
 'chmod':ref('build/prototypes/linux-chmod-v1/VALIDATION.md'),
}
# These evidence files are inspected and hashed, not recursively requalified.
evidence={}
for key,path,scope in [
 ('sdk20-native','ObfuscationOS/build/workstation-abi20-maintained-ext4-v1/native-six-layouts-v1/result.json','SDK20 privileged x86_64 six-layout provider guest; no user execution'),
 ('sdk20-linux','ObfuscationOS/build/workstation-abi20-maintained-ext4-v1/linux-final-v1/result.json','Two x86_64 Linux readonly reference boots; no physical/SMP'),
 ('sdk21-candidate','ObfuscationOS/build/workstation-abi21-linux-stat-v1/native-matrix-v2/result.json','Incomplete SDK21 frozen candidate qualification'),
 ('sdk21-commands','ObfuscationOS/build/workstation-abi21-linux-stat-v1/native-matrix-v2/output/results.json','Retained SDK21 candidate commands; not a completed matrix')]:
 p=ROOT/path; data=json.loads(p.read_text())
 evidence[key]={'path':path,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':p.stat().st_size,'scope':scope,'status':data.get('status') if isinstance(data,dict) else 'command-log','records':len(data) if isinstance(data,list) else None,'audit_depth':'top-level status and bytes inspected; nested artifacts not rehashed by this audit'}
ms=[]
def add(i,title,requirements,dependencies,sources,existing,gate_rows,evidence_ids=None):
 line=next(s for s in (ROOT/PLAN/'README.md').read_text().splitlines() if s.startswith(f'| M{i}:'))
 parts=[p.strip() for p in line.split('|')[1:-1]]
 gates=[]
 for n,(expectation,status,missing) in enumerate(gate_rows,1):
  gates.append({'id':f'M{i}.exit.{n}','expectation':expectation,'status':status,'missing_mandatory_work':missing,'source_refs':[R[s] for s in sources]})
 ms.append({'id':f'M{i}','name':title,'state':'incomplete','deliverable_verbatim':parts[1],'exit_gate_verbatim':parts[2],'dependencies':dependencies,'ledger_requirement_ids':requirements,'current_concrete_scope':existing,'source_refs':[R[s] for s in sources],'evidence_refs':evidence_ids or [],'gates':gates,'completion_claim':False})
add(0,'Specification baseline',['M0.inventory','P01.linux-abi','A06.sdk'],[],['plan','ledger','contracts','sdk'],
 'Versioned seed ledger, validation tooling, ten ABI tuples and explicit SDK identity validation exist. Four normative inventories are partial; the source ledger attaches zero execution receipts.',[
 ('Every requirement has an owner and semantics source','partial','Expand seed requirements to every Issue 8 clause/interface/utility/option, selected RFC MUST/SHOULD, exact ext4 format feature and permitted combination; preserve authoritative versions and ownership.'),
 ('Every requirement has dependencies and a planned acceptance test','partial','Create the missing normative rows and tests; mapping a subsystem summary to one test does not cover its constituent requirements.'),
 ('Ten ABI profiles have explicit qualification gaps','partial','Complete per-profile syscall/errno/flag/ELF/TLS/signal/struct inventories and authenticated source pin provenance. Existing bootstrap tuple tables remain valid subsets.')])
add(1,'Resource foundation',['P02.allocation','P02.process-frames','P02.arm32-firmware-process-frames','P03.vm','P04.wait-time'],['M0'],['frames','firmware','vm','wait','poll','schedwait','arch','native'],
 'Actual bounded anonymous VM, eager fork, guarded copies, native process-frame ownership, calibrated clock/sleep/poll/select subsets execute. Bounded firmware-qualified pools and explicit fallbacks remain; object allocation and synchronized general waits are absent.',[
 ('Ten native guests execute allocation/map/unmap/protection/pressure tests','partial','Replace fixed per-process/global metadata limits with policy-backed object/frame allocation; qualify quotas/reclaim, pin/reference ownership and rollback using real physical frames on retained platforms.'),
 ('Timer/wait tests cannot corrupt kernel or peers','partial','Unify typed generation-safe completion, predicate registration and cancellation; add IRQ-safe save/restore locking, timer queue lifecycle, real thread waits and no lost wakeups. Current boot-CPU scanning is a narrower contract.'),
 ('Locking/atomics/FPU context and hardware restrictions are qualified','partial','Per-profile nested IRQ state, atomic widths/orders, FPU/SIMD isolation and save/restore need dedicated native evidence; document unavailable instruction/protection/platform features without dropping profiles.')])
add(2,'Common OS objects',['P08.paths','P08.checked-callers','P01.paths-bootstrap','P01.descriptor-bootstrap','P01.pipes-bootstrap','P08.qualified-file-attributes'],['M1'],['path','fd','resources','schedwait','posix','native'],
 'Shared object-based resolver, retained cwd/dirfd, symlinks, open descriptions, dup/fork sharing, pipes and partial credentials are implemented and have native subset tests. Native AF_UNIX rights and TTY/PTY lifecycle are not present.',[
 ('Relative exec works from a renamed cwd','subset-evidenced','Retain this passing behavior while replacing fixed lifetimes; extend through mount cover/unmount and permission changes. This clause does not qualify all of M2.'),
 ('Open/unlink/rename races preserve identity','partial','Add synchronized mount/inode/dentry lifetime and concurrent namespace semantics; existing serialized identity checks do not establish races.'),
 ('PTY child and IPC peers terminate and wake correctly','unimplemented','Implement TTY/PTY/termios plus signal-dependent lifecycle, AF_UNIX/socketpair, SCM_RIGHTS, peer credentials, close/exit wakeup and descriptor-reference ownership.')])
add(3,'Libc substrate',['P01.linux-abi','P05.threads-tls','P06.signals','P07.futex','L01.musl-static'],['M1','M2'],['linux','linuxdata','sched','vm','musl','progress'],
 'Static musl startup/single-thread TLS, files/processes/clock subsets execute on all ten historical qualified SDK20 profiles. Actual runtime selects threads()[0]; no general native clone threads, signals or futex substrate.',[
 ('Each architecture executes musl-linked file/process/thread/signal/clock tests','partial','Implement real thread selection/stacks/TLS/sharing, clone flag ordering, thread-group exec/exit, futex wait/wake/robust exit, signals/sigreturn/restart/cancellation, then execute actual pthread/signal workloads.'),
 ('32-bit time64/off64 and endian layouts pass golden vectors and execution','partial','Existing bounded time/ABI codecs do not cover complete stat/TTY/signal/IPC structures; wide offsets remain restricted on 32-bit paths. Complete all required layouts and native negative cases.'),
 ('Auxv/static musl semantics include qualified startup entropy','partial','Implement source-qualified CSPRNG/readiness and startup entropy; exercise allocator/stdio/math/headers under defined FPU ABI and resource pressure, retaining native personality regressions.')])
add(4,'Durable default root',['S0.ext4-subset','S3.jbd2-replay','S3.recovery-completion','S4.bounded-metadata-transaction','S2.canonical-metadata-buffers','S2.owned-ext4-transaction','S2.mounted-metadata','S4.transactions'],['M1','M2'],['storage','ext4','journal','completion','buffers','mounted','block','progress'],
 'Real Virtio nonjournalled ext4 subset, narrow JBD2 recovery/metadata transactions, canonical bounded buffers and opt-in maintained timestamps exist. Readonly mounted namespace with internal metadata maintenance is not a general journalled root writer.',[
 ('Linux-created modern ext4 image boots and mutates','partial','Complete S1/S2 reader/group/checksum/64-bit/htree/extent and lifetime foundations; route ordinary namespace, allocation, extent, xattr/ACL and orphan mutations through one mounted transaction owner.'),
 ('Power-fail image replays and passes Linux/e2fsck','partial','Expand bounded whole-operation metadata fixtures to real mounted file/create/rename/unlink/truncate workloads, journal wrap/revoke/orphans and every commit/checkpoint interruption; maintain genuine failure-media captures.'),
 ('fsync ordering is verified through actual FLUSH','partial','Trace ordered data/journal commit/home checkpoint/clean publication and device flush under failures for the default writer; existing synchronous subset flush evidence cannot establish general crash consistency.')],['sdk20-native','sdk20-linux'])
add(5,'Useful POSIX userland',['L02.musl-shared','L05.shell-utilities','S6.cache'],['M3','M4'],['linux','vm','posix','init','musl'],
 'Small native shell/pipelines and static musl subset exist. Dynamic ELF admission is restricted and file/shared mappings, general pthread/signal semantics and conforming shell/job control remain open.',[
 ('Shared applications and dlopen/TLS execute','unimplemented','Implement PT_INTERP/ET_DYN, file/private/shared mapping and coherent cache, architecture relocations, loader paths, TLS DSOs, constructors, RELRO and safe unload.'),
 ('pthread cancellation executes correctly','unimplemented','Complete M3 signals/futex/thread lifecycle then public cancellation points, cleanup, robust/process-shared synchronization and loader/thread interaction.'),
 ('Shell pipelines/redirection/jobs execute with required utilities','partial','Port pinned shell and utility set after sessions/process groups/TTY/signals; implement required utilities, locale/text behavior and designated shell clauses.'),
 ('Designated POSIX suites execute in guests','unimplemented','Select versioned suites and clause mapping, report unsupported options truthfully through headers/sysconf/pathconf/getconf; close mandatory deviations instead of passing stubs.')])
add(6,'Connected host',['N.nic-sockets','N.internet-host'],['M3','M2','M1'],['network','netmodel','resources','poll'],
 'Loopback/debug network and device/service records are models. No observed real user socket to OS-owned NIC Internet host path qualifies this gate.',[
 ('Guest-host and guest-guest apps exchange actual NIC traffic','unimplemented','Implement OS Virtio NIC transport with IRQ/DMA/completion ownership on all ten, canonical socket descriptors/events, Ethernet/ARP/IP/UDP/TCP and route control; verify independent capture/peer bytes.'),
 ('Loss/reordering and host protocol requirements pass','unimplemented','Implement full TCP lifecycle/congestion/RTO/flow control, IPv6/ND/RA/DAD/PMTU/multicast/fragment behavior and hostile packet/pressure suites with real socket calls.'),
 ('DNS and HTTP/TLS clients work without debug transport','unimplemented','Provide resolver configuration/DNS UDP+TCP, time and CSPRNG trust prerequisites, DHCP/IPv6 configuration and pinned client ports; debug channel or synthetic receive does not count.')])
add(7,'Managed system',['N.services'],['M4','M5','M6'],['init','network','sched','resources'],
 '/init launches acceptance or one shell and returns when it ends. Parent-zero kernel reaping/service models are not persistent user PID1 supervision.',[
 ('Normal boot runs persistent PID1 with dependency/readiness management','unimplemented','Designate user PID1/reparenting/init-death semantics; implement foreground service manifests, authenticated per-launch readiness, generation-safe process control, privileges and resource limits.'),
 ('Crash/restart/dependency failures and orphan reaping recover','unimplemented','Implement real signals/process control/wait-any/SIGCHLD, service restart bounds/backoff, orphan and zombie policy; execute failures on all ten.'),
 ('Required services/accounts/sessions and log rotation work','unimplemented','Implement listed log/dev/network/resolver/time/storage/account/login/session/seat/job/update services with versioned credential-checked IPC and durable configs.'),
 ('Shutdown/reboot preserves consistency','unimplemented','Stop sessions/units in reverse dependency order, TERM/KILL with deadlines, drain logs/I/O, sync/unmount and device quiesce; record sync failure honestly and retain rescue.')])
add(8,'Isolated graphics',['G.compositor'],['M5','M2'],['desktop','gui','guibuffers','vm','network'],
 'Prelinked OS kernel extension draws desktop views; kernel buffer slots are not isolated shared mappings. Existing visual/model tests remain useful regression fixtures.',[
 ('Separate user compositor and two clients draw concurrently','unimplemented','Provide display/input FDs, revocable seat leases and owned buffers; implement AF_UNIX rights/shared file mappings then pinned Wayland software compositor and two real client processes.'),
 ('Client kill cannot expose peer buffers or stop input','unimplemented','Enforce page/FD/lease generations, buffer/presentation lifetimes, guarded truncated SHM access, protocol bounds and distinct credentials/address spaces; execute malicious client/death tests.'),
 ('Kernel rescue survives and text/PTY foundations work','partial','Keep boot/rescue diagnostics; add exclusive display owner transitions, scalable fonts/shaping/toolkit/input, PTY terminal, CJK/RTL and keyboard focus tests.')])
add(9,'Daily desktop',['G.apps'],['M7','M8'],['desktop','gui','init'],
 'Existing attractive app views are in-kernel extension views. They do not qualify user login, durable documents, networking, installation or accessibility workflows.',[
 ('Novice login/network/file-copy/save/reopen workflows pass','unimplemented','Implement independent Files/Editor/Settings/Tasks/Logs/Network/Terminal applications atop actual IPC, permissions, coherent files and durable root; supply error/loading/offline/full-disk states.'),
 ('Package install/rollback, lock and clean shutdown work','unimplemented','Add trusted package metadata/verification, durable staged install/update/rollback and installer/recovery media; qualified accounts/seat lock/revoke and shutdown required.'),
 ('Accessibility/persistent preferences and human workflows qualify','unimplemented','Implement keyboard-only navigation, UTF-8/CJK input, scaling and accessibility interfaces; execute scripted acceptance and record real human novice/screen-reader workflows.')])
add(10,'Ext4 breadth',[r['id'] for r in ledger['requirements'] if r['id'].startswith('S7.')],['M4'],['storage','ext4','journal','mounted'],
 'Explicit subset/modern metadata profiles reject unsupported combinations. Advanced feature requirements remain planned in the ledger.',[
 ('Every advertised read/write/replay profile round-trips with pinned references','unimplemented','Implement and qualify S7 legacy mappings, larger blocks/inline/ea_inode/large directories, quota/project, external journals, fscrypt, verity, casefold, bigalloc, MMP, fast commit and online growth as selected by full feature matrix.'),
 ('Unsupported combinations are explicitly rejected','partial','Expand exact per-bit/version/read/write/replay/tool combination table and corruption tests; do not describe safe current rejection as implemented advanced functionality.'),
 ('Mixed profiles preserve recovery/resource/security semantics','unimplemented','Exercise two-device failure, crypto/key/cache lifetime, Unicode policy, cluster allocation, simultaneous-mount fencing and fast/full commit crossover after their specific dependencies.')])
add(11,'Execution breadth',['A04.smp','A05.runtime-modules'],['M1','M3'],['arch','smp','sched','modules','block'],
 'SMP topology/lock records and prelinked module metadata are foundations/models. Current qualified runtime and maintained metadata are serialized on boot CPU.',[
 ('Native module relocates and executes new code','unimplemented','Implement bounded immutable ET_REL capture, exact SDK/compiler validation, per-arch relocation, W^X/cache finalization, initialization/unwind and real exported service call.'),
 ('No use-after-unload with callbacks/IRQ/DMA/work','unimplemented','Reference/pin module dependencies and active resources; stop publication, drain timers/work/IRQs/DMA and workers, reject EBUSY if not quiescent, then unmap; exercise repeated load/unload.'),
 ('Real SMP/TLB and concurrent filesystem/socket/GUI stress passes','unimplemented','Implement secondary startup/IPI/per-CPU execution, complete thread scheduling, atomics/lock ranks, remote TLB retirement and concurrent ownership; hosted spinlocks/topology do not prove it.'),
 ('Physical reference machines have separate evidence','unimplemented','Select explicit platform matrix and record actual boot/storage/NIC/display/input/IRQ/DMA/reset/hotplug behavior; QEMU evidence never substitutes for named machines.')])
add(12,'Full target',['M0.inventory','A06.sdk'],['M0','M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11'],['plan','ledger','progress','sdk'],
 'Strict SDK producer/consumer pipeline and many preserved subset receipts exist. No complete normative ledger, ten-profile workstation qualification or recoverable product release exists.',[
 ('No mandatory/selected-profile gaps','unimplemented','Close all exact inventories, code semantics and acceptance gates; preview waivers cannot mark M12 complete.'),
 ('Ten architectures pass applicable user ABI and product gates in Debug/Release','partial','Preserve ten profiles and existing qualified subsets while qualifying final exact sources/artifacts; physical platform selection is separate, and failed candidate matrices remain failed.'),
 ('Reproducible artifacts/documentation/recovery and published scope','partial','Produce matched reproducible SDK/sysroot/packages/install/recovery sets, update interruption evidence, release diagnostics and accurate capability/limitation table; repair stale docs and bind evidence to final source.')],['sdk21-candidate'])
wait_design={
 'id':'P04.wait-registration-v1','milestones_unblocked':['M1','M2','M3','M6','M7','M8','M11'],
 'owner':'ObfuscationKernel','status':'proposed-not-implemented','scope':'One generation-safe completion owner for existing boot-CPU pipe/sleep/readiness waits, with static-dispatch synchronization and native regression integration.',
 'dependencies':['Keep existing bounded page and descriptor pins; preallocate stable wait slots before blocking','Define one synchronization domain and lock order before registering callbacks','Preserve existing native/Linux pending-call copies and deadline semantics','New exported C++ layouts require next exact SDK generation and producer/consumer qualification'],
 'source_anchors':[R[x] for x in ['schedwait','poll','wait','vm','smp','instructions']],
 'interfaces':['WaitToken { slot, generation, pid, tid }','WaitSourceId { kind, object_id, generation }','WaitOutcome { ready, timeout, interrupted, canceled, source_closed }','prepare(thread, frozen_request, retained_sources, deadline) -> Result<WaitToken>','subscribe_and_recheck(token, source, predicate) -> Status','park(token) -> { parked, completed }','try_complete(token, outcome) -> bool','take_completion(token) -> Result<Completion>','cancel_and_drain(token) -> Status'],
 'states':['free','prepared','registered','parked','completed','consumed'],
 'invariants':['No raw TCB/FD-slot pointer survives scheduler compaction or blocking','All resources admitted before registration publication','Condition mutation and subscription use the same synchronization domain','First valid completion owns the terminal outcome; stale generation cannot claim','No user copy, allocation, I/O, sleep or destructor callback while holding wait/source locks','Completion copyout revalidates current address space; exit cancellation never copies out','Pins released once after every source membership and timer reference is removed','Generation exhaustion rejects new admission rather than wrapping'],
 'acceptance':['Deterministic hosted interleaving tests at predicate/registration/park/wake/timeout/cancel boundaries','ASan/UBSan and all-ten freestanding xmake compile','Actual native and musl pipe/sleep/poll/select guests preserving copied request and realtime-independent deadlines','Close/reuse/dup/fork/exit registration lifetime and exactly-once counters via independent receipts','Standalone Kernel plus SDK-only OS producer/consumer Debug/Release all-ten regression'],
 'explicit_nonclaims':['No general pthread/signals/futex completion','No SMP/physical/IRQ-worker qualification from boot-CPU integration','No unlimited dynamic wait allocation','No complete M1 or M3 claim']
}
out={'schema_version':1,'audit_type':'bounded-read-only-source-and-top-level-evidence-audit','created_at':datetime.now(timezone.utc).isoformat(),'workspace':str(ROOT),'constraints':'No shared source/docs edits, no QEMU/build, no candidate or ledger promotions. Preserve all ten Kernel profiles and existing OS userland profiles.','architecture_profiles':[a['id'] if 'id' in a else a for a in ledger['architectures']], 'ledger_snapshot':{'revision':ledger['ledger_revision'],'scope':ledger['scope'],'requirements':len(ledger['requirements']),'tests':len(ledger['tests']),'execution_receipts':len(ledger['evidence']),'state_counts':dict(Counter(r['state'] for r in ledger['requirements'])),'inventories':ledger['inventories']},'evidence':evidence,'source_references':refs,'milestones':ms,'next_feature':wait_design,'all_milestones_complete':False}
(OUT/'gate-mapping.json').write_text(json.dumps(out,indent=2)+'\n')
# Preserve the exact audited plan and ledger bytes without changing their owners.
for name,path in [('plan-README.md',PLAN+'README.md'),('source-ledger.json',PLAN+'contracts/ledger.json'),('source-progress.md',PLAN+'IMPLEMENTATION_PROGRESS.md')]:
 (OUT/name).write_bytes((ROOT/path).read_bytes())
lines=['# M0-M12 coverage audit','',f"Audit timestamp: {out['created_at']}",'','All thirteen milestone completion gates remain open. SDK20 provides substantial executed filesystem, ABI, memory and clock subsets, but the full target requires missing resource/thread/signal/IPC/durability/network/service/desktop/SMP mechanisms. Repeating metadata adapters alone cannot close the dependency graph. This audit performs no builds or guest execution and does not promote any requirement.','', '## Evidence boundary','',f"The current shared ledger is `{ledger['ledger_revision']}` / `{ledger['scope']}`: {len(ledger['requirements'])} requirements, {len(ledger['tests'])} tests, zero attached execution receipts; its four normative inventories are partial. State counts are {dict(Counter(r['state'] for r in ledger['requirements']))}. These counts are not a completion percentage.",'','The shared progress document reports delivered SDK/module20, native UAPI0.6.0. It records all-ten Debug/Release execution for bounded slices and separate hosted/Linux references. This audit inspected concrete source and selected top-level evidence status, but did not recursively rehash or rerun that qualification. The selected SDK20 six-layout receipt explicitly says privileged device execution, not user execution. The two Linux reference boots do not establish physical hardware, SMP or complete Linux build provenance.','',f"SDK21 candidate V2 currently records **{evidence['sdk21-candidate']['status']}**; its retained command file has {evidence['sdk21-commands']['records']} command records. A failed candidate is not shared delivery. The chmod archive states it is unexported and has no actual chmod user execution. Root integration may continue after this audit snapshot; new evidence must remain separately identified.",'','`gate-mapping.json` contains exact plan exit text, individual missing clauses, source paths/lines/hashes, selected evidence hashes and ledger requirement IDs. `source-ledger.json`, `source-progress.md` and `plan-README.md` retain the audited inputs. Source references identify observed implementation, not proof of every claimed runtime behavior.','', '## Milestone findings','']
for m in ms:
 lines += [f"### {m['id']}: {m['name']}",'',f"Plan exit gate: {m['exit_gate_verbatim']}",'',m['current_concrete_scope'],'']
 for g in m['gates']:
  lines.append(f"- **{g['id']} — {g['status']}**: {g['expectation']}. {g['missing_mandatory_work']}")
 lines += ['', 'Source anchors: '+', '.join(f'`{r}`' for r in m['source_refs'])+'.','']
lines += ['## Executable dependency order','',
 '1. Finish the current SDK21 integration as a bounded independent delivery; retain failed attempts. In parallel finish M0 normative inventories with verified source pins. Do not broaden the stat/chmod slice into an M1-M12 completion claim.',
 '2. Land P04 generation-safe wait ownership described in `WAIT_FOUNDATION_DESIGN.md`, with real existing pipe/sleep/poll continuations. In parallel advance P02 fallible object/frame allocation and stable process/address-space ownership; bounded native buffers must have explicit limits until replaced.',
 '3. Use those lifetimes to enable real runnable native threads and shared address spaces, architecture TLS/FPU context, clone/clear-child-tid and futex basics. Add per-profile signals/sigreturn/restart before pthread cancellation, supervisor kill and TTY job control.',
 '4. Complete M2 shared file/socket/TTY objects, AF_UNIX/SCM_RIGHTS and namespace locking. Drive static musl pthread/process/signal acceptance through all ten profiles; then introduce dynamic ELF/file mappings/coherent page cache and complete shell/utility/locale semantics.',
 '5. In parallel with libc, extend the existing private ext4 transaction owner into the ordinary mounted writer, including allocation/extent/directory/orphan paths and default-root recovery. Do not enable the new image format before fault/FLUSH/Linux checks pass.',
 '6. After waits/FD/IRQ/DMA lifetimes exist, bring up an actual OS-owned NIC and independent peer capture, then native UDP/TCP and dual-stack configuration/resolver/time/security packages. Separately implement persistent user PID1 with real supervision and authenticated IPC.',
 '7. After shared mappings/AF_UNIX and lifecycle work, introduce user display/input descriptors and a two-client software Wayland vertical slice, then greeter/session, toolkit/PTY and real daily applications.',
 '8. Continue SMP and runtime module work from the foundation stage, not as an afterthought. Qualify advanced ext4 combinations only after their writer/crypto/quota/fencing dependencies. Close release ledger and physical/human workflows last; no emulator substitution for these gates.',
 '', '## Documentation drift and audit limits','',
 '- `ObfuscationKernel/docs/NATIVE_VM.md` still says backing only comes from the linker-reserved arena. The later process-frame implementation and ledger document firmware-qualified pools plus explicit fallbacks. Retain the historic evidence labels and rewrite the current contract around current source.',
 '- `ObfuscationKernel/docs/NATIVE_WAITS.md` still lists select/ppoll/pselect as unimplemented, while later bounded Linux adapters and progress record those subsets. Their nonnull signal-mask/SMP limitations remain; update the distinction rather than claiming complete interfaces.',
 '- Some original ledger limitation strings still mention old ABI generations or pre-integration gaps. Requirement identities and evidence source snapshots must be preserved while updating current capability descriptions.',
 '- This is a bounded source audit, not formal certification or a security audit. It does not infer absence solely from names: the strongest missing-work evidence is the explicit planned ledger plus inspected runtime/initial process/network/GUI ownership. No physical machine or real SMP receipt was supplied by the audited shared progress.',
 '', '## Recommended bounded feature','',
 'Implement `P04.wait-registration-v1` next. It replaces separate wait completion ownership in the existing native runtime with one tested state machine and addresses the dependency shared by threads, IPC, socket events, service supervision and graphics. It is independently implementable on the current serialized boot CPU and gives useful executed behavior before full pthreads. Its acceptance explicitly remains a subset of M1 and does not claim SMP. See `WAIT_FOUNDATION_DESIGN.md` for interface, ownership, transitions, races and native test gates.','']
(OUT/'REPORT.md').write_text('\n'.join(lines))
print(json.dumps({'output':str(OUT),'milestones':len(ms),'exit_clauses':sum(len(m['gates']) for m in ms),'source_references':len(refs),'all_complete':False},indent=2))
