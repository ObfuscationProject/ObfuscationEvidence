# Accepted SDK32 PID 1 supervisor checkpoint

M0-M12 remains incomplete. The user deferred M11 physical hardware and M12
manual desktop acceptance. Continue implementation and automated qualification
without asking again. Preserve dirty top-level repositories, frozen sources and
failed attempts. Run Python with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, including
subprocesses. No commits or publication. Paths below are relative to
`build/prototypes`.

## Accepted source and mandatory predecessor

`native-signal-actions-sdk29-v1/working`: **Kernel901 / OS549, SDK32**.
Ordinary Debug/Release signals are enabled with semantic capability
`native_signal_profile: bounded-bootcpu-v1`. This is a bounded, serialized
boot-CPU runtime, not SMP qualification. ABI32 adds mandatory `native_init_profile: designated-pid1-adoption-v1`;
current consumers reject ABI31 and missing/contradictory capabilities. Historical
SDK31 campaigns remain archived with their matching source consumers. Preserve ten Kernel profiles and four ordinary distribution profiles.

The next promotion must use
`native-pid1-supervisor-integration-v1/promotion-v1.json`, SHA256
`08456afbc1b265eb352136d5e65de4f1d4033e055440e259a316310ecf689cb9`.
Its complete `after` inventories define accepted Kernel901/OS549. It adds
13 OS files and changes five, preserving existing SDK32 pressure and network
integration. Complete Kernel/OS backups and post-promotion checks passed.
The immediate static UDP predecessor is
`5cb897a4175120820bff9e91dc74e0c3fa2d92dd88cd19af40c7128eb2a7c4fb`.
Prior init/wire predecessor was
`06ec7a1f1235798ee0fa63711e8a6910fc80a34d4c5e285eca71e2d8200f22f6`.
Never rerun this or any earlier promoter. Raw Virtio predecessor:
`08cd7a7a093c9c1d385a936aa2613c9681e4f9ab7f12306abc8eead9b0574f78`;
geometry predecessor:
`fdc96ba2089e419d3a006c7491d9740b1f5e4f64037652dd8631b8e6f509af5e`.
Promoters modify only the accepted isolated working trees. Preserve dirty
primary repositories and their documentation updates separately.

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

## Accepted raw Virtio Ethernet driver

The OS-owned driver supports modern MMIO (four profiles) and modern PCI (six),
with eight-slot split-ring ownership, bounded reset/quarantine, RX retry, TX
completion and static transport selection. It negotiates MAC and VERSION_1
only. All ten Debug/Release qualifiers passed 60 fresh QEMU exchange/absent/
legacy scenarios and 1,920 exact external frames. SDK31 artifacts are explicit.
Native matrix SHA256:
`ac1fada199f40113ef160b28243ab7e7831f29502e635c34e6518d2b039d0081`.
Independent strict audit rechecked complete sources, all 20 SDKs, commands,
serials and captures; 16 negative controls rejected and all 60 images rebuilt
byte-identically. Rebuild/audit are not new execution. Root binding SHA256:
`7911e6a88d042eed381bc6cbd61ae48ef557729a3fd18f2be7a30cbf72701695`.
Frozen OS523 inventory SHA256:
`9690f4acda079bef47f3fdbbfb62423359c4c830c381ca7e5d63f91b01a0e716`.

Scope is serialized boot-CPU polling on coherent QEMU. No distribution NIC
integration, IP engine, socket, IRQ, SMP, noncoherent DMA or physical acceptance.
PCI uses a bounded bus-zero BAR window. Permanent author receipt audit needs
stricter validation before future reliance; current promotion uses the frozen
independent strict audit. Original MMIO/PCI failed attempts remain preserved.

## Accepted ABI32 init and network wire successor

Kernel designates published PID 1, adopts live and completed orphan children,
preserves SIGCHLD lineage and wait-any completion, and increases bounded child
capacity to 64. Created/unpublished init is not an adoption target. ABI32 and
mandatory init/signal capabilities are validated explicitly. The wire header
provides checked Ethernet/ARP/IPv4/UDP borrowed views and a UDP builder; no
routing, neighbor learning, socket or general protocol engine follows.

