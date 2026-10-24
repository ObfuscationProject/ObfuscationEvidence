# M0–M12 continuation — ARM32 integrated signal execution

User still requests the full implementation. The active goal remains incomplete.
M11 physical and M12 human desktop acceptance are explicitly deferred; do not ask
again. Continue implementation and automated qualification. Preserve all ten
profiles, Kernel/OS ownership, C++23/xmake and exact SDK consumption. Chinese
progress, English code/docs. Shared dirty SDK20 repositories were not edited;
all new work remains in private build/prototypes and qualification stages.

This snapshot supersedes older ARM/i386 agent states. Historical snapshot:
`build/CONTINUATION-before-arm32-integration-v1.md`.

## Terminal / agent state

All root sessions in this slice are COMPLETE. Do not poll old IDs:
28344, 92999, 62825, 89825, 15771, 79369, 32039, 71788, 28086,
6370, 31078, 69838, 91652, 80274, 98322.

All three agents most recently completed their tasks:
- chmod_review: ARM32 codec and policy/runtime independent reviews.
- entry_backend_review: i386 entry review+repair, then authored ARM32 raw probe.
- altstack_guest: ARM32 backend independent review and pthread parser repair.
No new task was dispatched after these completions. Revalidate agent states.
Prepared next review task files (files alone do NOT start agents):
- `/tmp/arm32-raw-independent-review-task-v1.txt` — suggest chmod_review.
- `/tmp/arm32-altstack-independent-review-task-v1.txt` — suggest altstack_guest.
The older `/tmp/arm32-altstack-port-task-v1.txt` was NEVER dispatched and is now
marked superseded; root completed that port. Do not implement it twice.

## Current mutable and frozen source

`build/prototypes/native-signal-actions-sdk29-v1/working/{ObfuscationKernel,ObfuscationOS}`.
Private Debug signal delivery now supports i386, x86_64, AArch64, ARM32, RV32,
RV64. Exported ABI layout remains28. Production actions/returns remain ENOSYS.
No full signals, M3/P06, SMP, Release or complete M0–M12 claim.

Latest frozen OS source is `delivery-guest-source-v23/ObfuscationOS`, inventory:
`8ffeaa6d869f3ace41d000f38b0bb9a90afdaf82027f7dd3daacac0325b4bfae`.
306 source files. Frozen OSv23 full tools:301 passed at sdk29-signal-tools-v13.
Earlier OSv22 tools300, OSv21 tools299 are retained; no failures in these suites.
Read mutable stage `STATUS.md`, `ARM32_EXECUTION.md`, `I386_EXECUTION.md`.

## ARM32 implementation now integrated

Root authored isolated `native-signal-delivery-arm32-v1`:
- `native_signal_delivery_arm32.hpp`: SA_SIGINFO selects static legacy/RT;
  explicit SA_RESTORER; raw altstack / AUTODISARM; full checked transaction.
- `native_signal_return_arm32.hpp`: both syscall SP direct, explicit normalized
  returned FPEXC publication into backend slot, required mapping callback,
  staged register/FP/mask commit, RT-only alternate stack application.
- Author21450 ASan/UBSan checks; ARM and Thumb freestanding objects.
- Compiler emitted memcpy/memset references (Kernel supplies them). Initial
  zero-undefined-symbol inspection expectation failed and is recorded; actual
  final Kernel linkage later passed. No fake no-undefined claim.
- Receipt46 files SHA
  `97ab4cf897374a6d22a969f0b3c62ead3123716d4456429a235db45b083d4e9e`.

The unchanged codec and actual FPEXC backend from prior isolated stages have now
been copied into SDK29working, including existing extended ARM native tests.
Integration changed11 Kernel files; prior mutable versions retained in
`arm32-integration-before-v1`; `arm32-integration-v1.json` binds final files.
`build_private_target_v5.py` admits ARM32 Debug beside other five private ISAs.
Runtime includes ARM policy, validates handler PC/restorer RX and writable SP-1,
routes119/173, suppresses ordinary syscall completion (restored r0 survives), and
applies altstack only on RT. New backend retains actual user FPEXC fp_state260.

Bounded hardware contract: little-endian synchronous ARMv7 D32/Cortex-A15;
FPEXC must be canonical EN. No FPINST hardware capture or general capability
probing. Zero FPINST payload represents excluded pending state, not measured
zero hardware registers. Preserve this restriction in future integration.

Documentation correction: immutable policy DESIGN says complete instruction
extent, which is too strong. Actual runtime admits minimum ISA-aligned fetch
(ARM4 bytes/Thumb2 bytes), not decoded full Thumb-2 instruction length. Crossing
into an NX page can still cause contained user fetch fault. This is documented
in stage ARM32_EXECUTION.md and independent policy report; no code change needed.

## New actual ARM32 execution

