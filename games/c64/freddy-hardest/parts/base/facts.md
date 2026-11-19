# Base

The prompt at `$0BB8` waits on `$1137`. `$101D` iterates
ten keyboard-matrix indexes at `$1146`, stores the digit's glyph
at `$1140` plus the current digit position, and waits for release.
`$0FF4` checks for position 6, then compares offsets 1–5 against
`$113A`. It sets `$1137` to 1 on a match. The mismatch path
writes zero to `$1139`. Code `25425` is stored as glyph bytes
`66 69 68 66 69` at `$113B`. The glyph map shared with the
surface title has A–X at `$4C–$63`, 0–9 at `$64–$6D`
and Y and Z at `$70` and `$71`.

The live store watchpoint on `$1137` hit once after entering
`25425` via the matrix. VICE stopped at `$1010` after the
instruction at `$100D`. X and the stored value were 1.
The simultaneous raster checkpoint at `$1055` also hit once.

## Base floors and ship interface

`$BBF2` selects each floor's tile and glyph data. `$B6E4`
reads two column IDs from the course cursor at `$3A68–$3A69`,
then adds two to the cursor. `$B749` converts each ID into an
8-byte tile-column address. `$B907` draws the two bands of the
initial room from 40 pairs. The two display pages at `$4000` and
`$4400` get their scene from scratch RAM through `$BA19`.
The four entering-edge routines are `$B78B`, `$B7EA`,
`$B849` and `$B8A8`.

| Floor case | Glyph source | Column dictionary | Course table bounds | Setup |
| --- | --- | --- | --- | --- |
| 1 | $E000 | $2AF8 | $1352–$1942 | $BC0D |
| 2 | $E800 | $2DE8 | $1A52–$1E6E | $BC76 |
| 3 | $E000 | $2AF8 | $1F52–$2224 | $BCDF |
| Other | $F000 | $30A8 | $2352–$2438 | $BD48 |

The reverse reader at `$B710` subtracts 82 bytes before fetching its
pair. In isolated traces with the cursor set to each forward start,
the loads at `$B729` and `$B72F` both triggered the watchpoint on
the first pair of that floor's prefix. The pairs read at `$1300`,
`$1A00`, `$1F00` and `$2300` were `32 22`, `06 10`,
`2C 06` and `1E 1B` respectively. Each prefix contains 41 pairs.

The routine at `$B52D` shifts 39 source cells one place to the
right per row. It includes destination offset 40. In an isolated
trace with the row pointer at `$4400`, the store instruction at
`$B532` triggered the watchpoint at `$4428`. The separate player
frame routine at `$8583` stored `$7B` and `$7C` at
`$3A20` and `$3A21` when stepped with X set to `$7B`.

`$A119` matches the map cursor to one of four pairs in
`$ACB3` and `$ACB7`. `$A60C` dispatches the ship readiness
checks and checks the selected ship's hyperspace and energy-cell
flags. `$A94B` chooses a message screen address from row and
column variables. The glyph strings from `$AE0A` contain separate
ready and not-ready messages, a captain-code prompt, choices for
Artex, Fenix, Borax and Audax, and successful and unsuccessful endings.
The relation between each physical terminal, collected item and
all relevant state bytes is open.

The location selector at `$A5D7` uses the low course-cursor byte.
The code maps `$50` and `$52` to 0, `$9E` and `$A0` to 1,
and `$EC` and `$EE` to 2. Other values select 3. Isolated store
watchpoints on `$3BD3` confirmed the outputs for `$50`, `$A0`,
`$EE` and `$08`. The response printer adds `$3BD5` as a column
offset, adds `$3BD4` rows of 40 cells, and stops after `$3BD6`
characters.

In an isolated sprite update at `$CF1E`, the store at `$CF32`
copied frame pointer `$7B` to `$47F8`. In separate audio tests,
the load instruction at `$B143` read the streams at `$9D40` and
`$9E0C` after the voice-one and voice-two initializers respectively.

## Register census

| Hardware | Evidence |
| --- | --- |
| CPU port $01 | $800B–$800D clears LORAM. $BA70 temporarily banks out the KERNAL to copy eight pages of floor glyphs to $4800. |
| CIA1 $DC00–$DC01 and $DC0E | $CAF8 rotates a keyboard column select and reads back port B. $CB9B reads port 2 from port A. $CBAA stops CIA1 timer A for raster-driven play. |
| CIA2 $DD00 and VIC $D018 | $81E9 selects the $4000 VIC bank. $BDAC selects the first screen page. The raster handler at $CBD0 selects which phase adjusts the screen and sprite state. |
| VIC $D011–$D012, $D019–$D01A | $CBA4 installs raster-driven play at $CBD0 and $C0CC schedules the phases from $C98B. |
| VIC $D016 | $CD70 and $CDC2 set the horizontal scroll value from $CFA3. |
| VIC sprites and collision latches | $CF1E and $CF5E copy sprite states and frame pointers. The phase starting at $CBEE samples the VIC collision registers into the game state. |
| SID $D400–$D418 | $AFB8 flushes the SID shadow from $3A49. $AFAE calls the three voice update routines. |
