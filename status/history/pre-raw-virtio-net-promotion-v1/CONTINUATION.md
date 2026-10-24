# Accepted ordinary SDK31 signal checkpoint

M0-M12 remains incomplete. The user deferred M11 physical hardware and M12
manual desktop acceptance. Continue implementation and automated qualification
without asking again. Preserve dirty top-level repositories, frozen sources and
failed attempts. Run Python with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, including
subprocesses. No commits or publication. Paths below are relative to
`build/prototypes`.

## Accepted source and mandatory predecessor

`native-signal-actions-sdk29-v1/working`: **Kernel896 / OS515, SDK31**.
Ordinary Debug/Release signals are enabled with semantic capability
`native_signal_profile: bounded-bootcpu-v1`. This is a bounded, serialized
boot-CPU runtime, not SMP qualification. ABI31 remains supported only with
explicit profile/capability and definition checks; old signals-off artifacts are
rejected. Preserve ten Kernel profiles and four ordinary distribution profiles.

The next promotion must use
`native-jbd2-geometry-integration-v1/promotion-v1.json`, SHA256
`fdc96ba2089e419d3a006c7491d9740b1f5e4f64037652dd8631b8e6f509af5e`.
Its complete `after` inventories define accepted Kernel896/OS515. This promotion
applied only the replay header and its hosted test, preserving full prior trees.
Never rerun this or any earlier promoter. The ordinary signal promotion remains
bound independently at SHA256
`6b8ea05c03c24f1d717fdfdc9cfacb22d7d1129e2280dd486945b53c673ed86d`.
No top-level repository was modified.

- Final contract V2: `7c5c0181c86ec67a10fcca971264008fdf869ee07bd75d44dfde4fa908bc13e0`.
- Final binding V2: `06e34e493a407b44c54804b70f1d6ab03ab2bc3a765b9ac90fcc05fd205cf451`.
- Native campaign binding V2: `7ed7775a710442f6d2c289878a5642274c82380a7b0e81fdbeb5c67fa0e7470c`.
- Final Kernel: consumer `candidate-kernel-final-v1/ObfuscationKernel`, inventory
  `2aa08042baa6054cbcb27899633d7d9a2ee472f8169e09c637657f032380da51`.
- Final OS: consumer `candidate-final-v2/ObfuscationOS`, inventory
  `5d917c71a160c7ecc7cf1c8a3f0c5435a420a9cee60b03210f40f49f89a18ce5`.
- Post-promotion result: consumer `post-promotion-v1.json`, passed.

## Accepted implementation and evidence

Ordinary signal runtime uses checked common completion for administrative
SIGKILL, preserves private diagnostics as a separate profile, and enables the
MIPS/PPC capture/assembly/compaction guards. Producer and consumer reject absent,
disabled and contradictory profile claims and direct, split or forwarded `-Wp`
protected macro overrides. Sixty measurement objects across all ten targets
showed 76 existing public and 14 additional guard layouts unchanged.

- Thirty fresh Kernel builds/exports: ten ordinary Debug, ten ordinary Release
  and ten diagnostic Debug. Twenty Debug standalone boots passed; no separate
  Release standalone campaign. `native-signal-production-build-v1/matrix-v1/result.json`,
  SHA256 `f22ecba31e1db84b03f0ea66f1fa7e8bcf0cd99e9f40e34c6021a502aaf2b0ee`.
- Final exporter re-exported all thirty SDKs with byte-identical manifests and
  artifacts after explicit AR timestamp normalization. Raw exports and the
  failed first comparison remain. No new compile/boot from re-export.
  `native-signal-production-sdk-v1/reexport-v2/result.json`, SHA256
  `5492772fc0e5d9a06951ec14d645d3f24630ce036d2f70e224ec7544fac5b68a`.
- Ordinary native matrix: forty qualifiers / eighty commands, both probes,
  Debug/Release, all ten profiles. Consumer `ordinary-matrix-v2/result.json`,
  SHA256 `c82adc4ba4ab55ef6ed21c710fcce5d75f99a1a7d28ea6176178d8450c28c989`.
  Extra x86 Debug representative has two commands outside the matrix count.
- Diagnostic native matrix: twenty qualifiers / forty commands, policy and
  pressure on all ten. Consumer `diagnostic-matrix-v1/result.json`, SHA256
  `74d59515d79b0948dd390d5929c6b27c2aba3981316a719a42aed0515bbaf05c`.
  Both Kernel/OS modes explicitly consume pinned Debug static musl; this is not
  rebuilt Release libc.
- Hosted OS tools: 67 suites / 617 distinct methods, composed from the full
  615-method run and replacement nine-method final collector suite.
- Independent ordinary observer review V5: six methods, 40 positives, 1,884
  negatives and 1,500 observer controls; thirty platform cases. All forty
  original receipts replay identically through final V5. Retained portable
  audit freshly passed from final OS. Replays/bindings are not new execution.
- Independent Kernel review: 303 actual-runtime hosted assertions per ordinary
  macro configuration, ASan/UBSan, plus 92 paired SDK predicate controls. Two
  portable admin audit files are retained and freshly passed. Inherited actual
  private lifecycle 364 checks and exec audit 164 checks passed separately.

