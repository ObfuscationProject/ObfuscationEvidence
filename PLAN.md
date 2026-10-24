# ObfuscationEvidence plan

## Done (2026-10-24)

- Moved the workspace `build/` evidence tree to `archive/` (ignored) and left a
  `build` symlink at the workspace root so recorded paths resolve.
- Versioned the small text evidence: continuation checkpoints, status history,
  milestone reports, prototype/qualification indexes, frozen progress log.

## Receipt layout for new campaigns

```text
receipts/<repository>@<short-sha>/<branch>/<campaign>/
  result.json        # machine-readable outcome, one object per command
  commands.txt       # exact commands, in order
  serial/*.log       # guest serial output, one file per boot
  hashes.json        # SHA-256 of every compiled input, SDK and output image
  ARCHIVE            # path under archive/ holding images, disks and large logs
```

A receipt directory is written once and never edited. A failed campaign stays
in place; its successor is a sibling directory. Product documentation cites a
receipt by this path.

## Next

1. Add `tools/index_archive.py` to regenerate `index/` and record per-directory
   sizes once the archive filesystem scan completes (the 2026-10-24 `du` of
   `prototypes/` and `qualification/` exceeded a five-minute budget).
2. Teach the ObfuscationOS qualification tools (`tools/*_evidence.py`,
   `console_receipt_admission.py`) to write receipts here instead of into the
   workspace `build/`; keep reading historical receipts from `archive/`.
3. Decide retention for `archive/prototypes`: keep promoted candidates and their
   independent reviews, compress or delete superseded attempts after their
   successor is promoted. Nothing is deleted before that decision is recorded.
4. Mirror `archive/` to offline storage; it is tens of gigabytes and not in git.
