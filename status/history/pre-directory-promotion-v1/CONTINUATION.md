# Current repaired directory qualification (supersedes earlier hold section)

Accepted source is still Kernel867 / OS456 SDK30. Required predecessor remains
9de1d0be7ecd286e3e9d7a9cc9f213189395b4beaa96ca8440d0a79d8d74f7e0.
No directory promotion yet. M0-M12 incomplete; physical/manual acceptance deferred.

- Kernel869 candidate-v4 final inventory506ff180547a43598721e947c3f3bfb4bf69cbdad98412f43c9f294721c2dd4b.
  Author native-journalled-directory-mode-v1/HANDOFF-v2.json
  d3f68e0223c7bad8c9efba7dd98a43d3c828c5fe3937834b2bdef76c6fe89b86; seal_v2 --verify passed.
  All final hosted/sanitizer/inherited gates pass. Independent holdclear
  source-review-v3/HANDOFF-v1.json213d88dd76477ece606a60e1bcd93fe2b5422273c137db3263cb753d9ba8d93e.
- Fresh native-journalled-directory-mode-build-v2/matrix-v1 passed20newSDKrows/10boots.
  result c375ca1d50fd287614da04468e4779438f2d6cd89e39c010d3819f75f438b6ea.
- Normal stage matrix-v2 passed30freshnative+30Linux,373338checks/1320writes/1140flushes.
  result72c49c53ca20126681d38667bf9018efc518ed69433aa935a908a688a3c5d587.
  Count differs from old diagnostic runs because C clock-boundary assertions vary.
  Fresh regular-x86-owner-v2 also passed126checks/55writes/47flushes.
- Distro-v2 ordinaryDebugSDKboot +5links/10boots passed; matrix result
  6f352714a67697373e195dc9c13102f48e9d7e52252ab5372585f08e48dffce2.
- Root native-journalled-directory-mode-integration-v1/verify_campaigns_v1.py
  sealed campaigns-binding-v1.json e844bad01427e302da9b390a18b91d4fa293575a1aa294fbbfa0d4d21976320b.
  Independent normal native review HANDOFF96d838fc4aca07e4d8e88f254a1fcfed989fb7a5ddfbaa2640fdfb9cf2374f16.
  Source/collector review native-journalled-directory-collector-review-v2 handoff
  ecf2b39bc00ff9d3d42498a00dc98c065930722d69d20fcb70d67b04e0313704;2675controls pass.
- Recovery campaign stage native-journalled-directory-recovery-campaign-v1.
  Uses OS474candidate2 unchanged, Kernelv4 freshSDK. Agent built x86/i386 images
  then failed before MIPS SDK existed; original images-v1/result stays running,
  terminal traceback retained. Root build_mips_image_v1.py completed images-mips-v1.
  Root capture_recovery_v2 selects that MIPS image and original x86/i386 images.
  Root launch_linux_v1.py binds independent Linux recovery; check_linux_recovery_v1.py
  compares exact home/data and only known Linux bookkeeping differences.
  Representative x86cut11 passed nativecut+recovery+clean+Linux;4233checks/boot.
  Matrix runner run_matrix_v1.py reuses that exact sequence once and adds remaining59.
  Full60cut/120native/60Linux still running in root session11682. Last seen44rowspass.
  Root owns pipeline after recovery-agent errored; do NOT launch duplicate runners.
- Root integration stage has PREPARED (not executed) verify_recovery_v1.py,
  compose_final_v1.py (OS475docs-only successor), bind_final_v1.py and promote_v1.py.
  Wait full60pass; then seal recovery, compose docs, seal final, promote exact32paths
  with backup; never rerun a promoter. Current normal binder already sealed.
- Next M3 work: pipe_signal_guest active read-only native-child-exit-signals-design-v1.
  Linux host18cases +alltenmusl siginfo layout measured; final design pending.
  SIGCHLD childstatus and parentcreatorTID may require nextSDK31; do not enable
  production flags from design. Reviewer vector_runtime_review completed existing
  tasks. Reuse agents when collaboration tools are available.

All paths above under build/prototypes. Always Python -B and PYTHONDONTWRITEBYTECODE=1.
Preserve all frozen sources, diagnostics and failed evidence. Earlier section follows
for detailed fixture/source pins; its candidate hold is superseded by final v4 review.

# Active directory-mode work: acceptance held for inherited cache regression

