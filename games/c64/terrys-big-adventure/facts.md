# Terry's Big Adventure technical facts

Evidence comes from `work/entry.vsf` and the targeted traces against the TNF build described in [orientation.md](orientation.md).

## Build and memory

- $6D00 jumps to $75F9, over a PETSCII dedication and the build identifier TBA C64 V1.0.
- $7631 writes $35 to the processor port. It makes RAM visible over BASIC and KERNAL and leaves I/O visible.
- $0400 and $0800 hold alternate screen matrices. $78DF zeroes both. $79F0 switches the visible matrix by toggling $30 in the $D018 shadow. Logical sprites use the same pointers in both matrices, at $07F8 and $0BF8.
- $4000 and $4010 are the low and high halves of the map pointer table. $B556 decodes to a page per tile row at $1000-$1B00. $FF ends a row. Other tokens below $80 copy themselves, and $80-$FE repeat the next byte by the low seven bits plus one.
- The filename table at $70BA begins with `STLEV1H` through `STLEVCI`, followed by other seven-byte names in eight-byte slots. $B61E calls the KERNAL LOAD after selecting a name from that table. The scene setup at $8410 calls $B556 instead. The three NOPs at $B3A3 precede the jump into that setup after a transition.

## Input and movement

- Title fire checks bit 4 of CIA1 port A at $7801. It clears the attract-demo flag at $7080, sets the life counter at $709C to five, and returns with carry set.
- In the live game $97C6 reads CIA1 port A and $97CD stores the inverted low nibble at $CA. With Right held on port 2, the trace showed A=$77 after the read, $07 after masking and $08 after inversion. The next instruction stored $08.
- $9858 increases or decreases the signed momentum at $6E1F by one on horizontal input, with limits of +96 and −97. An input opposing its sign enters $98AC first. That routine clamps it to ±26 and then moves it one step toward zero. Without horizontal input it takes the braking path when $6E83 is set.
- $9808 checks Up. A fresh eligible press seeds $6E27 with 7, extends it while held to the $10 threshold, and enters a decay path on release or at the threshold. The vertical update at $7AD4 uses that index into $71A3 and subtracts the table value from player Y. The player Y write is at $7AE8 on this path.
- $7A8B adds the camera delta to fine scroll at $BC. Crossing 8 requests a matrix swap and increments the character subcolumn $B4. Crossing three subcolumns increments the map column $CB. $7D04 reads the new map column one tile per row and emits two cells for each tile.
- $98E5 reads active-low fire. $98DB checks transition flags and a weapon-active flag before it launches. $6E08 selects the rock path, which decrements the count at $6DF5 while it is nonzero. $9986 advances the active weapon. $906C checks the weapon against several tables of active objects.

## Raster and sound

- A PAL frame from Scene 01 lasted 19,656 CPU cycles. The write trace in `work/play-frame.json` captured $8EC5 installed for the line-$F2 bottom interrupt, $797C restored during the bottom interrupt, and $8ACB restored by the frame handler. Execute checkpoints over 60 frames counted 60 hits at $797C, 300 at $8ACB and 60 at $8EC5.
- $8801 transforms logical object positions to values used by the sprite scheduler and stores the band for each at $D0-$DF. $8ACB writes the physical sprite slot next in the rotation. The band handler starts at line 42 and schedules subsequent interrupts at increments of 40 lines, with the bottom handler at line 242.
- $797C increments the frame tick at $A2. $7910 waits for a requested number of ticks through a wrap-safe equality test on that byte.
- $7F9C calls the timer subtraction every fifteenth eligible invocation. $7FB4 borrows across three decimal digits. Timer underflow sets the transition flags at $6EDC and $6EDD.
- $7F4C stores digit glyphs 0 through 9 as ten sets of eight rows. $7FE6 copies a glyph into one byte column of the HUD sprite, spaced three bytes apart per row. The sprites and character data use custom graphics. No full text alphabet is implied by the digit table.
- $CD8F selects music by loading three pointers from six consecutive bytes at $CD71 plus Y. $CDD0 advances the SID sequence from $797C if $9C is nonzero. In voice 1 a zero advances to the next pattern and $FF restarts the selected sequence. The routine writes the frequency high byte to $D401 and low byte to $D400.

| Register | Role | Instruction evidence |
|---|---|---|
| $01 | CPU banking | $7631 |
| $D000-$D00F, $D010 | Physical sprite positions and X high bits | $8AE3, $8AE8, $8AFD |
| $D011, $D012 | Display enable and line used by the raster scheduler | $79BD, $79C8, $8EAF |
| $D015, $D018 | Sprite enable and alternate screen matrix selection | $7996, $79FD |
| $D016 | Fine horizontal scroll and multicolour mode | $79B1 |
| $D019, $D01A | VIC IRQ acknowledgement and mask | $79DB, $B8AD |
| $D020-$D023 | Border and playfield colours | $7731, $799C, $79A2, $79A8 |
| $D025-$D02E | Shared multicolour and per-sprite colours | $82A1, $8B0A indexed |
| $D400-$D418 | SID frequency and control, and volume | $CDF6, $CDFC, $7712 |
| $DC00-$DC01 | Joystick port 2 and keyboard matrix | $97C6, $7719-$771C |
| $DC0D | Disable and clear CIA1 interrupt sources | $B8B2, $B8BA |

