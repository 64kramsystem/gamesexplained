# Test of Speed

- The instruction screen selects $A400 as its matrix and copies its custom font from $FA00. The scene uses a bitmap copied in part from $6000, and separately updates the water and suspended ball.
- The fire acceptance path is at $0A54. Joystick actions are sampled from CIA1 port A. The state machine at $1275 treats $C8 and $CC as control bytes for waiting or advancing with respect to the stored stick sample.
- The exit copies five pages from $EB00 to $C900 before jumping into the relocated loader. An execution checkpoint caught the subsequent KERNAL LOAD of file 3.
- The loop at $0875 calls $C1E0 to build 55 line records in 180-byte slots. The pointer table at $C8B5 selects 21 slots at $9000–$9EC3, 21 at $D000–$DEC3 and 13 at $F000–$F923. A CPU trace with processor port $34 followed each slot and recorded writes to 3,588 distinct byte addresses beneath I/O. Each generated pixel record holds the two-byte bitmap address and a bit mask.
- The bitmap initialization at $1B60 copies 21 pages from $6000 to $A000. The instruction trace confirmed writes throughout $A000–$B4FF. The matrix at $A400 is displayed during the instructions before the bitmap copy replaces it.
- The interrupt at $1C09 ran 72 times in 24 emulated frames. Checkpoints at $1C47, $1C9C, $1D36 and $1E63 each counted 24 hits. The water timer changes the immediate raster threshold at $1DE3.
- The ball update at $1643 moves its line index toward $1C. Controlled calls from indices 9 and 41 executed its increment and decrement respectively. The swing update at $1679 reached the patched boundaries at indices 26 and 30 for a line-length input of four and reversed the signed step.
- The water painter at $184A alternates sides. Instruction tests of all four frame selections for both sides reached the column and horizontal-strip pointers. With side progress at six the painter instead copied the open-water tiles at $5D00–$5D20 and cleared the remaining lower cells.
- Entering the result handler at $0A5A with percentages 49, 50 and 100 reached each award store at $0B50, $0B70, $0B90 and $0BB0. At 49 and 50 the additions were 13, 20, 24 and 17. At 100 they were 25, 40, 47 and 34. The flag store at $0B3C executed for 50 and 100.
- Both tune selectors used by the chamber ran through the music entry at $E170 in instruction tests. The two selectors set different track pointers and tempo bytes.