The accepted integration below is UNCHANGED: Kernel867 / OS456 SDK30, promotion
9de1d0be7ecd286e3e9d7a9cc9f213189395b4beaa96ca8440d0a79d8d74f7e0.
M0-M12 remains incomplete. Physical/manual gates remain deferred by the user.
Do not promote directory candidates1..3: author found inherited cache generation
exhaustion regression from new pre-prepare query. Author and independent reviewer
are repairing it. All prior diagnostics and successful guests remain retained.

## Current new work (paths under build/prototypes)

- Kernel author native-journalled-directory-mode-v1; candidates1/2/3 have869files.
  v1 inventory8e7fe7ac38dedf6792dc3ac8645cbcd4c908f56460a372c666618e7c30f67489;
  v2 f094d3a41636483c283dcf1ac9775deb82ad5d59a6ce4b6e31b7c3af60364b7c;
  v3 0257a892366202eb4ed720e5e0d768ec085d46fbf458b4ec69f70e17a1c5970c.
  v2 fixes hosted test wrapper, v3 docs wording only. All share the cache defect.
  Wait for repaired candidate and complete inherited/sanitized receipts before
  re-exporting. No public layout change; SDK30 with exact new hashes.
- Review source-review-v1/v2 and design-v1 stages use prefix
  native-journalled-directory-mode-. ACCEPTANCE-HOLD-v1.md explicitly supersedes
  earlier review acceptance. Retained getdents uses saved description readability;
  open/search/fchdir remain checked. Reviewer validated Linux reference semantics.
- Normal native author/root stage native-journalled-directory-mode-native-v1:
  OS464 candidate-v4 inventory6fae1af6b82b0265edcfdcdfb64523f648861fb4e0293cf5cb33bb7e7def4222.
  All456 accepted files unchanged. Adds probe/native fixture/builder/oracle/Linux
  comparator and nested fixture generator. Source candidate1/2 empty directory;
  candidates3/4 use actual /child/leaf inode16,24bytes. Candidate4 fixes loader
  provenance: MIPS/MIPS64/LoongArch64 linker; other profiles firmware.
  static-v4 allten compiled; prior static-v3 variable-name compile failure retained.
  fixture-v1 facts54c16de3d568c1f35169bc820e045cf9794511467188b6597e9d9879b3c42d4a;
  disk8baff55b10f1078d298305b26db898224d1574bc8205dfe3b3b4d375de543b05;
  fixture resultc37abf8ee9cb5a9350d2f7f5434e959064ca646c189f2da013802ad26ed249d5.
  matrix-v1 PASSED30native +30Linux,373355checks,1320writes,1140flushes, but uses
  defective Kernelv1 and is diagnostic-only pending reruns on repaired SDK.
  x86owner/root/negative reused3 in matrix; regular-x86-owner-v1 additionally passes.
- native-journalled-directory-mode-build-v1 PASSED20SDKrows/10privateDebugboots.
  native-journalled-directory-mode-distro-v1 PASSED ordinaryx86DebugSDKboot,
 5links/10distroboots. Same defective candidate; do not present as final acceptance.
  All root sessions for these pipelines have completed and been polled.
- Normal collector independent v2 review91syntheticcases passed. Root successor
  native-journalled-directory-mode-collector-successor-v1 replays91controls against
  OS464v4 +nonemptyfixture and corrected actual loader provenance. No extra guests.
- Agent native-journalled-directory-recovery-v1 prepared OS471candidate1 from old
  OS461v2, inventory77f3b499803aa7f4c6fd41cc27fc5c766925dba00ab4853b5659f8e0767163ad.
  Agent staticallten +cutprotocol242accept/1392reject +oracle180accept/456reject;
  SOURCE-HANDOFF5a40edd57541737c077a6f465222c2cfb8f579df8613e3f72aac5b4e538953a1.
  No agent native executions. Must use root rebase for nonemptyfixture.
- Root native-journalled-directory-recovery-integration-v1 composes OS464v4 plus
 10agent additions. OS474candidate2 inventoryde19356e45c7746f3912a4e6ea44de7edc887d57fff432a09233a78be6c06383.
  Adds leaf payload/statx to recovery C and collector; expects4233publicchecks,
  six inspected ordinary inodes (root checked separately). static-v1 allten passed;
  result e178d07f6dcc796606b16842c53cad00ef50ef32b30ec4db4d982865c9dfb0d3.
  Oracle controls180accept/468reject pass on nonemptyfixture.
  candidate1 archive name too long: first recovery imagebuild failed beforeguest.
  candidate2 shortens private basename to musl-jdir-recovery. images-v1 failure and
  BUILD-ATTEMPT-v1.md retained. Do not overwrite used scripts/candidates.
  One x86cut11 actually passed whole cut-disk oracle with olddefectiveSDK under
  cuts-v1/x86_64-cut11; diagnostic-only, no recoveryboot yet.
  run_cut_v1.py and build_images_v1.py still pinned to candidate1 and oldSDK buildv1;
  create successor runners for candidate2 and repairedKernelSDK, never silently
  reuse old kernel/evidence. Need capture/recovery runner, three representative
  cuts then60cut/120recovery+clean, Linuxrecovery, review/binding/promotion.
