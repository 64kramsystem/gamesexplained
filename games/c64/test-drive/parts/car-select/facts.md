# Car selection

The selector snapshot shows the Lotus and its specifications. The relocated CI header at `$2E64` gives entry `$2E68`. The TS header at `$2FAC` gives entry `$2FB0` and body length `$0713`.

`$301E` converts the zero-based index at `$40` into the car's ID suffix. The loop at `$3057` tests the confirmation latch and direction index. On a direction accepted by the table, the selection increments or decrements and wraps within five entries. The raster handler's port read at `$346B` masks the low nibble and searches nine choices. It reads fire at `$3483` and ORs an active input into the latch at `$46`.

A stop at `$312A` caught the bitmap copy with source pointer `$4000` and destination pointer `$C000`. The loop runs over 32 pages and the saved driving entry contains exactly matching banks across those pages.

The cold route reached a stopping checkpoint at `$2FB0`, with X/Y equal to `TS`, after side B was mounted at the flip prompt. Comparing that image with the steady-state selector found 1,813 of 1,815 bytes equal in TS and all 328 bytes equal in CI.

The physical RAM below I/O started clear at the TS hand-over. A store checkpoint on `$D100` stopped the processor at `$2D05`, with the effective processor port at `$30`. This is a write into the selector's second bitmap bank. The remaining work is to bound the generated bitmap and identify the loaded source assets.
