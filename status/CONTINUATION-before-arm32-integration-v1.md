# Active M0-M12 continuation — ARM32 backend snapshot

User still requires full M0-M12; substantially incomplete. M11 physical and M12
human desktop acceptance explicitly deferred; do not ask. Goal stays active.
Previous turn was concrete progress: actual ARM32 backend implementation and
new standalone/OS execution evidence. All ten profiles preserved. Shared dirty
SDK20 repositories untouched. SDK29 private working still has five-profile
signals only; ARM32 backend/codec are isolated and NOT integrated there yet.

## Current terminal state

All new root sessions COMPLETE:93202(normal/poison ARM backend),62791(negative
capture),31907(full ARM Kernel SDK),25837(OS pthread). No root process is running.
All older sessions listed below also terminal; never poll/restart old handles.

## New sealed ARM32 backend

Stage build/prototypes/native-arm32-fpexc-v1.
Receipt1490files SHAaffd1d92ab605aae6ee0de0b98ada8f1f0b33a2efc7dcd90190b3fa4c8594c4f.
Treat stage/draft and receipt-covered inputs immutable. Readstage/README.md.
UserFrame layoutunchanged; newarchitecture-privateFPEXCbytes260..263absolute420
followD0-D31(0..255),FPSCR256. NewArm32FpStatehelperinitializesEN,admitsonlyEN;
backendentryloadscheckedUSERvalue independentlyofsavedKERNELFPEXC;captureVMRS
storesactualFPEXCbeforekernelcanonicalnormalization. Kernelstatepreserved.
No pending/asynchronousVFPexceptions or FPINST/FPINST2 preservation claim.
This establishesboundedcanonicalstate neededbyARMcodec, notfullVFPcompatibility.

ExistingARM32nativeexecutionprobe retainedandextended:ARM+Thumb D0/D15/D16/D31,
FPSCRroundtrip, captureaftersyscall/fault/timer,10invalidretainedstatesrejected,
kernelFPEXCpreserved. Builtbynewstagexmakeproject (notad-hocgccscript).
validation-v1passed4actualCortex-A15QEMUruns:2normal+2testpoison. Test-onlymacro
OK_ARM32_FP_CAPTURE_TEST_POISON poisonsretainedslotafterhardwareload;everyactual
trapmustcaptureEN. NormalSDKneverdefinesthismacro. Negative-capture-v1 deletes
capturestoreinseparatecopy;brokenQEMUfails'actual user FPEXC capture'asintended.
Negativecontrol wrapperstatuspassonlymeanssensitivity,brokenbackendnotpassed.
ValidationSHA733880017228e5f15fe45c68b378a680f513ac676d7ccc488560f2bdd3847dd6.
NegativeSHA0e9b6299a34843d1cd800be91304ce1037ec7a87e51693bc8a9f343ff005d1b4.

FullstandaloneSDKbuild/qualification/arm32-fpexc-kernel-v1build/export/bootpass.
KernelresultSHA1d43ce8b8fc8f9c7431819595359bf2d93e095b589c5811546134a50f705aab3.
ExactSDK-onlyOSarm32-fpexc-pthread-guest-v1passes2ordinarymuslpthreadrunsusing
frozenOSv18;noKernel source compiled. Threadcreate/join,TLS/errno/masks/TSD,
nativepipelines,disk/resourcechecks. NoARMsignalsenabled/claimed.
GuestresultSHAf19e44a886ae53ba263bf6dbdf96119467402d30e8e38193038aa247882a29d3.
Authorstage/binding-v1.json rehashes2400filesandreadmitstranscript.

## i386 policy/altstack independent review now complete

