# Continuation checkpoint: MIPS signal policies and admission

The user requests the complete M0-M12 plan. It is still substantially incomplete.
Keep the goal active. The user deferred M11 physical machines and M12 manual
desktop workflows; continue implementation and automated acceptance without
asking again. Preserve all ten Kernel/OS profiles and exact SDK boundaries.

## Workspace and sources

Workspace: /media/data1/Project/System/ObfuscationProject.
Do not modify shared dirty ObfuscationKernel/ObfuscationOS repositories.
Mutable private source:
build/prototypes/native-signal-actions-sdk29-v1/working/{ObfuscationKernel,ObfuscationOS}.
Frozen sources and sealed evidence stay immutable. No commits/publication.
English source/docs, Chinese progress. No skill applied.

Working Kernel has NOT changed during this turn. Private Debug signals support
seven profiles: i386, x86_64, AArch64, ARM32, RV32, RV64, LoongArch64. Export
layout is SDK28; production action/return dispatch remains ENOSYS.

Latest frozen OS is delivery-guest-source-v29/ObfuscationOS:308 files, inventory
SHA256 d5f5c1817778fb9ca65428b3e60c9b55db745363125f4fd3e3ca25791acbd9d0.
It adds MIPS o32 common altstack/bad-SP sources, pthread architecture marker,
explicit parser/qualifier admission and parser controls. Tools suite309passes:
build/qualification/sdk29-signal-tools-v19. OSv28 remains exact raw LoongArch
qualified source. mips-os-before-v1 preserves changed OS sources.

## Root work completed this turn

1. native-signal-delivery-mips-v1:sealed isolated o32 policy,79,945 sanitizer
checks plus6,670 existing x86/AArch regressions; freestanding MIPS object has
only memset unresolved. Receipt
1a8b4f2c88d5e030a94063f796c7e824b10aefcafdb3fff65e5059b6b7712115.
Preserved initial warning-as-error failure and v2 source before expanded tests.
Adds typed context, SI_KERNEL8 zero payload, checked BE FCSR+force transaction;
generic SignalDelivery context now deduced rather than u32 in this stage only.
NOT integrated into working Kernel. verify.py rehashes108files/tools.

2. native-signal-delivery-mips64-v1:sealed isolated n64 policy,41,664 sanitizer
checks; freestanding ELF64BE n64 soft-float software object only needs memset.
Receipt6f83a225c48e187748d15cd7f0b4fba398c320c044c7bedc7f6cdb765ea80256.
Always RT808, alignment16, native64 pre-gap placement, full v0/a3 and raw stack
metadata, checked BE FCSR+force; all author attempts passed. NOT independently
reviewed or integrated. Uses separately sealed n64 codec below.

3. mips-pthread-signals-linux-reference-v1:OSv29 exact pthread ELF built with
pinned musl and passes twice under qemu-mips24Kf. Linux/qemu-user reference only,
not system-QEMU ObfuscationOS.

4. LoongArch raw independent review retained-reviews-v16, receipt
21fea75d0ac057ebd44543bcd68c51461a1055c39ef3d41d31a3d09d7f3a4c49.
2,162files/4,145external identities; fresh canonical raw boot+63probe source
mutants,111transcript controls,206static+12ABI. No Kernel implementation mutants.

5. MIPS prerequisite audit retained-reviews-v17, receipt
7d93bc00db946dac48867646a80654357569ec14f005f35e94700e021adb723d.
Actual 24Kf CP0/FIR/FCSR readbacks;76timer captures/75BD;3wrong-EPC backend
mutants fail exact delay side effects.2earlier EPC controls separately retained.
Initial flags0, missing admission and dropped Cause.BD prevent naive integration.

6. STATUS.md and LOONGARCH64_EXECUTION.md now include final raw native passes.
MIPS_INTEGRATION.md records current policies, probes and integration hooks.
osv28-bytecode-audit-v1.json proves5uninventoried OSv28 cache code objects equal
fresh compilation of frozen sources. Do not change frozen source/cache files.

## Other sealed author stages

native-signal-frames-mips64-v1:receipt
77ef2b59d9f213da224ef2e35bc254fca95375e44da21b771eb24ebc5cd7fc86.
394,276sanitizer checks,10mutants;433files root-rehashed. Actual n64 RT808,
FR1,64-bit GPR/HI/LO,offsets/layout oracles. Needs independent review/runtime.