Root binding SHA256:
`7f05b13d5b2117ecd20f11e2dc5bd44b3028cfd194b7f6c3067d3ab1fdc7af36`.
Twenty fresh wire/init SDK32 exports and ten standalone Debug boots passed;
all ten freestanding wire objects and 113,077 ASan/UBSan byte assertions plus
10,000 deterministic iterations passed. Wire matrix SHA256:
`60319f6f0adcb529fdae45a7dae07439630fab9d96f6efa7cce95da1438ced46`.
Twenty fresh SDK-only native init guests passed using these exact exports and
the strict complete-line observer. Root rechecks all inputs, outputs, commands,
SDKs, serials and disks; rechecks are not new execution. Additional malformed
or unterminated/wrapped markers are rejected. Prior strict observer audit
rejected 150 controls; final fresh-guest audit rejects 60 controls.

Final hosted tools passed 625/625. The executed OS528 guest source precedes two
hosted SDK-admission-only fixes in object-pressure helper/test; all compiled
inputs and active observer functions are identical, checked by complete source
maps and AST comparison. The failing 625-test inherited ABI31 fixture run is
retained. Current helper and fixture use ABI32. Many historical SDK31-specific
qualification campaigns have not migrated and must keep their archived source.
Both modes still consume pinned Debug static musl. Persistent supervisor,
service graph, native pressure/init death/subreaper, SMP and broad POSIX remain
open. No whole M7 claim.

## Accepted single-peer static ARP/IPv4/UDP service

`native-static-ipv4-udp-integration-v1` composes the SDK32 OS534 networking
slice onto OS528, preserving strict init observer and pressure admission fixes.
Final OS536 inventory SHA256:
`7626b007c5a2d291d329fb6449c54575160fa5a6031150423db075de9fe1d0ab`.
Root binding SHA256:
`f21f200fc8c9635a2be75ab64461101c856bb868cbba40e10e94b0cbbec48d45`.
Root strict audit SHA256:
`243a65bd4e1a79830d0c311a8d89b454514c7caa22804dfee61522928f7dc2c9`.

Twenty qualifiers / 80 actual QEMU scenarios passed, covering ten architecture
profiles in Debug/Release with exchange, hostile packets, absent and legacy
NICs. Captures contain 20 ARP replies, 1,940 UDP replies and 240 hostile packets
with no reply. The root rechecks every compiled input, SDK, command, image,
complete ASCII serial and bidirectional capture; 80 byte-identical image
reconstructions and 15 observer controls passed. Rechecks/reconstruction are
not new execution. Final compiled bytes match native OS534; three unrelated
accepted observer/admission files and two documentation additions differ.
A fresh hosted ASan/UBSan endpoint model passed 121,557 checks; LeakSanitizer
is disabled because sandbox ptrace prevents it, with original failure retained.
The final xmake compile-only entry passed. Inherited exact Kernel901 evidence
remains 20 SDK32 exports and ten standalone Debug boots.

This is a privileged, fixed-peer polling service only. No ordinary distribution
NIC, user socket, general routing/ARP learning, TCP/IPv6, IRQ, SMP, noncoherent
DMA or physical acceptance. `docs/STATIC_IPV4_UDP.md` records the limits.
Default root remains nonjournalled. No complete M6 or M12 claim.

## Accepted bounded static-musl PID 1 supervisor

`native-pid1-supervisor-integration-v1` composes frozen V8 onto OS536,
adding 13 files and changing five. It preserves SDK32-only pressure admission,
the strict init observer and the static UDP task. Historical SDK31 opt-in
helper changes are deliberately excluded. Kernel901 is unchanged.
Final OS549 inventory SHA256:
`1ef1c40425952d05137b0075943249ba33e3f700bf099c309e018bf9c65d125a`.
Root strict audit SHA256:
`7b7f99d3407fe493d2c89cd0c2d1161033b30c1074c87264412c052ece2a11c1`.

Twenty fresh Debug/Release deterministic PID1 guests passed on all ten
architectures using exact accepted Kernel901 SDK32 exports. Three additional
x86_64 production guests passed: Debug and Release each restart the actual
shell twice; a missing-shell guest produces three matching reap/exec-failure
sequences. Final hosted tools passed 630/630. The root rechecks complete source,
SDK, command, compiler-input, serial, disk and ELF hashes and rejects 80 serial
observer controls. Audits do not add executions. Original V8 twenty-guest
receipts used earlier compatible Kernel896 SDK32 exports and remain separate.

