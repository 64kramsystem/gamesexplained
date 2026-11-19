# Nebulus C64 facts

## Build and entry

The Danish Gold disk's first file passes control to the resident game at `$8017`. This was captured with an execute breakpoint, trainer set to limited lives. At the entry, `$8001=$01` selects the C64 banking and video path. The bootstrap at `$8017` sets the processor port, initializes the resident state and sound driver, and enters the title cycle at `$803E`. The second disk file independently autostarts into a documentation program labelled Hades Nebula.

The RAM at `$FE00-$FFFF` in the hand-over snapshot contains the final packed stream. The decoder at `$0100` reads through `($FE),Y`. An ordinary byte is written directly through `($2D,X)`. A `$6B` marker followed by a nonzero count and byte emits a repeated run. In a VICE debugger call with the source set to `$FE00` and the destination redirected to `$6000`, instruction steps showed the first `$6B $0D $00` marker take the repeat path. The return to `$0115` left 864 bytes that matched the hand-over image at `$FAA0-$FDFF`. A boot trace stopped at the decoder’s compare at `$0102` after dismissing the trainer intro. From there to `$0115`, VICE counted 512 reads at `$FE00-$FFFF` and 864 writes at `$FAA0-$FDFF`, and the written bytes matched the hand-over snapshot. The decoded sound records are in the resident image. The packed stream and the runtime vectors that overwrite its tail are outside its coverage ledger.

## Raster interrupts and display synchronization

The live port reads `$35` and the engine owns the RAM IRQ vector. The tower raster trace stopped at `$B88B` on line 0, `$B94B` on line 80, `$B981` on line 92 and `$B853` on line 250. Stepping the stores at `$B8E5`, `$B96F` and `$B875` established the vector transitions. The line-250 handler increments `$1707`, which the foreground polls at `$AA93`. The routines at `$AB44` and `$AB5F` clear the back screen and switch the roles of the two screen pages at `$7000` and `$7400`. The IRQ route can add a waterline split based on `$3E`.

The interlude was initialized in a debugger with `$1704=$80`, entering `$8305` and then `$83C8` without playing a route. Execution checkpoints measured the following raster split chain.

| Raster line | Handler |
|---:|---|
| 119 | `$BADC` |
| 143 | `$BB11` |
| 158 | `$BB44` |
| 166 | `$BB74` |
| 174 | `$BBA7` |
| 191 | `$BBD7` |
| 215 | `$BC0B` |
| 250 | `$B853` |

## Input and grounded movement

Stepping the live CIA1 read at `$AB85` through the stores at `$ABA3-$ABA7` gave the following values at `$24-$26` from the same tower snapshot.

| Port 2 input | Horizontal | Vertical | Fire |
|---|---:|---:|---:|
| Center | 0 | 0 | 0 |
| Right | 1 | 0 | 0 |
| Left | -1 | 0 | 0 |
| Fire | 0 | 0 | 1 |
| Right and fire | 1 | 0 | 1 |

In the sampled grounded context, executing fire alone reached `$917C`. The shot slot was free (`$9B=$FF`), and stepping showed `$9187` write state 5. A matched right-and-fire experiment reached `$8F90` and stepped through the store of state 1 and the capture of direction 1 at `$8F96`. The shot is created later, at animation phase 1 through `$91B6`. The direction and fire choices here depend on the preceding tile and facing checks in `$8E02`.

The lift probe at `$AFBE` returns carry set for map byte `$85`, `$89` or `$8D`, with direction +1, -1 or 0 respectively. The door probe at `$AFA9` requires bit 7 set and low bits 3, then returns bit 6 in A and sets carry. These predicates are traced. The full lift and door transitions remain open for live testing.

## Tower map and projection

The decoder at `$B043` selects a palette and the two streams using the zero-based tower index at `$4A`. The tile stream pointer is the pair formed from `$3000+index` and `$3008+index`, with `$20` added to its high byte. The mask page comes from `$B03B+index`, and `$3010+index` gives the height in rows. The two occupancy bytes for each row are read low bit first. Each clear bit produces zero and each set bit consumes the next literal tile. Output is column-major in pages `$02-$11` with the row as the low address byte.

| Tower | Rows | Occupancy | Literals | Literal count |
|---:|---:|---|---|---:|
| 1 | 47 | `$2000` | `$3018` | 140 |
| 2 | 71 | `$2200` | `$30A4` | 140 |
| 3 | 49 | `$2400` | `$3130` | 109 |
| 4 | 66 | `$2600` | `$319D` | 186 |
| 5 | 96 | `$2800` | `$3257` | 225 |
| 6 | 64 | `$2A00` | `$3338` | 155 |
| 7 | 80 | `$2C00` | `$33D3` | 158 |
| 8 | 96 | `$2E00` | `$3471` | 232 |

For each index a debugger call began at the unmodified `$B043`, stopped at its return instruction `$B0A1` and compared the output tile bytes with a separate decode from the hand-over data. All eight matched. These are isolated decoder tests from the same snapshot.

Angle `$C6` wraps at 128 units, with eight units per map column. At `$9CDC`, the relative angle is `(angle + $20 - player_angle) & $7F`, and the coordinate comes from `$C980`. The camera routine at `$C1B4` eases the view height at `$45-$46` toward the player height minus `$28`. The back-page renderer at `$C33E` selects edge row routines using `$C800` and `$C880`. The player/object sprite staging paths include `$BD1E` and `$BDA9`.

