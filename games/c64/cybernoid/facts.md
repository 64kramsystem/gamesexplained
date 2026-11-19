# Cybernoid technical facts

## Image and room data

- The final unpacker hands off at `$0824` with its destination pointer at `$D000`. Its initial destination is `$0800`. The upper RAM bytes outside that output match the earlier packed stream displaced by `$15F7`. The game builds the runtime bitmap, sprites and interrupt vectors in upper RAM from the unpacked image.
- `$0830–$08C5` holds 75 little-endian layout pointers and 71 distinct streams. `$3745` reads the selected pointer through `$55B3`. A plain byte emits one tile and `$FE,count,tile` repeats a tile. Exactly 190 cells are emitted over nineteen columns and ten rows. Decoding the 71 streams this way consumes `$08C6–$2CF2` contiguously. The concrete bounds and marker positions are in the listing.
- Tile IDs below `$E9` take the bitmap path at `$45B0`, with two rows of sixteen pixel bytes per graphic. The pixel atlas occupies `$873B–$A1BA`. The screen attributes draw from `$7528 + 4×ID` and packed colour data from `$7878 + 2×ID`. High colour-table indices can address the same bytes used for text attributes.
- The room-edge path at `$36CB` updates the layout index by one for left or right and by the stage stride for up or down. It wraps the player coordinate to the opposite edge and saves the new room entry position. The four starting fields and timer values are in the stage records at `$2E7B`.

## Text and display

The title displays character codes from the RAM glyph bank at `$C800`. The sprite logo is sourced separately from `$7D3E–$7F3D`. In gameplay the bitmap glyph writer `$47B0` uses the same eight-byte glyph records and copies them into the bitmap. A rendering of candidate pages is kept at `work/glyph-candidates.png`.

| Glyph codes | Meaning in the display scripts |
|---|---|
| `$20` | Space |
| `$30–$39` | Digits 0–9 |
| `$41–$5A` | Uppercase A–Z |
| `$21`, `$22` | Left and right halves around the C in the publisher's copyright line |
| `$2D–$2E`, `$3A–$3F` | The title star effect's frame codes, from `$8156` |

The common interpreter at `$589F` treats `$DF` as an absolute row/column command, `$FE` as a glyph offset command, `$E1/$E2` as repetition, `$E3` as a nested stream call and `$E4` as a repeated glyph. Commands in the `$CF–$DE` range select colour through `$4724`.

## Input and weapons

- The title menu dispatch records contain five handler pointers and keyboard row/mask pairs at `$8168`. `$4950` drives one active-low keyboard row at a time on `$DC00` and stores `$DC01` in `$4965–$496C`. In joystick II mode `$48BF` reads the active-low input bits directly from `$DC00`.
- The normal shot starts on a new press at `$563E`. Auxiliary dispatch at `$5B28` is available once the held-fire counter reaches eight. The bomb routine at `$6448` also tests for twelve, then sets the counter back to one. On a half-second first-room fire hold, execution checkpoints recorded one ordinary shot and ten visits to the bomb handler, and a store watchpoint on `$5B79` counted two stock debits. The live bomb count then read 18, down from 20. The trace is in `work/bomb-trace.txt`.
- The five 16-byte records at `$5B6E` carry the displayed name, live stock, handler, starting stock and limit. The stock debit at `$5B2B` depends on the handler's activation flag at `$5621`. The canister handler at `$6B2C` increments the selected weapon subject to its limit.
- The level clock at `$722E` counts down a 16-bit divider. Its reload advances the twenty-step bitmap bar. There is also a separate per-room timer at `$3A1B/$3A1C`, checked by `$704F`. The stage report at `$33FD` requires the level timer index below twenty and compares the cargo word to 1500 to choose the success text and award.

## Register access

| Register or range | Use and evidence |
|---|---|
| `$0001` | Startup banks out ROM, writes graphics in RAM under I/O and restores chip visibility at `$A1BC–$A242`. |
| `$D000–$D010`, `$D027–$D02E` | First and reused sprite groups write X, Y, high-X bits and colours at `$4B2D` and `$4BD4`. |
| `$D011`, `$D016`, `$D018`, `$DD00` | Title uses the `$C000` matrix and `$C800` characters. Play uses the same matrix, multicolour bitmap and bitmap base `$E000`. See `$A253`, `$86FD` and `$2E1E`. |
| `$D012`, `$D019`, `$FFFE–$FFFF` | Three-phase raster schedule from `$49A5`. The middle compare line can change with the sprite reuse group. The final handler sets the main-loop flag at `$49AF`. |
| `$D400–$D418` | The first raster handler calls the music driver at `$AE06` or effects at `$A601`, depending on the menu setting. Each path writes SID voice registers and filter state. |
| `$DC00–$DC01` | Joystick II and keyboard scan. The keyboard selection and direction masks are mutable operands. |
| `$DC0D–$DC0F`, `$DD0E–$DD0F` | Startup stops CIA timers and masks and acknowledges CIA 1 interrupts at `$A2E9`. |

## Open questions

- The original and the Zenith release were unavailable as matched gameplay snapshots. Which bytes in the handover near `$080D` are changes by the Beastie Boys remains open.
- The lifetime of the high-score table across sessions and the long-session audio problem remain open.

## Live verification

The checkpoint script and raw output are kept as `work/verify-checkpoints.py` and `work/verification.txt`.

| Test | Observation |
|---|---|
| Startup sprite copy | Before restoring I/O at `$A238`, the port read `$34`. Checkpoints counted 256 visits to the indexed source read at `$A21D`, one load from `$C000` and one store to `$D400`. All 1,024 physical RAM bytes at `$D400–$D7FF` matched their source at `$C000–$C3FF`. |
| Neutral versus held fire | Both runs began at the same room snapshot and stopped on the 24th main-loop entry. The neutral run left bomb stock at 20. Held fire visited `$563E` once, `$6448` ten times and the debit store at `$5B3D` twice. The store watch on `$5B79` also counted two, and stock read 18. |
| Level clock | Setting the active divider to one led to one execution of `$722E`, one store to the bar step, and a stop at `$725B`. The bar index rose from zero to one and the divider reloaded to `$01F4`. |
| Room timeout | With the room timer forced to `$0100`, the `$704F` and `$70C6` execution checkpoints each counted one. The stop immediately after the decrement showed three craft instead of four. |
| Lives digits at respawn | After a forced timeout, forcing the respawn delay to expire reached `$70D6` and stopped at `$70F2`. The count remained three and the 16 bitmap bytes for the two lives digits at `$E2A0` were unchanged. The `$57F9` lives-renderer checkpoint counted zero inside that respawn. |

The byte reference sweep found no authored instruction that names KERNAL LOAD at `$FFD5` or SAVE at `$FFD8`. The stage and room paths followed here read resident arrays. The file inventory and these traces support a single game image. No disk-persistence claim is made for the high-score table.

## The listing's error rate

An independent `gpt-6.2-sol` checker found six incorrect or incomplete details in a 60-comment sample from 1,159 comments, seed 1848. All six were corrected. They concerned the bouncing bomb's active gate and collision alignment, the effects workspace and credit overlap, the address of a patched music operand, and reuse of a sprite source as screen RAM. The sample rate was 10.0%, with a 95% Wilson interval of 4.7% to 20.1%. The estimate weighted by stratum was 12.5%. A full audit remains open.

The exported ledger matched exactly before and after verification, with 51,200 explained and 51,200 tracked bytes. The rebuilt listing has no uncounted stretches.