## Live tests

The stopped Scene 01 baseline had X=$0044 and Y=$A0. In 12 neutral frames, twelve execute hits at the direction read and twelve store hits at each position byte left X and Y unchanged. Right for the next twelve frames moved X to $004A. Up for twelve more frames moved Y to $79 while the previous horizontal momentum was still in effect. These tests use checkpoints on executed instructions and memory accesses. The local scripts and their output are in `work/probe.py` and `work/probe.txt`.

## Map streams

The row decoder was run against the bytes of all fourteen entries. The twelve regular streams give 255 tile IDs per row. Alternate entries $0C and $0D give 174 and 130 tile IDs per row respectively. The decoder advances the destination by a full page even for the shorter rows.

At $8339, a diagnostic set the normal scene index or alternate selector and let each setup continue. For all fourteen selections, execute at $B556, read at the selected stream's first byte and store at $1000 each counted one hit. Execute at $B61E counted zero in these tests. Scene 09 and the later streams read from RAM under KERNAL. The scene reference shots come from those tests. The alternate selectors establish how their maps initialize, with the conditions for entering the secret scene still open.

## Collision and pickup dispatch

- The lookup at $74F9 has 128 two-byte entries. $8FA8 doubles the tile byte to select a handler and turns high-bit map values into tile zero. $9C28 rewrites the destination of its own JMP and sets X to zero to identify Terry. The object version at $9C39 preserves X.
- The targeted trace replaced the tile at the first collision read, then followed its dispatch one instruction at a time. Tile $01 entered $73F1 and set carry. Tile $0A entered $73F3, reached the test with within-row offset 7 and incremented $6EDC at $7406. Tile $7E entered $B907 with the diagnostic prerequisite $1EF6=$08 and changed $6DF4 from zero to one at $B91C.
- $B92C advances that secret-entry countdown and selects map $0D. Tile $7B dispatches to $B961, which clears the alternate selector and restores the saved return column. $B374 selects map $0C after progressing the regular scene.
- $9EC1 marks a consumed map byte with bit 7. $9E33 adds one to four time units. $9DE3 requires Down before consuming its tile and incrementing the rock count.
- In separate instruction traces from the same Scene 01 baseline, Up at $9822 set $707E and $6E27 to 7. Fire at $9915 branched past rock setup with $6E08 clear. With diagnostic values $6E08=1 and $6DF5=2, the same input selected sprite pointer $91 and decremented $6DF5 to 1 at $9930.

## Life, score and display assets

- A collision with pickup sprite pointer $DB reaches $9614. The routine adds eight to $6DCE and, on reaching $28, increments $709C, redraws the life count and clears the accumulator. This takes five such contacts when starting from zero.
- The frame capture read $D018=$2F. The corresponding alternate configuration is $1F. Both point to the $3800 character set in VIC bank 0. At entry, renderable sprite graphics occupy $0C00-$0FFF and $1F80-$37FF. The title is assembled from pointers $35 through $38. Game Over uses $39 and $3A, and Bonus Scene uses $3B and $3C.
- The tile character table at $1C00 uses six character codes per tile arranged in two rows of three. $7D04 applies the selected subcolumn to both character rows. $8685 also changes some tile colour entries per scene.

## Retained data

The handoff contains a screen-shaped 1 KB block at $D000 beneath the I/O registers. Rendering its 40-column rows with the playfield font reveals repeated tile patterns. The tail at $D3F8 is byte-identical to the title's live sprite pointers at $07F8 and $0BF8, including $38,$37,$36,$35. The frame capture uses VIC bank 0, with $D018 selecting the normal matrices. The role of this retained matrix in the original build is open. The data near the old buffer-comparison helper at $CED9-$CFFE is labelled by structure and location. Its reader is open.

## Listing sample

The fixed seed 191106 selected 60 of 656 comments before the corrections. An independent `gpt-6.2-sol` checker flagged seven wrong details, all confirmed against the instructions and fixed. The sample estimate was 11.7%, with a 95% Wilson interval of 5.8% to 22.2%.

The corrections cover the life-loss counter and score-tally flag at $6EDC, the two phases of the $A00F sprite sequence, the RTS at $AB61 before the movement bytes, the direction-dependent tile probe at $B285, the ground-contact condition at $B8BE, the pre-increment comparison at $B92C and the per-slot branches at $BCBD. The local verdict file records the exact sample text and the evidence for each finding.
