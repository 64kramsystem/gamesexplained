# Mouse Trap facts

All addresses refer to the C64 ATC / Brute Force build after selecting
Normal. The listing image is `work/entry.vsf`. Measurements below use the
headless VICE MCP build and refer to CPU instructions or memory
watchpoints unless otherwise indicated.

## Boot and address space

- The trainer transfers execution from `$0938` to `$8E00`. A stopping
  checkpoint at the target captured the unpacked game before it wrote
  its first register. Startup at `$8E0C` sets the port register to
  `$05`. It then fills `$FF00-$FFFF` with RTS opcodes and installs
  vectors at `$FFFA/$FFFB` and `$FFFE/$FFFF`. It writes a jump to
  `$8F29` at `$FFEE` for its own character output.
- In the sampled 800 frames through title and the first room,
  the breakpoint at `$8E99` counted 956 IRQ entries and a store
  watch at `$0001` counted one store. That store is the startup write
  at `$8E13`. The observed CPU port remains `$05` in gameplay.
- The game consumes one packed PRG. The active room offsets point into
  the resident stream and the graphics, music, and title art have
  resident sources. There is no separate room load in the room builder.

## Controls and movement

- `$1414` switches CIA1 data direction A to inputs. Stepping the
  `LDA $DC00` at `$1419` gave A=`$FF` with the joystick neutral and
  A=`$EB` with left and fire held on port 2. Both tested lines are
  active-low.
- In player mode `$13A1` shifts off up and down and looks up the two
  horizontal bits in `$13D5`. The table holds `00 01 FF 00`.
  `$12A4` uses the selected signed increment and rolls the move back
  if the candidate coordinate falls outside its interval.
- `$12F7` checks the fire latch and current vertical motion before
  starting a jump. A jump enters the motion path at `$12DD` with
  action `$08` and comparison limit `$12`. Vertical increments come
  from `$0C20`. When landing, `$131E` compares the candidate landing
  position with the saved previous vertical position and sets failure
  when the difference reaches the configured limit. The branches
  distinguish different falling or landing conditions.
- Actor contact is tested at `$16B5` using the coordinate arrays and
  the collision fields of the actor shape records. Its later tests
  distinguish contact with supported actors, activation of a hanging
  actor, room completion and death. Graphics are XORed into the
  bitmap at `$1B00` and scheduled relative to the raster at `$3C04`.

## Rooms, collectibles, and counters

- `$3600` contains 22 little-endian offsets from `$2000`. The game
  begins at index 21 and decrements the index at `$1906` after a
  successful room. The complete C64 room stream spans
  `$2000-$26AB`. The room loader at `$18A3` returned for all 22
  indices when called via a checkpointed VICE trampoline. The
  read watch over that span counted 1,813 reads. A corresponding
  read watch over `$26AC-$26FF` had zero hits.
- A room header contains a tile-list index, two palette bytes, a
  spawn byte, and an actor count minus one. Each six-byte actor
  record supplies position, motion endpoints, packed cadence and
  type, and flags. The actor list is followed by a byte count and
  that many bytes of packed tile codes. The decoder uses the two
  nibbles and interprets a zero tile nibble as a run marker.
- In room index 21 the instruction at `$177A` was reached with
  Y=`$5C` and base pointer `$2600`. `$171B` received Y=`$60`,
  the position of the actor count field. The tile count read at
  `$11B7` was `$32` at `$2679`. The loader returned with the stream
  at `$26AC`, immediately after that room.
- `$123A` increments the room's collectible count at `$6D` when
  it encounters the collectible tile code. On contact with the
  resulting `$FF` cell, `$17AD` removes it, adds four to the score
  and decrements the count. On zero, `$17EC` finds the exit tile
  `$07` and sets it to `$F7`. The exit contact path signals room
  completion through `$98`.
- `$1BD8` runs the timer strip by decrementing a subdivision and
  erasing a mark on its expiry. The last mark sets room failure.
  `$18CF` loads five lives under the Normal option. `$1A7B` adds
  to decimal score digits, redraws the score, and awards a life
  when the digit watched at `$0CF3` changes.

## Video, text, and audio

| Register or region | Use | Code |
|---|---|---|
| `$00/$01` | Set port directions and retain I/O with both ROMs out | `$8E0C` |
| `$DD00`, `$DD02` | Set VIC bank bits to select RAM at `$4000-$7FFF` | `$8E3F` |
| `$D011`, `$D012` | Set bitmap mode and measure the raster for object painting | `$8E51`, `$3C23` |
| `$D016`, `$D018` | Enable multicolour and select the bitmap at `$6000` and screen matrix at `$5400` | `$8E59` |
| `$D020`, `$D021`, `$D800-$DBFF` | Set border, background and colour RAM | `$8E39`, `$8EB7`, `$9174` |
| `$D400-$D418` | Initialise SID, apply note and filter updates, or play a seven-byte voice-three effect | `$8E7B`, `$A2FC`, `$3403` |
| `$DC00-$DC03` | Read the joystick and scan the keyboard matrix | `$1414`, `$9122` |
| `$DC0D` | Acknowledge CIA1 interrupt | `$8EAE` |

