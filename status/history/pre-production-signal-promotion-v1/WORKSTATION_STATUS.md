# Workstation implementation status: incomplete

M0-M12 remains incomplete. The user deferred M11 physical hardware and M12
manual desktop acceptance. Continue implementation and automated qualification
without asking again. Preserve dirty top-level repositories, frozen sources and
failed attempts. Always run Python with `PYTHONDONTWRITEBYTECODE=1 python3 -B`,
including subprocesses. No commits or publication. Paths below are relative to
`build/prototypes`.

## Accepted source and predecessor

`native-signal-actions-sdk29-v1/working`: **Kernel887 / OS509, SDK31**.
The next promotion must use
`native-child-exit-pressure-integration-v1/promotion-v1.json`, SHA256
`d4fb41e3d6c0eca5c9ca550112c35d287ad70d3fee5169399d042b68f8916503`.
Its complete `after` inventories define the accepted sources. Eleven new OS
paths were promoted; Kernel source is unchanged. Complete prior Kernel887 /
OS498 backups and post-checks are in the pressure integration stage.
Never rerun `promote_pressure_v1.py` or an older promoter.

- Final pressure binding: `ea6cae7fe39d5c2076c4156acf5b3f608a82f384ddda3853768cff56018a4148`.
- Final pressure contract: `c51f42db036f379c3643f15ad9336d69834f5b9f6b54069d6844355c83af1040`.
- Kernel: `native-child-exit-integration-v1/candidate-kernel-final-v1/ObfuscationKernel`,
  inventory `61bc8a2698f6d1d859d14f4267216a6bc76cc9adb6d8231a0ff0f58a1b419c8b`.
- OS: `native-child-exit-pressure-integration-v1/candidate-final-v1/ObfuscationOS`,
  inventory `2ecb177881abe6e20500538f45eced38e35cd61cc9861547f03fe7fb3183e481`.

## Newly accepted pressure implementation and evidence

OS owns the three-wave musl pressure guest, strict guest journal, typed kernel
join, execution observer and SDK-only qualifier. Default, explicit IGN and
SA_NOCLDWAIT waves fork to actual failure while every successful child has an
actual blocked one-byte gate read. Read rearms retain copied identity and
advance tickets. Full child siginfo matches the first queued exit; explicit
reaping accounts for every automatic child. Page and privileged-stack counts
return to the live shell baseline. Recovery fork/wait succeeds after each wave.

- `pressure-matrix-v1/result.json` in the integration stage: ten fresh native
  qualifiers / twenty commands, SHA256
  `d94c15204c2fe255c4ed79e82cf41fad7d10fbe217d134f5e8084ffa7d841a79`.
  780 pressure children, 60 recovery children and 20 controllers = 860 published
  completions; 180 failed forks with exact unpublished ENOMEM127 rollback;
  520 automatic physical reaps. All ten profiles had thirteen children per
  wave; admission still uses dynamic counts and does not infer which pool ran out.
- `tools-v3/result.json`: 66 suites / 598 distinct hosted methods, SHA256
  `63d19422bbb96f01eb503ee4be9576675d325b2d526cb98e04c350072a70d1a7`.
  Fifteen pressure methods are included, not additional to this total.
- Independent review: `native-child-exit-pressure-review-v1/HANDOFF-v1.json`,
  SHA256 `4fd949dad99cf43017a45fd2f5e774a8c3377847fc50fe42b1ba9222924aa690`.
  488 complete-transcript controls (22 admissions / 466 rejections), including
  244 intended failing gates, plus 60 execution-observation controls. Reviewer
  authored the guest/parser; independent attribution covers root integration.
  Final OS retains the portable audit script; root replay passes all 548 controls.
- Frozen V3 (507 files) ran the fresh matrix. Final OS509 adds only the retained
  audit utility and qualification document. Binding replays all ten receipts
  from exact final collectors and verifies source/SDK/compiler/disk/output hashes.

