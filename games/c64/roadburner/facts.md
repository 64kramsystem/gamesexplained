# Roadburner facts

This is the Fusion PRG with all three trainer options answered N. Addresses refer to the resident C64 image at the `$11C0` hand-over, unless an address is explicitly a runtime value. The comparison Speedy PRG has the same `CE` decrement opcodes at `$0F60`, `$1B87` and `$1C40`. The two images differ elsewhere. See [orientation.md](orientation.md) for the input and boot recipe.

## Memory and video

| Area | Role and evidence |
|---|---|
| `$0400–$07FF` | VIC screen and sprite pointers. The road uses rows 0–19. `$4E73` puts the dashboard in rows 20–24. The trainer uses these pages before the hand-over. |
| `$080F–$0D01`, `$114E–$11B7` | Object scripts addressed through `$10EE` and `$111E`. `$11F6` interprets them. |
| `$0D0C–$1F93` | Core game, road IRQ handlers, interpreter, event definitions, play counters and four track descriptors. |
| `$2300–$377F` | Sprite graphics for pointers `$8C–$DD` in VIC bank zero. A shape starts at pointer × 64. The VIC reads 63 image bytes, three per row for 21 rows. |
| `$3800–$3FFF` | Character workspace. `$8602` copies the title set from `$5D00` or road set from `$6500`. |
| `$4000–$47DB` | Five dashboard rows, glyph-colour lookup, and the 75 road strips. |
| `$4800–$4E87` | Road display setup, strip pointers, staged road rows, sprite updates and collision handling. |
| `$5000–$5A74` | Title music driver, working state, note and instrument tables, orders and pattern streams. |
| `$5A80–$6CFF` | Title-frame strips and the two multicolour glyph banks. |
| `$7D00–$864E` | Title sequence, message renderer, messages and joystick reader. |
| `$8700–$8E63`, `$C493–$CBF6` | Track streams. `$CBF7–$CFA8` is a byte-for-byte duplicate of `$8AB2–$8E63`, including the third track's event area and all five bands. |
| `$9000–$9407` | Sound effects driver, voice state and tables. The embedded N.H. credit starts at `$9246`. |
| `$A000–$C492` | Three unrolled left shifts for screen and colour RAM. The CPU port value `$36` allows execution in RAM below the BASIC ROM. |

### Register census

| Registers | Use | Instructions |
|---|---|---|
| `$01` | Selects the memory map for driving. | `$0D1B` |
| `$D000–$D010` | Sprite positions. Logical X doubles, the carry selects the sprite's high-X bit, and the carry path adds one to the returned low byte. Y copies directly. | `$4BA8–$4C68` |
| `$D011/$D012/$D016` | Raster line selection, display control and horizontal scroll. The road bottom sets zero fine scroll and 40 columns for the dashboard. | `$0D9A`, `$0DC4`, `$0E30`, `$0E9F` |
| `$D015/$D018/$D01C` | All eight sprites enabled and multicolour during the road. The character base within the bank is `$3800`. | `$4800` |
| `$D019/$D01A` | Raster acknowledge and interrupt mask. | `$0DC6`, `$0E32`, `$0EA1`, `$8307`, `$8334` |
| `$D01E` | Sprite contact latch. The bottom IRQ reads it at `$0ECD` and saves it at `$4CF4`. | `$0ECD/$0ED0` |
| `$D020–$D02E` | Border, field, shared sprite and per-sprite colours. | `$4800`, `$1378`, `$1388`, `$8305`, `$8332` |
| `$D400–$D418`, `$D41B` | SID voice, volume and filter output, and oscillator-source read for one sound effect mode. | `$5000`, `$9028`, `$91A7` |
| `$DC00/$DC0E` | Active-low joystick port 2 and CIA timer A stop during raster IRQ setup. | `$4CFD`, `$862E`, `$0D9B`, `$82DC` |

The road handlers chain through `$0314/$0315`. `$0DC4` applies fine scroll and schedules `$0E30` at line `$36` on the regular pass, or schedules `$0E9F` directly at `$D2` on a group-fetch pass. `$0E30` schedules `$0E9F` at `$D2`. `$0E9F` sends the next interrupt back to `$0DC4` at `$2C`. The initial installation at `$0D9A` uses line `$24`. Title handlers `$8305/$8332` alternate the title's raster split on the active branch.

## Track and object formats

