# Ending

Payload eight supplies the code called at $9080 by the resident transition. The entry snapshot stops before that call. The play snapshot shows the laboratory scene, with Franz and Pearly in the two cylinders. The entry code installs the interrupt at $9196, sets up bitmap and sprite data, and copies colour data from $B3E8 and following pages.

After the laboratory sequence, the code at `$95D1` installs a split display. The first interrupt shows text in VIC bank zero. The second selects the bitmap in bank `$C000`. The initializer copies nine rows of 26 cells from three adjacent sources. The bitmap bytes start at `$A6DC`, the screen attributes at `$AE2C`, and the colour RAM values at `$AF16`. The destination tables at `$995A` and `$996C` describe the same cell positions in bitmap and screen memory.

With the second-phase initializer entered directly from the saved laboratory scene, instruction steps showed `$9637` reading `$55` from `$A7AB` with Y equal to `$D0`. The next instruction at `$963A` stored it at `$EB07`. The epilogue text is read from `$9752` by the renderer at `$990D`.