Earlier x86 V2 actually ran two successful commands but its collector rejected
legal shared-gate read rearms. Original failed receipt SHA256
`d9546ecd0a8d9bcda634b35cbec5215e16d90a261371e2a80c0b2544214e8c24` remains
executed=true, native_execution_accepted=false. V3 replay passes; this is not
another execution and is not included in the twenty fresh commands. Preserve
failed-hosted-join-v1 and reviewer test-premise attempts too. Natural ENOMEM can
emit an unpublished rollback exit127 within the failed call; its absence is
valid when failure precedes PCB creation. EAGAIN, published, duplicated or
out-of-window rollback exits remain rejected.

## Inherited accepted lifecycle evidence

The prior lifecycle promotion is
`native-child-exit-integration-v1/promotion-v1.json`, SHA256
`f513ae000e335cf08ee59fd9eab43bdee4490637fd21b56c86e5d1c46b214aa8`.
It implements private Debug automatic SIGCHLD, IGN/NOCLDWAIT autoreaping,
creator/replacement parent-thread lineage, saved leader cause and failure
barriers. Twenty SDK exports / ten private standalone boots, an extra ordinary
signals-off Debug export/boot, five distro links / ten ordinary distro boots
remain valid through unchanged production/compiler inputs. Binding:
`native-child-exit-integration-v1/compiler-inputs-binding-v1.json`, SHA256
`ca8da69303588d39964339d18207d80e4cc16c68e1c15eb740ea2f000db61499`.
Its 59 original qualifiers / 118 native commands and hosted Kernel lifecycle
audits remain separately bound in the archived prior status; pressure adds no
new Kernel build. Ten Kernel profiles and four ordinary distro profiles remain.

## Current successor work, not promoted

`native-signal-production-runtime-v1`: author implementing ordinary Debug and
Release `OK_NATIVE_SIGNAL_RUNTIME`, separate private diagnostics, complete
MIPS/PPC capture/assembly/compaction guards and checked administrative Linux
SIGKILL completion. Candidate V1 has 894 files, inventory
`ff4e830d4ee564bb7c30cc6b2d29ff82432c7724bfc955a12b73f52019f32a91`.
Independent review in `native-signal-production-review-v1` runs actual Kernel
administrative-kill hosted checks and paired SDK metadata controls. Exporter
V1 misses forwarded -Wp macro overrides; an exporter-only successor is pending.
Keep V1 evidence and bind compiler-equivalent final sources explicitly.

Root's `native-signal-production-build-v1/matrix-v1` is running thirty exports:
ordinary Debug/Release and private diagnostic Debug on all ten profiles, with
twenty Debug standalone boots. Session54145 owns this matrix; do not duplicate.
`native-signal-production-consumer-v1/working/ObfuscationOS` is rebased to
accepted OS509 and adds mandatory semantic SDK capability/definition checks.
Consumer boundary tests pass; complete successor source is not yet frozen.
Ordinary user-observed policy/pressure collector and qualifier authoring is
delegated separately to child_signal_codec_review. No ordinary native signal
acceptance has yet occurred. Source audit and SDK decision are in
`production-signal-scope-v1`; ABI31 may remain only after unchanged all-ten public
layouts. Capability is `native_signal_profile: bounded-bootcpu-v1`, consistent
with actual runtime and MIPS64 assembly definitions; reject old/disabled or
contradictory artifacts. Ordinary Release has no private/test-point definitions.

## Remaining target limits

Accepted production caught signals are still off until the new successor passes.
CPU-time signal fields remain zero. General OS init/subreaper adoption, stopped /
continued wait events, complete fault handling and SMP remain open. Natural
pressure does not substitute for injected native terminal-failure evidence.
Default journalled root, broad POSIX/filesystem behavior, networking, persistent
services, isolated desktop and remaining M0-M12 work are incomplete.

Existing journalled directory campaigns belong to SDK30. Three historical MIPS
regular-recovery FLUSH timeouts remain unresolved; a host fdatasync delay is not
an established production cause. Completion-boundary cuts do not qualify torn
writes, reordering, volatile caches or physical power loss. The selected external
Linux6.13.4 reference has 21 cases; newer WSL2 differs in leader cause, and binary /
source authenticity remains unestablished. Physical and manual acceptance are
deferred, not passed. Earlier full status is archived in
`build/status-history/pre-child-exit-pressure-promotion-v1/`.
