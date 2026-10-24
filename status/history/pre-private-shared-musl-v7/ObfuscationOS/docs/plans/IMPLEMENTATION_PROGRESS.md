# Workstation implementation progress

Implementation started on 2026-09-20. This record describes executable changes,
not completion of the [M0–M12 workstation target](README.md). The normative
inventories remain incomplete and no milestone is waived by a passing subset.

## Accepted isolated SDK32 PID 1 supervisor checkpoint

The current accepted isolated source is Kernel901 / OS549 / SDK32 at
`build/prototypes/native-signal-actions-sdk29-v1/working`. Primary repository
sources remain separate. The one-shot promotion receipt is
`build/prototypes/native-pid1-supervisor-integration-v1/promotion-v1.json`, SHA256
`08456afbc1b265eb352136d5e65de4f1d4033e055440e259a316310ecf689cb9`.
It adds 13 OS files and changes five, preserving the SDK32-only pressure helper,
strict init observer and static UDP task. Complete backups and post-promotion
inventories passed; the previous accepted OS536 checkpoint is retained.

Final composed sources passed 630 hosted tool tests, 20 fresh ten-architecture
Debug/Release deterministic PID1 guests against exact current Kernel901 SDK32,
and three production x86_64 guests: Debug/Release shell restarts and repeated
missing-service exec diagnostics. The root strict audit rechecks every pinned
source, SDK, command, compiler input, serial, disk and ELF and rejects 80
observer controls. Its SHA256 is
`7b7f99d3407fe493d2c89cd0c2d1161033b30c1074c87264412c052ece2a11c1`.
The independent V8 review covers re-signed ELF-machine/word-limit mutations and
three hosted pending-TERM mask/launch controls. These rechecks are not extra
executions. Original V6/V7 failures and earlier Kernel896 SDK32 campaigns remain
separate evidence.

This is a bounded one-service static-musl supervisor, not complete M7.
Readiness/dependency graphs, accounts/login, persistent configuration, full
filesystem sync/quiesce shutdown, rescue and init-death recovery remain open.
The default root remains nonjournalled and both OS modes explicitly use pinned
Debug static musl. Private SDK33 user UDP and shared-musl artifact work continues;
neither is part of this accepted checkpoint. M11 physical hardware and M12
manual desktop acceptance stay open by user direction.

## Earlier accepted isolated SDK32 static IPv4/UDP checkpoint

The root integrated this bounded service into the accepted isolated consumer,
preserving the strict init observer and pressure-admission fixes. The complete
checkpoint is Kernel901 / OS536 / SDK32 at
`build/prototypes/native-signal-actions-sdk29-v1/working`; primary repository
sources remain separate. The one-shot promotion receipt is
`build/prototypes/native-static-ipv4-udp-integration-v1/promotion-v1.json`, SHA256
`5cb897a4175120820bff9e91dc74e0c3fa2d92dd88cd19af40c7128eb2a7c4fb`.
It applies eight OS additions and one xmake contract change, with complete
Kernel/OS backups and post-promotion inventories verified.

The root audit also rejects embedded carriage returns and unterminated serial
tails, for 15 negative controls total. Its rechecks and 80 image reconstructions
do not add new executions. A fresh final-source ASan/UBSan endpoint model passed
121,557 assertions and the xmake compile entry passed. LeakSanitizer is disabled
because of the sandbox ptrace restriction; the original failure is retained.
The isolated implementation is a privileged fixed-peer polling service. M6,
ordinary user socket integration and M12 remain open.

V6/V7 PID 1 candidates remain held for independently reproduced defects. The
accepted successor is V8 composed onto OS549, as recorded above. A separate
private SDK33 user UDP path has x86_64 native evidence and ongoing ownership
review; it has not been accepted or promoted.

## Original SDK32 static IPv4/UDP network prototype

An isolated OS candidate adds a boot-CPU-polling Virtio NIC service for one
statically configured ARP/IPv4/UDP peer. It consumes an explicit architecture-
and mode-specific SDK32 export; it does not include or build Kernel source.
The frozen 534-file OS candidate and the SDK32 producer matrix are retained
under `build/prototypes/native-static-ipv4-udp-v1` and
`build/prototypes/native-network-wire-v1` at the workspace root. The former
contains an English handoff with exact source, SDK, matrix and audit hashes.

The final consumer matrix passed 20 ten-architecture Debug/Release qualifiers
and 80 actual QEMU scenarios. An external QEMU peer verified 20 ARP replies,
1,940 UDP replies and 240 hostile packets without a reply. An independent strict
audit reconstructed all 80 images from retained ELFs, checked the full serial
and bidirectional frame evidence, and rejected 13 corrupted-evidence controls.
The hosted packet model separately passed 121,557 checks; the x86_64 Debug
xmake compile entry passed. These diagnostic profiles do not change the ordinary
four-architecture OS userland matrix. Earlier failed/diagnostic attempts remain
retained.

This candidate is not yet promoted into the main OS and Kernel trees, which
still require a controlled cumulative SDK integration. No socket API, general
IPv4/IPv6 host stack, IRQ networking, SMP, physical-machine or desktop-network
acceptance is claimed. M6 and M12 remain open. The user has deferred physical
M11 and manual M12 desktop acceptance; automatic acceptance continues.

## ABI 20 maintained ext4 timestamp integration

Shared Kernel SDK/native modules use generation20 with native UAPI0.6.0.
Explicit maintained mounts of the clean nonjournalled ext4 subset update A/M/C
from one checked realtime sample per provider event. Encoding all affected records
precedes writes. Strict access errors publish no provider data, and uncertain
storage effects quarantine maintained metadata. The contract is
`ObfuscationKernel/docs/MAINTAINED_EXT4_TIMESTAMPS.md`.

The frozen776-file candidate passed20 Debug/Release rows and610 commands across
all ten profiles, retaining cumulative musl, storage, metadata, RTC and clock-set
gates. New SDK-only native fixtures cover120 ext4 geometry/architecture/mode
combinations. Twenty actual UID1000 native-to-musl boots validate file operations,
automatic timestamp authority, denied clock setting and7 final raw nodes per boot.
Linux stat stays ENOSYS. All mutable input and output disk bytes are retained.

Six-layout hosted event/fault runs pass in normal and ASan/UBSan modes, including
four-extent growth/refusal boundaries and lossless reconstruction of cache and
durable images for injected read/write/flush faults. These are model results,
separate from real guest execution. LeakSanitizer was disabled. Independent review found and drove fixes for remove error masking,
unsupported access mutation flags and continued directory reads after failure.
Evidence validation additionally rejects unequal samples within one event.

Sixteen extra epoch0/2040 boots retain cumulative public-clock/mkdir coverage.
Fresh Linux readonly references check mounted metadata, directory creation and
21 exact maintained A/M/C fields on7 nodes, including new extra-isize16 at2040.
Linux binary provenance is pinned; full source-build provenance is not established.
A fresh shared x86 Debug producer and SDK-only consumer passes21 commands with
three rebuilt musl probes. The shared tool suite passes144 tests.

Initial parallel native lanes include three retained failures. One
explicitly reports a Virtio completion timeout; two generic fault assertions do
not establish their original error status. Exact-original AArch64 replays pass,
and final selected replacement lanes are rerun from identical frozen sources
with lower I/O concurrency. Failed attempts remain failures; no timeout policy
or acceptance assertion was relaxed. Receipts identify the selected lane set.

Default writable root policy remains unqualified. Existing inode extra extents
never grow; newly zeroed256-byte maintained inodes declare16 bytes. RAM/archive
and synthetic timestamps remain unavailable. No Linux stat, default-root adoption,
utimens, birthtime, journalled timestamp updates, power-loss atomicity, complete
ext4/POSIX, physical platform or SMP claim follows. Calls retain serialized
boot-CPU ownership. The ledger has90 requirements and163 tests; M0–M12 remains
open. Exact frozen/retry/model/Linux/review/export receipts are retained under
`/tmp/obfuscation-writable-timestamp-stage` and the workspace build directories
`workstation-abi20-maintained-ext4-v1` and `workstation-abi20-timestamps`.

