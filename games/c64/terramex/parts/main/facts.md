# Expedition

## Display, controls and time

The expedition IRQ at `$8796` dispatches six internal jumps from `$87C0`. It banks I/O in during each phase and restores the saved port value at `$8939`. The playfield uses two screen matrices at `$4000` and `$4400` and switches which one the VIC sees. `$8942` reads the scene's scroll constraints, consumes a pending scroll step, and swaps the display and hidden-screen pointers on a character boundary. `$8E17` and `$91D7` move colour RAM in the two horizontal directions and fetch the replacement colour from `$1800`. The inventory raster reads the colour indexed by item ID from `$82CA` at `$9526` and writes it to the VIC at `$9529`. This lookup shares bytes with the selector-dependent copies beginning at `$82C2`. Empty inventory slots use colour index `$7F`. The HUD split at `$8D31` changes to the character set at `$7800`. The playfield character sets are based at `$4800` and `$5000`. The VIC bank is set by CIA2 at `$8087`.

At `$9607` the game tests CIA1's active-low joystick bits and prefers port 1 when it is active. Table `$9679` translates the physical inputs into right, left, down, up and fire bits, in order from bit 0 to bit 4. The fallback scanner `$96CD` drives one matrix axis, waits for stable input and checks the other direction for a zero result. The in-game keyboard legend points at the following controls.

| Key | Function shown on title |
|---|---|
| Z and X | Left and right |
| P and L | Up and down |
| Space | Leap |
| T | Think |
| S | Swap item |
| 1 and 2 | Scroll items |

The title legend at `$A168` is stored as PETSCII with carriage return and a zero terminator. `$8666` subtracts `$20` to convert printable bytes to character numbers in the rendered title charset. Thus `$20` is glyph `$00`, digits occupy `$10–$19`, and uppercase A–Z use glyphs `$21–$3A`. The glyph source is eight bytes per character at `$7800`. The live title uses the same routine to switch the status field between music and effects.

`$86D2` decrements the clock through minutes at `$0365`, hours at `$0364` and days at `$0363`. It skips decrement when the mode flag at `$03E5` is set and otherwise uses a phase bit in `$03E6`. `$DEE9` prints the three fields. The score at `$0376–$0377` is a binary word. `$E43B` adds a binary word and updates the screen, and `$E456` checks the word against the high score at `$0308–$0309`.

## Map, objects and explorer

`$9A3B` groups scene numbers into groups of twelve. `$9815` expands 32 tile IDs per strip from `$3500`; a tile at `$0800 + 16 × ID` contributes four rows of four glyphs. The expanded rows have a 448-character stride. `$9A83` copies the visible subset into both screen buffers and fills colour RAM. `$9D27` swaps 128 terrain colour entries between `$1880` and `$3E00` when the terrain mode changes. `$9D3A` animates an eight-byte glyph in the normal charset or two glyphs and two additional pixel rows in the alternate charset.

`$C2E7` expands packed actor definitions from `$C6E5` into the active map group's 14-byte actor records at `$C0EF`. `$C3A2` dispatches each occupied actor through the table at `$C45F` and writes back its position and sprite state. Scene-specific overrides are dispatched by `$BAED` through the word table at `$BB1B`.

`$D042` expands pairs from the two pickup placement tables at `$D142` and `$D1D2` into four-byte records at `$D262`. `$BEA9` handles a nearby available pickup if the 27-slot inventory has room. The held item lives at `$0328`. The inventory update at `$BCDD` checks key index 1 and swaps the held item with the selected slot. The player update at `$CB8A` uses the terrain passed back by `$DF28` and produces a player action. Action `$036E` selects a word at `$D2C3` and a phase counter lives at `$036F`. The leap path at `$DB0D` uses pose and vertical step tables and can scroll or cross a horizontal scene boundary.

Sprite records at `$F036` store three columns, 21 bytes each. `$A310` computes the source as `$F036 + 63 × frame` and interleaves the three byte columns for the VIC. Mirroring reverses the order of those columns and the order of the four two-bit pixels within each byte. `$9E21` generates the byte reversal table at `$0200`.