/tmp/i386-policy-altstack-independent-review-v1/receipt.json
SHA6c19909e03bd420a92a86ee08edd44daea1c716cb2485f080bff49b171325639.
22050independentmodelchecks;8policymutants;6LinuxELF32baselines/180assertions;
10assertionmutants;2OSguestreadmissions/40logmutants. No new defect. Original
commonprobeauthorshipbyreviewerdisclosed;peerportcheckbyentry_backend_review
alsofoundnoassembly/layout/weakeningissue. No newOSexecution inreview.
CopiedunchangedtoSDK29stage/retained-reviews-v8,862files,retentionSHA
 d346e06622c9a1c5bc91e4e9fbb8cabdc7036a5ee26536b18a96a6a06efc8f9d.
SDK29STATUS/I386_EXECUTION updated. Otherreviews unchanged.

## Agent status and next actions

All3agentslastreportedcompleted. Revalidatewithlist_agents. NOnewreviewtask
wasdispatchedthisturn;preparedfilesaloneDONOTstartagents. Readyboundedtasks:
- /tmp/arm32-frame-independent-review-task-v1.txt (suggestchmod_review)
- /tmp/i386-segmented-entry-review-task-v1.txt (suggestentry_backend_review)
- /tmp/arm32-fpexc-backend-review-task-v1.txt (suggestaltstack_guest; authored
  ARMframecodecbutnotrootbackend;discloseboundaries).
Allthreecanrunwhile rootimplementsisolatedARM32delivery/returnpolicyusingexact
codecheaderandvalidatednewbackendhelper. RoothasNOTwrittenARMpolicy/runtime.
NeedexplicitSA_RESTORERinitialfixture,SA_SIGINFOlegacyvsRT,rawaltstack/AUTODISARM,
ARM/ThumbPCalignment,Frame.pcuntaggedwithCPSR.T,restorerinterworkingLR,
return119/173SPdirect8aligned,RTonlyaltstackapply,checkedmappedPC/SPbeforecommit,
andcanonicalFPEXCfromactualretainedslotpassedviaexplicitExceptionState.
DoNOTclaimFPINSThardwarecaptured;newbackenddoesnotcaptureit. PendingFPstate
remainsfuturework. Independentreviewmayrequirestrongercapabilityproof.

Earlierworking/frozen i386/signal status follows (agent states in oldersection
superseded by thissnapshot). Historicalsource beforethisappend is saved at
build/CONTINUATION-before-arm32-fpexc-v1.md. MainM0-M12remainingprogram isstill
large:signalsallISA/restart/cancellation,VM,IPC/TTY,durableJBD2/modernext4,IRQ
storage/network,realservices/isolateddesktop,loadedmodules,SMP/releasegates.

---

# Active M0-M12 continuation — i386 implementation snapshot

User still requires full M0-M12; substantially incomplete. Keep goal active.
M11 physical and M12 human desktop acceptance explicitly deferred, do not ask.
English code/docs, Chinese progress. Preserve all ten Kernel/OS profiles. Shared
dirty repositories remain SDK20; private stages only. Frozen generations immutable.

## Root terminal state

All root processes in this slice COMPLETE: sessions29782,69859,77340,26574,
99454,80900,33078,63439,62768,85943. No root build is running. Do not poll old IDs.

## Current mutable / frozen source

build/prototypes/native-signal-actions-sdk29-v1/working/{ObfuscationKernel,ObfuscationOS}.
Private opt-in Debug now supports i386/x86_64/AArch64/RV32/RV64. Export ABI layout28.
Production actions/returns remain ENOSYS. No fullLinux/P06/M3/release/SMP claim.
Latest frozen OSv18 inventory:
65827e43e660a20646d99aef18a52ab1e242f48bf887a073237d2aa2aaf52bd1.
Read stage/I386_EXECUTION.md and STATUS.md for current bounded claims.

## i386 completed this turn

