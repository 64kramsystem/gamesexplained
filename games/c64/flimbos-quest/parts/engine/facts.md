# Resident engine

The resident listing uses `work/play.vsf`. It records working code and its stage-one operands. Runtime pointers and immediate values can change with the camera, the actors, the current raster phase and a new load.

The main playfield IRQ begins at `$16AD`, the shop chain begins at `$21A3`, and the lower title IRQ is at `$7CB7`. The resident raster handoff helper is `$791A`. Code at `$215A` loads the next stage and tests for the ending, while `$7992` loads the first stage from the boot path.

The stage parts own the overwritten ranges. Entry snapshots show the loader's output before drawing and gameplay mutate it. The engine owns both playfield screen buffers in `$C000–$C7FF` and the bank-zero panel screen at `$0400`.

Instruction and register evidence for the controls, timing, display and loader appears in the [game facts](../../facts.md).
