# Active M0-M12 continuation — current authoritative handoff

## Latest terminal snapshot (supersedes running states below)

All root processes have finished. Sessions42012,9082,92400,56246 are COMPLETE;
do not poll/restart them. x86/AArch64 entry-checked raw/pthread/altstack/bad-SP
v1 all passed; source-port altstack/bad-SP v2 also passed. RV32/RV64 altstack-v1
and signal-bad-SP-v1 each passed2 native runs against corrected Kernel-v2.
Latest frozen OS source is delivery-guest-source-v14, inventory
 a6ee9daad5f9158f1d4fa93635ab039d75b1013e77546a5879843ae3dd4f3658.
Latest parser requires fault-counter delta to match admitted contained-fault
lines in EVERY command, including raw/pthread/entry and baseline/tail. New
synthetics cover coherent counter increments. Full OS tools291 pass at
build/qualification/sdk29-signal-tools-v7/result.json.

Final author20-guest/4-kernel/24273-file binding:
stage/riscv-and-altstack-bindings-v2.json
SHA7a9f9e4ee31d08350765fb62d307dcf498ed88d972f94d4c1aea3ee0fc2c3f24.
This is four-profile private signals, not a fresh all-ten architecture matrix.
Independent corrected runtime review closed RV-SIGNAL-ENTRY-1:
/tmp/obfuscation-riscv-signal-integration-review-v2/receipt.json
SHA6fc77385acd0aa70a39a8135f41593affbbb9144fd1a8352122737221f51d26b.
18160 checked-entry/model/runtime checks; boundary ELF at0x40002000 verified.
Independent RV core8-guests finalreview also complete, closes fault-count gap:
/tmp/obfuscation-riscv-final-review-v1/receipt.json
SHA6e69c3f3660cefd9d52a79a0a901388b352d554744969bde6465a77a6e570e81.
476 RV and238 priorx86/AArch corrupted logs rejected;11074 files bound. It
excludes the newly added RV altstack/badSP native guests. Original reports,
failed strict references and old-kernel exit127 negative control remain.
All these reviews/models copied under stage/retained-reviews-v5,1749files,
retentionSHA76cf6b97b8ad19000b030082bd576ef8980e2792949b78124a3e543667d6308f.

RV altstack source stage native-riscv-altstack-guest-v1 COMPLETE authorvalidation:
receipt1c0b364b30617ee6ac328b19f8ec7666e03dba1c88c11fdcbdc3d88bd9e1139f.
altstackSHA4222e1bd929357a52da8970f66e6a27aa9334d8624b27de993c2b739ab81b01a;
badSPSHA1bc9856d3a95da4d088be608509424dbf0e7b9bcb503e5fe2defc9d24f675989.
Strict badSP references2/profile pass,18 source controls reject. Strictaltstack
qemu-user reference fails nestedflags/placement andAUTODISARM; kept explicit.
Ports are integrated into working and frozenOSv14. New native4guests pass but
independent review is still needed. Prepared bounded task file:
/tmp/riscv-altstack-final-review-task-v1.txt (NOT yet dispatched at this snapshot).
Next i386 policy task prepared /tmp/i386-delivery-policy-task-v1.txt (NOT yet
dispatched; no i386 policy/runtime code written by root). Agents from this turn
completed their prior tasks; revalidate live agents and follow up rather than
assuming these task files alone imply work started. Useful next parallel work:
new RV altstack independent review + i386 policy/integration + remaining ISA
frame codecs. Root can continue native runtime integration after reviewed code.
STATUS/RISCV_EXECUTION updated with current qualifications. Main goal remains
substantially incomplete and must stay active. The historical sections below
locate older evidence; their live/pending statuses are superseded here.


User objective remains complete M0-M12; substantially incomplete. Physical M11
and human desktop M12 acceptance are explicitly deferred; do not ask again.
English code/docs, Chinese progress. Preserve all ten Kernel/OS profiles.
Shared dirty repositories remain SDK20; do not reset/clean. All ongoing source
is private stages; frozen source/evidence generations are immutable. No shared
publication or V5 release lock. Model/compile/Linux/qemu-user/native OS/SMP and
hardware claims remain separate. Old historical continuation is retained in
`build/CONTINUATION-before-riscv-entry-v1.md`.

## Completed baseline

SDK28 all20 ten-profile Debug/Release matrix is COMPLETE:
`build/qualification/sdk28-signal-masks-matrix-v1/result.json`
SHAc894d2405784f044f731c4212c5e5de7a3e123eacf7c656ca242856d7ab9d03e.
All20 unique profile/mode rows and command returncodes rechecked in binding
script. SDK27 all20 plus hardened map supplement also complete. Preserve prior
SDK21 AArch64 Release epoch0 EIO failure; SDK26/27-v1 failures are retained.

## Mutable source and scope

