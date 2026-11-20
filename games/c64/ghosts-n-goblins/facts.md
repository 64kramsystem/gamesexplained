# Ghosts 'n Goblins (C64) — facts

## Edition and loaded bytes

The PAL Elite disk presents a loading picture before the game. The five
numbered loads belong to one resident gameplay image. The bootstrap's
KERNAL LOAD helper at `$02E5` increments the filename suffix at
`$0303`. The disk directory accounts for the active load chain, and the
orphaned bootstrap chain at track 12 sectors 3 and 13 is a separate copy
outside it. The addresses and byte comparisons are in `orientation.md`.

| Address | Role and evidence |
| --- | --- |
| `$0850–$3435` | Gameplay, screen, score and raster routines with interleaved tables. The first executed game instruction is at `$0850`. |
| `$3436–$35A9` | Raster masks, then the handler pointer, camera, sprite slots, encounter flags and player state written by the engine. |
| `$3800–$3FE8` | Music initialization and two sets of three voice orders and phrase streams, selected by `$3800` and `$3B14`. |
| `$4000–$BFFF` | Tile grid of 128 rows of 256 bytes. The viewport copy at `$2F3F` reads 40 columns for 19 rows. Collision at `$2653` uses the same grid and looks up the resulting code at `$2E2A`. |
| `$C000–$CFCF` | SID shadow state, music interpreter, gameplay effect mixer and scripts. Main tick `$C9B1`. |
| `$D000–$F3FF` | Relocated sprite images under I/O and KERNAL. The title's logo shares the lower part of `$F000` with glyph addresses. |
| `$F400–$F7FF` | Runtime screen and hardware sprite pointers. Scene setup at `$297A` writes all displayed cells, and the raster writes the pointers at `$F7F8–$F7FF`. |
| `$F800–$FFF7` | Playfield character generator and the overlapping upper sprite images. Two copies of an animated glyph at `$FFE0` and `$FFE8` are exchanged by `$3261`. |
| `$FFFA–$FFFF` | Processor vectors once the game's setup at `$31A6` installs them in RAM. |

At the loader handoff, `.4` and `.5` match in full at their PRG
addresses. The executed copy loop at `$7148–$718E` moves 12,280 bytes
from the start of `.3` into RAM under I/O and KERNAL. The destination
matches all 12,280 source bytes.

The listing uses the handoff snapshot for authored bytes. The gameplay
snapshot is the second image for the uncounted-data check. The ledger
excludes the VIC's generated screen and system output, zero-page
workspace, and two bounded music and effect tails. The stage-start
padding probes placed non-stopping execute, load and store checkpoints
over `$2C1F–$2C22`, `$35AA–$37FF`, `$3FE9–$3FFF` and
`$CFD0–$CFFF`. None hit in 120 frames of each stage entry, while the
control at `$3448` accumulated 559,487 hits. The four-byte ladder gap
follows the unconditional jump at `$2C1C`. The nearest indexed
references that could reach it would require indices above their actual
limits. The workspace tail follows the last addressed name editor byte
and repeats the captured RAM fill pattern. Phrase and effect pointers
and termination delimit the two audio tails.

## Display and raster

The game leaves processor port `$01=$35`, with chip I/O visible and
KERNAL and BASIC banked out. The VIC reads bank `$C000`. The hardware
IRQ at `$31E5` saves registers and jumps through the address at
`$3446`. A captured graveyard frame measured `$D018` writing `$DE`
at raster 48 and `$DC` at raster 201. The 19 playfield rows and the status panel share screen RAM at `$F400`
while the character base switches from `$F800` to `$F000`. The
raster handlers at `$32FE` and `$33A2` assign ordinary sprites in
sorted Y order and can reuse hardware slots lower down the display.
`$31F1` switches to the status panel and increments `$3448`, which
the main loop polls at `$319D`.