## ABI 19 administrative realtime integration

Shared Kernel SDK/native modules now use generation 19 with native UAPI 0.6.0.
Native clock_settime (227) and 14 Linux setter forms across ten profiles share a
checked CLOCK_REALTIME operation. Explicit administrative software time retains
the physical boot-clock provenance and never writes the RTC or resets monotonic
time. The contract is `ObfuscationKernel/docs/REALTIME_SETTING.md`.

The frozen 759-file candidate passed **20 Debug/Release rows and 550 commands**.
The new gates comprise 20 privileged software-provenance diagnostics and 40
actual native/musl root or initial-UID1000 fixture boots. Independent retained
serial audits checked 240 clock changes while waiters were blocked, 120 elapsed
wait instances, 80 exact wall/monotonic brackets and 56 raw setter-form records.
Relative sleep, absolute monotonic sleep, poll, select, ppoll and pselect preserve
their elapsed behavior across forward/backward wall changes. The fixture directly
observes sleep deadline/generation stability; poll/select deadlines remain
private and are covered by pending-syscall observations plus elapsed checks.
Root/fork/exec share the selected software clock; actual nonroot calls reject.

The cumulative suite retains 40 musl executions, 2680 storage cases, 328 mounted
metadata cases and 56 privileged RTC cases. **16 additional epoch0/2040 boots
and 32 cumulative musl executions** pass on the four qualified RTC profiles.
The native-created x86 image passes a fresh actual Linux readonly mount checking
19 nodes and four file payloads; two further Linux reference boots verify mounted
metadata. These runners now retain pre-guest and final disk bytes. That closes
the retention gap for this generation without retroactively qualifying missing
inputs from earlier generations. All disk, source, tool, SDK and probe identities
are bound to exact preserved artifacts; same-basename probe files cannot collide.

A further fresh shared x86_64 Debug producer and SDK-only consumer passed 18
commands, rebuilding both cumulative and clock musl probes and the native
launchers. Its two authority boots and privileged diagnostic are additional to
the frozen matrix. Hosted coordinator/adapter/empty-TLS tests, sanitizer runs,
all-ten target compiles, strict evidence parser tests and 136 OS tool tests are
separate from guest execution. A binary-pinned disposable Linux clock reference
checks root/UID1000 validation ordering and elapsed arithmetic; the host clock
is untouched. Full Linux source provenance is not established by that hash.

The exact delivered SDK18 negative returns ENOSYS for native/Linux setters.
Earlier empty-PT_TLS exec failures remain preserved; the admitted empty segment
fix retains duplicate/range/alignment and nonempty-template rejection. Initial
cross-fixture host-toolchain failures and the MIPS64 long-double printf link
failure also remain preserved. Final probes use integer diagnostics; complete
printf/math support is not claimed. Independent representative i386/ppc/mips64
Debug gates passed before the final matrix, with a standalone cross toolchain.

Authority remains effective UID0 or trusted kernel credentials, without Linux
CAP_SYS_TIME or user namespaces. Execution is the serialized boot-CPU main loop;
IRQ/NMI callers and secondary CPUs must not use this unsynchronized service.
No NTP, RTC calendar writes, absolute realtime timers, suspend/migration,
filesystem timestamp maintenance, Linux stat, general threads/signals, physical
platform or SMP qualification follows. The ledger has 88 requirements and 158
tests; it remains a seed inventory and every M0–M12 completion gate stays open.
Exact source, matrix, review, shared rebuild and SDK export receipts are retained
under `/tmp/obfuscation-clock-setting-stage`. Earlier delivery history follows.

## ABI 18 directory creation integration

Shared Kernel SDK/native modules now use generation18 with native UAPI0.5.0.
Linux mkdir/mkdirat use the common resolver, credentials and process creation
mask. The filesystem creation boundary accepts final mode and full UID/GID before
publication, returning a stable borrowed child. RAM and nonjournalled ext4 inherit
a setgid parent's group; directories also inherit setgid. Existing entries,
pathname copies, directory descriptors and duplicate/permission ordering have
explicit checked behavior. Readonly mounted metadata remains a separate provider.

The frozen739-file candidate passed **20 Debug/Release rows,470 commands and40
cumulative musl executions** across all ten profiles. Independent raw inode and
directory audits checked380 created/fixture nodes and80 new file payloads over
20 guest images (19 distinct nodes/four new files per boot). Another **16 fresh
epoch0/2040 boots and32 musl executions** on the four qualified RTC profiles
checked304 nodes/64 new payloads, alongside224 prior payloads. The previous2680
storage cases,328 mounted-metadata cases,56 privileged RTC cases and two Linux
mounted-metadata reference boots remain present. A further actual Linux guest
mounted the native-created image readonly, checked19 nodes/four files, and left
the disk unchanged. The Linux binary is pinned; full Linux source provenance
is not asserted.

A fresh shared x86_64 Debug Kernel producer, exact SDK-only OS consumer and musl
probe passed14 commands, two cumulative musl executions,19 node/four new payload
checks and14 prior file checks. This rebuild is additional to the frozen matrix.
All ten common/adapter models, all16 declared mkdir syscall forms, target
compiles and sanitizer checks pass. Six ext4 block/inode layouts cover3108
transport-fault scenarios and18 fsck-clean success/rollback images. Prior Linux
adapter regressions retain120 model-profile runs; these are hosted evidence.
ASan/UBSan ran with leak detection disabled because the sandbox uses ptrace.

Four earlier Debug prototypes passed56 commands/eight musl executions. The exact
ABI17 negative reaches ENOSYS at the first mkdir after passing public clocks.
The initial prototype failure was a host fixture parser rejecting debugfs's
signed rendering of a valid high GID; the corrected parser validates its range
before uint32 normalization. Those failed artifacts are retained. The mounted
model's initial wrong-fixture attempt and source/log-only legacy ext4 evidence
are also preserved. Pre-guest mutable disk bytes were not retained by the musl
runner, so recorded initial disk hashes cannot be independently replayed from
those final disks; retained final image bytes are independently verified.

This remains a bounded filesystem/ABI slice. Nonjournalled creation can fail
after correct-attribute publication; it does not promise crash atomicity or
all-errors rollback. Readonly providers currently report unsupported, without
an EROFS claim. The inherited allocator does not reconcile every corrupted
bitmap/count combination; a dedicated transport-fault trace for three-allocation
extent cleanup is still absent. ACLs, fsuid/fsgid, general limits, writable epoch
timestamps, Linux stat, threads/signals, SMP, physical platforms, networking and
isolated graphics remain open. The ledger contains86 requirements/152 tests;
M0–M12 are incomplete. Exact receipts and retained evidence live under
`obfuscation-linux-directory-create-stage`; earlier ABI17/16/14/13 history follows.

## ABI 17 checked public realtime integration

The shared source and matching SDK/native modules now use generation17 with
native UAPI0.5.0. Native and Linux clock_gettime/getres share a checked provider;
native legacy time/gettimeofday now use UNIX epoch time. Unavailable or invalid
sources return EIO before output. Native time checks register-width and errno
collision limits before optional copying; Linux time32/time64 layout and overflow
are explicit. Fork, exec and process switching preserve the one-shot RTC anchor.

The frozen R3 union passed **20 Debug/Release rows,470 producer/consumer commands
and40 cumulative musl executions** across all ten profiles. It also passed
**16 fresh epoch0/2040 boots and32 additional cumulative musl executions** on
AArch64/ARM32/RV64/RV32 in both modes. Default matrix clocks used leap-day2024.
Each boot includes native and musl parent, fork and exec checks;
protected-page copies, elapsed sleep, capability errors and legacy overflow are
checked. Independent retained-byte/UTC audits reread14 files per date boot and
verify exact SDK, source, direct tool, binary and serial identities.

All previous storage gates remain present:2680 earlier storage cases,328 mounted
metadata cases,56 privileged RTC cases and two actual Linux reference boots.
A forced shared x86_64 Debug producer/consumer and fresh musl build passed14
commands, two cumulative executions and14 offline file checks. These shared
checks are additional to the frozen matrix, not a replacement for it.

