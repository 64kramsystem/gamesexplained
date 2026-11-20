# Kendo Warrior facts

## Startup and memory

- The Hokuto Force and DCS releases both reach `$0880` with the same engine prologue. Their first handover snapshots match across most of the address space. The trainer screen and release startup memory below `$0880`, screen area `$4400–$47FF` and active character buffer `$4800–$4FFF` differ. Within the engine region the handovers differ at `$3C8E` and `$43FF`. The tail of the CPU's top page also differs. At `$3C8E`, Hokuto Force and the original tape have `E5 4E` (`SBC $4E`). DCS has `E9 4E` (`SBC #$4E`), which subtracts 78 from the actor energy instead of the passed damage value.
- `$0880` sets `$01=$35` before enabling the raster interrupt. The game IRQ entry is `$08FF`. In play its software dispatch writes the target at `$097E–$097F`. The executed checkpoint at `$097D` observed `JMP $0980` for the upper stage.
- `$0D39` writes two to the low bits of `$DD00`, selecting VIC bank `$4000`. The screen is at `$4400`. The IRQ selects character planes at `$5000` or `$5800` in the viewport and `$4800` in the panel. At `$3D78` and `$3DAE` the game copies distinct source charsets to `$4800`.
- In gameplay the active actor sprite state uses two layouts. Attribute arrays at `$0210–$0257` feed `$0BE6`, which permutes their slots into `$0BB6–$0BDD`. The IRQ then writes that cached order to the VIC and `$47F8–$47FF`.

## Input and display

- A stopping load watchpoint on `$DC00` with joystick port 2 right held caught the game just after `LDA $DC00` at `$0EBD`, with A equal to `$F7`. The `$0EC2` and `$0EC8` execution stops showed A equal to `$08` after inversion and before the store to `$38`. The action update indexes its tables with this active-high value.
- The panel text comes from little-endian pointers at `$1B2B`. `$1A5B` writes 24 character cells per message. The gameplay panel glyphs at `$F000` use ASCII positions for uppercase letters `$41–$5A`, digits `$30–$39` and space `$20`. The renderer's asterisk is `$2A`. The last line moves up when complete.
- Room number `$026A` selects a forty-tile record through `$2375`. `$20DA` takes each tile number through the pointer directory at `$23F5` and writes its sixteen characters into a four-by-four rectangle. Some tiles are substituted according to device state. `$21AF` maps the resulting character numbers to colour RAM with `$2215`.
- `$3C42` draws the two sixteen-cell energy bars from `$0264` and `$0265`. `$3C12` draws the operative count from `$1B`.

## Hardware references

| Register | Reader or writer |
| --- | --- |
| `$D000–$D010`, `$D027–$D02E` | Sprite positions and colours in `$0C0D` and `$0C4C`. |
| `$D011–$D012`, `$D016`, `$D018–$D01A` | Raster synchronization, IRQ scheduling and display modes in `$0880–$09E0`, `$0B07` and `$0B2A`. |
| `$D020–$D026` | Border, backgrounds and shared sprite colours in the IRQ, title and play setup. |
| `$D400–$D418` | The driver entered through `$BBFF` sends oscillator, envelope, filter and volume values. |
| `$DC00–$DC01` | Port 2 joystick in `$0EAF`, keyboard matrix scan at `$0F59`, and a dedicated inventory key check at `$2726`. |
| `$DC0D–$DC0F`, `$DD0D–$DD0F` | Both CIAs' interrupt masks and timers configured at startup. |
| `$DD00`, `$DD02` | VIC bank selection in `$09F1` and `$0D39`. |

## Movement and combat

- The active-high joystick bits are up `$01`, down `$02`, left `$04`, right `$08` and fire `$10`. `$277B` maps them to the player action in `$0261` when no action is active. Left and right share actions and set facing independently through `$29D1`. `$2837` chooses the three-sprite frame script for the action and facing. `$286E` chooses the trajectory bytes separately.
- `$24BD` examines the position and, for up and down, the stick. Its four slots in `$25BE` are west, up, down and east. A destination with bit seven set is rejected. For vertical exits the current player sprites move out before the new room is drawn.
- Player attacks are checked by `$2CE5` and opposing attacks by `$37F5`. Each sets up an attack band in the comparison scratch at `$0200–$020F`. `$0CFF` compares the horizontal edges as pairs of bytes and the vertical edges as bytes. A landed player attack selects its damage row according to actor type, then indexes it with the action. Each attack path has its own repeat delay.
- The replacement sequence decreases `$1B` at `$3B0B` and takes the failure branch when it becomes negative. `$3A3C` initializes the count to four on a new game. The player and actor energy bars are separate at `$46B4` and `$47CC`.

