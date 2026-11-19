# Agent history

## 19 November 2026

Booted the RCS/HCC disk on the assigned headless VICE build, identified the two game loads and traced the `MAIN` disk call and unpacked entry. Captured the selector and expedition snapshots locally. Used the ROM release only to compare named asset layouts with the selected disk. Recorded both packed files in the media ledger.

Seeded Regenerator from direct instruction flow and from live execute maps. A second pass added targets from the scene, actor and player-action dispatch tables. Traced graphics, map data, audio pointers and RAM under I/O separately. Exported each part and worked through the largest unexplained spans, retaining addressed unknowns in the coverage queue.

An independent same-model checker sampled 60 listing comments. Corrected the ten findings against the instruction bytes. Tested the selector, right movement, leap, time and SID writes with CPU checkpoints and store watchpoints. The traces, disassembler logs and snapshots are in ignored work folders.

Resumed the exported coverage ledgers from the saved snapshots. Traced the selector return at `$5B3B` through `$587C` to the KERNAL load, and the expedition's retained bootstrap bytes to the first title matrix clear. Classified the copied collision and HUD code by matching its routines and tables to the active set and checking its stale targets. A conditional watchpoint identified the consumer of the upper sprite colour table. Removed generated colour RAM field aliases at RAM code addresses after checking their references. Both exact byte counts match and both uncounted lists are empty.