`build/prototypes/native-signal-actions-sdk29-v1/working/{ObfuscationKernel,ObfuscationOS}`.
SDK ABI28 layout unchanged. Explicit Debug fixture supports x86_64/AArch64/RV32/
RV64; ordinary production action/return dispatch remains ENOSYS. No full M3/P06.
Canonical actions/queues, generated signal numbers, shared static transaction,
altstack/AUTODISARM, same-group tkill/tgkill, fork/exec state, fixed FP frames.
No interruption/restart/cancellation, process targeting, typed fault/timer/child
payloads, permission model, SMP or production signal claim.

## Final x86/AArch64 altstack review closed

Fixed original Kernel SDKs: `{x86,aarch64}-altstack-kernel-v2`.
Final stronger altstack guests `{x86,aarch64}-altstack-guest-v5` passed2each.
OSv10 inventory4bc4fb0a0c326fe22c430369e548ef0b23dbb6534dc287a84808ef78d29dbe4c.
Bad-SP `{x86,aarch64}-signal-bad-sp-guest-v1` previously passed2each; unchanged
source/ELFs rechecked with final parser, explicitly not fresh execution.
Review closed3findings: poison all initial old-stack fields; require1 Linux
image per probe or2before exec-child marker; fault lines before parentPASS.
Independent238 parser corruptions and26 probe mutants reject,6630 files bound.
Final review `/tmp/obfuscation-altstack-final-review-v1/receipt.json`
SHAedb77cacf655a3c9ab2279ea2c749ad26c9ab4aa9bad4b51b0f89fd81df57491.
Earliercopyout/parserescapes remain retained. Qemu-user AArch64 altstack strict
reference remains unsupported (raw nested flags/AUTODISARM), never claimed pass.

## RV32/RV64 actual execution, and entry fix

Initial exact Kernel-v1 SDKs both built/exported/booted. Frozen OSv11 pthread
`{rv32,rv64}-pthread-signals-guest-v1` passed2each with TID/errno/TLS/disposition
checks. RV32 uses explicit maintained musl adaptation at
`build/prototypes/rv32-musl-signal-abi-v1/build-rv32-debug-v1`; pass directory not
sysroot. ManifestSHA87e5f5be582f139ad17e5a0337e43087b73f2f238998ad684ac079546de5eb58.
Original SDK28 sysroots unchanged; shared musl recipe still has no patch hook.
Frozen OSv12 `{rv32,rv64}-signal-delivery-guest-v1` raw and
`{rv32,rv64}-signal-mapping-guest-v1` each passed2. Mapping probe tests8denials,
hintfallback/adjacent bytes/writefault/fork/failedexec/successfulexec/replay;
min3leases and2ordered images. OS-only reserved-page policy, not Linux vDSO.
Raw coversA0, actualF0/FCSR, editedTP withlibc restoration, returncode bytes,
mask/nesting/coalescing/NODEFER/RESETHAND and2badreturnchildren. Strictqemu-user
raw mask references failboth; separate mask-excluded diagnostics not acceptance.
Ordinary pthread reference passesboth. Probe stage
`native-signal-riscv-guest-v1/receipt.json`
SHAf337115145dd757a76b812e29e3b88005acf320dc3464bd76b5d414695f6436a.

Author exact binding12guests/6kernels/18817files plus offline parser recheck:
`stage/riscv-and-altstack-bindings-v1.json`
SHA5fc90730f1a5f5e6c0d34e2788c1de054e6f37a769c3a48ed96c987f9ed9bf54.
This binds onlyv1 runtime, NOT the fix below. SDK-only consumers compile noKernel.

Independent root integration review found RV-SIGNAL-ENTRY-1(P2): stagedSP==begin
or invalidPCmapping could commit thenbackend rejectexit127. Original report
`/tmp/obfuscation-riscv-signal-integration-review-v1/receipt.json`
SHA815219a2c83183dae9686ed6e9b1b174ef6a19b5c120aef85869ab1c1bbbc740.
17066 model+138 actualruntimefunctions checks passedotherwise (perprofile scope
inreport), authorship of codec/trampoline/port disclosed.