Independent V8 review SHA256:
`6d0b09884f9790762daabb0c6359698d66bf621fb7f6d9f129436259fb207390`.
It tests re-signed wrong/overflowing ELF admission and three hosted pending-TERM
mask/launch timings. V6/V7 defects and all failed attempts remain. The root's
first audit found four unexpected generated Python cache files, with every
source byte unchanged; the complete cache was moved into
`accepted-bytecode-quarantine-v1` and the strict inventory restored before
promotion. Nothing was deleted. Complete pre-promotion trees and post-promotion
inventories passed.

This is one foreground service with bounded restart and TERM/KILL shutdown,
not complete M7. Readiness/dependency graphs, service control IPC, accounts/login,
logging, persistent configuration, filesystem sync/quiesce, rescue and init-death
recovery remain open. Both OS modes explicitly use pinned Debug static musl.
Default root remains nonjournalled. Hardware/manual gates are deferred.

## Active isolated successors, not promoted

- `native-jbd2-sdk31-fresh-cut-v1`: storage agent runs fresh SDK31 directory
  software cuts 1,10,11,12,15,16,18,20 on x86_64/i386/MIPS passed: 24 native
  cuts, 48 native recovery/clean boots, 24 independent Linux recovery/e2fsck
  boots. Binding SHA256
  `c9a0d758338e15f250621731c58a8db6214035c799f6b3e72047415782b737e4`;
  accepted-checkpoint source correlation is retained. No source changes, no
  physical/volatile/torn-write/reordering claim. Old regular-mode MIPS timeouts
  remain unresolved.
- `native-user-udp-v1`: private SDK33 successor, V1 frozen at
  `candidate-v1` (904 Kernel / 538 OS sources), inventory SHA256
  `f1a727c25f40ed1cfdd847d63084fdecf5ba40a60cf463510580ca3bf6cebde9`.
  Independent review reproduces V1 owner-rebinding/reset lifetime defects.
  Do not promote V1. Author V2 repairs remain private: ten Debug/Release SDK33
  exports and ten standalone Debug boots reported passed; only x86_64 user UDP
  execution is qualified so far. Root requested all20 actual user UDP cases.
- `shared-musl-build-v1`: private M5 artifact recipe with explicit pinned
  linker artifacts. Eight profiles have successful shared-libc artifact builds.
  MIPS32/64 PIC runtime adapters now link, but DT_TEXTREL/WAX findings prevent
  qualification pending assembler fixes. These are artifacts, not native dynamic
  application execution. Linux-capable ld2.42 builds are isolated from native
  toolchains, including a new MIPS64 N64 linker. V4 is frozen; working recipe
  has a provisional MIPS64 linker admission extension. No promotion.

## Remaining target limits

CPU-time signal fields are zero. Init death/subreaper policy, stop/continue,
complete fault signals and SMP remain open. Default journalled root, shared
musl, broad POSIX/filesystem behavior, networking, persistent services, isolated
desktop and other M0-M12 requirements remain incomplete.

Historical journalled-directory campaigns belong to SDK30; fresh bounded
SDK31 cut/recovery qualification is recorded above. Three historical MIPS recovery FLUSH timeouts are unresolved;
a host fdatasync delay is not an established cause. Completion-boundary cuts do
not qualify torn writes, reordering, volatile caches or physical power loss.
External Linux6.13.4 reference has 21 cases; newer WSL2 differs in leader cause,
and binary/source authenticity is unestablished. Physical/manual acceptance is
deferred, not passed. Previous status is archived under
`build/status-history/pre-jbd2-geometry-promotion-v1`.

## Active private artifact and UDP qualification update

Accepted source remains Kernel901 / OS549 / SDK32 with predecessor promotion
`08456afbc1b265eb352136d5e65de4f1d4033e055440e259a316310ecf689cb9`.
No successor was promoted. Shared-musl V6 is composed on OS549 (553 files) and
passed 635 hosted tool tests. Its strict Debug/Release ten-architecture xmake
artifact campaign has 10 passes and 10 preserved failures. MIPS32 Debug later
passed a fresh full shared-libc build using the V3 Linux-assembler PIC runtime.
RISC-V/LoongArch PIC helpers and PPC secure-PLT runtime still need final artifact
qualification. These artifacts are not native dynamic-loader/TLS/pthread execution.
See `build/prototypes/shared-musl-build-v1/PRIVATE_PROGRESS_V7.md` for exact receipts.

Independent UDP V2 lifetime repair review passed. Private V3 is preparing a
frozen, mode/architecture-bound twenty-case actual user UDP QEMU campaign.
Current accepted SDK remains32. M0-M12 is incomplete; physical and manual
acceptance remain user-deferred.
