# Soldier of Light technical facts

These findings describe the F.S.N. disk and the raw RAM in `work/cleemalt-play.vsf`. Static deductions name their code addresses. Live evidence names the checkpoint, instruction trace or frame capture.

## Build and memory

The F.S.N. loader resumes the saved title raster IRQ at `$3F93`. This is the PC after single-stepping the restore stub's `RTI` at `$01EF`; it is recorded in `work/game-handover.vsf`. The title display can be rebuilt from its own setup entry at `$3F00`.

| Addresses | Role and evidence |
|---|---|
| `$0400` onward | Resident game logic includes a reset into the selector at `$0400`, a raster-paced ground loop at `$1401`, and display and output helpers. |
| `$4000–$7FFF` | Expanded ground map. `$1F50` calls `$1C00` four times per iteration for 256 iterations. Each call emits 16 character indices. Store checkpoints at `$4000`, `$5800` and `$7000` stop at `$1C62` immediately after the first store in the body. The space setup clears and reuses the lower pages. |
| `$8400–$87FF` | Live screen matrix and sprite pointers. `$3F28` rebuilds the title characters from `$0A00` and `$F400–$F6FF`. `$E644` copies the planet HUD template here and `$0870` updates the playfield sprite pointers. |
| `$A000–$A57F`, `$A600–$AFFF` | 64-byte VIC sprite slots holding Xain, ships, planets, enemies and effects. The gap at `$A580–$A5FF` contains code and padding. `$2CDA` calls `$A5B3` in that gap. |
| `$B000–$B2FF` | Panel glyphs and graphics patterns. The first 64 glyphs use the C64 uppercase screen-code order, with `$01–$1A` for A–Z, `$20` for space and `$30–$39` for digits. Glyphs were rendered directly from the snapshot. |
| `$B800–$BFFF` | Work buffer for the selected terrain font. The store checkpoint at `$B800` stopped at `$1BA8` following the store at `$1BA5`. Its eight source pages remain resident. |

## Planet sources

The ground loader banks out KERNAL with port value `$35` at `$1CC8`, then banks out I/O with `$34` at `$E69B`. It restores `$36` at `$1CFA` after expanding the map and copying the terrain glyphs.

A stop on the first execution of `$1C04` and inspection of the patched operands gave these source addresses. The graphics copy at `$1BA0` walks eight pages. The tile decoder forms a 16-byte record pointer by multiplying the fetched map byte by 16 and adding the selected base.

| Planet | Map indices | Metatile base | Glyph copy source |
|---|---|---|---|
| Cleemalt | `$F000` | `$9000` | `$D000` |
| Lagto | `$F400` | `$9300` | `$D800` |
| Cleedos | `$F800` | `$9600` | `$E000` |

The Lagto index stream shares three pages with the title's screen source. The executable bytes at `$F6E8–$F6ED` are past the 1,000 visible cells of the title matrix. The space initialiser at `$E895` calls them as instructions.

## Video and register census

The title uses KERNAL's RAM IRQ vector at `$0314–$0315`, pointing to `$3F52`. Its three handler targets are `$3F81`, `$3FA1` and `$3FC1`. Ground play installs `$190F`. That dispatcher rotates the low byte of its JSR among `$00`, `$30` and `$60` with high byte `$1A`, then acknowledges the VIC raster interrupt.

The Cleemalt frame capture recorded `$D018 = $1E` on line 104 and `$D018 = $1C` on line 226. VIC bank `$8000` makes those point to `$B800` terrain and `$B000` panel glyphs respectively. Sprite pointers change during these bands. For example, a store at line 225 writes `$BF` into `$87FA` to hide the sprite whose playfield shape was `$B1`.

| Register | Use and evidence |
|---|---|
| `$01` | Changes CPU banking for terrain, music and other data under ROM and I/O. The source checkpoint at `$1C04` measured `$34`. |
| `$D000–$D010` | Sprite coordinates. `$1500` doubles the eight coarse horizontal coordinates at `$1F48–$1F4F` and uses the shift carries for the high-X bits. |
| `$D011/$D012/$D016/$D018` | Raster timing, display origin and glyph banks. The ground phase handlers are `$1A00`, `$1A30` and `$1A60`. |
| `$D015/$D017/$D01B/$D01C` | Sprite enable, Y expansion, drawing priority and multicolour. Examples at `$1B5E`, `$8260`, `$1AB8` and `$1B99`. |
| `$D019/$D01A/$DC0D` | Acknowledge and enable VIC raster IRQs and mask CIA 1 sources. Ground IRQ tail `$192C–$193B`. |
| `$D01E` | VIC sprite collision latch, read at `$14AE`. It feeds collision tests separate from the character map reads. |
| `$D020–$D02E` | Border, background and sprite colours. Terrain defaults and sprite colours are set by `$1B00` and `$1B40`. |
| `$D400–$D418` | SID voice and filter data. Music combines a voice register offset with frequency, envelope and waveform values. The effect path at `$FE12` can write voice 3. |
| `$DC00/$DC01` | Joystick port samples. The ground loop uses both CIA ports, with port 2 controlling movement. |
| `$DD00` | VIC bank select. `$1B0A` writes 1, selecting the bank beginning at `$8000`. |