## Hardware register census

| Registers | Role | Writes or reads |
|---|---|---|
| VIC `$D000–$D010`, `$D015`, `$D01C`, `$D025–$D02E` | Position and colour for playfield and multiplexed HUD sprites | `$87D8`, `$9505`, `$957E` |
| VIC `$D012`, `$D019–$D01A` | Raster compare, acknowledgement and enable | `$8796`, `$8936`, `$8D60` |
| VIC `$D016`, `$D018`, `$D020–$D023` | Fine scroll, screen and charset selection and the playfield/HUD palette | `$87D8`, `$8D31` |
| CIA1 `$DC00–$DC03` | Joystick pins and keyboard matrix | `$9607`, `$96CD` |
| CIA2 `$DD00`, `$DD04–$DD05`, `$DD0D–$DD0E` | VIC bank and NMI timer | `$8087`, `$872F` |
| SID `$D400–$D418` | Voice pitch, pulse width, waveform, ADSR and filter/volume | `$A467`, `$A53D`, `$A596` |

Sound init `$A53D` installs the sequence, resets the voices and sets the active flag. The interpreter at `$A623` uses the track sequence pointers at `$AC5A` and pattern pointer tables at `$AD5A` and `$AD7F`. The unused paths and exact semantics of some sound commands remain open. VICE ran with dummy audio, so live SID evidence is register access rather than an audible comparison.

## Live instruction and store checks

The idle, right and fire probes used separate restores of the opening gameplay snapshot. Each advanced 12 VICE frames, which contained 66 entries at the raster vector, 11 passes through `$CB8A` and 11 port-2 scan entries at `$9623`.

| Input | Movement trace | Position after |
|---|---|---|
| Idle | Zero executions at right movement `$CC7A` and leap start `$CC53`. Zero stores to X at `$836A`. | X 11, Y 96 |
| Right | Eleven executions at `$CC7A` and eleven stores to X. | X 22, Y 96 |
| Fire | One execution at `$CC53`, followed by ten leap updates at `$DB0D`. | X 11, Y 81 |

All three trials counted six stores to `$0365` and went from day 30, 20:46 to day 30, 20:40. This agrees with the alternate-pass clock update from the captured phase. A separate 18-frame title snapshot run counted 102 raster IRQ entries, 51 entries to the voice event decoder at `$A623`, and 17 executions of each of the stores to the SID voice 1 frequency low byte and to SID volume at `$A47B` and `$A51A`.

## Bytes retained at disk handoff

The entry image holds a cassette bootstrap assembled for `$0400` at `$4000–$4169`. Its code installs IRQ and NMI entries and assembles incoming bits with CIA timing. The NMI vector and delay call point at `$054B` and `$055B`, corresponding to offsets `$14B` and `$15B` within the stored image. On the disk entry route the title clear at `$9FEB` writes to `$4000` before that matrix is used for the display. A store watchpoint after restoring the `$8049` snapshot stopped on that clear. The two bytes `$33 $26` immediately before the image are part of the unpacked range. Their role is open.

The second terrain and HUD code set starts with the tail of a clock renderer at `$E51D`. Its two terrain classification tables at `$E6EA–$E8E9` match `$E0BC–$E2BB` byte for byte. Several of the copied instructions retain old entry addresses. The copied terrain action branch points to `$E239`, now terrain class data, and the copied character output calls point to `$8673`, now an operand inside the emitter at `$8666`. The disk image retains the bytes through the second decimal constants at `$EB43–$EB4A`, followed by a short literal tail and zero fill. Write watchpoints during the `MAIN` depack observed zero stores to `$EB52` and `$EEFF` from the same depacker loop.

In a 12-frame restore from the opening gameplay snapshot, execute checkpoints counted 66 raster IRQs, 11 calls to the active terrain probe at `$DF28` and zero entries to the copy at `$E556`. A conditional read watchpoint attributed 33 accesses in `$830A–$8369` to `$9526`, with 33 matching stores by `$9529` to `$D027–$D029`. Those counts describe the observed opening scene.
