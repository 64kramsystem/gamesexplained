# Shinobi analysis handoff

Step 50 and the post-verification rebuild give these exact kit ledger counts. The loaded-data audit compared each rebuilt listing with its handover and play snapshots.

| Part | Explained bytes | Tracked bytes | Uncounted stretches |
|---|---:|---:|---:|
| engine | 42,749 | 42,749 | 0 |
| mission1 | 17,392 | 17,392 | 0 |
| mission2 | 17,392 | 17,392 | 0 |
| mission3 | 17,392 | 17,392 | 0 |
| mission4 | 17,392 | 17,392 | 0 |
| mission5 | 17,392 | 17,392 | 0 |
| Total | 129,709 | 129,709 | 0 |

The loaded engine ranges at `$1571–$1573` and `$8D61–$8D69` and the Mission 3 range at `$E8C0–$E91F` remain tracked as data. Their original purpose remains open. The observations and limits of the CPU traces are in `facts.md`.

The 15 pairs at `$A362/$A371` resolve to six combinations of resident sprite slots. Rendering the slots shows paired figure parts and confirms the all-zero image for pointer `$55`. The reader of these pairs and the use of the 32-byte allocation at `$8980` remain open. The common `$FD30–$FD4F` allocation matches the default KERNAL RAM vectors and counts in every mission. Its runtime role remains open.

The engine's saved project is `parts/engine/work/shinobi.regen2000proj`, with its live disassembler on port 23094. The mission projects are `parts/missionN/work/handoff.regen2000proj`. Each part retains its entry and play snapshots and `work/coverage.txt`. The game-level `work/` holds the disk, probe scripts, watchpoint results and the independent sample under `work/reports/sample-1729/`.

Step 60 corrected all nine findings in the 60-comment sample. A full listing audit is recommended. Step 65 did not require a recording because the analysis used controlled instruction traces and snapshot-entry recipes. Features that still need evidence are marked in `features.md`. The site, reader review and retrospective are outside this handoff. The Bronze tier remains until the Silver requirements, including the listing review on a proven model, are met.