Positive realtime sources remain ARM32/AArch64/RV32/RV64. The six other profiles
explicitly refuse unavailable sources. musl time/gettimeofday ignore upstream
clock failures, so their wrappers are tested only after a successful realtime
preflight. Legacy-time32 musl clock_getres supplies an internal output even when
its caller passes NULL; that wrapper correctly returns EIO without an RTC, while
the raw NULL syscall remains identity-only. No source/calendar fallback is used.

The R2 i386 full-matrix attempt exposed an incorrect probe assumption about that
libc NULL behavior. Its failed row and cancelled remainder remain retained. R3
corrected only the probe and documentation; tested production inputs stayed
identical. The102 R2 hosted commands and ten target compiles were rehashed and
reused explicitly, not relabeled as new executions. Four corrected R3 prototypes
passed56 commands, and the exact ABI16 negative fails at the new realtime gate
after all earlier umask checks. R1/R2/component evidence remains separately bound.

The seed ledger has84 requirements and146 tests. General POSIX, writable epoch
timestamps, Linux stat, realtime clock setting/absolute timers, threads/signals,
SMP, physical UTC accuracy, networking and the isolated desktop remain open.
M0–M12 are incomplete. Final artifacts are retained under
`obfuscation-public-realtime-r3-stage`; earlier ABI16 history follows unchanged.

## ABI 16 directory, creation mask, mounted metadata and RTC integration

The shared source and matching SDK/native-module artifacts now use generation16;
native UAPI0.4.0 is unchanged. The frozen combined source passed **20 Debug/Release
rows,470 commands and40 cumulative musl executions** across all ten profiles.
Independent byte/identity audits verified **2,680 earlier storage cases,328
mounted-metadata cases,56 privileged RTC cases and two actual Linux reference
boots**. The four isolated build lanes used identical722-file frozen inputs.
A fresh shared x86_64 Debug producer, SDK consumer and musl rebuild passed14
commands and two cumulative executions, with14 independently reread disk files.

Bounded getdents64 uses real provider inode identities, explicit target-endian
records and retained shared directory cookies. Missing identities remain errors;
directory SEEK_END rejects. The process creation mask follows common resource
ownership through fork and exec; all eight new files per musl boot retain the
expected modes and existing-inode truncation preserves its original mode.
The isolated directory and umask components also passed their separate full
20-row/270-command/40-musl matrices; those artifacts remain generation-specific.

Mounted ext4 keeps namespace/data readonly and permits only trusted internal
metadata maintenance through its private retained transaction/session/cache.
Repeated inode changes, all qualified publication/flush cuts, recovery and Linux
interop are included. The shipped persistent invariant regression additionally
covers post-success generation exhaustion and stale/foreign authority. The
initial owned-regression run used an incompatible mounted fixture; its failure
is preserved, and the unchanged suite passed against its exact original fixture.

RTC/epoch diagnostics qualify selected ARM32/AArch64/RV32/RV64 sources and retain
explicit unavailable-source refusals elsewhere. Public realtime is still disabled
in ABI16. The live monotonic getres correction is included. Separate SDK17 public
clock development remains a candidate, never an ABI16 capability claim.

The seed ledger remains83 requirements and143 tests. M0–M12 remain incomplete:
general POSIX, Linux stat, namespace races, threads/signals, journalled default
root, SMP, physical hardware, networking and the isolated desktop remain open.
Qualification artifacts are retained under `obfuscation-abi16-integration`.

## ABI 14 positional I/O, select, file attributes and owned ext4 integration

This combined candidate uses **Kernel SDK/native extension ABI 14** and native
UAPI **0.4.0**. Exported operation arrays, wait records and filesystem attributes
require rebuilt extensions; provisional ABI14 candidates are distinct snapshots.
The shared source and exact producer/consumer artifacts now use ABI14.

Linux pread/pwrite uses retained common file descriptions without changing their
shared position. Target-width aligned offset pairs and MIPS stack arguments are
decoded explicitly. Linux O_APPEND uses a static policy; the native positional
policy is preserved. Transfers remain bounded to4096 bytes and signed native-word
offsets/endpoints; full off64 and arbitrary partial-copy semantics remain open.

Select/pselect shares the existing retained poll wait engine. It preserves target
word/endian fd sets, real oldselect signatures, bit counts across sets, ordered
copyout and timeout updates. Inputs are copied once and saved frames complete
once; exec/exit cancel retained registrations. The local descriptor capacity is32;
nonnull temporary signal masks, signals/restarts/cancellation, sockets and native
SMP are separate work. The cumulative musl suite now runs positional checks before
select, with separate diagnostic ranges and strict complete-run evidence parsing.

File attributes carry explicit validity and provider provenance. RAM nodes have
monotonic inode identities; retained provider identities map to anonymous device
minors. Real epoch timestamps are decoded only from admitted clean readonly ext4.
Writable/RAM/archive/pipe/console timestamps remain unavailable. Linux stat-family
success stays disabled because the current musl fallback would expose unavailable
fields. Native stat copies exactly its unchanged UAPI size using zero-initialized
field-by-field byte projection. Root reproduced and corrected unspecified padding
in the initial candidate, and corrected its stale module-generation constant.
The candidate's previous artifacts remain preserved separately.

The owned ext4 transaction privately retains the canonical cache and its exclusive
block session through publication and checkpoint. Reader admissions quiesce before
mutation; credits and generation advances are checked in advance. Sealed images
and durability authority cannot be supplied by callers. Failure quarantines the
owner without retry/close escape. Logical partition offsets are normalized once.
This is a bounded metadata transaction, not journalled mount admission or an
unrestricted filesystem/cache implementation.

The positional candidate passed ten Debug rows,140 commands and20 cumulative
musl executions with exact disk contents and an old-ABI ENOSYS control. Owned ext4
independently passed3,879 sanitizer checks,23 authority-corruption cases, two edge
cases, ten standalone boots,120 SDK-only native device cases and two Linux guest
interoperability boots. Candidate evidence does not qualify the combined source.

Combined preparation passed all-ten select, positional and poll sanitizer models,
ten freestanding adapter compiles, ten cumulative musl builds, six ext4 attribute
fixture combinations and110 OS tool regressions. Independent integration reviews
also exercised the exact-boundary native stat runtime and combined owner headers.
The exact-source Debug/Release matrix passed **20 rows /430 commands /40
cumulative musl executions /2,680 storage device cases**. It includes every
earlier journal/session/cache gate, all44 owned transaction cases and six
readonly attribute device cases per architecture/mode. Eighteen original rows
and two fresh complete Release rows are independently audited. The first
MIPS64 Release attempt timed out in a block-session fault probe; its partial
row and failure logs remain preserved and excluded. The fresh same-source
retry retained the exact runner and assertions.

After integration, a forced shared x86_64 Debug SDK, OS and musl rebuild
passed14 commands and two cumulative executions, with fresh offline byte
checks. Every shared build input matches the qualified frozen generation.
The qualification receipt is retained under `obfuscation-abi14-integration`.

The ledger now records **78 seed requirements and133 tests**. M0 and every complete
M1–M12 workstation milestone remain incomplete. Physical devices, SMP, general
threads/signals, full POSIX, networking and the isolated desktop are not implied.

## Prior ABI 13 poll, legacy open, canonical buffers and ARM32 integration

The combined source uses **Kernel SDK/native extension ABI 13**, with native
UAPI **0.4.0** unchanged. Added Linux operation arrays and typed poll completion
metadata require rebuilt native extensions. ARM32 now uses the explicitly
validated `arm32-linux-image` boot artifact at `0x40010000`. Earlier provisional
ABI 13 candidate artifacts are not interchangeable with this final source union;
all exported SDKs and consumers are rebuilt together.

