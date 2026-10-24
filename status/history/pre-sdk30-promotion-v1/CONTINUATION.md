# Active checkpoint: journalled mode native recovery

Use `PYTHONDONTWRITEBYTECODE=1 python3 -B`, including subprocesses. Preserve
frozen/failed evidence and dirty top-level repositories. Never rerun promoters.
Historical contents: `status-history/pre-native-recovery-v1/CONTINUATION.md`.
Paths below are relative to `build/prototypes`.

## Accepted state

`native-signal-actions-sdk29-v1/working`: Kernel865 / OS439, SDK29.
Required next predecessor: `native-signal-wait-merge-v1/promotion-v1.json`,
`a19d5a4d351f9b5f17a9e4f91af51e1aaa6a2a3240b5029a2d52fae6e3f0dc65`.
Ten Kernel/four distribution profiles preserved; production signals disabled.

## Frozen candidates and passing bindings

- Kernel867: `native-journalled-mode-v1/candidate-v1/ObfuscationKernel`.
  Inventory `0cacc4d45421411b1a62f0d0580c56ab7d84686960bc4117462d4f2dda9b3e0a`.
  Two additions/seven modifications/no deletion relative accepted865.
  Author handoff `946eca2e55c1835679259f957b10bbe1f4b3996e4d03415db060a7a84ed2c8af`.
- OS449: `native-journalled-mode-integration-v1/candidate-v2/ObfuscationOS`.
  Inventory `be2bdb1c8928814c53e21d4e5ff20b10569f62b85a9dd431ecac6c898746e96a`.
  Ten additions/71 ABI edits/no deletion relative accepted439.
- SDK30 build: `native-journalled-mode-build-v1/build-binding-v1.json`,
  `a1bde2c891242b0f9638f3237b33a961153df21ac6044b492f2412533050b353`.
  All twenty SDK rows/ten Debug boots. Its older predecessor pin is historical;
  immediate Kernel865 source must reconcile to current signal-wait promotion.
- Inherited x86: same stage `regressions-os426-binding-v1.json`,
  `54e7f47ed569c5b944a547844d2a3cde9661c28d59b3aaac661a2e255dffd93b`,
  22 commands/2,824 cases.
- Fresh all-ten waits: same stage `wait-guests-binding-v1.json`,
  `f6d0adef9539332799ec9dda056e61c137b05e7c50e0ab213a8e0e03268410cf`,
  20 commands/4,840 cases.
- OS439 SDK30 migration: `native-signal-wait-sdk30-os-v1/receipt-v1.json`,
  `88412669769ea638447e33ac573448bb3c3d834705d4731af183afb1055000b4`;
  inventory `052c68c3e018a0fa68d1118692496fef3f1f5c2f0668173a43153585d8ea759c`.

The following three bindings in `native-journalled-mode-integration-v1` are
sealed and read-only replayed. Prior pending sessions have all been polled.

- `guests-binding-v1.json`: `be8362631c2372e6ba6d81b80e6db4a669b8224d4d48adf505ac95c16b2c91d8`;
  30 native +30 Linux readonly runs; 3,007 C checks,120 mutations,1,320 writes,
  1,140 flushes. `verify_guests_v2.py`; v1 wrong assumed3,000 count preserved.
- `recovery-binding-v1.json`: `fcd92101689db68742592a91263880caaf2f6b3caa8001c5fff6b7c1990ce376`;
  60 native cuts +60 Linux recoveries; final strict comparator replayed.
- `tools-binding-v1.json`: `a87a462c96c561be10c7d5d83db97563ceed93c53b3acf3142a263d9acdaba4f`;
  54 suites/533 methods +1,250 separately invoked raw-image model checks.
  Original mistaken unittest discovery of standalone model retained/reconciled.

## Active agents and next work

`pipe_signal_guest` owns isolated `native-journalled-mode-native-recovery-v1`.
Based on frozen449, implement60 actual native recovery boots +60 clean remounts.
Clone original cut disks; never modify originals. Explicit bounded exclusive
BlockSessions recovery before mount/cache publication; retired session then
maintained-noatime mount +musl statx/payload/fsync probe. Not executed yet.

`vector_runtime_review` independently closed repaired Linux comparator length
and head findings. Result `native-journalled-mode-recovery-closure-v1/result-v1.json`,
`0ae893cb5566429d641817432f505eed2d473745b1f652ee46c91da921f01c33`.
60 retained-output replays/79 controls (76 rejected,3 valid), no new guest runs.
Final report and manifest sealing still pending. Tool is exact449 copy SHA
`1364bd370938ae92a3015ac7ddc09f429496e55d668ca315a3f2eb9a1548f411`.

Root owns final source composition, binding/promotion and current status files.
A third status-agent spawn failed at thread limit; no such task ran.

After native qualification, compose additional approved OS files into a new
frozen successor; do not edit449. Review new collector/probe; bind unchanged
inherited sources and new evidence. Final binding and backed-up promotion must
use accepted865/439 and current wait predecessor. No final M4 binding/promoter
exists yet. Continue broader M0–M12 implementation afterwards.

Software cuts retain whole completed writes; no volatile-cache/torn/reordering/
physical claim. Side mount is not default-root/full M4. User deferred M11 physical
and M12 manual checks; no required question or permission pending.
