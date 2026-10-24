# Active M0-M12 implementation continuation

User requests complete M0-M12; it remains substantially incomplete. User has no
physical machine or human desktop acceptance available and explicitly deferred
those gates, asking for implementation and automation. Never ask again. English
source/docs; Chinese progress. Preserve all ten current Kernel/OS profiles.
Shared repositories are dirty SDK20; do not reset/clean/overwrite them. Work is
in private stages. Frozen source/evidence generations are immutable. No shared
publication or V5 evidence lock yet. Do not claim models as hardware execution.

## Completed in this continuation

SDK27 full ten Debug + ten Release matrix-v2 passed:
`build/qualification/sdk27-robust-lists-matrix-v2/result.json`
SHA9ee4625be1860cf51bfeb27fa32deca491d89ff5928c9847ef05fbdc17b0dab1.
Candidate-v2 preparation SHA59587f84e1f77a8aa470202f31c8dd5c06bf5aa0ca2cfce883e182b9299b76ff.
All20 exact standalone/OS ELF+map artifacts were independently structurally
rechecked with checker-v2; supplement
`build/qualification/sdk27-map-v2-supplement-complete-v1/result.json`
SHA9f35d4ccde520a207a8dd6866ae5658a7d6c1c4f9a3f65827bc57f92ec97f031.
Original failed SDK26 and SDK27-v1 evidence remains failed/preserved.

SDK28 matrix-v1 is STILL ACTIVE session16681:
`build/qualification/sdk28-signal-masks-matrix-v1/result.json`.
Last observed: all10 Debug + x86_64 Release passed; AArch64 Release running.
Candidate966 files SHA8de94e8c9feb26eea61df61ea65e4d682ed477d6f928d33265bc36792601e310.
Uses map checker-v2. Includes inherited regressions plus raw mask/exec and musl
pthread smoke each row. Inspect final receipt; do not claim all20 prematurely.
SDK28 stage STATUS was updated and raw-mask final v3 independent binding retained
under independent-reviews/raw-mask-v3, receipt
f75c5ee602fa99cb22d060b29ec8840467d8f6adb5e9221b3be62f9eda5631a4.
All original guest/Linux/compile source pins checked. Builder SHA pins outer
compile_probe_v2.py, not nested build_musl_probe.py (both separately verified).

## SDK29 current mutable source

`build/prototypes/native-signal-actions-sdk29-v1/working/{ObfuscationKernel,ObfuscationOS}`.
Based on SDK28 candidate-v1, SDK ABI remains28 because private delivery adds no
public structure-layout change. `private_signal_delivery_fixture` explicitly
selects x86_64 Debug only; ordinary native rt_sigaction/return remain ENOSYS.
This experimental option must not be advertised as complete Linux/P06/M3.

New/changed implementation:
- pending_signals.hpp reviewed, noncopyable stable queues with queue-bound tickets,
  monotonic sequences across reset, Linux synchronous-signal priority, standard
  coalescing/RT FIFO. Final SHA
  c6d2423aa54d6bf4d871a212c697f62f3b4b6080355778366a4530e8f396ffcc.
  882266 sanitizer assertions + all10 freestanding compiles passed. Receipt
  d2584f268c8d4400aae38707d7efd9c9475cbee97fdd5fa735fa2a8a6d32a694.
- Eleven generated signal syscalls appended, old enum values preserved. Pinned
  musl/Linux110 vector controls +110 static assertions +11 Python tests passed.
  Author receipt2e3761412867f958a374dc58c1075334f40b89160e9dddfa7e808887dc71cf90.
- X86 frame v3 verified with independent1039015 placement cases, hostile restores,
 1024host FXRSTOR and fresh freestanding compile. Header
 6a5d3c7053d4810ca8761f9af198b8d7084c85159e9e9fb87c8170dcbf20ebf2.
 Receiptc07b0a61c5b590f52c7231a1590ee6ecf5cf647a1311eb166931ae1d902e6be1.
