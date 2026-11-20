# Solomon's Key analysis facts

The addresses are for the Scouse Cracking Group disk after its unpacker hands control to `$080F`. The listing uses the handover snapshot.

| Subject | Finding | Evidence |
|---|---|---|
| Hardware setup | The game selects VIC bank `$4000` and installs hardware IRQ `$1569` and NMI `$1388`. The NMI returns immediately. | `$134F–$1388` and the live vectors in Round 1. |
| Sprite reuse | Four raster phases update one set of hardware sprites from four 34-byte buffers. The last phase also calls audio and advances the counter which paces the game loop. | `$1569–$15D6`, `$17B0`, `work/frame.json`. The store watch on `$D012` stopped after stores at `$159F`, `$15AC`, `$15B9` and `$15D1`. |
| Room layouts | The mapping at `$208C` translates the logical room index to the stored record. Each foreground and backdrop grid has 13 columns and 11 rows. Foreground codes start at `$8000`, backdrop codes at `$B6CC`. | `$14B8–$14FF`. Load watches on both source ranges stopped on the copy at `$14E1` and `$14E6`. |
| Initial room actors | An independent 128-byte record per room initializes lanes of actor data at `$0400–$047F`. The room rebuild clears the upper lanes and sets all 16 sprite pointers to `$7F`. | `$13CC` and `$1530–$1568`. |
| Tile composition | Each bitmap tile is six 8×8 multicolor cells. The source is 48 bytes at `$941C + code × 48`, and six palette cells per foreground tile begin at `$BB44 + code × 6`. | `$1A34`, `$1A7D`, `$1B85`, and the pointer tables under KERNAL. A tile-art load watch stopped in the foreground compositor at `$1B90`. |
| Input | CIA1 port A supplies joystick 2. The low five bits are active low on the port and active high in `$13`. Keyboard mapping uses separate row, column and result tables. | `$1982–$19EE`. With right held, single-stepping from `$1982` through `$1989` wrote `$08` to `$13`. The following watch on `$0410` stopped after the right-walk increment at `$39C5`. |
| Room editor | The enabled editor is resident. `$3C03` checks `$5A` and input bit 7. The score-name comparison at `$0D5C` checks ten adjusted glyphs and sets `$5A` after a complete match. | Control flow and the command pointers at `$3C7F–$3CA8`. An execution fixture with `ASSISTANCE` in the ten name cells stopped on the store to `$5A` with value 1. The comparison with `ASSISTANCX` returned with the flag clear. The fixture exercises the checker directly. |
| Timer | The time counter uses three packed-BCD bytes. `$1307` subtracts two in decimal mode, except in player state `$04`, and invokes the time-expiry effect at zero. Over 120 PAL frames, the fourth raster phase ran 120 times and the timer routine ran 60 times from the Round 1 snapshot. | `$12F7–$1333`, `$22AE–$2393`. The targeted routine test took 5100 to 5098 in state zero and preserved 5100 in state four. |
| Fairy awards | The overlap handler accepts actor type `$0B` when its timer byte is zero. The tenth fairy clears the count and adds a life if the lives byte is below five. | `$2220–$2287`. |
| Alternate key | A key with tile code `$31` sets a two-slot round increment on pickup. Casting on it can replace it with `$03`, whose handler opens the exit without changing the increment. The authored `$31` keys occur in displayed rooms 3-3, 5-6, 7-2 and 8-5. | `$24C0`, `$1CCF`, `$1EEA`, `$0884`, and the room tables. A write watch on the prepared casting phase caught the change from temporary tile `$2F` to `$03` at `$228F`. A separate execution stop at `$1EB0` caught the increment set to two by `$1EEA`. |
| Music and effects | The fourth raster phase calls a dispatcher for a three-voice music stream player and a separate effect player. | `$15C7`, `$C000`, `$C135`, `$CB26`. |

## Bitmap alphabet

The string helpers use bytes directly as glyph indices. They take eight rows from `$FC00 + index × 8`, using zero as the string terminator. The rendering in `work/font.png` and the title and HUD text agree on digits `$30–$39` and letters `$41–$5A`. Space is `$20`. The indices below `$20` include pictograms and animation shapes. The masked variant transforms each source byte through `$2800` and selects the corresponding merge mask at `$CF00`. The glyphs are authored bitmap data at `$FC00`, independent of the C64 character ROM.


## The listing's error rate

Seed 2063 drew 60 of 638 comments. An independent `gpt-6.2-sol` checker found five wrong comments, an estimated 8.3% error rate with a Wilson 95% interval of 3.6% to 18.1%. The checker may have missed errors. All five findings were corrected. They concerned tune selection at the time threshold and player death, the pulse-width and note-bias operands, and the shared tile-coordinate and sprite-offset boundary.
