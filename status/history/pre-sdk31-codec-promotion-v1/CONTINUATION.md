# Accepted checkpoint and continuation

M0-M12 remains incomplete. The user deferred M11 physical hardware and M12 human
desktop acceptance; continue implementation and automated qualification. Preserve
the dirty top-level repositories, frozen candidates and failed evidence. Use
`PYTHONDONTWRITEBYTECODE=1 python3 -B`, including subprocesses. Do not rerun a
promoter. Paths below are relative to `build/prototypes`.

## Accepted source

`native-signal-actions-sdk29-v1/working`: Kernel869 / OS475, SDK30.
Required next predecessor:
`native-journalled-directory-mode-integration-v1/promotion-v1.json`, SHA256
`0dea0d2569f373283b7baa3fdf480b1407b07d4bbcdaf121f6340eb022f625de`.
Its `after` inventories define the accepted source. All 32 changed/new paths were
promoted; the complete Kernel867 / OS456 predecessor is at that stage's
`before-promotion-v1`. `post-promotion-v1.json` passed, and root independently
rechecked both live inventories after resuming.

- Final binding SHA256: `03306f0aa0359051c9dc38cf1adccd5319314d6ce170637e3bca2650417da692`.
- Kernel candidate: `native-journalled-directory-mode-v1/candidate-v4/ObfuscationKernel`.
  Inventory `506ff180547a43598721e947c3f3bfb4bf69cbdad98412f43c9f294721c2dd4b`.
- OS candidate: `native-journalled-directory-mode-integration-v1/candidate-final-v1/ObfuscationOS`.
  Inventory `020d8c9568f1be16ae316f2b6d3b19d70e3b54084d1c29a458afd13fec414f50`.
- Original promoter stopped before backup/mutation on an empty `__pycache__`.
  Root recorded it and removed exactly the empty directory. Successor promoter
  passed identical gates. Both drivers and `promotion-attempt-v1.json` remain.
  Neither promoter should run again.

## Accepted directory behavior and evidence

Credential-aware journalled chmod supports allocated ordinary directories on an
explicit maintained-noatime side mount. Previously opened readable directory
handles remain enumerable after chmod0000; fresh open, search and fchdir check
current permissions. Root/reserved inodes and symlinks remain unsupported.
Maintenance-only updates remain regular-file-only. Default root remains
nonjournalled; production caught signals remain disabled.

- `native-journalled-directory-mode-build-v2/matrix-v1`: 20 fresh SDK builds,
  10 private Debug standalone boots; result
  `c375ca1d50fd287614da04468e4779438f2d6cd89e39c010d3819f75f438b6ea`.
- `native-journalled-directory-mode-distro-v2`: ordinary signals-off x86 Debug
  SDK boot, five distro links and ten boots; result
  `6f352714a67697373e195dc9c13102f48e9d7e52252ab5372585f08e48dffce2`.
- `native-journalled-directory-mode-native-v1/matrix-v2`: 30 native + 30 Linux
  readonly runs, 373,338 public checks, 120 mutations, 1,320 writes, 1,140 FLUSH;
  result `72c49c53ca20126681d38667bf9018efc518ed69433aa935a908a688a3c5d587`.
  Clock-boundary checks make this count differ from older diagnostic runs.
  Retained regular-file regression passed126 checks /55 writes /47 FLUSH.
- `native-journalled-directory-recovery-campaign-v1`: all60 completion cuts,
  120 native recovery/clean boots and60 independent Linux recoveries passed.
  x86_64/i386/MIPS each cover boundaries1..20; 507,960 public checks total.
  Representative x86cut11 is included exactly once. Result
  `48d4793be20bed1bcabbec9a5f34e948287d03b60537ab7e02df74cf7f46422d`.
- Integration `campaigns-binding-v1.json`:
  `e844bad01427e302da9b390a18b91d4fa293575a1aa294fbbfa0d4d21976320b`.
  `recovery-binding-v1.json` binds16,858 files:
  `9341f9f455a8c11a0850ec26bcf584758e6518b2a5c0d7b4fa1fa6da8554512f`.
- Independent Kernel source/inherited review, collector source/2,675 controls
  and normal native/Linux complete-disk replay passed. Recovery execution replay
  was root-owned. Do not attribute it to the independent reviewer.
- Failed candidate1 archive naming, partial recovery image preparation and
  Kernel candidates1..3 cache-generation regression remain diagnostic evidence.
  The final v4 avoids a redundant read before owner.prepare(). Do not rerun the
  author seal expecting the old accepted867/456 live tree after promotion.

## Active M3 work

`native-child-exit-signals-design-v1/HANDOFF-v1.json` sealed design/reference
stage, SHA256 `3ebda6d94bd4abbc59b556a57bd07542f6470b4f187ff3cd5c462c5aa2064ede`.
It binds18 host policy cases,3 host thread observations, ten musl layouts and an
independent lifetime review; it contains no Obfuscation implementation/execution.
The original867/456 audit base advance to869/475 is explicitly bound.

Root resolved the selected-binary leader-first reference gate:
`native-child-exit-linux-reference-v1/run-v1/result.json`, SHA256
`9dfca76b04d787ab4d0bf3f971820cc932fa4eeb29ab6181075f61d3f9112d52`.
One Linux6.13.4 x86_64 QEMU boot /three cases observes notification status17
while wait sees final status23/23/SIGTERM15. The WSL2 Linux6.18 observations differ;
retain version distinctions. Binary/source provenance is not established.
`verify_v1.py --verify` replays outputs and exact payloads; HANDOFF-v1 SHA256
`71240d31abb72a7d2f01be11fa58f06e9694b1ff6782bc06ceb24f1cb6de9fc0`.

Agent pipe_signal_guest is implementing the bounded trusted child payload and
shared128-byte encoder slice in a new private candidate based on869/475.
Public layout changes require SDK31 and exact OS consumer migration, all-ten
layout/BSS/headroom checks, inherited tests, standalone and consumer builds.
Agent child_signal_codec_review is independently reviewing codecs/reference and
preparing adverse vectors. No new implementation has been promoted.

Follow-on completion transaction must suppress never-published fork rollback,
preserve parent-creator/replacement TID, separate leader notification from wait
cause, preserve first standard pending payload and avoid inline PCB/TCB erasure.
Autoreap detaches completed child to parent0 without moving records; safe-boundary
reaping must expose unexpected failures. CPU-time accounting remains unqualified.
Keep production flags off until the broader integration requirements pass.

## Continuing limits and historical checkpoints

Three historical MIPS regular-recovery FLUSH timeouts remain unresolved. A separate
host timing experiment reproduced a timeout with12-second fdatasync delay, but
there is no production driver fix or established historical cause. The successful
directory campaign does not close that issue. A clean-image FLUSH can complete
without a host sync syscall. Whole-completion cuts establish neither torn-write,
reordering, volatile-cache nor physical-power-loss durability; no SMP claim.

Earlier detailed status and evidence pins remain in
`../status-history/pre-directory-promotion-v1/`,
`../status-history/pre-directory-requalification-v1/`, and earlier archives.
Do not use historical accepted-source claims as the current predecessor.
