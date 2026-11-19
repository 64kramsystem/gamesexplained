# Analysis still open

- Work the resident ledger's bare and uncounted ranges (run `kit/scripts/coverage.py` on the game and resident part). Finish classifying initialized data, the sprite bank's shape groups and the remaining engine and music routines.
- Resolve the catacombs map's loaded tail at `$75DE–$7600`. Trace consumers before classifying the extra bytes at `$7600` and `$3000` in the later loads.
- Complete coverage before the verification step. Sample listing comments using the agreed model, then rebuild the listings and recheck the exact counts.
- Resolve the feature rows still marked open, particularly the remaining stage mechanics. A full playthrough is outside this analysis handoff.

## Coverage at handoff

The rebuilt listings report zero uncounted stretches. The resident ledger tracks several stable hand-over ranges whose purpose remains open. The part ledgers still have 13,927 tracked bytes without explanations.

| Part | Explained bytes | Tracked bytes |
|---|---:|---:|
| Resident engine | 26,966 | 40,854 |
| Caves | 18,432 | 18,432 |
| Train | 8,704 | 8,704 |
| Catacombs | 18,398 | 18,433 |
| Airship | 18,432 | 18,434 |
| Grail temple | 18,432 | 18,434 |
| Total | 109,364 | 123,291 |

Step 50 is open. Steps 60 and 65 have no completed output. The overlay snapshots use the stage initializer directly and require no recorded play to reconstruct. Per-part reports and scripts are in the ignored work directories.