## Room objects and mission

- `$1182` recognizes an entry into a particle barrier by side and player X. Barrier codes three and up select a counter beginning at `$02CC`. An available charge is used before action `$0D` is installed. When the matching counter is zero the game selects hit action `$0B` and queues a message giving the required shield.
- `$10B6` checks inventory flags before installing the room's visible item sprite. `$1596` handles interaction with the alarm, gas switch, fuse panel and safe. Fuse flags select the installed fuse message through `$160D`. The panel text also names cobalt, rubidium and uranium shields, wire cutters, a pipe wrench and the digital sequencer.
- The safe logic starts at `$1616` in room `$15`, after the position gate at `$1596`. `$141C` displays digits generated by the random routine and advances a four-digit progress counter. The sequencer and manual modes have different advancement and success tests. Failure sets a lock countdown of `$FA`, decremented on eligible update passes. Success sets the document flag at `$02BC`.
- `$197F` handles extraction in room `$3F` when the documents flag is set and the current actor is clear. It starts four actor encounters and then the helicopter sequence. Once the helicopter is in position, the player must be in the horizontal pickup band and in a non-attacking action. The exit path checks the mission flag at `$3AF5`.

## Sound

- `$BBFF` enters the SID player. `$BC02` requests music and `$BC04` requests an effect. Four tune descriptors begin at `$C5C8`. Tune one is requested by the title, tune four by new-game setup and tune two by mission setup. The tune-four order lists contain three intro patterns and point into the tune-two lists at their loop markers. The runtime caller for request three is open.
- Eight effect streams are addressed through `$CCE9`. The effect with the lower nonzero ID may replace the one currently playing. Effect output uses hardware voice three. The four software voice states in page `$BC` preserve the music voice even when the effect owns its SID output.
- Music pattern events use bytes below `$80` for notes and a computed routine table at `$C200` for commands `$80–$9F`. The pitch-offset, duration, envelope, pulse-width and modulation code account for the changing oscillator values. `$C240` tests the high order byte for a loop marker.
- The `$BA00–$BBFE` transfer suffix is present byte for byte on the Byte Back tape and the Hokuto Force and DCS disk handovers. A store watchpoint on the original's tape loader counted 511 writes. The room maps end at `$B9FF`, the SID entry starts at `$BBFF`, and the suffix includes a zero run and a 256-byte `$65` run. Its two nonuniform segments have an open original purpose. They remain in the listing and in the ledger.

## Live instruction tests

- A 60-frame neutral baseline hit the IRQ entry 120 times and each of `$0980`, `$09BC`, and `$3BDA` 60 times. The store watchpoint on `$D018` counted 120 writes.
- From identical play snapshots, stops immediately before and after `STA $38` at `$0EC8` confirmed neutral, right and right with fire as `$00`, `$08` and `$18`. Stops at `$2780` also confirmed right, up, diagonal up-right, down, diagonal down-right, fire-right, fire-up-right, fire-down-right and fire-down select actions one through nine in that order.
- At the inventory's `$DC01` read, the value was `$FF` with I up and `$FD` with I held. At the following branch `$2730`, the mask yielded two and zero respectively.
- A synthetic left-barrier encounter entered at `$1182` with barrier code three and matching counters of zero, one and two. A store watch on `$0261` caught action `$0B` for zero and `$0D` for either positive counter. The counters afterwards were zero, zero and one.
- At the return from `$3C42`, setting player energy to 0, 1, 15 or 16 produced that many filled cells in the sixteen-cell bar. Cells after the energy value held the empty glyph.

The instruction tests and snapshots are in the ignored `work/` directory. The original tape comparison is held at `$0880`. Its entire `$0880–$3EF4` engine interval and `$BBFF–$CD74` sound interval match the disk listing bytes.

## The listing's error rate

Seed 641989 drew 85 of 977 line comments. The independent gpt-6.2-sol checker found nine wrong details. The observed rate was 10.6%, with a Wilson 95% interval of 5.7% to 18.9%, and the estimate weighted by stratum size was 8.9%. The findings concerned panel padding, device pointers, motion phases, a debug rectangle, actor action and frame limits, the SID's pulse command, the order-loop path and effect release timing. All nine were corrected, including related comments generated from the same descriptions. The sample estimates the pre-correction listing's rate and can miss errors.