- native_signal_delivery_x86_64.hpp stages frame writes then consumes pending and
  publishes handler state. NODEFER/RESETHAND/SIGINFO/RESTORER, ordinary stack,
  sender payloads only. Independent6301 ASan/UBSan checks passed, receipt
  5f21eae7bd9933cd3af59a3ad815a99f9ca56831631d6f2c62c875396f1987c8.
- tests/native/private_signal_delivery.hpp is included by runtime.cpp only under
  explicit fixture macro. Stable128 queue slots keyed by entry-stack lifetime,
 64 action tables, lazy owner cleanup, fork action copying, exec disposition
 reset/caller pending transfer, rt action/return, same-group tgkill+tkill, safe
 user-return delivery hook. Unsupported flags, job control and blocked targets
 reject explicitly. Ordinary profiles unchanged. Runtime uses generated syscall
 numbers since kernel-v3. No new success for default production action interface.
- Xmake fixture option validated in on_load callback (initial assert-in-DSL v1
  configure failure retained).

## Actual x86 execution evidence

Standalone Kernel v2 and v3 built/exported/booted; SDK-only OS never builds Kernel.
`build/qualification/x86-signal-delivery-kernel-v2/result.json`
SHA4e4969123b42e0b8fff1a261b0c3880d7c6491dac3e4897ff88263a2beae2ced.
V3 adds generated-number dispatch and tkill, uses same unchanged SDK28 layout.

Raw guest-v1 and v2 each passed two runs: seven main handlers, nested handler,
coalescing, masks/NODEFER/RESETHAND, saved RAX edit, XMM0 restore, two fork children
with invalid FP/RIP frames terminated with SIGSEGV; parent/shell baselines healthy.
- guest-v1 SHAe8ee8da2cef9fcb3e57f703617f2abdd01b9ba75feda3c19674d3d47f7fd9cb9.
- guest-v2 SHAbd80a8c10819459bb557ee546fd1ec1ede22fd2f2a2bfefbe3fb1859dd946726.
- root probe-v2 exact ELF SHA6be4112fe253a79eb82b644f73f027023c373f43a90e36bbb4835cda3d6ccf21
  equals guest-v1 ELF; two Linux host executions passed.
- independent guest-v1 review2334 files,37 corruptions,8fault-source mutants and
  two extra Linux runs passed, receipt
  88e3380ef2d451422080253d1e5fbd69e971ee56d240991737494748f2f95ae3.
  Found diagnostic offsets [25..27]/[37] overwrote '='; only mutable source fixed
  using sizeof-derived26..28/38. Original failure detection remained sound.

Ordinary musl `sigaction`, `raise`, pthread_create/kill/join guest-v1 passed2 runs:
`build/qualification/x86-pthread-signals-guest-v1/result.json`
SHA8c8ee2d090a8fe08fabe9f335fab7fd514d30832b4318f4735c696c4cb00b342.
Actual directed CPU-running peer, TLS/errno/mask checks; no blocked EINTR/restart
or cancellation claim. Same ELF Linux runs passed at x86-pthread-signals-probe-v2.
Probe-v1 compile failed due pinned sysroot lacking compiler stdatomic.h; v2 uses
compiler __atomic builtins, no unpinned implicit header search.

New qualifier supports --probe raw|pthread; parser has explicit x86-only guard
and11 meaningful synthetic tests. All282 OS tools and offline three-original-
transcript rechecks passed:
`build/qualification/sdk29-signal-tools-v1/result.json`
SHAcfbbe36e74b5742541a76cb7ecf0a24cb6d7b574f0722829cc61a0300a97f8c7.

Final diagnostic/parser source frozen at `delivery-guest-source-v3`.
Root session57425 (`final_delivery_guests_v1.py`) sequentially runs fresh raw
x86-signal-delivery-guest-v3 (last observed PASSED) and pthread guest-v2
(last observed building OS). Uses kernel-v3 SDK. Inspect completion, pin results,
run exact new raw ELF on Linux and perform final bindings/review as needed.
Old sources/outputs remain immutable. Do not attribute earlier source evidence
without documenting these deltas.