Linux poll/ppoll/time64 freezes target-endian descriptor inputs, retains open
file descriptions and completes saved frames once. A static policy preserves
native pipe behavior while providing Linux EOF/error/normal-event semantics.
Raw ppoll remainder copyback uses full timespec endpoints separately from bounded
wait deadlines. Non-null signal masks remain unsupported after checked admission;
no signals, EINTR/restart, cancellation, sockets, select/epoll or native SMP claim.
Legacy open/creat adapts the six profiles defining those syscalls to the existing
checked openat service. Public musl open/creat uses openat on the remaining four.
Current-directory object identity, narrow scalar flags/modes, copy errors and
resource/large-file admission before create or truncate are retained.

Canonical MetadataBuffers privately owns an exclusive block session and admits
bounded 1/2/4 KiB immutable canonical blocks, read pins and discardable private
transaction copies. Complete participant reservation precedes edits. A reviewed
transfer-bound defect was fixed: incompatible block size rejects before I/O and
cleanly releases the healthy session. There is no commit, checkpoint, home
writeback, journalled mount or production cache/reclaim claim. Quarantine retains
backing; it does not establish asynchronous cancellation or DMA fencing.

ARM32 captures actual loader registers/state, rejects unsupported data endianness
before stack/BSS stores, and checks mode/MMU/cache/CPU state before FDT access.
The full FDT, boot prefix and complete linked image including NOLOAD are excluded
from allocation. Runtime frames use the existing 256 MiB supervisor aperture,
while upper firmware RAM remains represented. Seven profiles now support bounded
firmware-backed process frames; LoongArch64/MIPS/MIPS64 retain explicit linker
backing. Missing/bad ARM firmware fails without fallback. The 1024-frame global
and 128-page process limits remain; this is not general allocation or board support.

Independent candidates passed and were separately audited:

- Poll and legacy open each passed ten Debug rows, 140 commands and 20 actual
  cumulative musl executions. Older kernels fail at the first newly required
  call with ENOSYS. Independent reviews reran sanitizer suites and rehashed the
  source, SDKs, artifacts, logs and expected persisted bytes.
- Canonical buffers passed 320 sanitizer checks, 127 session regressions, ten
  freestanding compiles, ten standalone boots and 50 SDK-only native device
  cases. Every scratch disk remained byte-identical. The original transfer-bound
  reproducer now rejects open without quarantining the device.
- Final ARM source passed ten Debug rows plus ARM Release: 153 commands and
  22 cumulative musl executions, 38 firmware/page/frame probes, 27 Debug session
  device cases and nine startup negatives. Its earlier successful generation
  predates the endian correction and remains historical evidence only.

Combined host validation passed Linux poll/open and native poll sanitizers,
metadata/session checks, firmware normalization/frame checks, strict evidence
parsers and **108 OS tool tests**. The frozen combined Debug/Release matrix
passed **20 rows /390 commands /40 cumulative musl executions** under
`obfuscation-poll-cache-arm-integration`. Its independent audit and shared
x86 rebuild remain preserved as ABI13 evidence, separate from ABI14.
The shared working tree separately force-rebuilt its x86_64 Debug ABI13 SDK and
exact OS consumer in `build/workstation-abi13-shared-x86/run-v1`: **14 commands
passed**, including standalone boot, native execution, persistence and two
cumulative musl executions including legacy open and poll. An independent audit
rechecked its557 source inputs/archive, exact SDK/artifacts/logs, frame provenance,
all five stored probe files and fsck. All557 shared build inputs match the frozen
union; other shared architecture/mode artifacts have not been relabelled.

The ledger records **73 seed requirements and 121 tests**. These additions do
not close M0 or any complete M1–M12 workstation milestone.

## ABI 12 sleep and exclusive block-session integration

This qualified generation uses **Kernel SDK/native extension ABI 12**, with native
UAPI **0.4.0** unchanged. Added sleep operations change the exported ProfileData
array layout, requiring rebuilt extensions and explicit rejection of older SDKs.
Linux nanosleep, clock_nanosleep and monotonic clock_getres use target-endian
legacy/time64 records and the shared native deadline helper. Saved-frame
completion never rereads the request. Successful calls leave remainder memory
untouched. Signals, EINTR/restart, cancellation, absolute realtime and CPU clocks
remain unavailable; this does not satisfy complete clock/wait or POSIX semantics.

Kernel-owned BlockSessions adds bounded exclusive registration, partition views,
request ownership and dirty/unflushed accounting. Transport calls run outside the
metadata lock. Duplicate registration rejects before raw geometry queries,
including during initial admission and after quarantine. I/O/integrity/geometry
failure or dirty abandonment quarantines the device without a reset escape.
The boot owner must still withhold independent raw aliases. Canonical metadata
cache, journalled mount admission, asynchronous cancellation, DMA fencing, native
SMP and physical power-loss qualification remain separate work.

Independent sleep qualification passed ten Debug rows, 140 commands and 20 actual
musl executions, including legacy/time64 and unchanged-remainder probes. The old
ABI 11 kernel negative control stops at clock_getres with ENOSYS. Independent
review reran sanitizer adapter, native poll/deadline and supplemental saved-frame,
exec/exit and stale-generation tests without a remaining blocker. The block
session candidate passed 118 hosted checks, ten target compiles, ten standalone
boots and 78 native device cases; every write/flush fault was exercised on
x86_64 and PPC, with independent reservation/error review.

The shared working tree force-rebuilt its own x86_64 Debug ABI 12 SDK and exact
OS consumer in `build/workstation-abi12-shared-x86/run-v1`: **14 commands passed**,
including standalone boot, native simplefs/ext4 execution, persistence and two
cumulative musl executions including sleep. The independent receipt rechecks the
source archive, retained SDK, artifacts and logs, runtime frame provenance,
offline file bytes and fsck. This explicitly selected row does not qualify the
remaining architectures or Release mode.

The frozen combined source completed
`obfuscation-sleep-sessions-integration/ObfuscationOS/build/workstation-sleep-sessions/run-v1`:
**20 Debug/Release rows and 370 passing commands**, including **40 cumulative musl
executions**. Independent audits rehashed every source/archive, retained SDK,
primary/nested artifact and log, parsed actual musl/runtime-frame evidence, and
checked offline file bytes and fsck. Device cases include 60 replay, 60 preview,
380 recovery-completion, 540 transaction and 540 exclusive-session boots; every
write/flush fault point ran on every architecture/mode. All **541 shared source
files** matched this qualified snapshot before the next integration.

Combined hosted checks passed the sleep sanitizer suite, 118 block-session
checks and all-ten compiles, and 94 OS tool regressions. This generation's ledger
has **69 seed requirements and 113 tests**. QEMU completed-operation faults do
not establish physical power-loss durability, DMA fencing or native SMP.
M0 and all other workstation milestones remain incomplete.

## ABI 11 pipe/seek/metadata-writer integration

The shared combined source uses **Kernel SDK/native extension ABI 11**; native UAPI
remains **0.4.0**. Added Linux operations change the exported ProfileData arrays,
so the OS rejects ABI 10 and earlier artifacts and native extensions must rebuild.

Linux pipe/pipe2 now use the common native endpoints, with MIPS two-register
pipe returns, target-endian descriptor pairs, NONBLOCK/CLOEXEC, copied-output
rollback and reference lifetimes. Admission preserves flags, global ENFILE,
per-process EMFILE and output EFAULT precedence. SIGPIPE is not implemented;
readerless writes only return EPIPE. Linux lseek/_llseek use shared native file
positions, including signed-word/split-offset adaptation, MIPS stack argument,
unaligned endian result copyout and retained position after EFAULT. Actual 32-bit
positions remain capped at INT32_MAX; full off64 and DATA/HOLE are still open.

The bounded ext4 writer durably stages a checksum-v3 descriptor, two metadata
payloads and end sentinel, then commit, recovery flag and journal publication.
Only one ordinary inode's permissions, ownership, ctime and version may change.
Successful publication leaves home metadata old until separate recovery
completion checkpoints it. Exclusive quiescent device ownership remains a caller
precondition. Journalled mounts, allocation/data/directory writes, general cache
coherence and arbitrary torn-control reconstruction remain unavailable.

