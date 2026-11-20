# Test of Strength

- The selection around $0D8C reads the active-low left and right bits and uses the countdown in $1717 when direction changes. Timing and scoring across a complete strike remain open.
- $1358 copies the chamber bitmap from $2000 and the colours from $4000. The play snapshot uses hardware IRQ $143F.
- The routine at $C900 loaded file 4 when entered directly. The shared result border and apprentice records survived that hand-off.
- The result handler beginning at $099B chooses its message from the outcome at $1711 and the zero-based attempt index at $1745. Entering the handler with outcome 1 and index 1 bypassed the award stores. With outcome 2, indices 0, 1 and 2 produced 0, 25 and 50 percent respectively. Outcome 1 and index 3 produced 100 percent.
- The $0A7C award path sets the active apprentice's flag at $CE2A plus the apprentice index at 50 percent or higher. The calls to $0BA2 scale the four training additions by the result percentage, rounding up. The base values are 50, 60, 0 and 14. Instruction checkpoints hit the four stores at $0A9C, $0ABC, $0ADB and $0AFB on each awarding path.
- Over 24 emulated frames, the raster handler at $143F ran 96 times and dispatched each of $147D, $15A7, $163C and $16CB 24 times. It moves through the compare lines $FA, $A5, $EA and $F0 in that order. The third phase uses all eight sprites in the bottom strip.
- A CPU trace of $1358 recorded writes to every destination byte from $A000 through $BFE0. The instruction screen first uses $A000–$A2FF for character pixels copied by $1244. The adjacent text marker at $9FF3 reads `C64-DL1 $C000` and ends with a $94 byte at $A000. Its role remains open.
- The play loop calls the sound-effect driver through $E000. Its register-offset dispatcher uses numbered effect streams starting at $E1CB, $E1DD, $E1F8, $E20E, $E220 and $E232. A CPU run for each effect recorded SID writes and no stream reads above $E252.
- The board and apprentice pose copier at $1075 writes six 64-byte slots per group in two chunks. Instruction traces identified the two single-byte holes at $8600 and $8780. The subsequent overlay copier at $112D writes both 64-byte slots at $8800 and $8840.
- Testing each height from zero through $50 through the gauge restore entries at $0E7A and $0EC2 reached $6400–$6457. The bar code applies an eight-bit mask before writing the selected bitmap cell.
