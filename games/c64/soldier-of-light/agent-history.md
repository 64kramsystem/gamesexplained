# Analysis history

## 20 November 2026

- Tested the TNG disk through the crack intro. Space dismissed the intro and the game stopped drawing while the CPU was cycling through the KERNAL serial path. Continued with the independently packed F.S.N. release. Both disks and the extracted payloads are in ignored `work/`.
- The F.S.N. release booted to the title after its two unpacking stages. The checkpoint at `$080D` captured the beginning of its second stage. Stepping the last `RTI` at `$01EF` showed that it restores a title IRQ in progress. The actual end of the wrapper is distinct from the earlier jump into the CIA and zero-page restore stub.
- Captured the three ground starts. All use resident sources and a shared map expander. A full Cleemalt frame captured the character-set split. `work/writers.log` has the store checkpoint stops and short instruction histories for the map buffer, the character buffer and the service byte at `$03FF`.
- Collected an execution map from the title, selector and three ground starts. The generic dump sized some high-address instructions from the visible KERNAL or I/O at the end of the capture. Recomputed lengths from the raw RAM in `work/cleemalt-play.vsf` for the same 4,853 recorded addresses. The result has 11,262 executed bytes with no instruction overruns. The original dump remains in `work/codemap-visible.json`.
- Found executable routines among the sprite slots at `$A580–$A5F5`. The rendering of those slots shows instruction-shaped noise, and `$2CDA` calls into the area. The four executed starts in the `$A000` bank also fall there.
- Completed the coverage ledger at 43,824 of 43,824 bytes with no uncounted loaded stretches. The listing uses the Cleemalt play snapshot and compares it with the loader handover in `work/entry.vsf`.
- Drew the independent listing sample with seed 112022 and an explicit music-template stratum. The checker used `gpt-6.2-sol`. Its verdicts, the sample and the kit count are in `work/reports/sample-112022/`. Corrected all six findings and clarified a matching sprite offset comment.
- Used VICE store watches on `$84D7` and `$D404` for a timer rollover and a SID control write. Neither test depends on a recorded player route.
- The shared listing check identified five instruction bytes hidden by overlapping table bases. Restored the JMP operand at `$1DAB` and the instructions around `$23C0` to code. The remaining planet Y values retain their data type.
