# Live and Let Die — technical facts

## Build and loaded data

The Fantasy disk loads all five phase files before the jump to `$0803`. The loader copies PHASE1 to `$E000–$FFFF` and PHASE2 to RAM under I/O at `$D000–$DFFF`. PHASE3 supplies `$4800–$CFFE` and PHASE4 replaces `$8000–$8FFF` immediately afterwards. PHASE5 supplies `$0800–$43FF`, including the entry and the main loop. The file addresses and final byte comparisons are in [orientation.md](orientation.md).

The briefing swaps 145 glyphs from `$D000–$D487` into codes `$3A–$CA` at `$79D0–$7E57`. The same `$CB6C` routine exchanges four pages between `$DC00` and `$8000` for the digitised sound. The copies agree throughout in `work/menu.vsf`. An instruction watch captured reads of the first four hidden pages at `$CB7C`, `$CB8C`, `$CB9C` and `$CBAC` while the I/O area was banked out.

`$CC17` swaps 112 bytes between `$9600` and `$D800`. In the briefing this area holds percussion code. In play the first 88 bytes here are the low halves of row addresses seeded by `$2AC1`. `$FF47` and `$FF5F` similarly exchange two pages of bank-1 scenery sprites with the copy under colour RAM. North Pole swaps in both of the alternate pages in the captured course sample.

## Boot, menu and input

- The briefing at `$0CDA` uses raster updates and a fire edge detected at `$09FB`. The selection counter at `$033A` wraps between zero and three. The menu reads CIA1 port A at its `$DC90` mirror. At `$0D39` it compares the full byte with `$7E` for Up and `$7D` for Down.
- `$0D6D` selects the course title and stores pointers to two independent course streams. Practice and New Orleans scroll the text selected by `$0DF4` across the panel before advancing. North Pole and Sahara take the direct branch at `$0CF7`.
- During play, `$AE9C` tests joystick Up as an active-low bit. *Live:* A read `$7E`, the mask at `$AE9F` yielded zero, and the branch entered the acceleration call at `$AEAA`. The separate Down path skips deceleration when fire is held.
- In the fire update at `$9E00`, the Down bit selects the missile branch if the launch conditions allow it. *Live:* Down and Fire read `$6D` at `$9E43`. The branch reached `$9E4F`, looked up the missile count and then wrote a zero to the missile display via `$9E56`.
- The HUD interrupt sets CIA1 port A to zero at `$1564`, then reads port B at `$1567`. Its state machine compares the saved port value at `$1610` with `$7F` for the Run/Stop pause toggle and `$FD` for Return. It requires a released key before accepting the second pause toggle. *Live:* On the same running Practice snapshot, stepping the read at `$1567` gave `$FF` with no keys, `$7F` with Run/Stop and `$FD` with Return. The neutral branch reached `$1616`. Stepping `$15D9` changed `$0354` from zero to one, and stepping `$15C7` changed `$EDF7` from `$46` to zero.

## Raster and graphics

The VIC uses bank 1. `$D018 = $1F` selects screen RAM `$4400`, bitmap RAM `$6000` and character RAM `$7800`. A playfield split writes `$2B` ORed with the display bit to `$D011` and puts `$10` into `$D016` at `$13B6–$13BB`. The dashboard split restores character-mode control values at `$154E–$1556`.

| Handler | Next IRQ target written to $FFFE–$FFFF | Work visible in code |
| --- | --- | --- |
| `$1829` | `$16F5` | Sky colour and start banner timing |
| `$16F5` | `$1802` | Horizon colours, fine scroll and the three-row character shift |
| `$1802` | `$1397` | Restores sprite enables and sets the playfield compare to `$72` |
| `$1397` | `$1535` | Bitmap playfield and sprite changes |
| `$1535` | `$1829` | Dashboard, keyboard, sound and gameplay updates |

*Live:* The vector stores at `$1836/$183B`, `$17EC/$17F1`, `$180C/$1811`, `$148C/$1491` and `$1688/$168D` gave this chain. The `$1829` entry ran 95 times during the 95-frame probe. VIC interrupt status is acknowledged at `$18BF` in that handler. The menu has a separate initial entry at `$0E0C`.

