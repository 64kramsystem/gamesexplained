# Facts

Evidence below refers to the Kurt release in `orientation.md`. Live instruction and state checks can be rerun locally with `PYTHONPATH=kit/c64 python3 games/c64/mermaid-madness/work/trace-checks.py` against the paused-capable headless build. Those tests start from a snapshot and several deliberately inject small state changes to isolate a branch.

## Engine and memory

| Address | Role and evidence |
|---|---|
| `$4000/$4006` | Cold entry and gameplay scheduler. The entry installs the IRQ. The main loop waits at `$4C9E` for line 200 before updating play. |
| `$0314/$41E9/$41F2` | KERNAL RAM IRQ vector, IRQ entry and mutable dispatch operand. The live operand cycled through `$421F → $42F2 → $439E → $421F` at lines 0, 90, 180 and 0 with the vector held at `$41E9`. |
| `$0400`, `$D800` | Screen and colour RAM. The HUD uses the upper screen cells. The playfield renderer writes both planes for each metatile. |
| `$1000–$1FFF` | Initial room tile map. The redraw loops across 16 tiles and down eight rows with a stride of `$80`. The entry snapshot contains the map before the engine's room patches. |
| `$2000–$224F` | HUD glyphs and panel border glyphs. `$4057` chooses graphics at `$2000` for the screen. The rendered glyph rows show A–Z at `$01–$1A` and the usual screen-code punctuation in the `$20` page, including space `$20`, ! `$21`, % `$25`, / `$2F` and digits `$30–$39`. Borders occupy `$40–$49`. Code `$00` is decorative. |
| `$6000–$7FFF`, `$8000–$87FF` | A 32-byte bitmap definition per metatile, then eight 256-byte attribute tables. `$450F` splits a tile index for two 16-byte copies and fetches four screen bytes and four colour RAM bytes. |
| `$A000–$BFFF` | 128 addressable 64-byte frame slots. `$537D` splits the frame index to select the low byte at `$4A1B` and the page at `$4A1F`. The calling routines select the individual player, gauge and creature shapes. |
| `$D000–$DFFF` and `$E000–$EFFF` physical RAM | All 4,096 bytes are equal at hand-over. Startup store checkpoints hit both ranges in the second depacker with `$01 = $34`. I/O and KERNAL cover them during play at `$01 = $36`, and VIC bank zero cannot fetch them. The comparison release has different bytes there. |

## Text

The small display uses a custom font with familiar screen-code letter positions. The stored item labels and credits use uppercase ASCII-range bytes. The draw loops at `$52BF` and `$C10A` subtract `$40` from bytes at or above `$40` before writing the glyph codes. The inventory names at `$5C7B` are concatenated as TYRE, D/MITE1, D/MITE2, D/MITE3, ANKH1, ANKH2, PEARL, SALT, CHEST, LANTERN and TORCH. Pointers begin at `$5C65` and lengths at `$5CB8`. The title stream at `$C12D` uses `$FE` to advance the destination row and `$FF` to finish printing. This variant includes a Kurt credit and a greeting.

## Movement and room state

- CIA1 port A at `$DC00` supplies active-low joystick port 2. `$47CF` reads directions. A right press yielded A = `$77` after the read and A = `$07` after masking. Stepping `$4852` and `$4854` increased player X from `$F6` to `$F7`. The four direction instructions are selected by consecutive shifts at `$480C`, `$4820`, `$482A` and `$4845`.
- The room column and row offsets are `$59 = 16 × column` and `$5A = 8 × row`. The engine limits the offsets to `$70` and `$18`. `$5592` forms the room ID from `($59 >> 4) + $5A`. `$559E` uses a four-byte visited bitset at `$4447`; an unset bit earns one BCD point through `$4F93`.
- In swim mode, `$4C3C` waits out a timer reset by Up input, then passes two synthetic Up inputs through the terrain filter and movement code. `$5698` separately applies bobbing during prescribed surface-room states.
- The first two opening animations are independently advanced by Myrtle's state machine at `$4A72` and Gordon's at `$53DA`. The captured title and promenade show both sides of the fire-to-start transition.

## Objects, damage and score

