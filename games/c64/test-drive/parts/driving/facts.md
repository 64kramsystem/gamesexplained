# Driving engine

The Lotus capture contains the common RD driver, the original D1 instrument module for this route, and the graphics data used by the first road. The other four cars load different instrument modules at the same addresses. Each road stage loads its own module at `$3600` and installs the three road-data pointers.

The driving IRQ entry is `$8AB3`. It banks I/O in, acknowledges the interrupt and updates VIC bank selection and the next compare line. The input watchpoint and the trace of up with fire reached `$8EA5` and the gear store at `$8EF4` respectively. See the root facts for the traced values and the road graphics format.

The listing uses `work/analysis.vsf`, the stage-one loader-return snapshot, because the `##` graphics payload at `$A286` is fully present there. `work/entry.vsf` is the earlier RD hand-over at `$6A1B` and `work/play.vsf` shows the road after drawing. The snapshot comparison distinguishes loaded instrument-panel art from the blank windshield the renderer fills.

The selector prepares the second bank's colour-selection matrix with the row-copy loop at $3593–$3598. A store watch on $E000 caught the CPU immediately after the store at $3595, with source pointer $6001 and destination pointer $E000. The row loop writes 40 cells before advancing. At the driving hand-over all 1,000 cells of the two matrices at $6000 and $E000 match. The trace is in the game's local `work/resume-matrix.log`.

FX builds parallel low and high address tables at $2D75 and $2D85.
The entries advance in 15-byte steps. Side B directory item $28/$C1
matches RAM at $2D95–$2DFF and holds a two-byte prefix followed by seven
complete presets. A CPU read watchpoint stopped at $2B00 when the
preset reader at $2AFE loaded the first byte of preset 0, 3 and 6 in
separate probes. In each case the pointer at $04–$05 matched the address
in the split tables. The remaining generated pointers lead past the end
of the item. Their use in ordinary play remains open. The trace is in
`work/resume-fx-watch.log` at the game root.

The 100 bytes at $2E00–$2E63 match the end of the selector's DP module
in both its snapshot and the side B catalogue. The selector listing
owns this retained tail.

The windscreen damage renderer uses seven coordinate groups and a
28-step draw schedule. Group zero stores a shared origin and eleven
endpoints. Each other group stores four coordinates per segment. The
parser at $9A96 chooses the format through the group index and hands
the endpoints to the midpoint subdivision routine at $9AFF. A CPU
probe of the renderer stopped at $9AC2 with $0E–$0F pointing to the
first group at $9BFE. Continuing reached $9B9F immediately after the
bitmap plot store. See `work/resume-glass-watch.log` at the game root.

The road span routine at $7D63 writes a half-open multicolor pixel span
into the one-row workspace. With X equal to one, Y equal to three and A
equal to $FF, a store watch stopped immediately after the write of $3F
to $06A0. A separate probe reached $7DF8 after reading the first field
of the object at $033C. The rest of that routine conditionally
exchanges all six fields of the two selected object records. Both
probes are in `work/resume-road-render-watch.log` at the game root.
