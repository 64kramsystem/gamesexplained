# Blood Money analysis log

## 19 November 2026

- The Accept disk autostarted from its first directory entry. The matrix SPACE key advanced its intro. Execution checkpoints caught the engine handover at `$1CD6` and each level loader's return at `$C9B6`.
- Loading takes long enough to pass through an empty frame and an IEC receive wait. The level 1 snapshot came from the settled gameplay screen after the loader completed.
- Accept's fourth-level load left the previous sprite data in RAM because the disk has no `CHARS4` or `DATA4`. The Syntax disk matched all 14 shared files and supplied both missing files. A direct transition from the level 3 play snapshot produced changes in the sprite update code near `$DBDD`. The menu-route capture preserved the engine there and is the listing source for level 4. Both probes remain under `work/`.
- Stopping load watchpoints in the level data stopped after the loads at `$CC6A`, `$D032`, `$DCA3`, `$DCAF`, `$E253` and `$DE31`. Their raw output is in `work/probe-reads.log`. The frame capture is in `work/level1-frame.json`.
- The live disassembler provided the resident engine symbols. The data annotations for the overlays were converted to local regenerator2000 projects through the kit writer after a large live batch stalled. The kit exported each symbol map from its project and built the listing from the corresponding VICE handover snapshot.
