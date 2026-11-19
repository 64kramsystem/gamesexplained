# Wonder Boy analysis facts

Addresses refer to the Remember +10 April 2005 build, with the trainer
options left at their defaults. The title-to-play execution map,
`work/entry.vsf`, `work/play-live.vsf` and the named local traces support
this handoff.

## Boot, control and timing

| Claim | Evidence |
|---|---|
| Game initialization starts at `$082A`. | Execute checkpoint at the trainer exit. A store watch on the hardware IRQ vector stopped later at `$08E6`. |
| The game selects one- or two-player mode at its text title. | `$F737–$F760` draws title animation and checks the matrix selectors. F1 from the title produced the first round banner and then controllable play. |
| The main control poll merges keyboard and joystick signals before detecting edges. | `$24F3` tests the five mask pairs at `$2538`, ANDs the result with CIA1 port A, and compares the result against `$0635`. In `work/control-probe.txt`, a checkpoint at `$29B9` recorded `A=$BF` with neutral input, `$BE` with up and `$A7` with right plus fire. Jump and fire edge latches at `$7A/$7B` were respectively `00 FF` for up and `FF 00` for right plus fire. |
| Fire raises the jump-motion constant, while direction and fire affect separate branches. | Instruction stepping from `$29B9` gave the neutral/up paths `$20=$20` and `$8C=$28`. Right plus fire took the instructions selecting `X=$30` and `Y=$40`. The later jump path uses `$8C` at `$2B0A`. |
| An axe requires equipment and an unused projectile slot. | `$2D2C` checks `$7A` and `$0631`, then initializes one of the actors at offsets `$20` and `$30`. `$35BC` clears the projectile's active status on a registered hit, while `$35CE` changes its direction and speed. |
| F7 pauses main gameplay updates. | Matrix scan and release loop at `$3D00–$3D79`, pause flag at `$0661`, direct checks at `$0EBC` and `$F38D`. The bundled manual describes pause changes in this release. |
| A video tick drives the main-line waits and the SID driver. | `$10AD` calls vitality drain when enabled, sets `$6D`, and calls `$E003`. The wait at `$0D39` consumes 100 tick flags. |
| Vitality uses two bytes at `$73/$74`. | `work/cpu-trace.txt` steps `$F3B8–$F3CF` and observes `$5D78 → $5D70`. The alternate `$FB` path subtracts `$14` instead of `$08`. The `$006E` store watch stopped at `$F3CF` with outcome `$0B` after the neutral snapshot's vitality was set to zero. The meter at `$F33C` shows four high-byte units per full cell. |

## Level and actor data

- `$6B` is the round index, `$6C` the one-hot area mask. `$0C80`
  advances the round modulo four and shifts the area mask on wrap.
- `$1EC1` selects one 22-row layout per round. The sources are
  `$8000`, `$9090`, `$9749`, and `$9CE7`. Each row has
  a two-byte length and compressed cell stream. `$1DD8` sets up the
  row cursors and `$1C8A` advances them, writing the next right-hand
  cell and its color. A 128-byte color table follows each layout.
  Its high nybble is for even codes and its low nybble for odd codes.
- `$C300` selects the event streams at `$C30F`, `$C63B`,
  `$C8EF` and `$CB30`. Records have a little-endian X word, Y, type
  and area mask. The lists contain 162, 138, 115 and 144 records and end
  in `$FFFF` X sentinels. `$1F96` considers events ahead of camera X,
  filters on the area mask, then initializes an actor from the table at
  `$20CA`.
- `$2DDB` uses the type-indexed update table at `$35EA`. The render
  list builder at `$3715` picks visible actors, chooses one of four
  shape pointers per type at `$BCB2`, and obtains the corresponding
  color from `$BF8C`. The register reload code at `$1149–$1270`
  can reuse the hardware sprite slots in the same frame.
- `$23F2` initializes the seven main boss types `$77–$7D`.
  The first set area bit selects the shot interval at `$24E2` and
  a hit target of seven plus three per area after the first. `$393A` runs the boss phase machine,
  including the countdown and the hit threshold. These branches
  were traced from the dispatch table.