Reviewed frame header c48d3ac... copied unchanged into working. New policy stage
native-signal-delivery-i386-v1 sealed:22362 authorASan/UBSan checks; truei386
freestanding object no undefined. Receipt2f079fead38b89fe7538a5b524935ff1b38836b531d22f460c5e0f732e532f94.
PolicyHeader6000fa117455730ce2aa3ebc5a2c65f2ad6f4769eb9f9198679d4b1d9e651bbc.
ReturnHeaderc0cb62de64d5551532a3babe2422364e167600d586fef9f3aebeb65f475c66c4.
Runtime integrated SA_SIGINFO selection, explicitSA_RESTORER, exactImage.used,
legacy119/SP-8 versusRT173/SP-4, RT-onlyaltstackapply, complete=false returning,
checked effectiveSSbase+ESP admission, selectorvalidation, currenttrustedTLSbases.
No backend edits. Newbuild script build_private_target_v4.py accepts i386Debug.

Exact standalone SDK build/qualification/i386-signal-delivery-kernel-v1 passed
build/export/boot. Five nativeOS SDK-only guests each passed2:
- i386-signal-delivery-guest-v2 (frozenOSv16)
- i386-pthread-signals-guest-v2 (OSv16)
- i386-altstack-guest-v1 (OSv17, exec37checks)
- i386-bad-sp-guest-v1 (OSv17,18checks)
- i386-signal-entry-guest-v1 (OSv18,8faultchildren/4segmentedpositive).
Author binding stage/i386-bindings-v1.json rehashes6870files andall5 parser
rechecks;SHA16876042d9ba105db77519ca79a6e2daec9ef7fd36472eff3e0b4b867eb615cd.
FrozenOSv18 full Python tools293pass at sdk29-signal-tools-v10.

Rawprobe covers both formats16handlers/2nested, coalesce/NODEFER/RESET, editedEAX,
actual x87/XMM/MXCSR restore and edits to authoritative oldFSAVE prefix, highmask,
4badreturns. Initial rawprobe v1 compilation failed pointer conditional types;
logretained. Probev2 passed2 Linux and2OS runs but independent omission controls
found zero-initialized RESET query could be skipped. Fixed alloldfields poisoned;
rawprobev3 andguestv2 arecurrent. Exact failed/earlier/corrected sources recovered
andverified againstoriginal manifests in stage/i386-source-history-v1.

Newentryprobe uses actual musl GS:0 TLSself/base and dynamic SS/GSselectors;
legacy+RT NXhandler/NXPC/readonlyflatSP/readonlyeffectiveSSSP children; handler
runsflatSS onaltstack andreturns segmentedSS:ESP. First2post-int80 instructions
readcookies throughreturnedSS:ESP beforeflatstackrepair. Positiveinterrupted
segmentedstackalsoforcesSA_ONSTACK. Exact Linux referencepass2; actualnativeOSpass2.
Independententryreview still needed (see preparedtask below).

All raw/pthread/altstackcore/altstackexec/badSP/entry exactELF32 Linuxreferences
pass2. Inside sandboxELF32signal syscalls were killedSIGSYS; approved outside-
sandboxexec worked. OriginalSIGSYS in i386-linux-reference-v1 preserved. Outside
reference receipts: i386-linux-reference-v2/v3, i386-pthread-linux-reference-v1,
i386-entry-linux-reference-v1. These are Linux, not OS or new hardware qualification.

## Completed independent reviews

chmod_review runtime integrationreview:845 hostedchecks including actual private
fixture/PCB/TCB with explicitowner/mapping/finishstubs. No newfinding; authorship
of policy disclosed. Receipt /tmp/obfuscation-i386-signal-runtime-review-v1/receipt.json
SHA1697c267f4eed438a42e3ccc9e002b513e8affaf22e8fabc255ee905328bc96d.
entry_backend_review finalraw/pthreadreview binds3365files,106logcontrols;
33raw+12pthread+10RESETqueryomission/partialcopy controls reject. Receipt
/tmp/obfuscation-i386-raw-guest-review-v1/final-v2/receipt.json
SHA0343a0810094cf311c1034d8562a18898935bd4d999f42a4514851fcaa12d241.
Both reviewtrees copiedunchanged to stage/retained-reviews-v7,1348files,
retentionSHAc53bba2e1fe6941160a0c212c436f04b69ac602561e21f73edfb3d28e38012c9.

