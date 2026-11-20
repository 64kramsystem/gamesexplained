# Shinobi (C64) facts

## Loader and stage data

- The X-Large loader's handover at `$1904` holds all 47,103 resident PRG bytes at `$0801-$BFFF`. The engine stores 1 as the initial mission number at `$FCC0`. The transition code increments this number at `$B00F`.
- The stage loader writes the mission digit to `$3E45` in the twelve-byte DOS name at `$3E3E`, opens the file on drive 8 and reads through KERNAL CHRIN. It switches the processor port before each store at `$3F60`. A running checkpoint counted 768 stores in about two seconds.
- An execution stop at `$3F22` follows both transfers. Each mission's payload matches `$6400-$68FF` for 1,280 bytes and `$C000-$FEEF` for 16,112 bytes. The routine then closes the channel. Its delay counts 255 visits of raster line `$F8`.
- Stage metadata gives separate pointers for tile and attribute grids, widths and heights, initial display parameters, palette and object placement sources. The setup builds separate row-pointer tables at `$0856-$08D5`. Stage placement entries contain a low destination byte, a high destination byte and a value. The resident setup applies the value and stops at the first zero value.
- A load checkpoint over the mission 1 tile dictionary stopped after `$17E5`, the indirect character load in the initial screen renderer. The dictionary entry has 16 character indices arranged as four rows of four. `$17CD` obtains that tile's colour from `$CF00`. `$1856` writes both screen pages and colour RAM.
- The resident program fills `$0600-$06FF` before the gameplay screen overwrites its setup routine at `$4C00`. All 256 resulting bytes match reversal of the four 2-bit pixel pairs in the input byte. Mission 5 uses this table in its sprite mirror routine at `$F836`.

## Controls and video

- At Mission 1, execution stopped at the joystick load `$3B84` and advanced one instruction to `$3B87`. The accumulator was `$7F` with no input, `$77` with port 2 right and `$6F` with port 2 fire. The keyboard merge at `$3B8F` can clear seven masks in the same input byte.
- The attract routine at `$98CA` checks the latest input mask in `$0ADC`. Left writes mode 2 and right writes mode 3. Fire branches to the player initialization at `$19B5`.
- The control handler also plays the demonstration from paired control and duration tables at `$3C6E/$3C8F`. Mode 2 fills these tables on input changes. These modes are traced in the handler at `$3BF3`.
- At Mission 1, the processor port is `$35` and the hardware IRQ vector is `$1E87`. A checkpoint at that instruction hit, and a single step reached `$1E88`. The handler acknowledges VIC status and selects its branch using the index at `$1ED3` and paired tables from `$1ED4`. The return path sets the next raster compare.
- At the masked graphics read `$1E17`, a trace stopped with the RAM bank selected (`$01=$30`), source `$CB00`, destination `$4000` and Y=2. Stepping the load returned `$98`, matching the source byte at `$CB02`. In other paths the wipe selects mission graphics at `$D000` or `$D800`.
- The 8×8 font starts at `$5000`. Glyphs 0–9 are digits. Glyph `$0F` is the two-dot separator, `$20` is blank, and `$21-$3A` give A–Z. Text templates at `$9722-$9860` store ordinary uppercase ASCII with position and zero terminator bytes. The renderer at `$9611` maps these characters to the custom glyph indices and copies the rows to text sprites.

## Stage timer

- From the same Mission 1 snapshot, 150 PAL frames produced 150 execution hits at `$261A` and three at the BCD decrement at `$2631`. The seconds and minutes bytes changed from `$57,$02` to `$54,$02`. The subsecond counter at `$2619` returned to `$29`.
- The routine uses decimal subtraction when its 50-call divider expires. Seconds underflow reloads `$59` and borrows one minute. A minute underflow writes the timeout outcome through `$2C/$27` and clamps both BCD bytes to zero. The panel renderer at `$2688` uses glyphs `$14-$1D` for the digits.

## Register census

| Registers | Uses traced in the listing |
|---|---|
| `$0001` | `$1907` selects the engine's RAM view. `$3F4B` and `$3F5E` alternate KERNAL-visible and RAM-visible memory during the disk transfer. |
| `$D011-$D012`, `$D019-$D01A` | `$1E48` sets the initial line and enables raster interrupts. `$1E8E` acknowledges the interrupt and `$1ECA` writes the next line. |
| `$D015`, `$D017`, `$D01D` | `$9889` turns off sprites and clears X/Y expansion after waiting on a message. |
| `$D022-$D023` | `$0B05` and `$0B0B` set stage colours from `$FCDD` and `$FCE1`. |
| `$D027-$D02B` | `$989E` sets the colours of the first five sprites while a message is displayed. |
| `$DC00-$DC03` | `$18D7` drives the keyboard matrix and captures input on port B. `$3B84` reads joystick port 2. |
| `$DD00-$DD02` | `$1922` writes VIC bank select for the playfield and captures values used for the serial clock. |
| `$D400-$D418` | The census locates indexed frequency, control and envelope writes near `$BD4D` and a volume write at `$BD26`. Individual effects and music remain open. |

The full register census, watch output and snapshot-derived glyph and sprite renders are in ignored `work/`. The findings above were collected during orientation and annotation. The step 60 listing sample and feature pass are pending.