## Character data and text

The message records at `$84BF-$86BD` are zero-terminated. The printable bytes use uppercase ASCII-compatible codes. Bytes `$01-$0F` change the colour before any following printable pair. At `$B708`, the glyph pair for A–Z starts at `$36+2*(letter-$41)`. The pair for digits 1–9 starts at `$6A+2*(digit-$31)`. The special table at `$B6F6` handles space, left and right angle brackets, at sign, asterisk and zero. The left/right codes are respectively `00/00, 7F/7F, 7E/7E, 7C/7D, 7E/7F, 52/53`. Each printable byte advances the display position by two cells.

The pristine 2,048-byte pattern block at `$7800` in the hand-over equals the play copy at RAM `$D000`. `$AA00` banks I/O out for the copy and `$A280` copies it back for the interlude. During the tower, `$AC6A` constructs a new pattern set at `$7800`. At `$A2B1`, with I/O banked out, a VICE instruction step wrote plain RAM `$D012`. The IRQ vector held `$A999` at `$A2CE` before I/O was exposed again. The glyph render used during analysis is in ignored `work/glyphs.txt`.

## Hardware census

| Area | Traced purpose |
|---|---|
| `$01` | Banking at `$801E`, `$AA7E`, `$AA8F` and `$B84F`. |
| `$D000-$D010` | Sprite positions and the high X bits. Preview at `$8746`, player pair at `$BD67`, object staging at `$BDA9`. |
| `$D011-$D01A` | Raster scheduling, screen, scroll and character pointer changes, sprite enable and expansion. Representative entries `$B853`, `$B88B`, `$B94B`, `$B981`. |
| `$D01B-$D02E` | Sprite priority, colour, multicolour and expansion. Raster handlers also set the scene backgrounds. |
| `$D400-$D414` | SID voice oscillator, envelope, pulse width and gate writes. Descriptor reader `$F0CA`, modulation update `$F216` and triplicate voice writers from `$F3C6`. |
| `$D415/$D417/$D418` | Initialization at `$F090` clears filter routing and sets volume 15. |
| `$DC00/$DC01` | Joystick normalization at `$AB80`, keyboard matrix reads at `$ABAA`. |
| `$DC02/$DC03/$DC0D/$DC0E/$DD00/$DD0D/$DD0E` | Port directions, VIC bank and CIA timer/IRQ setup at `$B7DB`. |

The title sequencer at `$3959` consumes three streams of pitch/duration pairs and uses the voice driver at `$F006`. Effects use fixed-width 32-byte descriptors from `$F800`. Audio routing and sequencer code were traced. The individual notes and sound identification remain open.

A controlled call to `$F0C4` with A=$15, X=0 and Y=$40 stepped through the store at `$F0DA`, which completed the descriptor pointer `$FAA0`. The stores at `$F140` and `$F143` then wrote the explicit pitch override `$40` to the original and modulated pitch slots at `$F015` and `$F039`.

## Tower bonus counters

The reset at `$B5E9` sets the selected player’s BCD technique counter to `$0100` and their extras to zero. The extras routine at `$B619` compares the resulting BCD high byte with six. In VICE, stepping `$B62B` after adding five to `$0500` took the branch to `$B633` and kept `$0505`. Adding one to `$0599` fell through to `$B62D` and wrote `$0500`.

## Local evidence

The hand-over and first-tower snapshots are `work/entry.vsf` and `work/play-tower1.vsf`. Targeted CPU logs are `work/joystick-trace.txt`, `work/branch-trace.txt`, `work/irq-trace.txt`, `work/underwater-trace.txt` and `work/map-trace.txt`. The inputs in these probes are debugger cases with isolated snapshots. There is no cross-emulator route recording.

The submarine background writer at `$A1C4` patches twenty absolute-indexed store operands to the bases of screen rows 5 through 24. In the sampled back page at `$7400`, those bases are `$74C8-$77C0`. Instruction steps at `$A1C7`, `$A1CD` and `$A1D2` wrote column 39 of the first three rows at `$74EF`, `$7517` and `$753F`. The next pass reached `$A1C4` with Y=38. The tower snapshot holds placeholder high bytes because its foreground uses the tower renderer.

The follow-up VICE traces are in `work/verify-loader-boot.txt`, `work/unpack-replay.txt` and `work/verify-followup.txt`. They use controlled debugger calls, which establish the instruction behaviour in the supplied states.

## The listing's error rate

Seed 20261119 drew 60 of 460 comments. The independent checker used `gpt-6.2-sol` and found two errors, an estimated 3.3% with a 95% Wilson interval of 0.9% to 11.4%. Both were corrected. The door animation can advance when its alignment step is blocked, and the camera update changes height without drawing. The checker may have missed other errors.

Seed 20261120 drew 60 of 900 comments. The independent `gpt-6.2-sol` checker found six errors, an estimated 10.0% with a 95% Wilson interval of 4.7% to 20.1%. The edits correct the restart flag, the interlude bonus reset, sprite mask source addressing, the extras clamp, the edge writer’s destination column and the title sprite strip. The checker may have missed other errors.