Root FIX now inworking: common deliver overload accepts staticCanEnter callback
AFTER byte preparation but BEFORE queue/mask/action/context/AUTODISARM commit.
Runtime passes private_signal_can_enter checking PCnumeric/alignment/executable
page and actual writableSP-1; sigreturn applies same validator before restoring
live state. Invalidtarget finishesSIGSEGV. Userbytes may already be modified,
per existing partialwrite/failedconsume contract. No backend source change.
Exact corrected `{rv32,rv64}-signal-delivery-kernel-v2` built/exported/booted.
Frozen OSv13 inventory
487a7b95c8b1f07b4bdf5a9d5120a3b2ddb85b6bfa2d8d2a84dcfb11ef635570.
New native_signal_entry_riscv.c has4SIGSEGVchildren:handlerNX/returnPCNX/read-only
returnSP/exactframebegin via separately alignedcodepage. All8corrected guests
passed2each (session31952 COMPLETE):
- `{rv32,rv64}-signal-entry-guest-v1`
- `{rv32,rv64}-signal-mapping-guest-v2`
- `{rv32,rv64}-signal-delivery-guest-v2`
- `{rv32,rv64}-pthread-signals-guest-v2`.
OldRV32SDKnegativecontrol isFAILED asintended code103/status32512 at
`rv32-signal-entry-old-kernel-control-v1`; wrapper receipt
`stage/entry-old-kernel-sensitivity-v1.json` onlymeansoldbugwasdetected.

## Current running/follow-up work

Root session42012 `entry_checked_regressions_v1.py` stillactive lastpoll:
x86fourcasespassed; AArch64fourcasesrunning. Uses exact newlybuilt
`{x86,aarch64}-entry-checked-kernel-v1`, frozenOSv13, outputs
`{x86,aarch64}-entry-checked-{altstack,bad-sp,raw,pthread}-guest-v1`.
Do notrestart; pollactualhandle. Session4225 tooltests COMPLETE290passes under
`build/qualification/sdk29-signal-tools-v6/result.json`.
Hosted newshared checks COMPLETE:
`/tmp/obfuscation-altstack-entry-admission-v1` and
`/tmp/obfuscation-shared-delivery-entry-admission-x86-v1`.
Priorx86boundarymodel failurewasstalepre-redzoneSP=end+1expectation; retainedv1,
fixedtest nowfailsend+129andcheckssave/repairend+1/end+128;6312passv2.
Prioraltstacksharedmodel328pass. NewCanEnter failure/success modeladded.
Need bindnewv2/runtimev13receipts, updateSTATUS/RISCV_EXECUTION latestsuccess,
retainindependentreviews afterclosure, finalnewregressionresults.

Agents dispatched:
- chmod_review reviewingFIXagainstfrozenRVkernelv2,task
  `/tmp/riscv-entry-fix-review-task-v1.txt`; originalv1reportsealedunchanged.
- entry_backend_review independently reviewingfinalRVguestsv2+entryv1, all8,
  sourceOSv13, plusoldkernelnegativecontrol. Task
  `/tmp/riscv-guest-review-task-v1.txt` isolder butagentknowslatesttargets.
- altstack_guest portingstrictaltstack+badSPprobesforRV32/RV64innewisolated
  `native-riscv-altstack-guest-v1`. Marker/countsunchanged35/37and18;leases5/6/3.
  Do noteditworkingnative_altstack/native_signal_bad_sp whileagentports.
  NeedsRV32waitpidfallback; mappedrestorernoactionmember; actualassemblySPcookie
  recoverywithhandlerrepair. Awaitsourceidentitythenintegrate/harnessadmission.

## Separate codecs ready for future integration

I386legacy/RTstage `native-signal-frames-i386-v1`,headerSHA
c48d3ac47e4ec14c5b9390f83bef4435d732ca1499da0e8d5d6dc2eb94e14f81.
Author118853ASan/UBSan,59Linuxlayout,nativecompile;independent32833checksplus
actualLinux32FXSAVE/FXRSTOR. Reviewreceipt
c0fcc240f57f90b49a8db25dcf94d2510bb2a80c7e1ad48f5ccbaab950deee24.
No runtime edits yet. CopyImage.usedonly;legacySPdelta8vsRT4;FS/GSbasestrusted;
legacydoesnotrestorealtstack;slots3private/12SS;backendSSmayTLSrelative.

LoongArchstage `native-signal-frames-loongarch64-v1`,headerSHA
 e6cfe450df78c6311a8d7df5339b01cd5db26902e84aaf3c4e9df96e574ee3da.
Author151901checks+layouts/nativecompile;independent1212330checksLinuxoracle.
Reviewreceipt9f2f9714d7f1677ceacbed666ffe342741cf8f496eb2afcc115b06cc3b36ba56.
MustcheckedwriteFCSRpatchbeforestatecommit andqueueSIGFPEbeforeuserreentry;
noLSX/LASX/LBT. No runtime edits yet.

Retainedreviews-v4copies569files includingfinalaltstack/i386/Loongarchand
passing/failingmodels. retentionSHA
ac8bcdaa828c031cc96626112c2dc3513844cff4768a68537b93aa37d6a397db.
No commit questions. Continue actual implementation/automation. Remainingfull
scope includesotherISAsignals,generalVM,IPC/TTY,durablejournalledroot,modernext4,
IRQsafenetwork/storage,realservices/isolateddesktop/apps,loadedmodules,SMPand
normativereleasequalification. Do notcallgoalcomplete.