Prior reviews copied and rehashed into stage/retained-reviews-v1; retention.json
pins all copied files. Action model portable script fixed/rerun63580 checks by
milestone_coverage. SDK29 STATUS/DELIVERY_SLICE and OS signal docs identify scope.

## Agents and outstanding parallel tasks

- milestone_coverage: active AArch64 frame implementation in separate
  build/prototypes/native-signal-frames-aarch64-v1 (check actual chosen path).
  No working/runtime edits authorized. Needs pinned Linux layout source oracle,
  hosted sanitizers/freestanding compile, disabled altstack initially.
- entry_backend_review: active canonical altstack helper/codec/ordered operation
  in separate build/prototypes/native-altstack-sdk29-v1. Task file
  /tmp/altstack-task-v1.txt. Confirmed x86 dynamic minimum needs SizeValid callback;
  Linux exec clears stack pointer/size but retains flags, unlike full reset.
- chmod_review: completed RV32 musl patch, now tasked via
  /tmp/riscv-frame-task-v1.txt to implement RV32/RV64 frame codecs in new
  native-signal-frames-riscv-v1; ensure dispatch actually started via list_agents.

RV32 musl adaptation stage `build/prototypes/rv32-musl-signal-abi-v1` is complete
AUTHOR validation, independent review still needed. Delete SA_RESTORER only from
riscv32/bits/signal.h; correct raw mask offset8, Linux copy16, libc object20 with
unused trailingptr16; public C layout unchanged. Source archive2697 files exactly
one changed. New static Debug sysroot stage/build-rv32-debug-v1/sysroot, manifest
SHA87e5f5be582f139ad17e5a0337e43087b73f2f238998ad684ac079546de5eb58.
Receipt02cf826d6bdc431ecf5b480ed139aecde4424f53606cafd823827e9ab52a3b1f.
20all-ten original/adapted layout builds,4096positive+4096negative vectors and
compiled raw+libc registration probe; no guest delivery. Original SDK28 sysroots
remain untouched. Need integrate approved adaptation only for later RV32 signal
qualification; never silently change Linux Kernel layout.

## Remaining critical work

General signal state/runtime still experimental: nine frame/return paths,
altstack, blocked syscall interruption/restart, process pending/permissions,
fault/child/timer tagged payloads, signal waits, cancellation, SMP. RISC-V/MIPS/
LoongArch need mapped return trampolines because Linux actions have no restorer
pointer. No trampoline helper has been written yet; root was inspecting pinned
musl/Linux restore assembly and runtime load page layout for next slice.

Beyond signals: general VM, IPC/TTY, IRQ-safe storage/network, journalled durable
root, real services/isolated desktop/apps, advanced ext4, runtime-loaded modules,
SMP and normative qualification remain. Physical/manual gates are deferred.
SDK24/25 all20 passed. SDK21 original AArch64 Release epoch0 code580/EIO remains
unresolved despite2+8+32 diagnostic replays; preserve failure. SDK26 original
stripped Release nm failure remains, not silently repaired by SDK27 success.

No need for routine confirmation or commit questions. User already authorized
complete implementation/automation; preserve dirty work. Continue making real
progress, update status with precise scope, avoid declaring M0-M12 complete.

## Final update after the checkpoint above

Session57425 completed successfully: raw guest-v3 and pthread guest-v2 passed
two runs each. Exact final guest ELFs each passed two host Linux references at
build/qualification/x86-signal-final-linux-v1/result.json. Final SDK/guest/Linux/
tool pins are build/prototypes/native-signal-actions-sdk29-v1/delivery-final-bindings-v1.json.
SDK28 matrix16681 now has all10 Debug + x86_64/AArch64 Release passed (12 rows);
inspect current progress before further claims.

## Latest handoff files and pending dispatch