## Controls and progression

- **Ground jump.** From the same early Cleemalt snapshot, a one-second neutral trial did not hit the jump-accept branch at `$1067`. Holding port 2 Up hit it and single-stepping followed `$1067 → $1069 → $0BE1 → $0BE4 → $0DC1`. The acceptance path writes 1 to the vertical state at `$1109` and requests a sound effect via `$C000`. The two runs and their instruction steps are in `work/input-trace.log`.
- **Jump phases.** The initial port check at `$1058` accepts Up, Up-Left and Up-Right with or without fire. The ascent routine at `$1118` reads 32 Y displacements from `$10C0`. Its branch after those steps samples Up again and can select state 3. The second ascent has an independent cursor at `$1189`.
- **Get Ready.** The prompt loop at `$3C45` waits for raster low byte `$80` and ticks the sound before reading joystick port 2. A value of `$6F` exits directly. Otherwise the branch through `$82A0` tests the music completion flag at `$C084`.
- **Map contacts.** `$15A6` derives a map pointer for the player using its sprite X and Y. The translation at `$1E00` uses 8-pixel coordinates and row origins at `$1F00`. The support path uses explicit character code tests starting at `$1200`.
- **Score.** The least-significant score logic updates screen-code digits in place. `$2ABD` carries into `$8483` and `$8482`. `$1041` saves five score characters into the HUD template at `$3E93`.
- **Timer.** A store watch at `$84D7` from the Cleemalt snapshot stopped at `$0833`. The preceding instruction at `$0830` wrote screen code `$39`, rolling the units digit from zero to nine before the borrow path.
- **Base result.** The path at `$2F3B` draws the destroyed-base and incomplete-mission messages using the strings beginning at `$E500`. Its exit path at `$9A60` tests a gate byte and the exact port 2 fire value before the next scene. The space setup at `$E800` and loop at `$E8DF` are resident in RAM under KERNAL. A targeted jump to the game’s transition entry at `$0C63` reached `$E800` and produced the space display. The disk helper at `$9CB0` had no hits during the transition or the next 70 frames.
- **End of mission.** `$0692` branches back to the destination selector while its return counter at `$0691` is below two. At two it draws the completion screen via `$069F`.

## Sound

`$C001` initialises a cue. The entry at `$C007` advances it and `$C004` stops it and silences the voices. The cue selects a timing value at `$C0AA`, starting voice at `$C755`, and three stream addresses from the six-byte groups at `$C75F`. The cue flag in the immediate operand at `$C084` also controls the Get Ready wait.

The track decoder at `$C0C8` handles stop, repeat, transpose and pattern selection. A selected pattern's two-byte pointer comes from `$C7A1`; the parser at `$C109` sets note and instrument state and computes the SID frequency. `$C63B` writes cached control and frequency bytes. A store watch on `$D404` from the Cleemalt snapshot stopped at `$C648`, immediately after the control store at `$C645` with the first voice selected. Both store stops are recorded in `work/verify-timer-and-sid.log`. The sound-effect entry at `$FE12` consumes an effect index from `$C000`, uses parameter groups beginning at `$FEA3` to initialise voice 3, and advances its own control and pitch streams.

## Open analysis

The play snapshot contains the legacy file-loading entry at `$9CD1`. Its four calls to `$9CB0` select the one-byte names P, 3, 4 and V. The catalogued F.S.N. disk has one directory file and no file under those names. Neither the typed-reference search nor a direct call and jump opcode scan located an edge to `$9CD1`. The live watch covered the targeted space entry and 70 following frames. An indirect or later entry remains open.

The terrain contacts, hit paths and end-of-mission code have static annotations. Legal-play reachability of the final result, pickup sequences, air steering and the rest of the space sequence remains open. The space test set the PC to the game's transition entry. Its evidence establishes code behavior from that state.

## The listing's error rate

The independent `gpt-6.2-sol` checker sampled 80 of 1,506 comments from seed 112022. Six of 60 comments in the general stratum had wrong details. All 20 comments sampled from the 63 music-template comments passed. The unweighted estimate was 7.5% with a 95% Wilson interval of 3.5% to 15.4%. Weighted by the two strata's sizes, the estimate was 9.6%. The checker may have missed errors. All six findings held and were corrected. They concerned the tail of a music pattern, a mutable cursor, the location of collision flag stores, a zero-page Y offset, VIC column mode and the use of a patched planet comparison. The parallel Y offset comment was also clarified.