- Title drawing copies `$E000-$FCFF` to `$6000-$7CFF`, and
  `$9800-$9AFF` to `$7D00-$7FFF`. Stepping the first source
  read at `$91A4` and destination write at `$91A6` showed
  `($B0),Y = $E000` and `($B2),Y = $6000`. The title watch
  counted 7,428 reads in the high bitmap range over the sampled run.
  The matrix bytes come from `$5000` and the title's colour RAM
  bytes from `$9400`.
- The bitmap printer at `$8F29` interprets controls and grows each
  eight-row one-bit glyph into a 16-byte multicolour cell. The font at
  `$8A00` begins at character code `$20`. The rendered sheet in
  `work/font.png` shows digits at `$30-$39`, upper case at
  `$41-$5A`, lower case at `$61-$7A`, and line and corner shapes
  above `$7A`. Blank cells are kept in the font. The rendered cells at `$22`, `$27`, and `$2E` contain
  a low dot, an apostrophe, and a period respectively. The title text and initial high-score records are stored
  at `$0F5E-$1061`.
- The title SID player reads its stream bases from `$A245`.
  The byte at each base is skipped by the reader's initial increment.
  A zero event loops, a negative event selects a SID register and
  consumes its new value, and a positive event selects a duration and
  waveform and consumes a pitch byte. Voice three writes are disabled
  in the title configuration. Gameplay effects update voice three
  using the presets at `$3441`.

## Loaded bytes outside the main engine

- The $0B46 cue reader was adapted from the BBC Micro release. That
  release calls OSWORD 7 after preparing a command. The C64 routine
  omits that call and its cue area at `$3300` starts with `$FF`,
  while the later sequence from `$3334` is zero-filled.
- The sixteen bytes at `$0C00` match the corresponding MOUSE2
  bytes on the BBC disk. The first 80 bytes beyond the C64 room
  stream match the TRAP3 tail at BBC address `$2FAC`. Other RAM
  keeps BBC BASIC testing text and assembler fragments. The C64
  listing identifies these retained bytes separately from live code.
- `$C700` starts an earlier loader which copies staged pages from
  `$A700` to `$E000`, clearing the source. The sequence recurs in
  the high-memory staging bytes. A store watch on `$C800` hit
  the second-stage relocator store at `$082D` and then the unpacker
  store at `$009D`. The monitor reported the following instructions,
  `$082F` and `$009F`, with the I/O window banked out. Stores watched at
  `$D100`, `$D400` and `$DFB0` hit the same unpacker.
  Resident read watches over `$C700-$CFFF` had zero hits through
  the title, first room and the 22 room loads. The VIC bank selected
  by the game cannot fetch from that range. The high RAM below
  visible I/O is excluded with the loader residue.
- The block at `$4700-$47FF` is a detached byte sequence preserved
  by the loader. A write watch caught the final store from packer
  code at `$009D`. The actor frame table has no source in page
  `$47`, and separate watches over the block heard no read in the
  title, the sampled gameplay, or during any of the 22 room
  initialisations. Its original purpose is an open question.

The comparison disk is [Mouse Trap, BBC Micro Games Archive](https://bbcmicro.co.uk/gameimg/discs/641/Disc036-MouseTrapTynesoft.ssd).
The second C64 distribution and the matching ATC T64 came from
[Mouse Trap, C64Games](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=5732).

## Instruction checks

- From the first-room snapshot, set the fire latch and clear vertical
  motion, then call `$12F7`. The checkpoint at `$12DD` saw
  A=`$08` and X=`$12`. On return, `$74` and `$78` held `$08`
  and the duration threshold at `$6C` held `$12`.
- Set the remaining collectible count to one and call `$17AD`
  on a `$FF` cell with a neighbouring test exit cell at `$07`.
  Stepping the stores at `$17B3` and `$17FA` produced `$00` in
  the collectible cell and `$F7` in the exit cell. The count was zero.
- Set the timer and its subdivision to one before calling `$1BD8`.
  Stepping `$1BE6` showed the timer storing `$01` to `$98`.
- The game loop reads `$EC` at `$19D9` and tests literal
  values for its wait, sound gate and forced outcome paths.
  A live C64 producer for `$EC` remains open. The keyboard
  scanner confirmed in the code at `$9122` is used by the
  high-score editor.
- These are controlled instruction probes. Step 65 had no recorded
  route, port comparison or solution to perform.

## The listing's error rate

The sample with seed 5031 drew 60 of 307 comments. The independent
`gpt-6.2-sol` checker found eight incorrect details. All eight were
corrected. They concerned frame pointer and height-offset selection,
the cached score digit, the partial room stream copy, the source of
room and ending graphics, and the width of a SID workspace field.
The observed rate was 13.3% with a 95% Wilson interval of 6.9% to
24.2%. Weighted by the two sample groups, the estimate was 18.6%.
The checker may have missed additional errors. A full audit is
recommended for a later run.