The river renderer starting at `$2B80` iterates distance rows using addresses from the split pointers at `$8280` and `$82D8`. It combines signed lateral offsets with `$8200` to locate the bitmap byte. It selects one of four two-bit pixel boundary masks using the offset's low two bits. The rendering and colour updates use a mix of generated bitmap and character rows.

The character image at `$7800` uses code `$00` for blank, `$01–$1A` for A–Z and `$30–$39` for 0–9. `$1B–$1F` show period, asterisk, left arrow, dash and copyright glyphs. `$21` is plus, `$3A` is comma in the entry charset, and `$F6–$F8` are exclamation, percent and question mark. Other indices include tile graphics and panel fragments. Text readers use the images' native codes. The title repeats the software, graphics, sound and design credits at `$B730–$B7BA`.

## Course data

- `$E000` and `$E008` contain four pointers each. The first table chooses a section-selector sequence, and the second a curve sequence.
- `$1EE7` fetches a section selector, masks it with `$3F`, then reads that section's stream pointer at `$E010`. Each stream holds triples of progress, operation and argument. At a matching progress position, the middle byte selects a dispatch target through `$1FFB`, and the final byte's low nibble supplies X. Operation `$2C` advances the selector sequence and operation `$2D` sets `$20F4`.
- `$276C` takes turns from the second stream when `$27A8` reaches zero. The low nibble sets the remaining duration and the high nibble encodes a signed-magnitude turn. The high-bit-set magnitudes are negated after masking with seven.

## Sound

Three SID score selections start at `$8A61` through the nine split channel pointers at `$8C0C`. The score decoder at `$8603` uses commands at `$8841` to select instruments, call phrases, loop channels and switch volume. Phrase pointers are split between `$8DB9` and `$8DE7`.

The percussion player at `$9605` expands a 16-event pattern per ID from either of two order lists at `$96F7` and `$9729`. Three event types select packed, four-bit volume samples. The sample routine at `$9672` writes each nibble in turn to `$D418`. Event type three is the rest.

The effect system at `$98DA` starts a separate stream on a selected voice. At `$9918`, commands change the pulse width or frequency step, set new control and frequency values, or release or loop the voice. The per-tick loop `$98DD` adds each voice's two-byte frequency step and writes the updated frequency.

## Fuel and contact

`$F687` advances the fuel gauge outside Practice and the start banner. Its counter at `$F73A` measures depleted scanlines across four glyphs at `$7D98`. On a drain tick, full depletion, zero speed and an empty outcome byte allow `$F687` to set `$20F4`. The checker exercised each guard in the CPU simulator. The contact handler at `$F84B` starts a refill and clears a contacted object. `$C0B9` advances a falling supply sprite, changing its image at selected vertical positions.

## Coverage and live evidence

The hand-over ledger covers 62,463 bytes. Code accounts for 25,491 and data for 36,972. The denominator includes all 4,096 bytes under I/O loaded by PHASE2. Repeating fill patterns around the hidden resource pages are preserved as loader-carried bytes. A bank-conditioned watch found a read at `$D400` and no reads in the watched ranges `$D488–$D54F` and `$D870–$D9FF` over the first 65 frames. Whether any later state reads the anomalous bytes within those ranges remains open.

The executed traces are local in `work/control-trace.txt`, `work/keyboard-probe.txt`, `work/play-watchpoints.txt` and `work/hidden-tail-probe.txt`. The disk call trace and hand-over comparisons are described in [orientation.md](orientation.md). Course selection used the standard menu for all four starts. No claim here depends on replaying a recorded input route.

## The listing's error rate

An independent `gpt-6.2-sol` checker sampled 70 of 1,393 comments with seed 251120. Seventeen findings held and all seventeen were corrected. They covered overlapping graphics or audio data, the scope of shared fields and guards, and instruction details such as the value stored at `$EDF6` and the tail jump at `$BF7D`. The pre-correction estimate was 24.3%, with a 95% Wilson interval of 15.8–35.5% and a stratum-weighted estimate of 25.2%. The checker may have missed errors. A full audit is recommended.
