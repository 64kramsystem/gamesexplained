# Hunchback technical facts

These addresses refer to the Ocean PAL cassette build in `orientation.md`. The evidence marked **live** comes from a VICE execute breakpoint, instruction step or watchpoint. Other claims come from the tape payload and its traced code.

## Build and memory

| Range | Use |
| --- | --- |
| `$0801-$087B` | BASIC bootstrap. Its LOAD puts the second tape program at its recorded address, and SYS enters the game at `$4000`. |
| `$3C00-$8000` | The entire 17,409-byte `HCODE` payload, byte-for-byte in the entry snapshot. Main program at `$4000`, with sound and display helpers below it. |
| `$033C-$03FF` | State and scratch RAM. Includes stage at `$033D`, player X at `$0340/$0341`, seven score digits from `$0349`, lives at `$0351` and the input latch at `$03FF`. |
| `$5B00-$62FF`, `$6400-$65FF`, `$6800-$6D7F` | Rope, rescue and other actor sprite images. A sprite pointer addresses a 64-byte slot in the VIC's `$4000` bank. |
| `$7400-$77FF` | Live screen codes, with sprite pointers at the end. The game clears and redraws the screen. The supplied `$91` at `$77FF` seeds the heart and HELP animation. |
| `$7800-$7FFF` | VIC glyph address window. Also holds SID presets and pitch and delay data in its upper slots. |
| `$8100-$8131` | Five mutable high-score records copied from `$7180` at startup. Each record has seven digit codes and three initials. |
| `$8400-$8BFF` | Off-screen wall glyph and colour buffers, initialized at `$4219` and copied to the display by `$56A7`. |

`$4005-$4028` programs CIA2 and VIC-II for multicolour character mode. `$DD00=$C6` places the VIC at bank `$4000` and `$D018=$DE` selects screen `$7400` and glyphs `$7800`. The processor port reads `$27` at hand-over and first play, leaving BASIC and KERNAL ROM and I/O visible.

## Timing and hardware

| Register or vector | Use |
| --- | --- |
| `$0314/$0315` | KERNAL RAM IRQ vector. `$46AD` checks title keys, `$4580` animates the attract character and calls the tune routine, `$4B74` pulls the hero back during a wall transition, `$4BF1` handles gameplay objects and `$3C73` flashes background colour. |
| `$D000-$D010`, `$D015`, `$77F8-$77FF` | Position, enable and shape selections. Draw paths include `$49DC` for the player, `$530B` for the pursuer and `$539E` for both rope segments. |
| `$D01E/$D01F` | Sprite and background collision latches. `$5745` reads both when initializing an attempt. Play tests at `$5465` and `$56F3-$57DF` combine collision bits with the stage mask and position checks. |
| `$D022` | Extra background colour, toggled by the death effect at `$3C73`. |
| `$D400-$D418` | Sound frequencies, gate, waveform, envelope, filter and mixer volume. Music and effects both write these directly. |
| `$DC00/$DC01` | Port 2 input is read from port A. Keyboard input sets selectors on port A and samples port B. |

**Live.** From the first input breakpoint, a 120-frame PAL interval gave 142 entries to the gameplay IRQ at `$4BF1`, 51 joystick register reads at `$4925` and three guard draw calls at `$530B`. The IRQ count and main-loop count track different clocks. CIA1 timer A is running, while the game does not install a VIC raster IRQ. Descriptions of guard and rope delays use IRQ services as their unit. `$52B4` decrements the guard delay in that IRQ path. `$6DC0` supplies reload values `$30`, `$20` and `$10` for the three passes.

## Controls and movement

- The title handler at `$46AD` checks the KERNAL current key. SPACE enters the input menu, F1 enters instructions. The menu at `$47C0` uses GETIN and accepts J or K, storing the mode in `$03FC`.
- `$4920` writes a common active-high action byte. Its left, right and fire masks are `$04`, `$08` and `$10`. Joystick up and down are masked out. The keyboard branch samples eight selectors at `$5AC0` and applies the three row and column pairs at `$5ABD` and `$5ABA`.
- **Live.** Neutral, right, left, fire and up reached the store at `$492C` with A equal to `$00`, `$08`, `$04`, `$10` and `$00`. From X `$0020`, the right and left paths reached `$49BA` at `$0022` and `$001E`. Fire alone set jump active and left X unchanged.
- `$4965` starts a jump only with fire set and jump state zero. The horizontal movement is a separate pair of tests. `$49DC` draws the standing baseline at Y `$75` and subtracts one of 16 jump displacements at `$6E18` during a jump. It adds `$18` to world X for the VIC coordinate.

## Stage data and collisions

