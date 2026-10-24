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
