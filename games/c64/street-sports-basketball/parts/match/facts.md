# Basketball match

## Raster split and sprite queue

The hardware IRQ vector points to $575B during ordinary match frames. Starting from the live school match, a stopping watchpoint on $D018 repeatedly caught the store at $5792 on raster line $F2. A held $34 and the register read back $35. The next stop was the store at $57D5 on line $FC, with A=$36 and $D018 reading $37. Both settings select screen RAM at $CC00 in the $C000 VIC bank. The first selects the generated score glyphs at $D000 and the second selects the court glyphs at $D800.

The vector store watch stopped just after $574B. The low byte had changed from $F8 to $5B while the high byte still read $56. The next store at $5750 installs $57 and completes the switch back to $575B. The driver at $56F8 takes target lines from $03C3 and sprite operations from $03DB. Some requests set sprite Y, and others change a sprite pointer in both screen matrices. The return to the main handler schedules $F0.

## Court and sprite data

- A CPU load watch on $C000–$C57F hit the indexed read at $3C7E from both the setup and a live match. The pointer table beginning at $468E advances by 17 bytes for each column. The reader halves $0550 and subtracts eight for its row, then dispatches by the code it found. The file provides 80 columns covering $C000–$C54F. Bytes after that map are still being classified.
- A CPU load watch on $6A00–$BFFF hit $2CF0 in a school match. It reads the six slot pointers beginning at $7002. The base-pose table at $700E is indexed through $0322,X. The body at $70F4–$95EC parses as 106 consecutive variable-length records. Every record consumes 129 minus its first byte, and the final record ends exactly before the first character-specific catalogue. The part's annotations record each run of equal headers.
- A CPU load watch on $FD80–$FEFF hit the recolour loop at $3334. An earlier setup step patches that instruction's source operand from $3355. The six templates are spaced by 64 bytes and rendered as 21 rows of three multicolour bitmap bytes, with a padding byte per template.

## Match panel encoding

The printer at $17DD reads zero-terminated strings. It maps digits to indices $00–$09, space to $0A, uppercase letters to $0B–$24, and colon, exclamation mark, question mark and period to $25–$28. Each screen index goes to $CFC0 plus the column. Its colour goes to $DBC0 plus the column.

| Hardware | Use | Evidence |
| --- | --- | --- |
| $01 | Hides KERNAL for the match, exposes character ROM during score font preparation | $0EC2, $0F31 |
| $D012, $D018, $D019 | Raster schedules, display split and IRQ acknowledgement | $572C, $5733, $5792, $57D5 |
| $D021 | Restores the court background colour from the selected court's $EFFD byte | $57A6 |
| $DD00, $DD02 | Select VIC bank $C000 | $0EEC, $0EF4 |
| $DC00, $DC01 | Match input and confirmation | $17C0, $1FCB, $1FD1 |

## Target score and award

With the match paused on the target prompt, port 2 right hit the execution checkpoint at $164C with A=$22 and decimal mode set. Stepping exactly one instruction changed the low BCD byte at $EA from $20 to $22. The paired branch at $162B subtracts two and has a lower bound guard. The right path stops increasing the target when the hundreds byte at $EB becomes nonzero.

The award routine at $558F adds two to one of the BCD totals at $37–$3A. Setting the ball action to $50 in a saved school match reached the CPU checkpoint at $55B0 with A=$02. One instruction changed the blue total from zero to two. That controlled branch check establishes the score update. The conditions that take a shot into the award phase remain open.

The court asset has a character bank at $D800, screen-code halves at $E000 and $E400, and 24 rows of 80 colour codes at $E800. The routine at $3667 copies four ten-cell strips per row from a moving source column. The palette is stored separately at $EFFD–$EFFF.

Movement, control switching, CPU decisions, ball physics, match sound and the rematch path still need full coverage.
