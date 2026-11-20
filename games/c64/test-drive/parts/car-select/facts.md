# Car selection

The selector snapshot shows the Lotus and its specifications. The relocated CI header at `$2E64` gives entry `$2E68`. The TS header at `$2FAC` gives entry `$2FB0` and body length `$0713`.

`$301E` converts the zero-based index at `$40` into the car's ID suffix. The loop at `$3057` tests the confirmation latch and direction index. On a direction accepted by the table, the selection increments or decrements and wraps within five entries. The raster handler's port read at `$346B` masks the low nibble and searches nine choices. It reads fire at `$3483` and ORs an active input into the latch at `$46`.

A stop at `$312A` caught the bitmap copy with source pointer `$4000` and destination pointer `$C000`. The loop runs over 32 pages and the saved driving entry contains exactly matching banks across those pages.

The cold route reached a stopping checkpoint at `$2FB0`, with X/Y equal to `TS`, after side B was mounted at the flip prompt. Comparing that image with the steady-state selector found 1,813 of 1,815 bytes equal in TS and all 328 bytes equal in CI.

The physical RAM below I/O started clear at the TS hand-over. A store checkpoint on `$D100` stopped the processor at `$2D05`, with the effective processor port at `$30`. This is a write into the selector's second bitmap bank. Stops at $2CD8 and $2D30 bracketed the mask pass with $01 equal to $30 and the bitmap base bytes $40 and $C0. The store watchpoints at $D000 and $DFFF each fired four times in that interval. The code at $2CED permutes all 32 pages and the outer loop indexes all 256 offsets through $2D52. Each of the four passes masks the second bitmap at $C000–$DFFF.

## Bitmap and colour resources

The five car bitmap resources have IDs $C3/$31 through $C3/$35. The selector makes the low byte from the car index at $40, then hands the pair to GP. A second call uses $C3/$36 for shared artwork. The corresponding packed bytes in the selector snapshot match all five side B catalogue items and the shared resource inside the UJ archive $2A/$C3.

GP reads the traversal flag and nine escape bytes from the bitmap header, then decodes literal bytes and runs. CPU stops at $2AA1 and $2A26 caught the Lotus resource being read from $B599 and a decoded byte about to be written to the bitmap. The colour call at $2AC2 was about to read the six-byte leading header from $FED8. The five colour objects `_1` through `_5` match the UJ archive byte for byte. GP reads ten escape bytes starting at byte seven, then reads its colour stream starting at byte 17, high nibble first. The writer at $2B78 uses dimensions from the header to advance through two screen passes and a colour-RAM pass.

The Lotus colour stream occupies $FED8–$FFF7 in the snapshot. On the first
selector draw, a load watchpoint on $FFF8–$FFF9 stopped at $2B45, just after
the nibble reader loaded $20 from $FFF8 with RAM visible. Single-stepping
showed $2B41 returning its high nibble, 2, to the colour decoding loop at
$2AD8. The following steps reached the colour writer at $2B78. Both bytes
above the resource matched the disk intro snapshot. The store and
execution watches stayed at zero through the return to the selector loop
at $3057. The trace is in `work/resume-selector-tail-watch.log` at the game root.

The captured selector also contains GP at $29BC–$2C3A and DP at
$2C3B–$2E63. The headers give the relocated addresses and body lengths.
GP supplies the previously traced bitmap and packed colour decoders.
DP supplies the previously traced merge and mask passes. Its page
order and byte order tables are complete permutations of the 32 page
indices and the 256 byte offsets respectively.