- `$1F64`, `$1F70`, `$1F7C` and `$1F88` select four resident tracks. Each descriptor contains six high bytes followed by six low bytes. The first five streams supply strip IDs for the five vertical bands. The sixth supplies events. Each regular group contributes five columns. Each band has 153 group entries followed by `$FF`.
- Each strip at `$4200 + 20 × ID` is four rows of five glyphs, arranged row first. `$1008` copies each selected strip into a separate 20-byte staging band and then reads the event. The five staging bases are `$48EF`, `$4905`, `$491B`, `$4931` and `$4947`. `$495D` reads the same column from each staged row to update column 39. `$107C` requests another group when the last staged column has been used.
- `$1098` subtracts the scroll step from the fine-X accumulator and requests a coarse shift on wrap. `$A000` shifts visible rows 0–7, `$AEA1` shifts rows 8–12 and `$B7C6` shifts rows 13–19. Each row moves columns 1–39 to columns 0–38, for both glyph and colour.
- Before active play, `$194A` handles event `$63` by stopping the road and starting the opening scripts. Script command `$F8`, handled at `$1441`, sets active play at `$19D7` and sets the course-start flag at `$19D8` for a nonzero argument. During play event `$64` saves the current group minus one for a restart. A strip-stream `$FF` starts the finish scripts, which deliver control to the track change through `$0FBD`.
- `$17AF` uses the event index minus one to select one of 45 lists through `$147C/$14A9`. Each entry has nine bytes: X, Y, colour, sprite pointer, script ID, script-active state, road-scroll flag, projectile reaction and contact type. A following `$FF` ends the list. The destination rotates through traffic sprites 1–6. The player uses slot 0 and the shot uses slot 7.
- `$1458` selects object scripts with the split 48-entry address table at `$10EE/$111E`. Each ordinary action contains X and Y deltas. Values below `$32` add and larger delta values subtract the value minus `$31`. `$11F6` selects the command decoder at `$1283` for values at least `$E6` in the first byte position. Command handlers cover coordinates, shape, colour, repeats, scroll binding, effects, completion and one saved script-call frame per slot.

## Controls, resources and contacts

- Port 2 fire starts the title sequence through `$862E/$7E4E`. During active play `$4CFD` reduces the active-low direction bits to signed axis deltas and leaves fire in carry. `$1AB4` uses a fire latch to distinguish a new press. Up and down change logical Y within the comparisons against `$31/$C2`, while right selects scroll step two and can increment X below `$64`. Left selects step one and marks the player to follow the road at X at least `$28`. Terrain and some active scripts gate these controls.
- `$1B79` requires the shot slot to be free and ammo above the zero glyph `$E0`. It decrements ammo at `$1B87`, positions sprite seven six logical X units ahead, assigns script six, and requests effect `$0A`. The corresponding HUD cell is `$07AA`.
- `$1BB0` reduces the right gauge index on expiry of its `$78`-tick countdown. `$1C33` reduces the left GAS gauge on expiry of its `$64`-tick countdown. `$184D` fills GAS on contact type 1, and adds four right-gauge segments on contact type 2. Underflow in either timer path reaches `$1BD4`, which starts the crash script in slot 0 and clears the active-play flag.
- `$4C6B` needs both sprite bits in the collision latch and compares logical coordinates. Its acceptance interval is greater than the opponent's lower bound and at most its upper bound. Extents are ten logical X units and `$13` screen Y units. `$184D` uses it for the car, while `$1906` uses it for a projectile. Terrain contact is separate: `$4D1E` reads three cells near the front of the car, and `$1CC4` dispatches based on the centre cell.
- `$0F3F` dispatches score requests and slot-zero completion. An ordinary completion decrements the life digit at `$0F60` and restarts the round unless the resulting code is `$DF`. The initial life digit is `$E5`. Pause is requested with KERNAL key code `$04` at `$0E8E` and released by code `$03` at `$0F87`.
- Score increments happen at `$1DB8` and `$1DDC`, in the ones or hundreds place of the five mutable digits. The dashboard has a fixed trailing zero for each six-digit field. `$1E55` compares score and high score from their most significant digits.

## Text and sound

Title messages have a three-byte header for column, row and colour, followed by glyph IDs terminated by `$FF`. `$83CD` draws a letter from the four consecutive tiles beginning at its ID. It also accepts `$20` for a one-cell space. Rendering the message records against the title glyphs gave these starting IDs for the letters seen:

```text
A 00  B 04  C 08  D 0C  E 10  F 14  G 18  H 1C
I 21  J 25  K 29  L 2D  M 31  N 35  O 39  P 3D
R 45  S 49  T 4D  U 51  V 55  W 59  Y 61
```

`$A5` draws a blank two-by-two group in several messages. Message IDs `$1B/$1C` read GET READY, `$1D/$1E` read GAME OVER, and `$1F/$20` read WELL DONE. The dashboard digit glyphs `$E0–$E9` come from the road glyph set and encode 0–9.

The active title raster handler calls `$5000`. Its initialization command uses the upper nibble of `$55F4` after clearing bit seven to select a group of three voice-order pointers. The title sets `$87` at `$7E0C` and `$A7` at `$8070`. The driver has pointer groups at offsets 0, 6 and 12 in `$5674`. These two call sites select groups 0 and 2. `$9028` is the independent road effects driver. `$4DE2` routes a global effect request to separate per-voice requests at `$02A7–$02A9`. The second pitch mode four reads oscillator 3 at `$91A7`, masks the read from `$D41B` with `$0F` and adds it to the voice byte at `$921C+X` before the high frequency write at `$91B0`. Dummy audio leaves audible behaviour and variation in the oscillator value open.

