# Flimbo's Quest technical facts

The [resident engine](parts/engine/facts.md), the seven stage overlays and the [ending](parts/ending/facts.md) have separate listings. Details below refer to the disk release named in [orientation.md](orientation.md).

## Disk and banking

| Address or range | Use and evidence |
| --- | --- |
| `$02A7` | Pre-load filename index. `$7737` adds ASCII '1', patches `$778E` and increments the index after the load. Stops at `$215D` confirmed `1.*` through `8.*` and resulting indices 1–8. |
| `$76D4–$7746` | Stage loader wrapper. Saves zero page, suppresses display and audio during transfer, then restores the game workspace. |
| `$9080–$BFFF`, `$CA00–$FFF7` | Stage payload ranges. The monitor write map and before/after snapshots show the replaceable spans. The RAM beneath I/O was verified with stage-two write watchpoints at `$DFFF` and `$D000`. Both stopped just after the store at `$759F`, with the port's banking bits clear. |
| `$9080` | Entry point for the ending overlay. The transition at `$2166` checks for load count eight before reaching the call at `$2170`. |

For stage two the five stream header bytes at `$FB–$FF` were `F0 00 C0 05 0E` at `$7673`. At the decoder exit `$7638`, the output pointer in `$FC/$FD` held `$9080`. The loader uses a shift sentinel at `$FB`; `$754B` stores literal bytes and `$759F` stores bytes copied from a backwards-decoded match.

## Video and text

| Register or data | Role |
| --- | --- |
| `$D012`, `$FFFE/$FFFF`, `$D019` | `$791A` schedules a raster line and its IRQ vector, acknowledges the VIC, then restores the saved registers. The stage frame starts at `$16AD`, switches through `$19AD` and `$1A59`, and draws the status panel from `$1A89`. |
| `$DD00`, `$D016`, `$D018` | The IRQs select bank `$C000` for the scrolling field and bank zero for the panel. `$1A31` derives the playfield character-bank offset from `$7370`. The panel uses screen `$0400` and character set `$0800`. |
| `$D000–$D010`, `$D027–$D02E` | The sprite loop at `$175E` transfers actor positions and colours and writes pointer bytes to the active screen page. |
| `$D800–$DBFF` | The playfield colour routines at `$126B` and `$2A72` translate character codes through the current stage table at `$9200`. |
| `$9200`, `$E000/$E800/$F000/$F800` | Stage tile properties and the four character pages selected by the scroll phase. `$199B` can rewrite the character slot at `$FFE0` in play. |
| `$9990`, `$A250` | Secondary layer, ten rows with a 220-byte stride. Foreground layer, 18 rows with a 400-byte stride. `$1103` overlays the two with foreground code zero transparent. Stepping `$109F` and `$1108` observed effective reads of `$A32E` and `$9A12` during stage 1. |

The font at `$3000` has 8-byte glyphs, and the banner routine at `$136A` masks source bytes to six bits before selecting a glyph. The message strings at `$7261–$7362` use `@` for a blank and `A–Z` at `$41–$5A` before masking. The fixed-length banners include GET READY, PAUSED, GAME OVER, OUT OF TIME and the various bonuses. The menu's visible text includes screen codes `$01–$1A` for A–Z and `$FE` for a space in its tutorial. A distinct inverted panel font resides at `$0800`.

| Panel code | Rendered glyph |
| --- | --- |
| `$E8–$F2` | C, E, I, L, M, N, O, R, S, V, Y |
| `$F3–$FC` | 0–9 |
| `$FD` | £ |

## Controls and mechanics