- Stage index `$033D` addresses 48 wall entries at `$7011`, 48 hazard masks at `$6FE1` and 48 wall colours at `$6FB1`. Stage transitions wrap the index at `$30` and branch to the rescue sequence when its low nibble is `$0F`.
- `$4219` initializes the display buffers, then walks the layout bits from high to low. `$425F` dispatches through split pointer tables at `$6F9F/$6FA5`. From bit zero through bit five the entries are `$42E2`, `$4338`, `$4399`, `$428D`, `$4350` and `$4287`. The drawing paths resume dispatch at `$4262`. **Live.** With stage indices zero, one and two at wall initialization, the indirect JMP executed to `$4287`, `$428D` and `$4287` respectively.
- The IRQ animates wall guardians where layout bit zero is set. The variants of arrows and fireballs at `$4D59-$525E` depend on hazard bits one through seven. Projectile resets in several variants use `$4F34`, which multiplies a 16-bit state by `$05E5` and adds `$29` modulo 65536.
- Hazard bit zero selects the rope. `$539E` advances its 32-step animation. `$5406` tests overlap of player and lower rope sprites before accepting a grounded attachment, with an X range check. A caught player takes the horizontal position indexed from `$6348`.
- `$54B1` and `$3C02` scan the same four intended platform thresholds at `$6344`. The initial range comparison at `$54A5` permits values below `$E0`, while the table ends at `$D8`. **Live with a forced lookup input.** At the pitch write `$3C23`, X arguments `$78` and `$D8` selected indices zero and three and frequency high bytes `$14` and `$32`. Forced `$D9` and `$DF` selected index `$D0` and consumed pitch high byte `$65` from `$3FEF`, inside the wall-base tile map. Whether normal platform collision can produce either out-of-range argument is open.
- `$56F3-$57DF` chooses stage-specific fall and collision tests. These include unsigned X windows over floor gaps, sprite overlap, background contact and the pursuing guard's horizontal comparison once it reaches Y `$75`. The death path at `$57E2` moves the player sprite down to Y `$FF`, decrements lives and restarts the same wall while lives remain.

## Progress and scoring

- `$49C7-$49D5` branches into wall completion during the main loop when player X high is nonzero and its low byte is at least `$1E`. The bell animation and audio at `$3EA7` are called as part of this sequence.
- At `$54DC`, the wall bonus overlay looks up `$0377`, the guard's action counter. The first descending threshold at or below the counter picks the base award from 1 to 9. The routine multiplies it by stage index plus one in packed decimal and adds the result to the score in hundreds. **Live with forced timer values.** Stopping at `$5583` gave 900 for stage index zero and counter zero, 100 for index zero and counter 80, 1800 for index one and counter zero, and 14400 for index 15 and counter zero.
- `$4A77-$4AA9` increments the wall marker count and spends all five markers when the count reaches five. The sequence adds 5000 per consumed marker. `$4AC9-$4AD6` checks the ten-thousands score digit and awards one bonus life, guarded by `$0350`.
- The rescue celebration at `$55D3` has separate text and heart sprites. Its four-frame pointer sequence is at `$5AD7`. `$525F-$52AB` also toggles the heart and HELP pointer every time its countdown expires. Sprite 7 is enabled for the last wall of a pass. **Live.** Stepping the store at `$52A0` wrote `$90` from an earlier pointer of `$91` during first-wall code.
- `$581D` compares a final score to five league entries, most significant digit first. `$588E` draws the initials grid and `$5945` commits a qualifying score and three initials using the selected record pointer.

## Text and graphics

The glyph sheet rendered from `$7800` shows letters A–Z at `$01-$1A`, digits at `$30-$39` and a space at `$20`. Custom glyphs include wall tiles, rope-stage decorations, life and bonus markers, and fragments of the title lettering. Some text runs mix those glyphs directly into the screen codes, such as the joystick symbols at `$677E`. The glyph sheet and sprite render are in ignored `work/`.

The wall-base map at `$3F38` includes a copy of the bottom screen pattern. The map at `$6EB8` includes tile indices `$A0-$A7`. They address the upper glyph bytes starting at `$7D00`. The HUD modifies glyph `$63` at `$7B18` before showing the progress marker, and the gameplay IRQ uses the eight bytes at `$7B98` to toggle glyph `$72`.

## Sound

The attract tune routine at `$3CEF` uses a 64-note index and three equal-size arrays. `$7F00` is SID frequency high, `$7F40` is low and `$7F80` is the delay. The delay helper adds three before the IRQ counts down. The voice 1 triangle gate is restarted for each note. The jumps, projectiles, wall bell and death sequence have separate voice register presets or effects. This run measured the program's register writes and lookups. The dummy output configuration provides no audio recording.

## The listing's error rate

Seed 1319 drew 60 of 249 comments. The independent `gpt-6.2-sol` checker found eight errors, an estimated 13.3% with a 95% Wilson interval of 6.9%–24.2%. The checker may have missed other errors. All eight findings were corrected. They concerned lookup bounds, a constant colour, overlapping attract actions, fireball colour, the number of initials rows, the wall-score overlay and the initial HELP sprite pointer. The sample documents the listing before those corrections.

## Live tests

| Test | Instruction evidence |
| --- | --- |
| Tape entry and first input state | Execute breakpoints at `$4000` and `$4920` captured the two snapshots in `work/`. |
| Input normalization | Store watch on `$03FF`, execution stops at `$492C` and `$49BA`, single step across the store, with `$4925` hit control. |
| IRQ, input and pursuer rates | Non-stopping execution checkpoints at `$4BF1`, `$4925` and `$530B` during the same 120-frame window. |
| Wall layout dispatch | Execute stop and single step at `$425F` from three isolated calls to the wall builder. |
| Bonus value | Execute stop at `$5583` after the packed decimal product, with the known default IRQ vector restored for the isolated test. |
| Platform lookup boundary | Execute stop on the SID write at `$3C23` from four forced inputs. |
| HELP sprite seed | Execute stop at the read at `$5297`, then single step across the write at `$52A0`. |
