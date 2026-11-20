# Stage 5 overlay

The disk loader's selector 4 installs the following ranges. All 17,918 bytes match the stage's execute-stop snapshot at $8100.

| Disk file | Exact loaded region | Purpose |
|---|---|---|
| Z | $1600–$47FF | Map cells at $1600, then playfield glyphs at $4000. |
| 0 | $5A00–$67FE | 64-byte VIC sprite slots in bank $4000. |
| 1 | $F500–$F6FF | Metatile properties and object spawn fields. |
| 2 | $E400–$E7FE | Four pages of metatile quadrant codes. |

The resident engine reads map cells through the patched operand at $A0F0 and collision properties through $851B. The four quadrant pages supply character indices at the same metatile index. The object seed loader at resident $8851 copies slots 31 down through 1 into work arrays, with the high X byte from $F600 and low X byte from $F620, high Y from $F640 and low Y from $F660. It uses the next three tables for image, direction and action state.
