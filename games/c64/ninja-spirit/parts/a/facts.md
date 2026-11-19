# Disk load A

- `$29D5` draws the title and reads the active-low fire bit. Port-2 fire entered Round 1 in the PAL emulator.
- `$291F` uses `$3A3C` to choose between two round setup routines. `$28B0` advances this local index, and `$291A` enters file B’s loader after the second round.
- `$2BCE` tests world positions from three parallel coordinate tables against the camera window and dispatches visible placement records through `$2D03`.
- `$2BA7` writes the selected weapon. An execution stop at `$2B7E` following a matrix Space hold saw A=`$EF`. Stepping the eventual store changed `$25D2` from `$00` to `$02`.
- The packet has a fill-dominated gap after `$3A42`. The longest component-slot index from `$3A3E` is 3. The local playback probe logged no CPU reads or writes inside `$3A43–$3FFF`.