Initial ordinary matrix V1 rejected forty tasks before compiler/QEMU because of
an invalid inventory scope; original receipts and failure analysis remain.
Actual ordinary executions used frozen OS514 V3. V3 to final OS515 changes only
collector/tests, portable audit and docs; binders check complete compiler inputs
and SDK/image/output hashes. Final collector rejects private, wrapped, malformed,
duplicate and cross-profile platform records. MIPS64 requires the exact
`N64_SIGNAL_PLATFORM_PASS before-cxx=1 fp=fr1` as first complete normalized boot
record. Keep all V1-V4 review failures and corrected test-premise evidence.

Ordinary observations establish user-visible policy/pressure behavior. Hidden
blocked-read/reaper/rollback joins and first queued sender remain supported by
separate diagnostic receipts, not inferred from ordinary output. Historical
pressure and private lifecycle promotions remain independently bound; see the
archived status for their counts and limits.

## Newly accepted recovery geometry correction

RecoveryIo rechecks pinned geometry after every successful journal read, home
write and FLUSH, rejecting changed geometry during final FLUSH instead of
reporting durable replay. This does not detect identical-geometry replacement.
Root binding V3 SHA256 is
`d2448be510808752f268669b5d5d34b3e294bb97d48537587c94fe0dceb2a02d`.
The accepted Kernel geometry inventory is
`010baef78b5d30f1b25779b20afc84bdbb3ce939f75ac9632c9baae85ab74295`;
OS is unchanged. Ten fresh ordinary Debug SDK31 builds/exports and standalone
boots, 78 native OS completion boots and six recovery/clean boots on historical
SDK30 cut12 disks passed. Root additionally verified every SDK/output hash,
complete sources and strict directory serial/disk replay. No fresh Release
campaign or fresh cut campaign is included in this acceptance. Root's initial
binding attempts mistook missing command-status fields and inner-volume versus
guarded-disk hashes; failed attempts are retained, no guest failure implied.

## Active isolated successors, not promoted

- `native-init-adoption-v1`: reserved PID1 and orphan adoption, nine Kernel
  changes. Public PCB/scheduler layouts changed, requiring ABI32 and explicit
  new SDK validation. `native-init-adoption-review-v1` found that created,
  unpublished init was selected for adoption; fix and regression are underway.
  `native-init-guest-abi32-v1` passed native x86_64 and aarch64 Debug/Release
  adoption guests and strict observers after repair. A separate successor with
  the accepted geometry fix is building/exporting SDK32 and running the complete
  ten-profile ordinary native matrix. Do not substitute old SDK32 evidence for
  the combined source. Whole M7 service policy and native pressure remain open.
- `native-jbd2-sdk31-fresh-cut-v1`: storage agent runs fresh SDK31 directory
  software cuts 1,10,11,12,15,16,18,20 on x86_64/i386/MIPS passed: 24 native
  cuts, 48 native recovery/clean boots, 24 independent Linux recovery/e2fsck
  boots. Binding SHA256
  `c9a0d758338e15f250621731c58a8db6214035c799f6b3e72047415782b737e4`;
  accepted-checkpoint source correlation is retained. No source changes, no
  physical/volatile/torn-write/reordering claim. Old regular-mode MIPS timeouts
  remain unresolved.
- `native-virtio-net-mmio-v1`: frozen OS521 V2 inventory
  `6598fa76da120aea87e6a01183c71caabfd7143af79ade82ac250a98f8794fdd`.
  All ten ordinary Debug/Release freestanding compiles passed; four MMIO profiles
  had 24 fresh QEMU executions and 768 external peer Ethernet frames. Native
  exchange/absent/legacy rejection and restart/receive retry passed. Initial
  missing memcmp, sandbox SO_TYPE and uninitialized clock attempts remain.
  Independent ledger/poll audit passed 524,329 checks. Root closed reviewed
  object-lifetime/stale-base issues in V2; V1 remains. PCI successor delegated to
  `nic_pci` under `native-virtio-net-pci-v1`. No IP/socket/IRQ/hardware claim and
  no networking promotion yet. MMIO matrix uses explicit local socket test
  escalation because sandbox blocks SO_TYPE; no external network contacted.

## Remaining target limits

CPU-time signal fields are zero. General init/subreaper policy, stop/continue,
complete fault signals and SMP remain open. Default journalled root, shared
musl, broad POSIX/filesystem behavior, networking, persistent services, isolated
desktop and other M0-M12 requirements remain incomplete.

Existing journalled-directory campaigns belong to SDK30 and require fresh
SDK31 qualification. Three historical MIPS recovery FLUSH timeouts are unresolved;
a host fdatasync delay is not an established cause. Completion-boundary cuts do
not qualify torn writes, reordering, volatile caches or physical power loss.
External Linux6.13.4 reference has 21 cases; newer WSL2 differs in leader cause,
and binary/source authenticity is unestablished. Physical/manual acceptance is
deferred, not passed. Previous status is archived under
`build/status-history/pre-jbd2-geometry-promotion-v1`.
