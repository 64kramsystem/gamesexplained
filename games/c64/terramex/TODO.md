# Analysis handoff

The game has two exported symbol maps and source listings. The kit gives each load its own listing and rejects a third copy at the game root. The branch covers the requested analysis stages and contains no site work.

| Part | Explained | Tracked | Coverage | Bytes outside the ledger |
|---|---:|---:|---:|---:|
| Explorer selection | 25,275 | 25,275 | 100.0% | 79 |
| Expedition | 43,973 | 54,577 | 80.6% | 364 |
| Total | 69,248 | 79,852 | 86.7% | 443 |

- The largest expedition gap is the 2,531-byte run beginning at `$E51D`. The decompressed image contains instruction-like bytes and calls within this region, but the direct roots and the scene, actor and player-action target tables do not resolve its incoming entry. The bytes stay tracked and unexplained. Establish how it can be entered, or prove the block's role in the disk build before excluding it.
- The large remaining main queue entries include the action data and paths around `$D4CC`, the screen builder around `$9959`, sound command paths around `$A681`, and scene and actor continuations. Full event and object names, all actor dispatch effects, and the end-state conditions remain unresolved.
- The selector's `$5843–$5891` and main's `$3FFE–$4169` are the uncounted ranges flagged by the listings. Verify their consumers and origins before treating the ledgers as complete.
- The installed build terminated when capturing the selector's full raster frame during checkpoint deletion. A clean restart supported individual instruction checkpoints and store watchpoints. The selector facts give the measured input and IRQ counts, and the expedition frame trace is retained locally.
- `work/` contains the disk images, unpacked snapshots, command transcripts and the sample. Each part's `work/coverage.txt` has its largest remaining runs. `orientation.md` gives the route and input image hash.
- The step-60 sample found errors in 10 of 60 comments before corrections. A later full audit would measure the remaining listing. `gpt-6.2-sol` was used for the analysis and sample, and the kit requires a proven-model check to award Silver.
- Step 65 did not require a gameplay recording here. The two loads have a written boot route and exact transition checkpoints in `orientation.md`. The live checks are short controlled instruction and watchpoint probes from the saved snapshots.
