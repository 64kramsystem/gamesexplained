# Strider II technical facts

The [orientation](orientation.md) gives the snapshot recipes and breakpoint results. The code addresses below refer to the resident listing unless a stage part is named.

- The disk contains the X-Ray boot program and five packed stage streams. For each stream, the stage index plus six enters `$CC00`, which adds `$3B` to form `A*` through `E*`. Each stream reaches the same `$8000` engine entry after rewriting the stage slot `$0B00–$4FFF`. The breakpoint and store-watchpoint results are in the ignored local work files.
- The forest's top playfield uses VIC bank `$4000`. The captured frame writes `$12` to `$D018`, selecting the screen at `$4400` and characters at `$4800`. At line 169 it switches to bank `$C000` and writes `$A6`, selecting the HUD screen at `$E800` and characters at `$D800`. These addresses come from the captured writes and the VIC address fields.
- The stage tile renderer at `$9827` patches its map-read operand at `$98AB`. It advances that pointer by `$60` after each tile row. It expands each byte through the four quadrant tables at `$0B00`, `$0C00`, `$0D00` and `$0E00`. The lookup at `$A092` takes its byte from the separate `$0F00` table.
- The title uses the character set at `$D000` in VIC bank `$C000`. The rendered glyphs put A–Z at codes `$01–$1A` and the digits 0–9 at `$30–$39`. The title screen pointer table at `$CBF8` contains `$4C–$53` in order. The rendered sprite shapes at those offsets include the letters of STRIDER.
- The HUD uses another glyph order. Its rendered decimal digits 0–9 are codes `$D2–$DB` in the character set at `$D800`. The local sheets in `work/` were rendered directly from the snapshot.


The upper RAM at `$E000–$E117` includes eight-byte glyphs with vertical stripes and layered bands. The tail at `$E798–$E7FF` includes a descending ramp of filled rows and a fixed vertical stripe in its final slot. The render establishes the shape data. The route that selects this upper glyph set remains open.

## The listing's error rate

The independent sample used seed 1120 and drew 90 of 883 comments. The `gpt-6.2-sol` checker found nine wrong details and all nine were corrected. The sample caught a stage selector confused with encounter mode, a reversed sprite sort, a 64-byte sprite boundary described as character alignment, missing sword and meter conditions, regeneration of lookup entry zero, and three sound-data descriptions. The plain estimate was 10.0% (95% Wilson interval 5.4% to 17.9%). Weighting by stratum size gave 10.9%. The checker may have missed further errors. The measured minimum before fixes was nine of 883, or 1.0%.