| Register | Use in the game |
| --- | --- |
| `$01`, `$DC0E` | `$31A6` disables CIA1 timer A and exposes RAM vectors. |
| `$DC00` | Active-low port 2. Title fire at `$0ED2`, directions at `$2C5C` onward, fire at `$26C9`. |
| `$DD00`, `$DD02` | `$2929` sets CIA2 bank-select lines as outputs and selects VIC bank `$C000`. |
| `$D000–$D010`, `$D027–$D02E` | Logical actor X, Y, X high bits and colour written by `$32FE` and `$33A2`. `$3243` reuses sprites for lives and weapon. |
| `$D011`, `$D012`, `$D016`, `$D018` | Raster scheduling, fine scrolling, display geometry and character-memory selection in the raster chain. |
| `$D019`, `$D01A` | IRQ acknowledge in the raster handlers and raster enable at `$31D2`. |
| `$D015`, `$D017`, `$D01C`, `$D01D` | Sprite enable and multicolour at `$2945`, sprite expansion cleared at `$0861`. |
| `$D01B` | Tile-driven sprite/background priority selected by the terrain check at `$2D87`. |
| `$D020–$D023`, `$D025–$D026` | Border and background set in the scene setup. Shared sprite colours initialized at `$294D` and `$2952`. |
| `$D800–$DBE7` | Background colour rows filled through `($FB),Y` at `$29CC`. |
| `$D400–$D418` | `$C2F8` writes note frequency, pulse and envelope fields. `$C31D` changes the music gate. `$CAFA` can take over SID voices 1 and 2 for gameplay effects. |

The original `.3` graphics use VIC 64-byte sprite slots for 21 rows
of three bytes. The sprite image formula is `$C000 + 64 × pointer`.
The game uses sixteen logical slots, with slots 14 and 15 for the
weapon and Arthur.

## Text

Rendered glyphs at `$F000` identify the panel and name-entry alphabet.
The glyphs `$58–$61` are 0 through 9, with 0 also serving as O.
`$62` is colon, `$63` copyright, `$64` erase, `$65` ED, and
`$66` space. `$67–$74` are A through N, and `$75–$7F` are P
through Z. The panel labels at `$2B08` and title text in the first 40
columns of rows `$6400–$7600` use this alphabet. The name-entry at
`$0B88` uses `$FF` for a new row and `$FE` for the end of the grid.
The default names at `$0D30` are CHRIS, MUSICMAN, ELITE, CAPCOM,
ALISTAIR, DAVE and KAY, followed by a blank slot.

## Gameplay and state

- **Start and retry.** Port 2 fire leaves the title at `$0ED2`.
  `$087E` installs five lives. `$08B0` redraws the stage, uses its
  restart X/Y from `$3595–$3597` and resets the timer to 2:59.
  `$1FFB` replaces those restart coordinates when the camera enters a
  midpoint marker's window. The life-loss branch at `$0936` retains
  the restart coordinates. On the final life, the score is ranked and
  the game returns to the title.
- **Stage map.** The internal stage byte is `$3536`. Setting it to
  0 through 3 and entering the game's setup at `$08AA` selected map
  origins `$4000`, `$AC00`, `$5200` and `$7D00` at the first
  `LDA` at `$2F5A`. The instruction step advanced to `$2F5D`
  with A equal to the map byte at origin plus 39. Stage entry screenshots
  show the graveyard, ice palace, clouds and labyrinth.
- **Input and collision.** `$2BAA` chooses the path for Arthur's
  state. The ground path at `$2C54` takes port 2 horizontal motion
  and interprets up according to the ladder tile above him. The down
  path at `$2CED` checks for a ladder below, and crouches otherwise.
  `$2653` converts the proposed position to a tile and reads its
  flags. Bit zero marks solid ground, bit one ladder and bit two can
  put sprites behind the surface.
- **Combat.** Fire at `$26C9` is latched at `$352C`. The selected
  weapon `$3528` supplies velocity, sprite and colour, or selects
  the alternate update branch through `$269E`. The projectile overlap
  at `$1085` normally consumes it while the shield, index 5, survives.
  Overlap in `$1030` first compares X-page flags, then uses X and Y
  windows. The two crouch poses tighten the upper Y test. Contact with
  a harmful actor at `$1129` changes the frame base from `$40` to
  `$80` and sets the grace countdown at `$3592` to `$96`. A later eligible
  contact increases the base to `$C0` and `$2DEC` leads to the death
  state.
