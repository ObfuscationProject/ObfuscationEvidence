# Workstation implementation status: incomplete

M0-M12 remains incomplete. The user deferred M11 physical hardware and M12 manual
desktop acceptance; continue implementation and automated qualification without
asking again. Preserve dirty top-level repositories, frozen sources and failed
attempts. Always run Python with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, including
subprocesses. Do not rerun any promoter. Paths below are relative to
`build/prototypes` unless otherwise stated.

## Accepted source and exact predecessor

`native-signal-actions-sdk29-v1/working`: **Kernel887 / OS498, SDK31**.
The next promotion must use `native-child-exit-integration-v1/promotion-v1.json`,
SHA256 `f513ae000e335cf08ee59fd9eab43bdee4490637fd21b56c86e5d1c46b214aa8`.
Its `after` inventories define the complete accepted trees. All65 added/changed
paths were promoted with complete Kernel875/OS477 backups in
`native-child-exit-integration-v1/before-promotion-v1` and post-checks in
`post-promotion-v1.json`. Do not rerun `promote_lifecycle_v1.py` or an older promoter.

- Final binding: `8258b5bad86197188d95327da4c290f13345b12cd0926324e382efe0adf15bae`.
- Contract: `5d604299579f1973bc8bc92e3bf74b51ee0830a234b645bbcfbc2fc5a46203ad`.
- Final Kernel: `native-child-exit-integration-v1/candidate-kernel-final-v1/ObfuscationKernel`,
  inventory `61bc8a2698f6d1d859d14f4267216a6bc76cc9adb6d8231a0ff0f58a1b419c8b`.
- Final OS: `native-child-exit-integration-v1/candidate-os-final-v2/ObfuscationOS`,
  inventory `2f6d6f04ddf3704423c131eb5b2eb21ae11ee8c5db21c54e2c2590b97dd4f016`.

## Implemented bounded behavior

Private Debug child completion now supplies automatic SIGCHLD, explicit-ignore
and SA_NOCLDWAIT autoreaping, creator/replacement parent-thread lineage, saved
leader notification cause distinct from final wait cause, checked deferred
reclaim, rollback exclusion and failure barriers. Native parents retain native
waiting for Linux children. CPU-time fields stay zero; production caught-signal
flags stay disabled. Administrative infrastructure/debug/GUI kills and general
orphan adoption remain outside this experiment. All76 existing public layout
measurements match across ten toolchains; exact exported SDK libraries and
headers are still required. OS never compiles Kernel source.

## Completed qualification

- Twenty fresh Debug/Release exports and ten private standalone boots:
  `native-child-exit-runtime-build-v1/matrix-v1/result.json`, SHA256
  `fe323369a5f1ca03664bf4b763fc15fcc11fddbf35c2273f8d602041f8d87d93`.
  Compiled Kernel885V2 inventory is `51f291480cb89d19e359de55ca377bf2902cad239f4dde16ab92e98b89a17f8e`.
  Final Kernel887 adds only preserved hosted tests and qualification docs.
- One ordinary signals-off Debug SDK build/boot, five ordinary OS links and
  ten OS boots across the four distribution profiles. Final compiler-input
  binding is `ca8da69303588d39964339d18207d80e4cc16c68e1c15eb740ea2f000db61499`.
- Policy: all ten profiles,20 commands/360 cases;800 process completions,
  160 physical deferred reaps,300 notifications,60 coalesced. Original V4
  executions pass strict V5 replay, binding
  `04ee0f75b3af1852b46c3b72bf8df8d6391b8e9c8491e59c7a03e30b0be8e5a4`.
- Lineage: all ten profiles,20 commands/140 cases. Actual ARM/EXIT/terminal
  ordering covers sigtimedwait real_blocked and ppoll temporary masks. The
  lineage collector admits valid immediate-ready pipeline waits and says
  `all_native_waits_traced=false`. Independent review handoff SHA256
  `18af03cde89c3c2e509be60757783c7549fc83b9e7fb8c4b91b35ec798f7ec87`.
- Legacy signal frame/wait all ten plus process/directed x86:22 qualifiers,
  44 commands. Independent native review SHA256
  `3c401c36db1b78603626c67e4ac7ec6c83b592a4f9648ff49aa25bde0522c779`.