AArch64 draft completed (author 25040 sanitizer checks + independent extracted
30-field Linux oracle + freestanding compile). Header SHA
bb673171aab23d0242d0b0af88d58ea866d1a377113eb452f25ecc710ef7535f;
receipt e016721da0493b3f1e226fd49ac39fa7ff7bfd85a7967f65a9053d9523cf4ea7.
Root read/reviewed codec and copied only its header into SDK29 working, not yet
used by runtime. Root plans static shared delivery mechanism + AArch64 frame
policy and actual AArch64 raw/musl guest after retaining x86 behavior.

Altstack headers done (agent finishing receipt). Handoff
/tmp/altstack-review-handoff.txt; 251458 model checks,256 Linux cases/2816
operations plus lifecycle, ten compiles passed. Independent review still needed.

IMPORTANT: /tmp/signal-trampoline-task-v1.txt and
/tmp/final-x86-review-followup.txt were PREPARED BUT NOT DISPATCHED as of this
write. Need send via collaboration followup to milestone_coverage (trampolines)
and entry_backend_review (final x86 guest/pthread independent review) once idle.
Do not mistake files for running agent work. chmod_review RV32/RV64 frame task
was dispatched and its draft directory is being populated.
SDK28 matrix last observed13 passed rows, LoongArch64 Release running.

## Latest active root continuation: two-profile delivery and altstack

SDK28 matrix is still active session16681; last observed18 passes, MIPS64 Release
running. Read compact JSON status, never print the 200k-token source manifest.

Two-profile pre-altstack integration completed: aarch64-signal-delivery-kernel-v1
and x86-signal-delivery-kernel-v4 passed standalone/export. OS raw guests AArch64v1
and x86v4, pthread AArch64v1/x86v3 passed2 runs each. Exact ELF byte matches verified
against2 Linux or qemu-user/Linux runs each. Binding two-profile-bindings-v1.json
SHA8be7a64abd1bc1c0f8144b85e2a8ae8ed8ea39a651f49c1066c03da418245844.
283 tools passed sdk29-signal-tools-v2. Frozen OS delivery-guest-source-v4.

Independent final x86 review receipt feb2bee60d840db9295954ecaddd6d4b2ee6854d90b3c0c4db94fb4829ab698c
(/tmp/obfuscation-final-x86-signals-review-v1) found probe TLS/old-action gaps.
Root strengthened common pthread probe with actual TIDs, handler errno, main
TLS/errno readback, known non-default prior action and old/installed/restored
queries. Frozen OS delivery-guest-source-v5. New pthread guests AArch64v2/x86v4
passed against same pre-altstack SDK. two-profile-pthread-bindings-v2.json pins
receipts. entry_backend_review independently rechecking source sensitivity now.

Current mutable Kernel adds real altstack into private experiment. Exact headers
from native-altstack-sdk29-v1 copied unchanged; shared SignalDelivery takes stack,
prepares raw saved stack+frame then consumes and commits context then AUTODISARM.
X86 place_below separates red zone; AArch64 own stack selection/frame placement.
Private per-entry-slot stack resets with queue owner, fork copies calling thread,
exec carries raw flags after base/size clear, new clone VM thread starts disabled.
Raw decode stacks use pass-through policy; Linux stack semantic errors suppressed
only after all frame validation. No public layout/ABI change.

165 new two-profile sanitizer transaction checks passed at
/tmp/obfuscation-altstack-transaction-v1; inherited delivery regression6296 passed
/tmp/obfuscation-altstack-delivery-regression-v1 (SA_ONSTACK now supported).
Frame-only x86 regression active session19282, output
/tmp/obfuscation-altstack-x86-frame-regression-v1. AArch64 codec tests+fixture+runner
now copied with header into working (header unchanged; not rerun unnecessarily).
Both new standalone SDKs passed: aarch64-altstack-kernel-v1/x86-altstack-kernel-v1.
Root active altstack_regression_guests_v1.py session to inspect via receipts:
outputs {aarch64,x86}-altstack-regression-{raw,pthread}-v1, frozen OSv5.
No actual alternate-stack guest test yet. ALTSTACK_INTEGRATION.md describes scope.