- Separate native-mips-flush-timeout-diagnosis-v1 sealed/replayed.
  handoff4474bfae26c5601b714b7146064291fcc564934b3f5599be3517806965d0ef13.
  5newboots:3concurrentbaselinespass, deliberate12s hostfdatasyncdelay produces
  sameguesttimeoutat5.000427seconds, itsfailed disk resumes. Originalthreefailure
  causes unresolved. DMA staticlifetime/quarantine reviewed. FreshQEMUcleanFLUSH
  can perform ZERO hostsyncsyscalls; guestFLUSH cannot provehost/physicaldurability.
  No productiondriverchange. Reportlocator erratum line39 shouldline26 retained.

Root collaboration tools became unavailable after initial dispatch; prepared
ROOT_INPUT_UPDATE files do NOT themselves wake/deliver to agents. Author and
reviewer are currently active and communicating with each other. Recovery agent
completed prep from staleOS461; root independently rebased it as above. Resume
normal delegation when tools are callable. Active thread goal remains M0-M12,
with no token budget; never mark complete from this bounded slice.

## Earlier accepted checkpoint (preserved)

# Accepted checkpoint: SDK30 journalled mode and native recovery promoted

Use `PYTHONDONTWRITEBYTECODE=1 python3 -B` including subprocesses. Preserve dirty
top-level repositories, frozen candidates and failed evidence. Do not rerun
promoters. Older checkpoints are in `status-history/pre-sdk30-promotion-v1/` and
`status-history/pre-native-recovery-v1/`. Paths below are under `build/prototypes`.

## Accepted source and next predecessor

`native-signal-actions-sdk29-v1/working`: Kernel867 / OS456, SDK30.
Required next predecessor `native-journalled-mode-integration-v1/promotion-v1.json`,
SHA256 `9de1d0be7ecd286e3e9d7a9cc9f213189395b4beaa96ca8440d0a79d8d74f7e0`.
All97 new/changed paths promoted with backup865/439 at integration/before-promotion-v1.
Root post-promotion source comparison passed. Promotion session15411 may need poll.
Final binding `f38cedb350316d4624b868fc5497f7eb9b84e2a9514ee2d7e3740b1b52c66314`;
`bind_final_v2.py` seal + promoter read-only replay passed. Earlier v1 binder
count-versus-list assertion failed before seal/mutation; preserved separately.

Kernel867 frozen inventory `0cacc4d45421411b1a62f0d0580c56ab7d84686960bc4117462d4f2dda9b3e0a`
at native-journalled-mode-v1/candidate-v1. OS456 final-v2 inventory
`11dde96dc42f5cd5b1ebe3076b59ae96e19de3b761a7ef8e80e99dac5a34c30a`
at native-journalled-mode-integration-v1/candidate-final-v2. Immediate final-v1
`ab6f99fd61b66fb28e9e7c5c30620fa1ae156b64681bdf09bf1bbf80ca83d156`
differs only in the new recovery documentation. All449 base files are unchanged.
Kernel delta:2added/7changed. OS delta:17added/71 ABI edits; no deletions.

## Closed bounded qualification

- Kernel author hosted7,664 checks, inherited suites/controls, independent review.
- SDK30 all20 rows and ten private Debug boots; bindinga1bde2c891242b0f9638f3237b33a961153df21ac6044b492f2412533050b353.
- Inherited x86 22commands/2,824cases; binding54e7f47ed569c5b944a547844d2a3cde9661c28d59b3aaac661a2e255dffd93b.
- All-ten waits20commands/4,840cases; bindingf6d0adef9539332799ec9dda056e61c137b05e7c50e0ab213a8e0e03268410cf.
- OS449 normal30native +30Linux readonly:3,007checks,120mutations,1,320writes,1,140flushes;
  integration/guests-binding-v1.json be8362631c2372e6ba6d81b80e6db4a669b8224d4d48adf505ac95c16b2c91d8.
