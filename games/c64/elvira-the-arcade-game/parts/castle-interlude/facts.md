# Castle interlude

The CL overlay sets up its illustrated screen at $1800. The raster IRQ at $1945 increments the tick at $19A4 and calls the driver at $0CDD on odd ticks. The screen matrix copy starts at $3DE5 and lands in RAM at $D400.

The next transition runs $0810 to request the B file. $0887 relocates loaded pages, then $0875 jumps to LOAD for the A file. The synthetic return enters the quest at $0812. See the game’s orientation for the two names and breakpoint evidence.

The picture reveal at $08DB works from $1DE5 into the bitmap at $E000. A 256-byte permutation at $0945 selects one two-bit pixel mask and one byte offset per pass. The inner loop merges the selected pair at $091C and advances the source and destination by $30. An instruction stop at $091C showed the source pointer on $1DE5, the destination pointer on $E000, and the first offset at $19. The preceding clear is at $1DC9.

The controlled Ice-to-CL transition stopped at $1800. Its CPU access map recorded zero underlying RAM writes in $D000–$D3FF and $D800–$DFFF. Both ranges match the Ice play, CL entry and illustrated screen captures. Accesses logged at those addresses during the illustrated screen were to I/O. The disk prompt uses the first eight slots at $D000–$D1FF after clearing them at $1A7C with character ROM visible.