Agents now: chmod_review implementing /tmp/signal-trampoline-task-v1.txt in isolated
native-signal-trampolines-v1 after completed RV32/RV64 frame receipt
7116d89d362e329055d093d914984b9972ffd147a1138dadf28481fb4297f890.
entry_backend_review new pthread negative controls, then can review altstack
integration (it authored base helper, so must distinguish self-review).
altstack_guest newly spawned, independently implementing C alternate-stack probe
in isolated native-altstack-guest-v1. Root will copy reviewed probe and add third
qualifier kind with exact marker/admission tests, then run SDK-only guests.
Successful self-exec planned separate explicit --exec mode (qemu-user AArch64
cannot assume binfmt). No shared/frozen edits, no user questions needed.

SDK28 MATRIX NOW COMPLETE: all20 rows passed, exact profile/mode uniqueness and every
recorded command returncode checked. Final result SHAc894d2405784f044f731c4212c5e5de7a3e123eacf7c656ca242856d7ab9d03e.
STATUS updated. Do not continue treating session16681 as active.
Altstack integration review found bad-interrupted-SP recovery issue to confirm/fix;
entry_backend_review is testing Linux repro. Root165+new tests now pass v3 with
/tmp/obfuscation-altstack-transaction-v3 (v2 retained test-only compile alias failure).
Altstack guest agent draft both compiles, x86 Linux --exec passes, AArch64 qemu-user
nested raw uc_stack flags check207 differs and is being investigated; no frozen
probe/OS altstack execution yet.

## Active alternate-stack guest qualification (latest)

Independent integration review confirmed bad saved-SP rejection in v1. Fixed
working x86 selection to subtract redzone unsigned before valid-altstack selection;
AArch64 program_state validates PC/PSTATE while encode captures SP verbatim.
Decode remains strict; a handler must repair bad SP before returning.
Root transaction-v4 passed328 sanitizer checks including five badSPs/profile and
repair/unrepaired decode controls. AArch64 frame25040 checks+native compile passed
/tmp/obfuscation-aarch64-frame-captured-sp-v1. New standalone SDKs passed:
{aarch64,x86}-altstack-kernel-v2. Reviewer is independently rerunning v2 now.

Copied strict frozen native_altstack.c probe SHA85463c55f11f833fa2fa4a5b9ab3772ef726c5913eae57f9044c9379d99b4a23
to working OS. Source agent receipt32e91fe1e1f70518b424406d379028f7cf82622633b2b6af80bae7ee67a845fa
at native-altstack-guest-v1/receipt.json; validation-v3 stronger mutants.
Native x86 Linux core/--exec2 runs each passed; AArch64 qemu-user8.2 does not
implement raw nested flags/AUTODISARM, explicitly failed reference retained.
Do NOT weaken OS checks or claim qemu-user full pass.

Qualifier now has altstack/altstack-exec kinds. Exact marker/checkcount/execchild
order and prompt/accounting controls tested (13 parser tests;284 all tools at
/tmp/sdk29-signal-tools-v3.log, then13 parser rerun after absolute path fix).
OSv6 frozen at delivery-guest-source-v6; first altstack guests both failed code152
because argv0 was shell PATH basename and raw execve does not search PATH.
Do not modify failed artifacts. OSv7 switches only altstack command invocation
to /bin/native-signal-altstack-{arch}; exact probe stays unchanged.
Currently ACTIVE session95116 altstack_guests_v2.py, sources delivery-guest-source-v7,
outputs {aarch64,x86}-altstack-guest-v2, pinned kernel-v2 SDKs, --exec2runs each.
Inspect receipt/serial next. Minimum lease delta6 (main+4fork+pthread; exec reuses
leader lease), not7 suggested by probe author; successful exec has explicit child
marker plus native image evidence.