Standalone `build/qualification/arm32-signal-delivery-kernel-v1` passed full
build/export/boot. Result SHA
`35869db5c3dbd6f6bbdac74792f373240b4c69ca05909fdc0a9ceab0eded776f`.
Exact SDK manifest
`d1c20b235bea05a975ae8604df18b66b7e581b6d4362818045c1e858a75a5dd4`.

Four SDK-only native OS guests each passed two Cortex-A15 QEMU runs:
1. `arm32-pthread-signals-guest-v1`, OSv19: musl raise/pthread_kill, peer,
   siginfo/masks/TLS/errno/join. Result832d8758ca67f3864b3196fdae40cb78503c6c5a958349d06a6b2406d6d6cf42.
2. `arm32-signal-delivery-guest-v1`, OSv22: strict raw legacy/RT, all eight
   handler/restorer ARM/Thumb combinations; ARM+Thumb interrupted callers;
   actual edited r0, D0/D15/D16/D31 and FPSCR restoration/edits; 88 primary
   handlers,8nested,96actual restorers per run; masks/highword/coalesce/NODEFER/
   poisoned all-fields RESET query;4bad-return children with valid exit sentinel.
   Result2b45d2fb14125d14c6c09a460d65909cc201478e3a44311c4487b8cacd95cf84.
3. `arm32-altstack-guest-v1`, OSv23:37checks/run including successful exec,
   nested/onstack/AUTODISARM/raw stack restore, fork/pthread/failedexec/2children.
   Resultdaba6782c86427696807373283cef00c03cc51430327ab263a5b2ca4fb1f2eb8.
4. `arm32-bad-sp-guest-v1`, OSv23:18checks/run,3badSPrescues,first2postSVC actual
   cookie loads through returnedSP,2children.
   Result407cbaed2b57a61c1f05309ef0cf40a4f27b5280c2c211345063693859d6095c.

Each retains exact source/SDK/ELF/rootfs/disk/serial/accounting/commands and runs
native pipelines before/after. OS compiles no Kernel source. No SMP/hardware board.

Raw probe author stage `native-signal-guest-arm32-v1` by entry_backend_review:
receipt165 files SHAf79933228fbe87495712d49020ea53692c4e7830edaca29e8cf9bb83be8035c7.
Strict source0822a8becb4afb8d6ee981b4351ee9ef5287e4c06f0faf5ee33ee100812c25ea.
Strict ELF aee7f611cd8ec7b1439ceee118655bb18c3508ad8e0b49cd83925d43702ea730 is
BYTE IDENTICAL to the actual OS guest probe ELF. Root reviewed source before use.
Strict qemu-arm Linux reference fails twice: legacy uc_flags is0 instead of Linux
0x5ac3c35a. A separately labeled diagnostic removes ONLY that assertion and passes2;
13diagnostic controls reject. Strict source kept original assertion, OS passes it.
Do NOT describe strict Linux reference as passed. Raw guest independent review pending.

Altstack/badSP author stage `native-arm32-altstack-guest-v1` by root:
receipt81files SHA f96f811ed50118c9f33e5689ccdd46c6218b73ee5b92b538df94e598cde6397d.
Common assertions unchanged; ARM-only packed/aligned4 action wire fixes20bytes/
maskoffset12 without altering other ABI. Actual musl arm_sp. AAPCS callee saved
regs and8alignment; first2postsvc loads via restoredSP. Exact source/ELF compile
via pinned OS tool; author/OS ELF byte-identical. Six badSP omission/cookie controls
reject under qemu-user. Strict badSP Linux emulation passes18checks; strictaltstack
core+exec fail107/207 nested rawuc_stack. Preserve failures, no assertion relaxation.
No legacyAUTODISARM execution claimed (policy models cover it); independent review pending.

## i386 independent review found and corrected real probe defects

Frozen OSv18 entry probe had EIGHT false-positive permission controls: removing
NX or readonly protection still passed because zero instructions or later empty
stack returns caused unrelated SIGSEGV. Original entry guest-v1 is RETAINED but
its permission assertions are INVALIDATED; positive segmented checks remain useful.

Independent review receipt `/tmp/obfuscation-i386-segmented-entry-review-v1/final-v1/receipt.json`
SHA64df3879fdb5d2d66a588517798af75c553aa62db847e5b35df1b51522ce1c72.
2393bindings,54parser controls rejected,13positive segmented controls rejected;
8permissionomissions incorrectlypassed. Geometry: raw segmented ESP need not be
mapped; actual effective SS.base+ESP is admitted. Earlier task's mapped-raw wording
was impossible with current i386 user window/TLS restrictions; corrected docs.