- `$523C` tests the fire bit and a one-press latch. Its drop branch tests two visible room slots. A traced drop of lantern index 9 in room `$14` wrote `$94` to its packed room/present byte and `$80` to the held slot. `$5767` uses recorded sprite overlap on pickup and rejects lit dynamite. `$C1DD` resolves contact with both item sprites by testing coordinates.
- `$45E9` tests for item 9 in the held slot or either visible item slot when the room is `$14` or `$1C`. An isolated call with room `$14` and empty slots produced dark flag 1 when empty-handed and 0 with item 9 held. The renderer zeros the cell attributes with that flag set.
- `$5ACB` arms dynamite on landing, with `$C8` ticks and its room ID. `$5AED` checks whether the player is in the blast room, and sets energy to 0 and end pending to 1 at `$5B12–$5B18`. A stopping checkpoint and instruction steps confirmed those writes using one tick remaining. The map patch table targets rooms `$1C`, `$14` and `$10`.
- `$52EF` filters the sprite collision latch before subtracting energy at `$532A`. The energy byte at `$24` starts at `$FF`. `$5101` consumes a visible stout bottle on an allowed overlap plus fire, adds `$20` and saturates at `$FF`. The bottle graphics use the high three bits of energy at `$533C`.
- The air counter at `$4422` starts at `$7F`. `$5228` reloads the prescaler to `$C0`, decrements the counter and sets end pending on underflow. Stepping the routine with the prescaler at 1 and air at 0 produced `$FF` and end flag 1. `$5217` derives the needle frame from the air counter's high nibble.
- The heart delay between animation loops comes from the room-indexed table at `$5C38`; a second table at `$5C5E` controls the time between frames by map row. An end animation takes a separate path at `$53A2`.
- `$514A` starts the rescue when item 10 has room ID `$19` and the player is there. It clears three map tiles, locks player movement and adds eight points. `$517E` advances the motion table at `$51C4`. The terminator raises both the completion flag and end pending. This is traced in code.
- `$C047` retains the higher packed-BCD score at `$4450`. The reset loop's cleared block ends before it. The captured title of this release begins with 35% already displayed as the high score.

## Register census

| Register group | Game use and sites |
|---|---|
| `$00–$01` | Processor banking at `$4057–$405B`. Play uses `$36`. |
| `$D000–$D010`, `$D015`, `$D017`, `$D01C–$D01D`, `$D025–$D02E` | The three raster bands share sprite hardware. The upper handler assigns HUD positions and colours. The playfield handler uses those registers for player, actor, enemy and object sprites via `$4969`, `$54D8`, `$4EF1` and `$563B`. |
| `$D011–$D012`, `$D016`, `$D018–$D01B` | Selects display mode, schedules raster changes, selects graphics base and acknowledges raster IRQ. Setup is at `$4057` and `$41BF`. Runtime band changes start at `$421F`, `$42F2` and `$439E`. |
| `$D01E–$D01F` | Sprite and background collision latches read by the IRQ and by the gameplay contact logic. |
| `$D020–$D021` | Border and background colours. The raster phases supply black for the HUD and blue or light blue in parts of the playfield depending on room state. |
| `$D400–$D418` | SID voice frequencies, controls, envelopes, pulse widths and mixer settings written by the music and effects routines. `$9000` and `$9001` receive requests. Raster code invokes `$9005` when sound is enabled. |
| `$DC00/$DC01` | Active-low joystick directions and fire at `$47CF`, `$5242` and `$53D0`, and the sound toggle's bit-4 read at `$43B8`. A held Space press stepped through `$43CC` and changed the sound flag from 0 to 1. |
| `$DC0D` | Timer IRQ mask and pending flags handled at start-up at `$41E1` and `$41E4`. |

## Bytes outside the gameplay ledger

The metatile attribute readers use an eight-bit tile index into the eight pages at `$8000–$87FF`. A full redraw of room 1 made 1,024 loads there. An adjacent watch on `$8800–$8FFF` recorded zero loads. The decoded indirect readers use the address tables for the bitmap, sprite banks, creature paths and item names. The exact origin of the retained bytes at `$8800–$8FFF` is open.

The sound driver's indexed reads adjacent to `$99A5` use X equal to 0 or 2 for pitch pairs and an X masked to two bits for envelope selection. The retained bytes from `$99A5` through `$99FF` include KERNAL I/O code and have no decoded entry from the driver. A loader watch caught stores to `$CC80` at post-store PCs `$082D` and `$0147`. A playfield redraw triggered neither a read nor execution watch in `$CC80–$CFFF`. The alternate release carries different bytes there.

The run kept a store watch on `$01` and an execution checkpoint at `$FFD5` during a 90-frame swim sample. Neither fired. The bank store positive control fired at the cold entry, where effective `$01` became `$36`. The room transition and redraw code uses the resident map.