Corrected pipe and seek candidates each passed ten Debug rows, 140 commands and
20 musl executions with exact source/SDK/artifact audits. The writer candidate
passed 438 hosted cases, 210 completion regressions, ten target compiles and
standalone boots, 78 private-device cases and two Linux interoperability guests.
These isolated results do not substitute for combined-source qualification.

The frozen combined source completed
`obfuscation-pipe-seek-writer-integration/ObfuscationOS/build/workstation-pipe-seek-writer/run-v1`:
**20 Debug/Release rows and 350 passing commands**, including 40 complete musl
executions. Exact-source and deep audits rechecked the archive, every retained
SDK file, primary/nested artifacts and logs, runtime frames, offline ext4 bytes
and all device-case receipts. Every architecture/mode ran all writer and
completion fault points: 60 replay, 60 preview, 380 completion and 540 transaction
private-device boots. All 531 shared source files matched the qualified snapshot
before ABI 12 integration. These are completed-operation fault injections, not
physical power-loss or native SMP qualification.

Combined hosted gates passed all-ten pipe/seek sanitizers and target compiles,
process-resource regressions, 438 writer cases, 210 completion regressions,
ten musl probe builds and 93 OS tools. The ABI 11 ledger had **67 seed requirements
and 108 tests**; M0 and all other milestones remained incomplete.

The shared working tree also force-rebuilt its own x86_64 Debug ABI 11 SDK and
exact OS consumer under `build/workstation-abi11-shared-x86/run-v1`: 14 commands
passed, including standalone boot, OS userspace, persistence and both cumulative
pipe/seek musl runs. Its receipt rechecks all 531 captured source files, source
archive, retained SDK, artifacts and logs. Shared build artifacts now include
this current x86_64 Debug generation; staged matrix artifacts remain separate.

## ABI 10 runtime/storage integration

Kernel SDK/native extension ABI is **10**; native UAPI remains **0.4.0**.
The descriptor large-file admission field and atomic CLOEXEC duplication method
require rebuilt native extensions; the OS rejects ABI 9 and earlier SDKs.

The current combined source adds:

- Actual process allocation from qualified firmware frames on i386, x86_64,
  AArch64, RV32, RV64 and PPC. ARM32, LoongArch64, MIPS and MIPS64 retain explicitly
  labeled linker pools. Supported firmware discovery failures cannot silently
  fall back. Final linked images, including OS extensions/archive/NOLOAD, are
  excluded before allocation. Owner/generation handles and all shared/staged
  backing remain pinned until failed replacement tables are actually retired.
- Linux getcwd/chdir/fchdir/readlink/readlinkat and scalar dup/dup2/dup3/fcntl
  operations through common native objects. Linux scalar widths, per-descriptor
  CLOEXEC, shared offsets/status and large-file admission metadata are preserved.
  New probes execute real PROT_NONE buffer edges, fork/exec inheritance and
  descriptor exhaustion/reuse; offline descriptor-test bytes must be `abcdef!x`.
- Bounded ext4 recovery completion on an exclusive private device: validate the
  final view and allocated ordinary inodes, flush home writes, publish an empty
  journal, then clear the filesystem recovery flag and flush again. The admitted
  one-transaction 1 KiB profile remains narrow; no journalled mount or writer is
  enabled. Invalid torn checksummed metadata rejects before further mutation.

Independent stages passed ten Debug architecture rows each. Frame ownership
passed 80 commands and eleven actual startup rejection cases. Path and descriptor
stages each passed 140 commands with exact retained source/SDK/artifact/log hashes.
Completion passed 209 recovery/fault cases plus one inode-budget case, 410 existing
preview regressions, ten target compiles, ten standalone boots, 62 private-device
recovery boots and two Linux guest interoperability boots. Linux independently
recovers the original dirty image; our completed image is readable on a readonly
Linux device and remains byte-identical. The journal sequence is 4 for the pinned
sequence-2 fixture. QEMU completed-operation fault injection is not physical
power-loss qualification.

Independent reviews found no remaining blocker in these bounded contracts.
The completion review corrected overly broad unchanged-bitmap target admission.
The path follow-up now explicitly tests permission-denied cwd changes and an
unlinked cwd. Combined hosted checks passed both VM backing modes, frame registry,
Linux runtime/poll/path/descriptor adapters, 210 completion cases and 91 OS tools.
The contract ledger now contains **63 seed requirements and 100 tests**; its
schema validates, while the complete normative inventory and M0 remain open.

The ABI 10 combined source completed `build/workstation-runtime-completion/run-v1`:
**20 Debug/Release rows and 330 passing commands**. Its `verified-summary.json`
rechecks the source archive, every retained SDK file, primary artifacts and logs
against the source before ABI 11 integration. Every recovery write/flush point
ran on each profile/mode, totaling 380 private-device completion boots. The 1024-frame global/128-page process and 32-fd limits
remain. General allocation, threads/signals, complete POSIX, journal writer,
network/services, isolated graphics, SMP and physical workstation gates remain
unfinished. No M0–M12 milestone is complete. Separate pipe/seek and journal-writer
candidates are still outside this shared integration.

## ABI 9 integration: completed qualification

Kernel SDK/native extension ABI is **9**; native UAPI is **0.4.0**. The new
fallible VFS metadata/lookup slots require rebuilding every native extension.
The OS validator rejects ABI 8 and earlier. UAPI 0.4 adds the native `MAP_FIXED`
flag without renumbering existing syscalls.

Integrated typed captured-firmware discovery, checked VFS resolver/open metadata
and lookup, consuming `PathReference::release()` with explicit open cleanup,
actual mapped `brk` and private-anonymous fixed replacement, and read-only
device-derived ext4 internal-journal binding. No journalled mount gate was
relaxed. Firmware discovery still does not enable a native allocator. Other VFS
metadata callers and complete Linux process/thread semantics remain work.

The canonical musl probe now executes heap allocation, zeroing, alignment,
replacement, reuse and exhaustion/recovery. All ten applications use
`-fno-builtin`: a retained PowerPC negative control demonstrates that Clang 18
otherwise removes a malloc pressure loop and folds its errno test. This was a
probe compiler issue; libc is unchanged. `--musl-heap` and
`--jbd2-runtime-binding` select the new gates in the workstation qualifier.
The integrated hosted checks passed VM/runtime/path sanitizers, all-ten path
ownership and Linux adapter compilation, 418 ext4 binding cases, 84 OS tool
tests, 29 QEMU runner tests, and ten actual standalone firmware probes.
`build/workstation-abi9/run-v2` passed all ten Debug rows. Its first Release
build stopped on a GCC 14.2.0 internal compiler error in `kernel_syscalls.cpp`;
the compiler crash and logs are retained, and its cause is not established.
`run-v3-release` passed all ten Release rows with an identical source-hash
snapshot. The combined result is **20 rows and 290 passing commands**;
`build/workstation-abi9/abi9-exact-source-summary.json` records verification of
source archives, retained SDK contents, primary artifacts and log hashes.
The first attempt
stopped during compilation on a preserved debug
assertion still naming UAPI minor 3; it was updated to 4 before the fresh run.
The completed Debug rows retain exact ABI 9 SDKs, source archives and all guest
inputs. Staged results do not qualify later combined source.

The next batch has integrated Linux identity/fork/exec/wait including RV32's
musl waitid path, qualified firmware RAM normalization, entry-to-runtime frame
ownership probes, checked POSIX/VFS and executable-load callers, and a read-only
journal replay view. Independent review added a hard-link destination lookup
guard, corrected Linux leader identity/LP64 wait scalars, and retired ext4 views
on dangling selected directory targets or any underlying reader failure.
These follow-up changes are separate from the preceding ABI 9 baseline matrix.
`build/workstation-process-preview/run-v1` completed all ten Debug/Release rows: **20 rows / 310 commands**. Its `verified-summary.json` rechecks the source archive,
all retained SDK contents, primary artifacts and logs against that exact source.
Thirteen integrated host/build/tool checks passed, including 410 ext4 preview
cases, the normalization oracle, native VM rollback and checked exec cleanup.
An old runtime test expected native TID from Linux set_tid_address; it now checks
the admitted Linux leader PID. ASan/UBSan remain enabled; LeakSanitizer cannot
run under this ptrace environment and is explicitly disabled. They add no existing object
layout or virtual-slot changes, so SDK ABI 9 and UAPI 0.4.0 remain unchanged.
No M0–M12 milestone is complete.

