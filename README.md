# ObfuscationEvidence

Qualification evidence for ObfuscationKernel and ObfuscationOS: execution
receipts, prototype trees, promotion bindings, status snapshots and the frozen
progress history. Product repositories hold source, tests and documentation only
(ObfuscationOS `docs/decisions/0003-evidence-repository.md`).

## Layout

| Path | Versioned | Content |
| --- | --- | --- |
| `archive/` | no (ignored) | The complete pre-2026-10-24 evidence tree, moved verbatim from the workspace root `build/`: `prototypes/` (2,869 directories), `qualification/` (780), `milestone-*`, `status-history/`, `sources/` and root-level xmake outputs. The workspace keeps a `build -> ObfuscationEvidence/archive` symlink so recorded paths still resolve. |
| `index/` | yes | Directory listings of `archive/prototypes` and `archive/qualification` |
| `status/` | yes | `CONTINUATION*.md` checkpoints and the 18 `status-history/` snapshots |
| `reports/` | yes | Milestone audit (2026-09-23), review and repair reports (2026-10-19): REPORT.txt, report.json, integrity and inventory files |
| `frozen/` | yes | Documents frozen out of product repositories, such as the 846 KB ObfuscationOS implementation progress log |
| `receipts/` | yes | New evidence, one directory per `<repository>@<sha>/<branch>/<campaign>` (see PLAN.md) |

Large binary trees are never committed here. A campaign commits its receipts
(`result.json`, serial logs, hashes, commands) and names the archive path that
holds images and disks. `archive/` is retained on the workstation and in offline
backups only.

## Reading the current state

1. `status/CONTINUATION.md` is the last accepted-source checkpoint (Kernel901 /
   OS549, SDK32 at the time of writing).
2. `reports/milestone-review-20261019/REPORT.txt` and
   `reports/milestone-fixes-20261019/REPORT.txt` are the latest M0–M12 review
   and repair results.
3. The per-requirement capability matrix is generated in ObfuscationOS as
   `docs/plans/STATUS.md` from `docs/plans/contracts/ledger.json`.
