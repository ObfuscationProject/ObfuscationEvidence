# Accepted checkpoint and continuation

M0-M12 remains incomplete. The user deferred M11 physical hardware and M12 manual
desktop acceptance; continue implementation and automated qualification. Preserve
dirty top-level repositories, frozen candidates and failed evidence. Always use
`PYTHONDONTWRITEBYTECODE=1 python3 -B`, including subprocesses. Do not rerun any
promoter. Paths below are relative to `build/prototypes`.

## Accepted source

`native-signal-actions-sdk29-v1/working`: Kernel875 / OS477, SDK31.
Required next predecessor:
`native-child-siginfo-codec-integration-v1/promotion-v1.json`, SHA256
`e9a57bbf29c0c79e2c0601a34cf949c4eb69803d6b30b66b5893da11783a1ac7`.
Its `after` inventories define the accepted source. All134 changed/new paths were
promoted; full Kernel869 / OS475 backups are at that stage's `before-promotion-v1`.
`post-promotion-v1.json` rechecks both live trees and both complete backups.
Do not rerun `promote_v1.py`.

- Final binding: `c8f62f4aa9990b511ed84f267b3361c561eb5908ff2b8b3383ef1ddb2c127bcc`.
- Kernel docs successor inventory:
  `f73965ec398337d28621da56145aeb8b67bc4330c9f8152b644a0d0d9dcaaa89`.
- OS docs successor inventory:
  `a985e30c9824dea0743910f5f040b05230e2861b7ec7ac0215e14d4f33e827f5`.
- Source directories are `native-child-siginfo-codec-integration-v1/` plus
  `candidate-kernel-final-v1/ObfuscationKernel` and
  `candidate-os-final-v1/ObfuscationOS` respectively.

## Accepted SDK31 prerequisite and evidence

Typed trusted ChildExitStatus, dedicated child queue admission, child_status in
all nine signal-frame policies and common128-byte target-endian siginfo encoding
are implemented. Generic sender paths reject forged child-only fields. MIPS
code/errno ordering is preserved. Automatic SIGCHLD/autoreap is not in this
accepted slice; CPU times stay zero. Production caught signals remain disabled.

- Author Kernel875V2 compiled inventory:
  `00524dc1221deaba1e213599793cecbd9770872823790454ed68b1c5a4d88bad`.
  Author HANDOFF `828a0e3c5cb39ede6d6591e17f1fa212bc145c1352afaea1a9d50c2944abd2c3`:
  13,820 new sanitizer checks,12 inherited binaries, ten target layouts/90 vectors.
  V1 constexpr fixture compilation failure is retained; V2 changes only its
  compile fixture. Two later documentation corrections do not change code.
- Independent codec checks36,575; actual frame-policy checks8,728. Frame handoff:
  `aa10fb14ff333606ab982251fe8d69884235909239aee3e66eac6c2af12620da`.
- `native-child-siginfo-codec-build-v1/matrix-v1/result.json`:
  `048c09759a6bddc503d6ef480d014f55607d615049bef253c05fc7cbd55b156e`.
  Twenty fresh Debug/Release SDK rows, ten private standalone boots.
- `native-child-siginfo-codec-distro-v1/matrix-v1/result.json`:
  `e7b95c75dbb53b116beca67d8b646dfb77b567a5a837d59c9ff15b71930cb1ad`.
  Five ordinary links/ten boots, plus one ordinary signals-off SDK build/boot.
  OS476V2 distro compiler inputs are identical in final OS477; collector/docs
  changes are explicitly bound. Build binding:
  `8737d654f8c68bf34b22201c0f077383303fd85378e43175fcad91411f8e6536`.
- All20 image section/PT_LOAD measurements are in `image-layout-v1.json`;
  queue growth48,384 bytes i386 /96,768 others. Actual BSS padding differs.
  Measurements alone do not prove general physical memory capacity.
- Native binding `cd0f369e9f6e151b6e6bdcb013743be459371cc0c1950a1b683399ba099c3f9b`:
  ten-profile frame+wait plus x86 process/directed,22 qualifiers/44 commands.
  Uses18 `other-guests-v1` rows, only passed wait/process from `x86-guests-v2`,
  and fresh delivery/directed from `x86-guests-v3`. Final strict V4 collectors
  replay every execution and match its complete original result.
- OS migration:55 unittest suites/542 methods,1,250 raw-image model checks;
  all20 intact SDK30 exports rejected and20 exact SDK31 exports admitted.
  V3 repaired two old collectors; V4 rejects command events touching inherited
  wait owners. V4 inventory `3bee5d45e025b5abad3173c1df3362fe6acd3b604edc947f9f5881ccc7dd493c`.
  Fourteen affected hosted suites pass. Independent final collector review:
  `native-child-signal-collector-review-v2/HANDOFF-v2.json`, SHA256
  `7f16c72a35e289e0982f03e1a8804eced06ddeef06783660550e438cd37bf5e4`;
  3,720 controls,20 sealed attacks rejected, two old failed serials replayed.

Retain `x86-guests-v1` pre-build inventory-schema failures, two actual V2 collector
failures (executed=false was a pre-acceptance field), V3 false-admission review,
and all reviewer/runner attempts. The strict V4 replay closes acceptance without
relabeling those originals or claiming new executions by reviewers.

## Current follow-on work

`native-child-exit-runtime-v1` is the active unpromoted lifecycle candidate, owned
by pipe_signal_guest. It starts from exact Kernel875 docs successor, importing
the separately sealed scheduler detach/checked-reap prerequisite. It adds private
lineage, saved leader cause, completion prepare/commit and safe-boundary reaping.
Do not use an unfrozen source or a running test as accepted evidence. The additive
scheduler methods preserve76 existing public layout values on all ten target
toolchains; fresh same-generation SDK/library identity remains required.

`native-child-exit-guest-v1/DESIGN-v1.md` describes the next SDK-only OS workload
and strict lifecycle collector. Native WNOWAIT/procfs are unavailable; use actual
waiting, pipes and handler/synchronous-signal observations for ordering.

Selected Linux6.13.4 reference is now two x86 boots/21 cases: original three
leader-first cases, plus18 disposition/coalescing/action/fork/exec cases.
`native-child-exit-linux-reference-v1/POLICY-HANDOFF-v1.json`:
`15183833d0faf7df6f2ef45b20f47746b032ca9e6b3b394bf7ad81927fd3d6f5`.
Notification retains leader17 while wait sees group23/23/SIGTERM15. The newer
WSL2 host differs; selected binary/source provenance remains unestablished.
Reference execution is not Obfuscation execution.

## Inherited storage and remaining limits

The accepted directory chmod/recovery implementation is unchanged by SDK31.
Its original SDK30 native/Linux campaigns remain bound to that predecessor,
not relabeled as new SDK31 storage runs. See the complete preceding checkpoint
in `../status-history/pre-sdk31-codec-promotion-v1/CONTINUATION.md` and current
`../WORKSTATION_STATUS.md` for milestone gaps.

Historical three MIPS regular-recovery FLUSH timeouts remain unresolved; no
production transport fix or established cause. A separate12-second host
fdatasync experiment is not proof of that historical cause. Completion cuts do
not establish torn-write/reordering/volatile-cache/physical-power-loss/SMP
durability. Default root stays nonjournalled. Full filesystem/POSIX breadth,
networking, services, isolated desktop and M0-M12 remain open.