The subsequently integrated process-frame, recovery-completion, pathname and
descriptor work is described in the ABI 10 section above; this completed ABI 9
result does not qualify that later source.

## ABI 8 boot/file/replay: completed qualification

Kernel SDK/native extension ABI is **8**; native UAPI remains **0.3.0**.
Implemented Linux openat with architecture-specific flags/errno, bounded checked
pathname copies, pre-mutation descriptor admission, append read/write behavior,
and 32-bit large-file policy. Linux fsync/fdatasync share the native node sync
path. Existing tests remain intact; all-ten adapter/open/sync models and process
resource ASan/UBSan pass. OS tool regressions pass **83 tests**.

Virtio now uses an exported monotonic-clock deadline instead of a CPU iteration
count. All ten staged driver probes passed ordinary read/write/flush/ring wrap,
reopen, readonly, injected read error/recovery, absence, healthy delayed I/O and
elapsed-time timeout with queue retirement. The independent healthy-device
failure establishes the old polling defect; it does not identify either
historical ext4 failure's exact first operation.

JBD2 supports an explicit caller-qualified Linux internal-journal tag UUID form,
while default strict tag checks and superblock/checksum identity remain intact.
All ten staged Debug guests replayed a Linux-created dirty journal through real
Virtio and reopened it in a fresh VM; an exported ABI 7 x86_64 pilot also passed.
This preserves the dirty journal/recovery flag and does not enable journalled
mounts, checkpointing or a journal writer.

The exported-SDK x86_64 musl pilot executed two complete file/sync probes with
native parent exec/wait/exit checks and a following shell pipeline; offline
stored bytes were `abcdef` and e2fsck passed. ABI 7 `run-v1` stopped at MIPS64
with a stale incremental `posix.cpp.o`: disassembly returned the old overflow
status although the source returned the new descriptor-limit status. Source
copies had preserved mtimes, and incremental compilation reused the old object.
That run is a failed mixed-build attempt, not exact-source qualification.
A cache-disabled full rebuild passed the same MIPS64 file/sync guest and offline
checks; exact old/fresh objects and logs remain preserved.

ABI 8 adds owned raw boot-register capture on all ten entry paths and the bounded
BIOS E820 collector/parser. Eighteen isolated verification commands passed,
including all ten native profiles, x86 poisoned tables, selected kernel-fault
variants, and hosted E820 ASan/UBSan. Capture does not enable firmware allocation.
Pathname truncate now preserves a release-time I/O failure after successful
truncation and retains the original error when truncation itself fails. Hosted
1/2/4 KiB ext4 validation passed 303 clean sequences, 126 single I/O faults and
three dual-fault priority cases. This does not identify the original historical
LoongArch failure.

The forced ABI 8 `run-v2-abi8` passed seven complete Debug rows, then the
ARM32 standalone harness lost a prefetched completion marker by combining
`select()` with buffered `readline()`. The unchanged retained image passes an
unbuffered binary reader. A two-line child independently reproduces the reader
bug; the repaired transport and preserved QEMU/window tests pass 29 cases.
The failed run and exact ARM32 SDK/raw serial remain retained.

`run-v3-abi8-debug-tail` passed ARM32/RV64/RV32, followed by
`run-v3-abi8-release` passing all ten Release profiles. Each row retains its own
source archive and runner revision. Only the standalone reader and its tests
changed from run-v2; production Kernel/OS sources did not change. All compiled
Kernel/OS images and musl runners are forcibly rebuilt with compiler cache
disabled. The qualifier retains source, build policy, completed SDK/artifact
rows and logs itself. Collective qualification is complete: **20 rows and 290
passing commands**. `build/workstation-files-replay/abi8-equivalent-production-summary.json`
records the exact two runner/test differences. Source archives, logs, primary
artifacts and all retained SDK contents were rehashed. These are equivalent
production-source results with two declared harness revisions, not a claim that
every byte of the harness was identical.

The following changes were independently staged and subsequently integrated as
ABI 9; they are not part of this ABI 8 qualification:
typed captured-firmware discovery; checked VFS metadata/lookup and consuming
path cleanup; actual mapped brk/fixed anonymous replacement with musl heap
pressure tests; and runtime on-device ext4 internal-journal binding. Their
hosted/build/native evidence remains separate until explicit integration.

## ABI 6 bootstrap history

This historical batch used Kernel SDK/native extension ABI **6**, and native UAPI is **0.3.0**. The
ABI 5 clock/ext4 batch below completed its full ten-profile debug/release matrix.
ABI 6 adds per-image native/Linux personality, Linux auxv and bounded adapter
dispatch, plus best-effort child-tid clearing before teardown. Its native musl
guest acceptance passed x86_64, i386, MIPS, AArch64, ARM32, RV64 and RV32
Debug rows in `build/workstation-linux-bootstrap/run-v2`. That attempt then
failed on the LoongArch64 musl probe; the standalone/native gates for that
profile had passed. The full ABI 6 debug/release matrix remains incomplete;
the ABI 5 result does not qualify changed ABI 6 source. Clear-tid does not implement
futex wake or thread join semantics.

`scripts/test_musl_userland.py` stages an explicit hashed bootstrap ELF and a
native parent runner in an isolated ext4 rootfs. Its acceptance requires two actual
musl startup/TLS/errno/monotonic-clock runs, native parent exec/wait/exit checks
and a subsequent native shell pipeline. Initial `run-v1` correctly failed because
the simplefs disk did not publish appended probes into the embedded-archive
namespace. `run-v2` uses ext4 for the musl lane and keeps simplefs/archive native
regression. Failed attempts remain recorded. An available runner is not a pass.

The LoongArch64 failure was an unoptimized libc LL/SC loop in first-clock
initialization: the exact probe also times out in QEMU Linux user emulation.
An optimized musl build passes both that emulator and the actual OS ext4 guest
with repeated exec/wait/exit. The recipe now uses `-O2` in both modes, with `-g`
for Debug. New all-ten artifacts and final qualification must use that corrected
recipe. [The diagnosis](contracts/LOONGARCH_MUSL_ATOMICS.md) preserves the
failure, CPU samples and successful comparison without attributing Linux-user
emulation to native Kernel execution.

The corrected v6 musl artifacts now exist for all ten profiles. Independent
manifest/compiler/ELF/TLS inspection passed; that inspection is not guest execution.
`run-v3` passed MIPS64 and PowerPC Debug, then stopped at a LoongArch native
ext4 pathname-truncate assertion before its musl lane. The old harness deleted
the actual temporary guest disk; the preserved packaging image is explicitly
not a failure-disk capture. Twenty subsequent clean scratch boots passed, so
the original cause remains undetermined. Failure diagnostics now emit errno and
preserve the actual mutated guest disk, command and hashes via `--failure-dir`.
`run-v4` stopped at an i386 native-ext4 open returning EIO; its actual scratch
disk was preserved and passed readonly e2fsck. It is not a complete matrix.
Its completed rows and preserved SDK/source/artifact copies are under
`build/workstation-linux-bootstrap/run-v4`. An in-progress run is not a full pass.

A separate staged driver experiment reproduces fixed-iteration Virtio timeout
on a healthy QEMU disk limited to one I/O per second. A clock-deadline candidate
passes delayed completion and actual elapsed-time timeout/queue-retirement
checks on LoongArch. This finding does not identify the original truncate
failure, and the candidate is not part of the frozen ABI 6 qualification.

Hosted tests now cover actual image loading with mapped-copy mocks, maximum
argv/envp, auxv pointers, exec rollback, result selection and exit child-tid
clearing. ASan/UBSan, the ten-profile process-resource/readiness models and 79 OS
tool tests pass. Bootstrap stdout/stderr now correctly report O_WRONLY through
F_GETFL. Linux scalar I/O checks descriptor access before copying; set_tid_address
records an arbitrary pointer without dereferencing it, matching Linux behavior.