## Video, input and sound register census

| Registers | Role and representative instructions |
|---|---|
| `$00/$01` | Processor port DDR and bank selector. Startup and the live play snapshot establish the mapping described in orientation.md. |
| `$D000–$D010` | VIC sprite coordinates and X high bits. Initial sprite writes around `$1014–$106E`, with further writes via the raster reload entries at `$1149`. |
| `$D011/$D012/$D019/$D01A` | Raster setup, IRQ acknowledgment and handler chaining, initialized at `$082A` and updated at `$0D4B`, `$0DE5` and `$1101`. |
| `$D015/$D01C/$D01D` | Enable, multicolor and horizontal enlargement settings. Initialization at `$082A`, banner mask at `$0E71`, reload enlargement at `$115E`. |
| `$D016/$D018/$D021–$D023` | Playfield fine scrolling, character source selection and palette at `$0D58–$0D76`. Panel values restored at `$0DF4–$0E17`. |
| `$D025–$D02E` | Shared and per-sprite colors. The banner and the actor render paths set these, for example at `$0E3D–$0E64` and `$1080–$10AA`. |
| `$D400–$D418` | Three SID voices and filter/output controls. The music interpreter feeds them at `$E87C–$E8E7` and through its command table at `$E932`. The selector-dispatched sound effects use voice 3. |
| `$D800–$DBE7` | Cell color RAM. The game shifts playfield colors with screen codes in the unrolled `$1504` routine and writes the incoming color in `$1C8A`. |
| `$DC00/$DC01/$DC0D` | Port-2 joystick and keyboard matrix in `$24F3` and `$2542`. CIA1 interrupt acknowledgment at `$0D51`. |
| `$DD00/$DD02` | VIC bank bits and their DDR, set by the game initializer. |

The instruction census lists candidate indexed accesses as well as direct
ones. The exact captured table is in `work/census-final.txt`.

## Glyphs and text encoding

The VIC uses the bank beginning at `$4000`, with the matrix at `$4000`.
The split selects fixed panel characters at `$7000` and round characters
at `$7800`. `$F3D0` expands four round-specific streams from
`$AB1F–$BBD1` to `$7818–$7FFF`. The five marker values at
`$AB12–$AB16` correspond to runs of zero, `$FF`, `$AA`, `$55` or
an explicit byte.

| Panel screen codes | Glyphs |
|---|---|
| `$00–$07` | Meter fill and panel line shapes |
| `$10–$15` | P L A Y E R |
| `$16–$17` | Header digits 1 and 2 |
| `$19–$1C` | H I G H |
| `$20`, `$21`, `$2E`, `$2F` | Space, exclamation, period, slash |
| `$30–$39` | Digits 0–9 |
| `$41–$49`, `$4C`, `$4E–$50`, `$52–$57`, `$59` | A–I, L, N–P, R–W, Y |
| `$63`, `$6E`, `$6F`, `$72` | Lower-case c, n, o, r |

Title strings begin at `$C286`, `$C28C`, `$C294`, and `$C2A6`.
The copy at `$F244` clears bit 7 before display and uses the same bit as
the terminator. For example the `$A1` in the press prompt renders
`$21`. The glyph render is kept locally in `work/glyphs-7000.png`.

## Coverage probes

