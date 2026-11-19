# Catacombs

The renderer reads 150-byte rows from the map at `$3600` and displays the loaded glyphs from `$2800`. The filename stop at `$B85E` selected `INDIANA3  (EBES)`. The part listing uses the snapshot taken at `$B861`, when the loaded cells are present before stage initialization changes them. Row 109 starts at `$75DE`. Its loaded prefix extends through column 34 at `$7600`. With the camera staged at Y=872 pixels, a read watchpoint stopped at PC `$895A` after the patched `LDA $75DE,Y` at `$8957`. Column 0 returned `$66` and column 34 returned `$02` in separate probes. How far normal play can scroll into that row remains open.

See [orientation.md](../../orientation.md) for the measured write ranges and [the stage screenshot](../../reference/catacombs.png).