## ABI 5 clock/ext4: completed qualification

Implemented in this batch:

- Calibrated architecture-selected monotonic clocks on all ten retained profiles;
  native relative/absolute sleep with copied requests and deadline completion.
  `/init` exercises a sole sleeper; child/parent tests exchange timestamps to
  check progress inside the sleeping child's interval.
- Descriptor-shared NONBLOCK/APPEND flags, atomic pipe2 flags, pipe readiness,
  retained description pins, and bounded native poll with finite/infinite waits.
  Requests are frozen and pins are released on completion/teardown. Console input
  remains owned by the native input loop. Signals, select/pselect/ppoll, socket
  events, general wait queues and SMP synchronization remain unfinished.
- Native tasks now run through the console/GUI service loop from startup, so a
  live sleeper or persistent background task does not prevent console service.
- ext4 fast and one-block symlinks, malformed-layout rejection, failure-atomic
  creation and retained unlink/replacement. The native shell has `ln -s`; restart
  acceptance checks both relative and absolute links against offline debugfs.
- ELF load segments stream from the retained executable after prefix/header
  validation. Large debug files no longer exceed a whole-file bootstrap buffer;
  unsupported dynamic images are rejected explicitly.
- Independent Linux ABI codecs and saved-frame adapters cover ten profiles,
  endian/word-width handling, time32/time64, bounded MIPS stack arguments and
  MIPS/PowerPC error conventions. Static ELF PHDR/TLS admission and auxv encoding
  plus a bounded syscall adapter now have separate hosted/build tests. They were
  independent of ABI 5 native execution; ABI 6 integration is described above.

The native VM still uses the linker-reserved page arena. Independent firmware
memory parsing and JBD2 replay planning now exist; native firmware handoff,
allocator integration, journal replay, static musl execution, services/network
and isolated graphics remain open work. See Kernel [native waits](../../../ObfuscationKernel/docs/NATIVE_WAITS.md),
[platform clocks](../../../ObfuscationKernel/docs/PLATFORM_CLOCKS.md),
[path resolution](../../../ObfuscationKernel/docs/PATH_RESOLUTION.md) and
[Linux codecs](../../../ObfuscationKernel/docs/abi/linux-user-codecs.md) for exact
contracts and restrictions. These changes do not complete M1, M2 or M3.

The final `run-20260920T202929Z` under `build/workstation-clock-ext4/` passed all
**230 steps**. All ten profiles passed debug/release native simplefs, native
ext4 and ext4 sync/restart acceptance, together with SDK/OS packaging, UAPI and
libc checks. All ten debug profiles also passed standalone Kernel QEMU tests.
This includes native wait/time and ext4 symlink behavior; it does not exercise a
Linux personality, journal crash recovery, physical hardware or SMP.

`abi5-matrix-summary.json` records the exact commands and 230 verified log hashes.
`abi5-artifacts.json` captures 100 input/output artifact hashes;
`abi5-sdk-manifests/` preserves all 20 architecture/mode SDK manifests; and
`abi5-source-before-linux.json` pins the source before ABI 6 changes. Later
rebuilds may replace ordinary build paths, so use these preserved records to
identify the qualified snapshot. Earlier failed attempts remain in the same
evidence root. No ABI 5 execution claim is carried over to ABI 6.

## Independent foundations and musl build evidence

The current source ledger contains **50 seed requirements and 73 tests**. The
new foundations remain `model-only`, while complete Linux ABI/static-musl
requirements remain planned. The source ledger has no execution receipts;
available entrypoints and artifact inspection do not establish a verified gate.

| Foundation | Implemented scope and recorded validation | Remaining integration |
| --- | --- | --- |
| Linux ABI/frame bridge | All-ten hosted codec/frame checks; ASan/UBSan; isolated freestanding frame builds; pinned Linux 6.13.4/musl 1.2.5 definitions and save/restore source anchors | ABI 6 native dispatch qualification; complete syscall/structure/flags/errno coverage |
| Static ELF/auxv | Exact static ET_EXEC prefix, readable PHDR and initialized TLS mapping; target-width/endian auxv; all-ten hosted, sanitizer and isolated target checks | ABI 6 stack/entry qualification, TLS runtime and qualified entropy |
| Linux bootstrap adapter | Bounded I/O/VM, monotonic time, TLS and tid registration delegated through checked copies; hosted x86/i386/MIPS cases; all-ten target compilation | ABI 6 native guest acceptance, complete tid wake/join lifetime and broader semantics |
| Firmware parser | Bounded FDT RAM/reservation parsing; hostile-input and unchanged-output failures; sanitizer, six explicit QEMU DTB audits and isolated ten-target compilation | Actual boot arguments, full-map/capacity policy and allocator ownership |
| JBD2 plan | Checksum-v3, committed ordered actions, revoke filtering and wrap; synthetic fixture checked against e2fsprogs CRC32C; GCC/Clang and sanitizer runs | Replay writes/durability, mount admission and Linux crash interoperability |
| JBD2 executor | Private plan/scratch, validated contiguous journal mapping, journal exclusion, ordered BlockDevice reads/writes and flush; 1/2/4 KiB exact-byte and partial-write/flush/crash models, sanitizer and all-ten target compilation | Filesystem-derived admission, checkpoint/clean-state protocol, actual guest replay and Linux/e2fsck interoperability |

Kernel reproduction entrypoints are `scripts/test_linux_user_abi.py`,
`scripts/test_linux_native_bridge.py`, `scripts/test_linux_exec.py`,
`scripts/test_linux_bootstrap.py`, `scripts/test_native_poll.py`,
`scripts/test_linux_runtime.py`, `scripts/test_fdt_memory.py`, `scripts/test_jbd2.py`
and `scripts/test_jbd2_replay.py`. The bridge/exec/replay runners
use `--cross`; the bootstrap runner is itself compile-only. These tests are
independent of the native qualification matrix. The FDT audit records missing
ARM32 direct-ELF DTB handoff and malformed QEMU 8.2.2 LoongArch memory cells;
neither is accepted as a valid physical memory map.

All ten explicit musl 1.2.5 `build/musl-bootstrap-v4/<arch>/bootstrap.elf` files
now link and have inspected readable PHDR/TLS mappings, non-executable GNU_STACK
and explicit Linux ELF identity. The PowerPC C application uses Clang 18 with
the Linux musl target and retained musl startup/libc/cross-linker; the native
Kernel SDK compiler remains unchanged. This resolves the earlier ordinary-main
link blocker for this probe and corrects the initially unmapped PHDR layouts.
The original nine-profile GCC success and PowerPC GCC failure remain historical
results, not the current bootstrap build count.

Every v4 manifest remains **built-not-executed**. The
[exact artifact audit](contracts/MUSL_BOOTSTRAP_BUILD_AUDIT.json) verifies all ten
manifest/ELF/source/tool identities and records decoded layout and command-log
hashes. It is a read-only inspection of local builds, not native musl execution,
full compiler ABI qualification or completion of M3/L01. See the
[contract ledger guide](contracts/README.md) for the bounded test contracts.

## ABI 4 foundation: historical implemented slices

| Work | Behavior now implemented | Remaining gate |
| --- | --- | --- |
| M0 contract/evidence tooling | Versioned requirement/test/reference schema, all ten native/Linux ABI tuples, dependency/evidence validation, generated capability report, strict SDK generation 4, pinned musl source audit | Full clause/interface/utility/option inventories, qualified Linux ABI layouts and complete dependency/reference pins |
| P02 allocator foundation | Reserved regions override usable ranges; sparse/overlapping RAM accounting; bounded capacity failure; owner/generation handles and stale-release rejection; explicit fallible kernel allocation contract | Firmware RAM/reservations, general object allocation, quotas/reclaim and SMP lifetime rules; the boot diagnostic map remains synthetic |
| P08 pathname foundation | One object/mount resolver for POSIX and native exec; search checks for each component; retained cwd/dirfd after rename/cover; bounded RAM symlinks; follow/no-follow/exclusive creation and retained new objects | ext4 symlink format, larger paths/pools, general mount/dentry lifetimes, supplementary groups, full metadata and concurrent permission semantics |
| P03 native anonymous VM | Real anonymous private mmap, mprotect and partial munmap; zero-fill; inaccessible-page backing retention; eager fork; transactional mapping replacement and failure rollback | General allocators, shared/file mappings, brk, COW, faults/demand paging, SMP shootdown and complete mmap flags/protections |
| L00 source/build spike | Exact musl 1.2.5 archive/content hash, all ten source ports audited, explicit cross-build recipe, static libc/probe artifacts isolated from the native sysroot | Correct Linux personality, auxv/TLS/threads/signals/futexes and actual musl execution; bare-metal compiler success alone is not ABI qualification |