Agents: entry_backend_review independent v2 altstack review; chmod_review i386
legacy+RT frame isolated implementation via /tmp/i386-signal-frame-task-v1.txt;
altstack_guest now separate bad-SP actual guest probe via
/tmp/signal-bad-sp-guest-task-v1.txt (3 repaired parent deliveries,2faultchildren).
Trampoline helper finished: native-signal-trampolines-v1 receipt
6e2175d396a6a61f4f727c71792f0528e4650c068abe07c8a7d2522c692d2712,
header09b772f821454a3211a0e986cd8b30477989e238f7765830a9e615693dc1af1b.
Five targets/six entries/23146checks exact bytes, author validation only. Runtime
map not yet integrated; root wrote RISCV_INTEGRATION.md concrete next contract.

## Latest root checkpoint before continuing

SDK28 all20 finalreceiptc894d2405784f044f731c4212c5e5de7a3e123eacf7c656ca242856d7ab9d03e.
Altstack final OSv8 frozen includes exact altstack and bad-SP C probes and all
5 qualifier kinds; inventory SHAb1517523b84f3e5e4eac71b24c9816b20de1e2024af150de77a0f0f0e02fff61.
Root session17609 altstack_and_bad_sp_guests_v3.py STILL ACTIVE. Both
x86-altstack-guest-v3 and aarch64-altstack-guest-v3 PASSED2runs --exec each;
x86-signal-bad-sp-guest-v1 and aarch64-signal-bad-sp-guest-v1 now building OS.
All use fixed kernel-v2 SDKs. Need inspect completion then finalbind/review.

First altstack OSv6/v1 code152 failures preserved (argv0 PATH basename).
OSv7 x86v2 completed program, parser failed because nested stack exhaustion
raised expected hardware fault=contained; AArch64v2 passed. OSv8 explicitly
admits max2 fault lines for the2intentional children AND exact entry counter
faultdelta match. Synthetic positive/negative accounting tests added;286 OS tool
tests passed and retained at build/qualification/sdk29-signal-tools-v4.
13=>14=>15 parser test updates; full current suite286. Root offline recheck
of x86v2/AArch64v2 succeeded with new parser, original failedreceipt unchanged.

Independent integration review v2 complete: receipt
ef96eb08bc49cbea671c860d61486b856f4caf2b19466d61259b0465da4af6bf.
560 transaction +258badSP sanitizerchecks,6repros,3Linux references passed.
Both700/705-file frozen inventories checked; helperself-author role disclosed.
V1 badSP defectreceipt582b33f671231a52e87f603b90a5835f1564ef072b9277d90a8243a236688d78 retained.
Both reviews now copied/rehashed stage/retained-reviews-v3.

Bad-SP actual probe completed/frozen: native-signal-bad-sp-guest-v1/receipt.json
SHA3b7c9c3e984fdd26f2b0222934041b1f7f095d1fa369d2f9192e6633a810a4d9;
source4b5ea9dfb6c2f0fb8dfcb947c3f9aa25df69abd290d0858ebf0979bc804b581e.
2Linux x86+2qemu-userAArch64 passed;4source mutants reject;3repaired parent
SPs+2faultchildren,2markers and count18; min3leases. Copied unchanged into OSv8.

IMPORTANT pending dispatch: /tmp/altstack-final-guest-review-task-v1.txt and
/tmp/loongarch-signal-frame-task-v1.txt are PREPARED BUT NOT YET SENT.
entry_backend_review now idle after integration review; assign first task
(independent final probe/harness/binding review, can start before guestsfinish).
altstack_guest now idle after bad-SP probe; assign second task isolated LA64frame.
chmod_review already active i386 legacy/RT codecs via taskfile.
Do not mistake prepared files for active agents. Next root step after current
guestbinds is RISC-V frame/trampoline map integration per RISCV_INTEGRATION.md;
no new RV runtime code written yet. M0-M12 remain substantially incomplete.