- Remaining11 child/pipe/futex/poll consumers migrated with typed lifecycle
  validation and original interrupted-WAIT/SIGNAL adjacency. All11 x86
  workloads pass; child wait, pipe vectors and temporary poll masks also pass
  on i386 and big-endian MIPS:17 qualifiers/34 commands. Frozen source review
  has559 full-wrapper evaluations (58 admissions/501 rejections) over553 unique
  transcripts, plus440 earlier adjacency controls. Final HANDOFF-v2 SHA256
  `a452ce8ee81fa13f4ac3e9e9e1853d4779259536deebf69b9f9660e1e936db45`.
- Final OS498:63 hosted tool suites/583 methods;1,250 independent raw-image
  model checks. Final source replay matches all59 original qualifiers/118
  commands, binding `de9d6111223dd598af1fce2b50ad321f17497d8ec94bb475720e7c49bc02649f`.
  Replays create no additional native execution.
- Hosted Kernel evidence remains separate:14,090 lifecycle checks,364 actual
  runtime/mock-backend checks,3,511 inherited checks,57 independent checks and
  164 additional actual-runtime ASan/UBSan audit checks. Audit tests are retained
  in Kernel887. These do not close native pressure/injected-failure gates.

All root matrix/test/binding sessions at this checkpoint finished and were
polled (including37878,48431,69584,8969,19755,42013). Do not launch duplicates.

## Preserved failures and limits

Retain policy V1's incorrect41-lease rejection (live-leader exec reuses its
canonical stack; correct minimum40), lineage V1's immediate-ready pipeline
rejection, pre-execution legacy inventory-schema failures, original collector
counterexamples and the remaining-consumer fixture/adjacency findings. Remaining
review V2 corrects five V1 mutation premises to use exact inherited owner tickets;
both original receipts and the supplement remain sealed. Final OS composition
V1 hit an exclusive-create receipt name collision after source generation;
its source and failure receipt remain, and V2 supplies the accepted docs source.

Default journalled root, broad POSIX/filesystem behavior, networking, persistent
services, isolated desktop, SMP and production signals remain open. M11 physical
and M12 manual acceptance are deferred, not passed. Existing journalled directory
campaigns belong to SDK30. Three historical MIPS regular-recovery FLUSH timeouts
remain unresolved; a host fdatasync delay is not an established production cause.
Completion-boundary cuts are not torn-write/reordering/volatile-cache/physical
power-loss qualification. Selected external Linux6.13.4 has21 reference cases;
newer WSL2 differs on leader cause. Binary/source authenticity remains unestablished.

## Immediate next implementation

The OS-owned pressure guest is frozen separately at
`native-child-exit-pressure-guest-v1/candidate-v1/ObfuscationOS`,501 files,
inventory `f23066f4db2835bd8831e007d5888f867e4f6ca3e6c8c3183e4fc4705e22eb20`.
It adds four files to combined OS497; preserve that frozen source and overlay
only its four added files onto exact newly accepted OS498 in a successor stage.
Author HANDOFF-v1 SHA256
`42d40191e122d7d53409dacf9d77f26e08f39e1f1b530674d59a64a55e64c7fc`.
All ten musl builds passed; six hosted methods include170 positive and17,220
negative guest-journal controls. No pressure QEMU execution occurred.

The three waves use blocked DFL, SIG_IGN and blocked DFL|SA_NOCLDWAIT, three
failed forks each, WNOHANG0 live checks, gated release, WAIT/ECHILD, full128-byte
coalesced siginfo and ordinary recovery after each wave. Counts are dynamic.
Per-parent child capacity16 may be the first exhausted resource; do not claim
global PCB, VM or stack exhaustion merely from natural fork failure.

Root's `NEXT-PRESSURE-v2.md`, `PRESSURE-DECISION-v1.md` and the guest stage's
`ROOT-INTEGRATION-DECISION-v1.json` record the collector decision: an ENOMEM fork
after internal PCB creation may emit at most one exact unpublished
CLD_EXITED127 rollback EXIT inside that failed call window. Bind it separately
from successful children and reject any publication/signal/autoreap. Literal
absence of every internal completion diagnostic was an overstrict V1 assumption.

Next: rebind the guest to the accepted promotion, add root-owned typed lifetime,
signal, pipe-wait and explicit physical-reap joins and qualifier, review hostile
controls independently, then run representative and all-ten native pressure
campaigns through the unchanged exact SDK artifacts. Preserve failed attempts.
Do not enable production signals or close M0-M12 from this next bounded slice.

Earlier full status documents are archived under
`build/status-history/pre-child-exit-promotion-v1/`.