- The active-low gameplay read at `$244E` uses CIA1 port A, `$DC00`. Stepping the read gave `$7F` at rest, `$7F` for left and fire on port 1, and `$6B` for left and fire on port 2.
- Instruction stops with right, left, down plus fire, and fire reached stores setting `$14` to one or `$FF`, `$5B` to one, and `$18BF` to one respectively. `$245F` gates the crouch against movement and terrain state. `$25B0` tests up alone and compares the player's tile coordinates against the door tables.
- The shop's six-item selection is stored at `$225A`. At `$201A` a port-2 down input changed it from 1 to 2 through the store at `$205A`. The price path at `$226B` subtracts the selected packed-decimal price from `$02AB–$02AD` and rejects a borrow before updating the balance.
- The shop path at `$1F86` tests for duplicate heart colours against `$02CD–$02D1`. Its fifth distinct colour takes the bonus path through `$272C`, which caps the life counter at nine.
- `$1FE6` compares the progress count in the operand at `$2709` with a table at `$73F9` indexed by the loaded stage byte `$998C`. The stage-completion path builds the tally at `$20FE` and uses `$215A` to call the next load.
- The BCD timer at `$2835` uses seconds at `$24`, minutes at `$25`, and a divider at `$2A`. Breakpoints at `$2842` and `$2873` verified 17:00 to 16:59 and 00:01 to 00:00. The latter set both `$13` and `$33` to one.

## Audio

The resident stage-tune entry at `$29EB` uses the low bit of the overlay's stage index at `$998C`. Stepping to `$5500` for indices 0–6 gave entries 3, 2, 3, 2, 3, 2, 3.

The F1 and F3 title key matrix reads at `$7AF0` select separate bits in the audio flag `$6B`. Matrix tests stepped through the toggles, changing `$00` to `$80` for F1 and `$00` to `$01` for F3. Music reaches `$5506`, and the effects path goes through `$5104`. The resident music and effect paths write the SID at `$D400–$D418`. Logical SID writes were analyzed with dummy audio.

Test scripts and their raw outputs are in ignored `work/`, including `verify.txt`, `under-io.txt`, `mechanics.txt`, `display-checks.txt`, and the per-payload write maps.

## The listing's error rate

An independent gpt-6.2-sol checker sampled 75 of 581 comments with seed 6502. Five had wrong details (6.7%, Wilson 95% interval 2.9%–14.7%, and a 4.3% estimate weighted by stratum size). The five findings were confirmed and corrected across the affected comment families. The estimate applies to the listing before those corrections and the resident follow-up, and the checker may have missed errors.

## Stage room and actor data

The special-room setup at `$1CB6` exchanges two 192-byte character strips, then decodes `$9098–$91FF` into 18 rows of 40 screen cells. Each source byte holds two indices. The low nibble goes first. The code at `$1CF8` looks up the character at `$4FDD` and the colour at `$C6E0`. A VICE load watchpoint on `$9098` stopped after `$1CF8` with A equal to `$CB` on stage one. Stepping the next stores put tile `$7C` in `$C000` and colour 8 in `$D800`.

The actor code at `$4185` and `$418A` builds a pointer from `$4DF3/$4E09`. The first eight directory entries point to 188-byte allocations beginning at `$9328`. The next four entries point into the 33-byte allocations beginning at `$9908`. Later entries can point inside those allocations. A load watchpoint across the first stage's record area stopped at `$4191`, just after the indirect read from `$418F`. The state reads at `$427D–$428C` use a separately selected index.

The stage setup instruction `CMP $988E,Y` at `$14B3` uses Y equal to `$FE`. It reads the stage index at `$998C`. Single-stepping this instruction and its branch with each of the seven hand-over snapshots confirmed values 0 through 6 and a fall-through on equality.

## Resident graphics and sound

The sprite copier at `$275D` splits the frame number into a page index and a 64-byte offset into the `$8800–$907F` sheet. It transfers the 63 visible bytes to the slot whose low address is passed in X. A read watchpoint during the title-to-play transition caught the transfer with source base `$8F80` and Y equal to `$3E`.

The boot copy at `$5490` moves ten 256-byte blocks from `$9080–$9A7F` to `$C000–$C9FF` before the first stage load. The source and destination page operands increment after every 256 bytes. A store watchpoint at `$C843` stopped at `$549A` with X equal to `$43`. The patched source at `$5494` read byte `$03` from `$98C3`. The resident listing uses a snapshot taken after this copy.

The music setup at `$59E4` selects an eight-byte record containing two tick values and three voice sequence pointers. The voice sequences select note patterns through the split pointer table at `$5A79/$5AD3`. On the title snapshot, stepping from `$55B5` through `$55C5` resolved pattern 43 and fetched `$36` from `$62C5` with Y equal to 12. The separate effects driver uses the setup records at `$5294` and stream descriptors at `$52C4`.