- **Encounters and exit.** Stage-indexed pointers at `$1DAC` choose
  X, Y and type arrays. `$1E02` scans visible entries and dispatches
  their initialization using `$1FAA`. `$1902` releases jars when
  the parent breaks and chooses a bonus or the next weapon on landing.
  Boss key spawn at `$1B23` is followed by collection at `$144B`.
  `$2C23` takes Arthur right with the key and sets the advance flag.
  `$091E` advances four stage indices, then calls the rescue at
  `$0DA1` and returns to stage one.
- **Score.** The packed-decimal score at `$3598–$3599` is drawn in
  hundreds and `$0F88` adds a life when the high byte rises to five.
  `$0949` inserts qualifying scores in order and moves each name
  together with its score. `$0C01` handles letter entry, erase and ED.

## Sound

The music orders at `$3875` and `$3B4E` go with high-score name
entry and the main score. Each holds a sequence of 16-bit phrase
pointers for each SID voice. `$C5B4` loops the order when it sees a
zero high byte. Notes contain duration and packed octave/pitch bytes.
`$C74F` decodes control events from `$C8` upward using the command
table at `$C793`, while `$C635` selects temporary instrument
sequences through the separate table at `$CA0C`.

Gameplay writes effect numbers to `$CAF2`. The mixer at `$CAFA`
doubles the number to look up a little-endian pointer at `$CC20`.
The eleven nonzero script entries use a header with a timing byte,
envelope and pulse settings, optional filter and second voice settings,
then control/frequency events terminated by `$FF`. The last script
begins at `$CF73` and stops at `$CFCE`. The emulator ran with dummy
audio, so this pass checked instruction paths and register use.

## Live checks and limits

- **Controls.** From the same play snapshot, execution stopped at
  the call at `$08E6` to set or release port 2 input. At the next
  instruction checkpoint at `$2E1E`, idle left both requested
  velocities zero. Right and left set X to 1 and −1. Up set Y
  to −4 and entered the airborne path. Down selected pose `$11`
  with zero motion. On fire, a store watchpoint on `$34B0`
  stopped at `$2709`, after the projectile type was set to 1.
  The ladder branches are traced from their tile probes. The
  controlled graveyard start supplied ordinary footing.
- **Timer.** Over 150 idle PAL frames, execute checkpoints at
  `$31F1`, `$0F28` and `$0F32` hit 149, 150 and 3 times.
  The displayed units went from 2:58 to 2:55 with the prescaler
  unchanged at `$1A`. The display and gameplay interrupts resume
  from the snapshot's existing raster phase, so use gameplay
  update counts when timing the clock.
- **Armor.** A controlled overlap at the entry of `$1129` used a
  harmful actor and Arthur at the same X and Y with the damage latch
  clear. A store watchpoint at `$3527` stopped at `$116B` with the
  frame base changed from `$40` to `$80` and `$3592=$96`.
  The death path and the retry through `$0936` follow from the
  listing and the armor base test at `$2DFB`.
- **Music commands.** With the track pointer at `$3C76`, controlled
  calls to `$C74F` with `$D3` and `$D4` reached `$C8D6` and
  `$C8D7`. Store watches at `$C000` and `$C01F` showed both
  clearing voice one's bit. The pointer was `$3C76` at the return
  from `$D3` and `$3C77` from `$D4`. None of the 24 indexed
  phrase streams decodes a `$D3` event.
- **Two-sprite mouth.** The initializer at `$22F5` adds 16 to the low
  X byte and copies the parent's high-X flag unchanged. At low
  X `$F8`, that wraps the follower to `$08` in the same X page.
  Its allocation call at `$2325` can also return Y=`$FF`, which
  the following indexed writes use directly. These are instruction
  outcomes for controlled states. Normal-play reachability is open.

The live probes and their output are in `work/`. Stage probes enter
setup directly and capture the mechanics at their instruction entries.
There is no route, port, or demonstration recording in this analysis.

## The listing's error rate

Seed 54221 drew 60 of 613 comments, checked independently by
`gpt-6.2-sol`. The lead confirmed 18 wrong details and corrected all 18.
The raw estimate on the sampled revision is 30.0% with a 95% Wilson
interval of 19.9%–42.5%. Weighted by stratum population it is 33.4%.
The sample found omitted conditions in the actor and music paths,
and overbroad music-phrase template wording. All 24 phrase comments
now use event counts and terminators parsed with the command lengths.
The checker may have missed errors. This sample measures the listing
before those edits.