## Live verification

- Execution stops at `$0DF6`, `$0E44` and `$0ECA` captured accumulator values `$36`, `$D2` and `$2C` immediately before the raster-line stores. The corresponding next IRQ vectors were `$0E30`, `$0E9F` and `$0DC4`.
- Stopping at `$0ED0` and `$0ED3` showed the read collision value in A and the same byte stored at `$4CF4` in the observed pass. The sampled value was zero. The contact classification is supported by the code.
- From the same driving snapshot, four neutral frames reached four input updates and zero ammunition-decrement instructions. Port 2 fire reached `$1B87` with ammo `$E9`, then `$1B8A` with `$E8`. The call at `$1BA0` had X=7 and Y=6.
- Setting the gas timer to one reached the DEC at `$1C40`, changed segment index `$0A → $09` and reloaded the timer to `$64`. Setting the right-gauge timer to one reached `$1BC6`, changed its index `$0F → $0E` and reloaded `$78`.
- Stops at `$1DB8` and `$1E15` observed the ones digit advance from `$E0` to `$E1` during a score update. The first four digits stayed at `$E0`.
- The title music stop at `$504D` captured an accumulator of `$1F` for the SID control store. This establishes a register write under dummy audio.
- The resident course setup at `$0D43` was used with selectors two, three and four. Each reached active play, with `$19D7` equal to one. These tests use direct initialization for each course.

- Stops at `$8614` and `$862D` bounded both character copies. The title copied `$5D00–$64FF`, and the road copied `$6500–$6CFF`, each to `$3800–$3FFF`. At return from the road copy the next pointers were `$6D00` and `$4000`. Stops at `$7D0F` and `$480F` confirmed the VIC character offset `$3800`.
- The title loop at `$7D62` used X from `$00` through `$4F` and left at `$7D6D` with X equal to `$50`. The dashboard copy at `$4E75` used X from `$C7` down to zero and returned at `$4E87` with X equal to `$FF`.
- Injecting effect request 1 at `$9028` reached the initializer at `$905B` for voice offset zero. The gate duration stored at `$9096` was `$18`. The value at the control write at `$90C3` was `$25`, matching the cached control byte. Stops at `$91A7`, `$91AA` and `$91B0` verified the mode-four read and calculation. With dummy audio the observed oscillator byte was zero and the SID high-byte write carried the base value `$53`.

## Coverage and retained bytes

The ledger starts with the final depacker's complete `$0801–$CFFF` output. The `$3800–$3FFF` live character copy and trainer/screen workspace are excluded with their producers documented. RAM above `$CFFF` contains the depacker's input tail. The exported symbols explain all 49,151 tracked bytes and the listing has zero uncounted stretches. Retained payload outside the active tables stays in the count.

- `$6D00–$7CFF` is a 4 KB patterned payload common to Roadburner and Speedy. Of its 2,048 odd-address bytes, 2,011 are `$00`, `$40`, `$BF` or `$FF`. The dominant byte changes at page boundaries. The tail at `$5C10–$5CFF` matches 177 of 240 bytes at the corresponding offsets in page `$79`. Those similarities extend beyond the bounds of the title screen and character-copy loops.
- `$4E89–$4FFF` and `$9D79–$9FF6` contain another family of repeated patterns. The halves at `$4F80` and `$9D80` match at 124 of 128 offsets. The code at `$4DDE` restores X from `$4E88`. During four 60-frame driving probes, execution hits at `$4DDE` matched all the reads recorded at `$4E88` and there were zero reads in `$4E89–$4FFF`.
- `$3780–$37FF` occupies two sprite slots beyond the `$DD` maximum in the direct assignments, event lists and script shape commands. `$40C8–$40FF` follows the 200-cell dashboard. `$47DC–$47FF` follows the last strip, whose pointer is `$47C8` and whose fetch length is 20. `$5A75–$5A7F` sits after the final pointed-to music pattern's `$07` order advance and before the title frame. The probes recorded zero CPU reads in these tails.
- Store watchpoints at the first byte of each of the eight retained ranges above stopped with PC `$01A9`, after the final depacker's store at `$01A6`. The destination operand, accumulator and written RAM confirmed each write. The range scan found no fixed CPU operand that reaches the 4 KB block. The indirect character-copy operands and the VIC bank and character pointers put the active glyph data elsewhere. The title and four driving probes recorded zero CPU reads in the patterned payload. The original source of the patterns and the tails remains open.

## The listing's error rate

The independent gpt-6.2-sol checker drew 65 of 804 comments using seed 1119062 and found 9 errors. The estimated error rate for that draw was 13.8%, with a 95% Wilson interval of 7.5%–24.3%. The weighted estimate was 13.6%. The checker may have missed errors. All nine findings were corrected, including three script sequence descriptions, the road IRQ's pause branch, the strip-band index, steering during script countdown, the title pitch ornament, the fourth track's event tail and the effect pulse sweep. The script-description fix also preserves repetitions in the rest of that family.