native-signal-frames-ppc-v1:receipt
45111ec4304948f668f538452d7366b3f63d9a12a2eea88c975a653e5029eaf3.
570,094checks,22implementation mutants;578files root-rehashed. Native32 e500/SPE
legacy+RT; untouched224-byte ABI gap; redirected context pointers. Native
object/libgcc relocation leaves only kernel memcpy/memset. No classic FPSCR,
no runtime/SDK/OS qualification. Needs independent review/policy/backend gates.

native-mips-altstack-guest-v1:receipt
67d08be134c3c890a2446f53afd109fe1cbd72624af1b82a965123014d95cc09.
1,701artifacts root-rehashed before source integration.70ABI,23source mutants;
14prior architecture object/ELF pairs unchanged. Bad-SP twice18PASS;altstack
core/exec4strict107/207failures retained. First cache-audit failure preserved;
all reported results rerun from exact308-file inventory-only OS tools copy.

## Active agents (revalidate status)

chmod_review: after sealed prerequisite audit, implementing isolated
native-signal-mips-admission-v1. Task actually dispatched via
/tmp/mips-o32-admission-implementation-task-v1.txt. Owns backend CPU readback,
private frame-bound token, lease readiness and native validation. Draft APIs:
include/ok/arch/mips_o32_private_signal.hpp,
include/ok/user/native_signal_readiness_mips_o32.hpp,
include/ok/user/native_signal_gate_mips_o32.hpp.
DRAFT UNSEALED: do not integrate yet. Preserve UserFrame/Trap/TCB SDK28 layouts.
Its child /root/chmod_review/elf_admission implements checked ELF32BE o32
PT_MIPS_ABIFLAGS helper/tests in /tmp, to be imported into parent's stage.

entry_backend_review: completed PPC codec, now actually dispatched independent
o32 policy review via /tmp/mips-o32-policy-review-task-v1.txt. Original o32
codec authorship disclosed; review is independent of root's new policy only.
No working source edits. Sent exact runtime fixture/prior review paths.

altstack_guest: completed and sealed MIPS common probe port; now idle (its slot
was used by chmod_review's ELF subagent). Can next independently review n64
policy but must disclose its n64 codec authorship, or author raw MIPS guest.

## Required next work

- Inspect/verify active admission and o32 independent review; fix concrete defects
in new versions, retain sealed evidence. Do not falsely supply enum attestations.
- Integrate o32 only after gates. Need128signal queue,16-byte action masks,MIPS
job-stop numbers; backend private eligibility; initial/fork/clone/exec/entry/
capture/handler/sigreturn lifecycle; preserve v0/a3; owned RX32-byte dual-entry
trampoline. TimerBD defers handler without mutation or EPC advance; ignored/
default dispositions can process. Reject unsafe syscall delay operands before
backend overwrites original EPC. No guaranteed BD-loop signal liveness claim.
- Build/export/boot standalone MIPS Debug then exact SDK-only OSv29 pthread,
altstack-exec,bad-SP guests. Native signal execution has not happened for MIPS.
Use a new builder generation; v6 allows only earlier7profiles.
- Review n64/PPC codec/policy independently and continue full signal/ABI/runtime
work before larger milestones. M0-M12 remains incomplete: targeting/permissions,
restart/cancellation/job control,general VM,IPC/TTY,journalled modern ext4,
IRQ storage/network,supervised services,isolated desktop,loaded modules,SMP,
Release and normative qualification are substantial outstanding work.

## Latest completed LoongArch execution (for reference)

Standalone loongarch64-signal-delivery-kernel-v1; SDK manifest
 d76c27005d9319026aa88b6404b29e4fb16d252e223d73c6862091bfc0ac05ad.
Five guests each pass2actual OS QEMU runs: pthread-v3(OSv25),altstack-v1,
bad-sp-v1,mapping-v1(OSv26),raw-signals-v2(OSv28). Raw source-v3 ELF
7dbde4273324cb020651e5380a1ac3098f958daa82156fe67e3ce0452678c745.
Binding loongarch64-bindings-v2 rehashes14,988files;SHA
3586cf681aa90d1dafe8af588a8ad6b3c6dc814f162b978ed6dc8e126d2b8a70.
Raw v1 failure ORI-only oracle corrected to ORI/ADDI.W exact pair with syscall0;
no Kernel repair; strict Linux qemu-user reference failures remain failures.
VFS31-byte component limit remains; native command aliases use la64.