NewRV altstack/badSPreview completed:6389files,262parsercontrols,28badSPmutants,
10altstackprefixmutants, actualELFcookieinstructions/layoutchecks. No newfinding.
Receipt/tmp/obfuscation-riscv-altstack-final-review-v1/receipt.json
SHA244b69cfdcf3bb548c74c07772ada5facdc44b235e7ff05cdfd6f936dda84bdd.
Copiedall5reviewdirs understage/retained-reviews-v6,400files,
retentionSHAabeffd327763b06d7b286f27832a7fe24de5205709f0694e02507eba6127bc7f.

## Active agent and prepared tasks (read carefully)

altstack_guest/Raman is RUNNING independent i386policy+newi386altstack/badSP
review at/tmp/i386-policy-altstack-independent-review-v1. Latestmsg:verified
policy60files,OSv17source304entries,bothguestinputs/outputs;actualassemblyoffsets
correct. Reviewer authoredgenericoriginalaltstackprobes, disclosedpartial
independence. Awaitfinalreport/receipt andretain afterclosure.
chmod_review andentry_backend_review completed prior tasks, no newturn dispatched.
Prepared but NOT dispatched:
- /tmp/arm32-frame-independent-review-task-v1.txt
- /tmp/i386-segmented-entry-review-task-v1.txt
Revalidateagents then followup these bounded tasks; filesalone doNOTstartwork.

## ARM32 isolated codec completed, integration absent

stage native-signal-frames-arm32-v1 byaltstack_guest. Header
ccaab1bfded9e7ec4dc1e481b00e83c790826767105e29265cd64d3bc02a8ab8;
receipt6473ce676e505a2ed2bb1a2ddff1fad1ae382fcd00fe023ded4d95052b704baf.
1515673ASan/UBSanchecks,43Linux+15muslconstants,8implementationmutants,
ARMandThumbfreestandingobjects. Legacy760/RT888;ucontext744;FPat160inUserFrame,
D0-D31bytes0..255,FPSCR256. Legacy119andRT173useSPdirect8aligned.
Handlerbit0selectsThumb;currentbackendpreservesIT/CPSR. RTonlyaltstackrestore.
IMPORTANT:backendexecution.S savesKERNELFPEXCprivately anddoesNOTcaptureUSER
FPEXC/FPINSTinUserFrame. Codecrequires explicitcanonicalEN/zeroFPINST attestation.
No inventedslot, no runtimeclaim. Needindependentreview plus backendpolicy/capture
contract beforeintegration. Root onlyREADbackend; NO ARMbackend/policy edit made.

## Next useful work

1 Dispatchpreparedreviews;finishactivei386policy/altstackreview andretain.
2 ARM32backendcanonicalFPEXCcapture/validation+policy afterreview;orotherISA
frames (MIPS/MIPS64/PPC) canrunindependently. LoongArchreviewedcodec stillready.
3 i386legacyAUTODISARMpersistenceactualguest couldsupplement currentRTaltstack
andhostedlegacycoverage; no such newcode yet.
4 Sharedsourceport x86/AArch64/RVcommonaltstack actionmask typechanged to u64
for i386; layoutsunchanged for existing64profiles, staticassertsadded. Rootcompiled
all8altstack/badSPprobes fromOSv18:byte-identicalELFstoearlierexactguests.
Receipt stage/i386-common-source-compile-regressions-v1/result.json
SHA6549df1adb46a9129e4cf8d333b767b0b2938756bb31a18b1a450b2b39dc4db0.
This isnewcompilation, notnewnativeexecution; no redundant reruns needed.
5 Remainingsignal interruption/restart/cancellation andbroaderM0-M12.

Earlier authoritative history is build/CONTINUATION-before-i386-v1.md; preserve
priorfailures andSDK28matrix. Mainremainingprogram includesgeneralVM,IPC/TTY,
durablejournalledroot/modernext4,IRQsafestorage/network,realservices/isolatedGUI,
loadedmodules,SMP,normativereleasequalification. Do NOTmarkgoalcomplete.