The native VM uses the existing linker-reserved 1024-page arena, with 128 pages
and 16 coalesced areas per process, plus a spare backend address-space slot for
replacement. It does not allocate from the synthetic boot memory map.
Supported protections are NONE, READ and READ|WRITE. The retained MIPS CPUs
still lack hardware execute-inhibit support. The new frame allocator remains a
separate, bounded ownership bookkeeping component.

The source descriptions are in Kernel [pathname resolution](../../../ObfuscationKernel/docs/PATH_RESOLUTION.md),
[native VM](../../../ObfuscationKernel/docs/NATIVE_VM.md) and
[allocation contract](../../../ObfuscationKernel/docs/DEVELOPMENT.md).
The historical public native UAPI was 0.2.0; existing syscall numbers/layouts remained,
with added symlink/readlink calls. Native extension/SDK ABI 4 rejects older SDKs.
The native personality continues to use project syscall numbering on all CPUs;
this is not a Linux ABI declaration.

At that foundation snapshot the contract ledger had 43 seed requirements and
50 planned/available tests. musl static libc and an ordinary probe ELF built on
nine profiles; no musl program executed. The retained PowerPC bare-metal compiler injects
`__eabi` even with Linux/no-EABI command-line options. Its separately documented
[compiler startup blocker](contracts/PPC_MUSL_BLOCKER.md) requires a Linux-targeted
user compiler; it does not remove PowerPC from the native OS matrix. Two isolated
x86_64 musl builds matched all 234 installed/probe file hashes.

## ABI 4 foundation: historical validation and evidence

Qualification on 2026-09-20 independently built the Kernel, exported its exact
architecture/mode SDK, validated the OS consumer, built sysroot/apps/rootfs and
executed guest tests. All 20 architecture/mode combinations passed:

| Architecture | Debug native: simplefs / ext4 | Release native: simplefs / ext4 | ext4 sync/restart/e2fsck: debug / release |
| --- | --- | --- | --- |
| i386 | pass / pass | pass / pass | pass / pass |
| x86_64 | pass / pass | pass / pass | pass / pass |
| aarch64 | pass / pass | pass / pass | pass / pass |
| arm32 | pass / pass | pass / pass | pass / pass |
| rv64 | pass / pass | pass / pass | pass / pass |
| rv32 | pass / pass | pass / pass | pass / pass |
| loongarch64 | pass / pass | pass / pass | pass / pass |
| mips | pass / pass | pass / pass | pass / pass |
| mips64 | pass / pass | pass / pass | pass / pass |
| ppc | pass / pass | pass / pass | pass / pass |

Standalone debug Kernel QEMU gates passed on all ten profiles. Each mode also
passed UAPI validation, native libc checks and rootfs packaging. The host checks
passed 73 OS Python tool tests, 25 Kernel QEMU harness tests, all-ten-profile
process-resource models, VFS/archive/kernel-service tests, ext4 mutation/reopen
tests, and allocator/native-VM transaction checks under ASan/UBSan. Leak detection
was disabled for the sandboxed sanitizer runs; VM sanitization excludes unrelated
virtual-device vptr instrumentation.

Logs and command/hash records are in `build/workstation-foundation/results.json`;
raw logs and scratch ext4 restart images live alongside it. The final qualification
summary is `matrix-summary.json`, with SDK/image/rootfs hashes in
`native-artifacts.json`. `final-source-hashes.json` identifies the build-source
snapshot; later documentation edits do not alter that source evidence. The early
i386/MIPS/AArch64/ARM32/RV64 debug builds passed a separate recorded refresh
against the final `statat` flag validation and VFS interface comment, checking
unchanged linked app/boot-archive/rootfs hashes. The first refresh stopped on an
overly strict intermediate-libc-archive hash check after all i386 execution gates
passed: this xmake configuration can rebuild dependencies despite `--shallow`.
Its recorded follow-up verifies that the actual reused executable/disk inputs
were unchanged. The remaining refresh permits re-archiving intermediate libraries
while retaining those executable/disk checks. These generated artifacts are local
and unversioned.

`ledger.evidence.json` overlays the source ledger with 66 hash-checked execution
records, including the incomplete musl cross-build result. The final SDK/image/
rootfs manifest covers 100 artifacts; all 20 SDKs match current exported headers
and the required compiler identities. This does not promote partial requirements
or waive missing gates:

```sh
python3 tools/plan_ledger.py validate \
  --manifest=build/workstation-foundation/ledger.evidence.json \
  --evidence-root=build/workstation-foundation
```

The hosted suites separately exercise namespace/state behavior, allocator
bookkeeping and VM transactions with injected pool/table/retirement failures.
ASan/UBSan runs do not turn these into hardware tests. QEMU native acceptance
executes user instructions and syscalls; it still does not qualify physical
machines or SMP.

The new required guest markers are:

```text
OK_VM_NATIVE scope=hardware map=pass zero=pass protect=pass unmap=pass fork=pass pressure=pass
OK_PATH scope=hardware relative_exec=pass symlink=pass
```

The ext4 lane requires the same relative-exec and memory tests but reports
`symlink=unsupported-filesystem`. That limitation is permitted only in the
explicit ext4-subset lane; a RAM-root run missing symlink coverage fails.
Release images run `posix-check` through the serial shell. Persistence tests
write/rename/link/sync, restart the guest and run host e2fsck/debugfs against
scratch images. They test the current non-journalled ext4 subset, not JBD2 crash
recovery.

## Reproduction

From the Kernel repository, select the target/mode and explicit toolchain, then
build `kernel-sdk`; in debug also run `xmake qemu-test`. From the OS repository,
select the same target/mode/toolchain and build `distro_image`, `uapi-test`,
`libc-test`, `rootfs-simplefs` and `rootfs-ext4`. The OS build consumes SDK
artifacts only. Debug guest acceptance uses:

```sh
xmake qemu-distro --fs=simplefs --require-native --timeout=100
xmake qemu-distro --fs=ext4 --require-native --timeout=100
```

Release shell acceptance uses `scripts/test_interactive_userland.py` with
explicit `--arch`, `--qemu`, `--kernel`, `--rootfs`, `--log` and `--posix-check`.
The separate `scripts/test_persistent_ext4.py` uses explicit images and output
paths and never operates on an installed disk.

Contract validation/reporting is available through `xmake plan-check` and
`xmake plan-report`. `tools/plan_ledger.py gate-m0` deliberately fails until a
complete normative inventory replaces this seed schema. An accepted schema or
an artifact hash is not a completed requirement.

## Remaining dependency work

Finish the M0 clause/option inventories and remaining per-architecture Linux ABI
layouts; connect real boot RAM/reservations to allocator ownership; qualify the
ABI 6 Linux bootstrap changes and thread/TLS/signal lifetimes. The existing
FDT parser does not complete native memory handoff. Storage recovery must build
on the independent JBD2 parser/plan with safe replay writes, durability and real
crash fixtures before any journalled writer is enabled. Real network services and the
isolated Wayland desktop remain later work, with existing rescue paths retained.

The P04 clock/sleep/poll implementation above replaces the foundation's nominal
trap-count clock. Full event waits, signal interruption and Linux time64 execution
remain separate acceptance gates. No physical-hardware or SMP result is inferred
from the QEMU or hosted test results.
