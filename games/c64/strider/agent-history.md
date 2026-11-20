# Strider analysis history

- 20 November 2026. Oriented the Five Immortals disk in the installed headless VICE build with dummy audio. The first catalog entry is separate from the entry used to boot the game. Saved the loading picture after file A, the resident hand-over before stage 1 and the five stage hand-overs at $8100.
- Mapped all stage files byte for byte at their load addresses. Recorded execute coverage around gameplay input and used recursive disassembly to recover paths outside that observation. Used the pre-overlay snapshot for the resident listing to preserve the original data in the windows overwritten by stage 1.
- Completed the ledger before verification. Used stepped input and tile reads, raster and SID write counts and a forced stage-completion test. The independent comment sample found six wrong details and informed the correction pass.
