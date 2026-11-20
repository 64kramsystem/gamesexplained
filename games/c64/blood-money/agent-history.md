# Blood Money analysis log

## 19 November 2026

- The Accept disk autostarted from its first directory entry. The matrix SPACE key advanced its intro. Execution checkpoints caught the engine handover at `$1CD6` and each level loader's return at `$C9B6`.
- Loading takes long enough to pass through an empty frame and an IEC receive wait. The level 1 snapshot came from the settled gameplay screen after the loader completed.
- Accept's fourth-level load left the previous sprite data in RAM because the disk has no `CHARS4` or `DATA4`. The Syntax disk matched all 14 shared files and supplied both missing files. A direct transition from the level 3 play snapshot produced changes in the sprite update code near `$DBDD`. The menu-route capture preserved the engine there and is the listing source for level 4. Both probes remain under `work/`.
- Stopping load watchpoints in the level data stopped after the loads at `$CC6A`, `$D032`, `$DCA3`, `$DCAF`, `$E253` and `$DE31`. Their raw output is in `work/probe-reads.log`. The frame capture is in `work/level1-frame.json`.
- The live disassembler provided the resident engine symbols. The data annotations for the overlays were converted to local regenerator2000 projects through the kit writer after a large live batch stalled. The kit exported each symbol map from its project and built the listing from the corresponding VICE handover snapshot.

## 20 November 2026

- The restored branch arrived without the ignored work files. Both downloads matched the recorded disk hashes. I recaptured the resident entry at `$1CD6` and all four overlays at `$C9B6`. The overlays match every byte in the previous listings. The resident entry comparison differed only at `$0000` before the new annotations were added.
- The resumed store watchpoints are in `work/resume-watchpoints.json`. The swap probe restored level 1 play, set PC to `$3A81`, and stopped immediately after the load at `$3A9A` from `$B800`. Its register state and hit count are in `work/charset-swap-watchpoint.json`.
- The engine retyping restores the computed shop and tile-object handlers to Code. New automatic labels appeared when regenerator2000 rebuilt the cross-references, including labels at SID pattern addresses. The pattern descriptions now follow the individual entries in the pointer table.
- The title timing watchpoint is in `work/title-timing-watchpoint.json`. It establishes the upper byte read by the schedule copy.
- The cache initialization probe in `work/cache-initialization-watchpoints.json` stopped first on stores at `$CD8A` or `$CDA7`. The runtime title countdown probe in `work/title-countdown-watchpoint.json` stopped just after the store at `$C759`. The entry contents in these ranges include editor fragments such as `open_line` and `c_indent`.
- The pixel comparison in `work/compare_masks.py` recovered the two extra CHARS masks from their relationship to the first hull mask. The comparison is exact for all nonempty masks.
- The stream walk from the level event roots is in `work/trace_object_streams.py`. Each part has its walk output in `work/object-script-leads.json`. A level 1 watchpoint caught the opcode load at `$D5C7` with the script pointer at `$8BA9`. The watchpoint capture is in `work/object-script-watchpoint.json`.

- The resumed coverage pass followed sprite and tile spawn pointers through the event records, script commands and object properties into LEVEL. The decoded leads are in each level's `work/remaining-records.json` and `work/tile-assets.json`. The common tile frames in the LEVEL tails are reached through the resident table at $1CBE.
- The new instruction-address stops are in `work/resume-cpu-watchpoints.json`, `work/shot-stream-watchpoint.json`, `work/tile-frame-watchpoint.json` and `work/mine-frame-pointer-watchpoint.json`. The staging and slot initialization probes are in `work/staging-initialization-watchpoints.json` and `work/slot-initialization-watchpoints.json`.
- The Syntax disk also booted to $1CD6. Its snapshot is `work/syntax-engine-entry.vsf`. Autostarting the separate picture entry produced `work/syntax-picture-screen.png`.

- The independent listing sample used seed 31749. Its draw and settled verdicts are in `work/reports/analysis-31749/`. The sprite-property and copied-zero template findings were applied across the overlays.
- The verification probes for the player count, title pacing, sprite properties, full stamp allocation, shop action, coin contacts and life decrement are in `work/verification-mechanic-watchpoints.json`. The controlled replacement test is in `work/coin-replacement-watchpoint.json`.
