# Yie Ar Kung-Fu · analysis facts

Addresses refer to the PAL tape hand-over listing in `listing.json`.

## Serial DATA check on the title

The title loop at `$08FE` calls `$051D`. The latter temporarily patches `BIT $D000` at `$0524` into `BIT $DD00`, then restores the operand and branches on the saved sign flag. If the serial DATA input (bit 7) is low, it calls the memory exchange at `$1C03` with A=1. The tables at `$1D17–$1D22` select twelve pages at `$0400` and `$A000`, exchanging the front end with part of the fight engine. With the default virtual drive configuration, the instruction trace sampled `$DD00=$1C` and N cleared at `$0527`. The machine later fetched instructions from bitmap memory, including a JAM at `$EA68`. With the drives and printers disabled before boot, the same instruction read `$9C` and left N set. The title proceeded to the player menu and first fight. The tape loader itself warns about those peripherals.

## Joystick decoding

The front end combines both active-low CIA1 ports at `$0BB0`; when a sample repeats, it drops the fire bit and keeps the direction bits. In a fight, `$BB8C–$BB9B` reads only CIA1 port A. In the first-fight instruction trace, holding port 2 right gave A=`$F7` after `LDA $DC00`, `$17` after masking, and `$08` after inversion. The store at `$BB98` wrote `$08` to the input latch at `$A04B`. On the matching-sample path, `$BBB8` waits for the stability counter at `$A050` before installing a new move code. `$BBC3` translates the code for reversed facing.

## Screens, colors and text

- The title routine at `$0B51` selects VIC bank `$C000` and multicolor bitmap mode. The image is `$E000–$FF3F`, with two cell colors from `$CC00–$CFE7`. The copy from `$C800` gives color RAM its multicolor selector 11. The common background color is 6.
- Fight screen RAM begins at `$4000`. `$D018=$0D` selects the character set at `$7000`, and `$0F` selects the one at `$7800` in VIC bank `$4000`. Rendered glyphs at `$7000` show @ at $00, A–Z at $01–$1A and digits 0–9 at $30–$39. Upper codes also draw terrain and panel tiles. The front end converts its text to screen codes with `AND #$3F`, for example at `$0E05`. The game shows its Konami and Imagine credits, staff names, mode selection, a perfect-round award, and a 20,000-point bonus life.
- The screen stream at `$3B80` builds the first 120 cells of the panel. The streams at `$3C00`, `$3800` and `$3600` begin at `$4078` and draw the waterfall, temple and opponent preview respectively. The decoder at `$1C26` emits literal glyphs below $FB. $FB repeats a glyph, $FC sets the cursor, $FD skips 20 source bytes, $FE sets a color, and $FF returns from the decoder.
- The IRQ at `$C3A7` selects a phase routine from `$C3F9` and changes the operand at `$C3BC/$C3BD`. For the early fight the palette changes in the raster capture include writes to `$D021` of $0F at line 74, $0E at line 114 and $00 at line 256. The IRQ phase at `$C491` feeds the fight tick counter at `$A061`, which the main loop consumes at `$BCE4`.

## Opponents and sprites

`$A07E` holds the opponent index during the fight. `$A47C` loads 223 bytes from one of the ten page-aligned records at `$1000–$19DF` into the parameter area at `$B65F`. The main loop chooses a stage-specific jump target at `$A7CC` using the table at `$B22F`. `$A205` advances the index and reinitializes the fight; the branch at ten clears the index and increments the bounded pass counter. The opponent preview temporarily uses a negative index and the corresponding IRQ phase group.

The picture routines at `$BC00` and `$BC71` use three sprite pieces for Oolong. `$B53D` selects the corresponding pose path for the opponent. The current facing chooses ordinary or reflected shapes. `$BD08` generates a 256-entry lookup table at `$C274` that reverses each byte's four two-bit pixels. Reflection copiers use it while reversing the column order. `$BA1E` writes the eight sprite pointers and positions, doubles the logical X coordinates and assembles the extension bits in `$D010`.

## Register census

| Access | Purpose | Example instructions |
|---|---|---|
| `$01` | Select RAM and I/O in the game. The alternate CIA direction check clears all three banking bits. | `$C39C, $BD3F` |
| `$D000–$D010`, `$D015`, `$D01C`, `$D025–$D02E` | Sprite coordinates, X extension, visibility, multicolor selection and colors. | `$BA2A, $BA37, $BA45, $BD99, $C4F9, $A4B3` |
| `$D011, $D016, $D018, $DD00` | Switch between title bitmap and arena character mode, and select the bank and data bases. | `$0B5A, $0B5F, $0B64, $0996, $C4C7` |
| `$D012, $D019, $D01A` | Raster timing, IRQ acknowledgment and enable. | `$08FE, $C388, $C3AE, $C392` |
| `$D020–$D023, $D800–$DBFF` | Border and background colors, raster palette and per-cell color RAM. | `$0B6E, $C4E7, $C4EC, $C4F1, $0B83` |
| `$D400–$D418` | Three SID voices, the filter and master volume. The sound entry at `$8000` selects song, effect or service operations with even values of Y. | `$814A, $835D, $8677, $8990, $8160, $8175` |
| `$DC00, $DC01, $DC02, $DC0D` | Joystick reads, port direction check and CIA IRQ control. | `$0BB0, $0BB3, $BB8C, $BD35, $C397, $C3EA` |
| `$DD00` bit 7 | Serial DATA input checked by the title loop. | `$0524` after operand patch |

## Sound streams and score

The music entry at `$8000` indexes a little-endian jump table with even Y offsets. Song starts load three stream pointers from `$8E7C`. The game title selects the last set, beginning at `$96D7`, `$9AEB` and `$9CE8`. The voice readers separate note-and-duration pairs from their even command bytes `$C0–$DC`. The commands select instruments, repeat pieces of the stream, transpose or redirect it, and dispatch other voice operations. The SID frequency is assembled from the low-byte table at `$8DC3` and the high-byte table at `$8D64`. The separate effect descriptors are 31 bytes each, with selected SID initialization fields copied by `$81CA`.

The game keeps three packed BCD score bytes at `$0380–$0382`. `$C5C3` adds another three BCD bytes with decimal carry. `$C5E7` displays the result as six digits. `$C635` tests a change in bit 1 of the highest BCD byte and can increment the lives display counter if it is below eight. The player and opponent KO counters initialize to `$0F` at `$B81C`. Their decrement paths set the losing or winning state when the associated counter becomes negative.