Agent authored separate `/tmp/obfuscation-i386-entry-repair-v1`, receipt
b1ca54b811c3a3741a3920b6e9f048906618905a6726d9d836c5fd0d1c9e7b21.
Source36440c28083edfbd39ea1fa8b7ff1ca8b9eaa57d7034fc9e46730f2974fce6e6.
Fix: readonly landing's FIRST instruction stores -4(%esp), then direct exit95
without C/stack return. NX page has normal exit95 machine code, not zeros.
All8permissionomissions now reject, plus13positive controls+landing-store omission.
Root independently inspected source and actual assembly, copied unchanged toOSv20.

New `i386-signal-entry-guest-v2` passed2 actualOS runs using unchanged exact i386
signal SDK. Result1929c3ba67e4d68d32c4eec80b10edbc00d1a65c52bdd364fca2013f13d1b8a0.
Actual probeELF7fa5f14e989381e9c3128a0537c86eedd38e819b8c007e57cc54f0dafbb1bb85
also passed2 EXACT localLinuxELF32 executions at
`i386-corrected-entry-linux-reference-v1`, result
0da8650fb52e379620b666c3ddae5cbdabc9c5d5357bc00184f867077b7f4132.
The source-identical author's ELF differed, so root ran this exact final ELF too.
SandboxblocksELF32signals; narrowlocalself/childtestescalation approved, no rejection.
No physical-machine or newOS claim fromLinuxruns.

## Completed independent ARM reviews and parser repair

Codec: `/tmp/obfuscation-arm32-signal-frame-review-v1`, receipt
99b295cb928c239f8f6563872e2aaad3c1331872227b315d1dfb95c9aac7b5fd.
50930ASan/UBSan checks,6mutants rejected,Linux43+musl15layout/restorer oracles.

Backend: `/tmp/arm32-fpexc-independent-review-v1`, receipt
6e81c925b6fdfdb8cc815999437749f567acbe33f3278239472951666107f0e0.
135952native checks,14independent standaloneQEMUexecutions including8rejected
backendmutants andactualFPEXC0capturecontrols. EN0/EN1 kernel preservation and
CPACR none/privileged/full covered. Bounded synchronousD32 pass, no backend defect.
Found existing ordinary pthread evidence parser accepted missing/duplicateimage.

Parserrepair: `/tmp/arm32-pthread-image-admission-repair-v1`, receipt
7e58b0f94c5efaeec40eb1f89759ac5451ceed132e808af53a2082dee00ad946.
Rootreviewed/copiedexacttwofiles intoOSworking (parser + tests),OSv21onward.
Requiresoneimageperprobe,firstoutput,correctfirmware/linkersource,uniqueexisting
OK_LINUX_ABIarchbootmarker.297authortoolspass;12serialcontrolsreject;oldparser+
4omissionvariantsfailnewtests. OriginalARMordinarypthreadtranscript replays
identically. These are parser checks, not freshguest execution.

All above +i386review/repair copied unchanged to stage retained-reviews-v9:
13937 files; retention9135ee4deb278ef794517e918b9b90cc94fbb40e4ecb2f8e76fe675be3680448.

Policy/runtime: `/tmp/obfuscation-arm32-signal-policy-review-v1`, receipt
3816979a6a3560098709719337b030c3f96dab2031a122b953dbe6b09bd8f9ad.
26876ASan/UBSan checks,6mutants rejected; exactprivatefixture, realPCB/TCB with
hostedowner/mapping/finishstubs; no fullscheduler/hardwareexecution. Copied to
retained-reviews-v10,986files, retention
052789e0835934ecb1047ca964733882b9dcc8074c9b849093ce2d56635da06f.

Root `arm32-i386-bindings-v2.json` rehashes14169 files across6guestresults, replay
withlatestfrozenOSv23validators is identical. Includes4newARMsignalguests,newi386
entryguest,andolderARMordinarypthreadguest. BindingSHA
75e311121dd4b9d4d1d420cf744bc87abbb7db53e62dc61bacfef1b4a82c1928.
No newexecution inferred from rehash/replay.

## Immediate useful work

1. Dispatch prepared independent ARM raw/pthread and ARM altstack/badSP reviews;
   keep unrelated useful implementation moving. Files alone are not dispatch.
2. Remaining signal ISAs: LoongArch codec previously reviewed, not integrated;
   MIPS/MIPS64/PPC codecs absent. Preserve backend FP/TLS/entry capabilities and
   exact frame oracles; do not pretend missing FPINST/capabilities are supported.
3. Real legacy AUTODISARM persistence tests would strengthen ARM/i386 coverage.
4. Larger backlog remains process targeting/permissions, typed payloads,
   interruption/restart/cancellation, general VM, IPC/TTY, durable journalled root
   and modern ext4, IRQ-safe storage/network, supervised services, isolated GUI,
   loaded modules, SMP and normative release qualification. Old SDK28 ten-profile
   Debug/Release matrix predates these private signals; do not reuse it to claim
   this source is release-qualified. Keep goal active; do not mark M0–M12 complete.