- Original60 native cuts +60Linux recoveries;
  integration/recovery-binding-v1.json fcd92101689db68742592a91263880caaf2f6b3caa8001c5fff6b7c1990ce376.
- OS449 tools54suites/533methods +1,250 raw-image modelchecks; integration/tools-binding-v1.json
  a87a462c96c561be10c7d5d83db97563ceed93c53b3acf3142a263d9acdaba4f.
- Linux comparator closure handoff16d5ba3df342a309bcd8d103987c80a127f34b768ca2d9a4f6cf2d1be1c8afca;
  60replays/79controls, no new guests.
- Native recovery author stage native-journalled-mode-native-recovery-v1 FROZEN.
  receipt6899c14d8a889ed0677a31ccfa294bfeb94efc38ab72965ddfeb1e901d7a1acb;
  handoffaf86ed947ab8d304c111e397eaa160c8d9e2156ad8e9755de55e39ed94f76fae;
  candidate453v3 b13d858d9c31015e082f81f9151c69260b135a0e29ba298448f378dd4d37e6fe.
  120primary boots +6serialized repeat; all4new source files present unchanged in456.
  Root verifier replay output integration/native-recovery-author-replay-v1.json
  f932ae0cf34710665cc1dadbc4cb0828831b574c1026bfb603826a77d0170adc passed.
  Independent review handoff5628bfc293e98b614e0514cbd45caaa6e650775338d1356d44e6d57c22d0f575;
  98controls:97rejections/1allowednoise. Repaired loader full grammar collector
  fcbdbf63e64754e01edaf3719d5df3352ef5eb5bd0d52e4ee27ddfab22d19432.
- Root ordinary distro5links/10boots +ordinary x86DebugSDK boot;
  native-journalled-mode-distro-v1/binding-v1.json
  7758f6322527bbae18f327a7cd9989ce02b9bbba9d750c871cf2e077c12b0ac9, seal/replay passed.
- Root separate cut tools2additions, exact copied cutC++, normal source unchanged;
  native-journalled-mode-cut-tools-v1/binding-v1.json
  e446b1f9204614008c1574e78c85606ba3c2926099bbe2d8ff008c3448e61369;
  3new actual representative cuts +exact disk oracles, seal/replay passed.
- Root resumed EXACT3 retained MIPS timeout disks, each followed by clean boot:
  native-journalled-mode-timeout-resume-v1/binding-v1.json
  22dae2bd2e5d782149a933c6305224d3f727708f835e870d21d43d7b3489348c;
  6new native boots/25,008public checks, exact full disks; seal/replay passed.

## Genuine failures and limits

Author recovery total168 launches =120primary +6serial repeats +4extra successful
phases preceding failedpairs +3actual MIPS recovery timeouts +35preboot image locks.
Root failure-disk resume adds6separate launches. Three original failures are NOT
preboot lock failures (earlier provisional summary was corrected). MIPS cuts16/17/18
failed on Virtio flush with status11 before mount/user publication. Driver uses
5second monotonic timeout; cause not claimed repaired. Cut16failure disk equals
original cut16; cut17/18 failure disks already look clean after SB write, and need
fresh successful flush before publishing. Root explicit failed-disk boots verify
this. Do not claim full concurrency/transport reliability from repeats.

Whole-block CRC of checksummed superblocks can be a common residue; ledger alone
does not uniquely identify each intermediate payload. Full final disks and pinned
code provide additional evidence. No volatile-cache/torn/reordering/physical-loss,
default-root/fullM4/SMP or complete M0–M12 claim. Production signals remain disabled.
User deferred M11physical and M12manual; do not ask again. Ten Kernel/four distro
profiles remain intact. Top-level dirty repos untouched.

## Next work

Continue broader implementation. A concrete next bounded design question exists
at native-journalled-directory-mode-design-v1/ROOT_QUESTION-v1.md for ordinary
directory chmod. It is NOT dispatched and NOT implemented. It identifies mounted
admission, writer hard-coded inode type, and replay admission that must change
together while preserving namespace/allocation/type bytes. Root inode2/symlink
remain separate. Collaboration became unavailable in root tool context late in
this turn; prepared files alone do not wake idle agents. pipe_signal_guest and
vector_runtime_review completed current recovery work. Reuse them when callable.

Status docs now reflect accepted867/456. Any next candidate/promotion must start
from the new SDK30 predecessor above, not the earlier wait receipt.