| Claim | Evidence |
|---|---|
| Startup overwrites the flagged contents in screen RAM. | A VICE store watch on $4009–$4253 stopped in the clear loop at $088F. The execute checkpoint at $0898 found $20 in the cleared cells. See `work/resume-probe.txt`. |
| Round setup briefly rewrites the actor release entry. | At $3E40 on the round-start path, single steps showed $30A8 change from $A0 (LDY) to $60 (RTS) and back to $A0. See `work/resume-round.txt`. |
| The final packed glyph stream ends at $BBD1. | The instruction and memory trace for $F3D0 ran all four round indices. The last stream read $B7D1–$BBD1. Each index wrote all bytes from $7818 through $7FFF. See `work/resume-cpu.txt`. |
| The signed clamp at $2DB9 branches on the incoming N flag. | The instruction trace tested both signs, the two in-range limits, and the adjacent out-of-range values. Its limits are $C1 (−63) and $3F (+63). See `work/resume-cpu.txt`. |
| Sound selector $19 reads its score through $EFE0. | The score parser resolved the phrase branches and a 3,000-call CPU trace of $EF30 reached a maximum score read of $EFE0. See `work/sound.py` and `work/resume-cpu.txt`. |

## Checkpoints, pickups and bonuses

- Round advancement at `$0C80` wraps the round index after four
  rounds and shifts the area mask. An instruction trace of the final
  transition took the branch at `$0C8D` when the mask became `$80`.
  That branch leads to the end-of-game path. The ending presentation
  remains open.
- The restart routine at `$0BDC` tests the four entries in the current
  round's world-X table at `$0C2D` in descending order. It writes the
  first entry at or behind the player's X to `$47/$48`. Instruction
  traces selected the third entry in each round at `$07E0`, `$07E0`,
  `$0800` and `$0800`, respectively. See `work/verify-features.txt`.
- Player contact at `$30C8` sets the axe flag. The pickup at `$334F` fills vitality to `$60F8`, and `$3367` adds a life and redraws
  the life icons. The routine at `$337B` sets the contact protection
  byte to `$FF`. These paths share the overlap test and release the
  collected actor slot.
- The egg handler at `$2F61` can dispatch the contents on projectile
  contact. A player overlap at `$2F74` assigns type `$3A` and starts
  the falling path. The contents initializer at `$2FBB` substitutes
  type `$3D` for `$72` or `$6B` when the player lacks the axe.
- The round bonus at `$F4FF` spends `$19` vitality subunits per
  iteration and adds to the packed-BCD amount at `$064B–$064D`.
  `$F550–$F5B9` pays the amount once, then pays it again when
  the item flag `$0660` is set. The second payout also includes
  a separate increment in Area 7, Round 4.
- Boss setup at `$23F2` clears `$066A` before using the area mask. CPU
  traces through `$2415` obtained hit targets 7, 10 and 25 and shot
  intervals 255, 208 and 64 in Areas 1, 2 and 7.
- A VICE store watch on sprite 0 coordinate registers stopped after
  `$1164` and `$116A`, confirming that `$04BD` supplies X and
  `$04CD` supplies Y in the first reload. The same invocation
  copied the shape pointer from `$04AD` to `$43F8`.
  See `work/verify-vic.txt`.

## Retained payload

The listing counts 54,703 bytes and has no uncounted stretches.
Boot store watches from `work/title.vsf` in `work/depack-watch.txt`
caught writes to the gaps later retained in the game image. They
include the small values beside the boss part handlers, the
tail after the four packed character streams, the sequence after the
boss badges, monitor material after the object list, and the bytes
after the last traced score. Their individual bounds and open
consumers are recorded beside the data in the listing.

The CPU trace in `work/range-consumers.txt` read six boss-badge bytes
per area from `$C2CB–$C2F4`. With the cursor at each object list's
`$FFFF` sentinel, the reader at `$1F96` fetched two bytes and
returned without advancing. The fourth sentinel is `$CE00–$CE01`.
The bytes after the sentinel include the depacked register heading
and command material, then an `$AA` run through `$CFFF`.

## The listing's error rate

An independent gpt-6.2-sol checker reviewed 65 of 938 comments with
seed 20261119. Fifteen contained errors and all fifteen were corrected.
They included swapped sprite arrays, reload masks, the terrain cursor
pointer, and inaccuracies in actor state and score comments. The
observed error rate was 23.1%, with a 95% Wilson interval of 14.5% to
34.6%. Weighting by the two sampled groups estimates 22.7%. The sample
does not measure the corrected listing and the checker may have missed
errors.
