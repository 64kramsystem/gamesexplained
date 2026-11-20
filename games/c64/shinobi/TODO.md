# Shinobi analysis handoff

The branch contains Bronze analysis. Step 50 remains open. The table comes from the exported symbol maps and rebuilt listings.

| Part | Explained bytes | Tracked bytes | Uncounted stretches |
|---|---:|---:|---:|
| engine | 16,808 | 47,709 | 0 |
| mission1 | 9,302 | 17,392 | 0 |
| mission2 | 9,603 | 17,392 | 0 |
| mission3 | 9,521 | 17,392 | 0 |
| mission4 | 8,985 | 17,392 | 0 |
| mission5 | 11,911 | 17,392 | 0 |
| Total | 66,130 | 134,669 | 0 |

The largest remaining ranges are in the resident engine, the mission-specific routines after the stage layout data, and gaps between each mission’s known data tables. Determine the remaining regions from their readers or writers. The full ledger queues are in each part’s ignored `work/coverage.txt`.

Step 60 and any applicable step 65 recording remain pending the exact step 50 gate. A proven-model review is also required for Silver.
