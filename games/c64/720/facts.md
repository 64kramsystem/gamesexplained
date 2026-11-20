# 720° analysis facts

The addresses refer to RAM in the C64 Comics Group release, after its final unpacker jumps to $0850. The handover and first city frames are in the local work directory. The C64 game credit identifies Chris Butler, and the title shows U.S. Gold (1987) and Atari Games (1986).

## Start and display

- The title routine at $0E09 composes the seven ranked scores, credits and a four-sprite logo. At $0E53 it waits for port 2 fire to be released and at $0E5A waits for bit 4 of $DC00 to go low. The title and city capture show the two states either side of that gate.
- The game chooses VIC bank $C000 via $DD00. $D018 uses $F400 as its forty-column character screen and $F800 as its glyph generator ($39B9–$39DA). The entry image contains a title-screen template at $F400. City rendering replaces the first 19 rows with a scrolling view, leaving the lower rows for the status panel.
- $39FC sets the IRQ hardware vector to $3A3B and the NMI hardware vector to $3A3A. The IRQ prologue saves the registers and jumps through $12–$13. Stops at $3A47, $3A81 and $3AA9 confirmed those dispatch addresses in order during the city raster chain. They change coarse VIC mode, split the sprite-pointer settings and reapply fine scroll. $3AA9 increments the counter that $39F0 uses to pace the foreground.
- $D000–$F3FF contains 144 sprite slots, each 64 bytes, fetched from the selected VIC bank. A slot holds 21 rows of three pixel bytes. The skater's two layers use sprite slots 0 and 1 and the separate shadow uses slot 2. The title logo uses four expanded sprites with pointers $BA–$BD. The sprite atlas was rendered from the handover bytes.

## Tile map and controls

- $4000–$BFFF is a 256-column by 128-row matrix of custom VIC character codes in memory. $3096 and $30AA form a map pointer using the column as its low byte and the row plus $40 as the high byte. $3848 writes the viewport into the load operands of 19 row-copy loops. In the live trace at $38E9 the first row's operand was $6E4B. With Y=$27 the instruction read $6E72 and the next instruction wrote that tile to $F427.
- $35B2 maps tile IDs to gameplay actions. The high bit controls skater sprite priority. The low code selects movement factors, obstacles or special actions. The three table directories at $33CE, $33F2 and $3416 choose Y motion, acceleration and two-sprite facing frames. $326E moves the skater using signed arithmetic and $36F8 updates the viewport within the course's bounds.
- Port 2 is active low. $30C1 checks the fire latch at $3E9E. On a fresh press it records takeoff facing and sets vertical motion, using the shoes upgrade to select an offset. $310C–$318E maps the bottom four bits of $DC00 into eight facing indices. $2FBD counts changes in facing in the air. $2F8D tests the shortest distance around the eight headings at landing and compares it with the helmet level.
- Tile $CA invokes the park entrances at $1C9B. The code selects by the skater's world position. The visit guards at $3EA4–$3EA7 are cleared per round and set by the respective park on return. Each park spends one ticket and increments $3EB0. Four started parks send the city loop back to round setup.
- The compact city overview is two 20-by-19 grids at $3B85 and $3D01. Tile action $10 and a clear cooldown permit $0A1F to display it. $0AF8 chooses one of six marker locations from the current skater coordinates.

| Event | Entry | Result calculation |
|---|---|---|
| Jump | $1D14 | Separate packed-BCD clock at $3EAC, medal meter increased by trick values. Finish tile $CC or an empty clock ends the course. |
| Downhill | $1F51 | Timer bar decreases through $206C. A finish or empty bar ends the course. The threshold branches use $10 and $20 while the bar is draining. |
| Slalom | $20EB | $24AA checks the neighbourhood for gate tile $D1 on contact with tile $D3. It changes scored tiles to $D2 and adds two bar units per tile. |
| Ramp | $220B | Separate packed-BCD clock and the ramp-drop routine at $2300. The scoring path adds manoeuvre values to the medal meter. |

## Money, scoring and the city timer

- $3E8F–$3E90 hold four packed-BCD score digits, high then low. The status panel and title rank display append two zero glyphs. $155D adds score and compares against the threshold table at $1529. It advances the milestone while capping the held tickets at four.
- $3E9A–$3E9B hold the packed-BCD cash balance. The first session sets it to $0100. $2E11 subtracts the current round's shop price, leaving the balance unchanged on borrow. Shop order at $1C67 is helmet, shoes, board, pads. Helmet affects facing tolerance, shoes takeoff velocity, board speed ceiling and pads crash recovery.
- $1E7E multiplies the selected packed-BCD prize at $1F22 by the round index plus one. $0964 drains remaining cash into points when play ends.
- $15CC drains the city timer bar through selected raster-counter values. On expiry it activates the chaser flag and draws SKATE OR DIE. $2839 moves the pursuing actor toward the player on both axes and requests the continue or game-over path on contact.
- $0BCD shifts the ranked scores and eight-glyph names to insert a new result. $0C58 lets the player choose characters from a circular 32-entry strip with the joystick. Glyph $F5 acts as backspace and $F6 ends selection.

## Character codes

The table was rendered from $F800. Each glyph occupies eight consecutive bytes and its screen code is the glyph index.

| Code | Use |
|---|---|
| $20 | Blank in the ordinary text rows. |
| $84–$9D | A through Z in order. |
| $9E–$A7 | 0 through 9 in order. The game also selects some digit-shaped glyphs as letters in stored text. |
| $A8 and $EC | Draw the full and partial timer cells. $1664 rewrites the eight bytes of $EC at $FF60. |
| $F5 and $F6 | Backspace and finish in the name-entry strip. |
| $F7 and $F8 | Copyright and full stop in the title credits. |

## Hardware accesses

The full register census and separate instruction traces are in `work/census.txt` and `work/city-trace.txt`. I/O is visible in the observed play state (banking bits $05).

| Address | Use |
|---|---|
| $01 | $3A10 clears the KERNAL mapping bit so the hardware vectors in RAM are active. |
| $D000–$D010 | VIC sprite coordinates. $2539 projects visible actors and $3782 projects the skater and shadow. |
| $D011/$D012/$D016 | Raster split schedule, screen mode and horizontal fine scroll. |
| $D015/$D017/$D01B–$D01D | Sprite enable, size, priority and multicolour configuration. |
| $D018 and $DD00 | VIC screen and glyph addresses and bank selection at $39B9. |
| $D019/$D01A | Acknowledge and enable VIC raster interrupts. |
| $D020–$D02A | Border, background and sprite colours. |
| $D400–$D418 | SID voice and filter registers, updated mainly by $C133. Impact effects also write voice 1 directly. |
| $DC00/$DC01 | Port 2 joystick and CIA1 keyboard scan; the title reads port 2 fire at $0E5A. |
| $DC0E | Stop the normal CIA1 timer at $3A08 when using the game IRQ. |

## Music and patterns

- $C000 selects a cue number. $C003 steps the active sequencer. The six pointers at $CA39 select three per-voice sequences for each of the two cue numbers used in play. The city starts cue 1. The rank-entry screen starts cue 0.
- $CB70/$CB8F are the two halves of a 31-pattern address table. Each pattern has note-duration pairs intermixed with instrument, rest, filter and pitch commands. $FF ends the pattern and returns to the track unless the repeat count is still active. Cue end clears the active byte at $C006 and the three gates.
- $C007 holds nine-byte instrument presets. The effects use separate pulse ($C9BA), vibrato ($C9E2), waveform ($CA06), pitch-step ($CA11) and filter-mode ($CA2A) tables.
- The dummy audio setting is suitable for inspecting writes to the registers. It does not establish audible timing or quality.

## Live tests

| Test | Evidence |
|---|---|
| Fire latch | Stepped from $30C1 on the city snapshot. The neutral trace branched at $30C6 to steering. Fire reached $30D4 and set the airborne flag to 1. |
| Park dispatcher | Set tile $CA and one ticket, and stepped $1C9B to the target. Column $A4 went to Jump at $1D14. Below $A4, row $0B went to Downhill at $1F51, row $48 to Slalom at $20EB, and row $11 to Ramp at $220B. These are branch tests with supplied locations. |
| Ticket award and cap | Stepped $155D with A=1 and score $0049. The next score was $0050, shown as 005000. Three tickets became four. Four stayed four. Both advanced the milestone index from 0 to 1. |
| Shop debit | Stepped $2E11 at round zero. Cash $0024 was refused unchanged, $0025 became zero, and $0050 became $0025. The listing checker also exercised the max-level path in the CPU simulator. $1B89–$1BA1 still attempts the debit at level nine, then skips the level and visit increments. |
| Park clock | Stepped $21D8 with the clock at $10. Tick $3F skipped the decrement, tick $40 changed the BCD value to $09. |
| Slalom gates | With tile $D3 at $3E89, a watchpoint on the flag cell stopped after the store at $24D0. The cell changed $D1 to $D2. Two increments changed the bar from $20 to $22. The control with tile $D2 returned at $24DB and left the flag and bar unchanged. |
| Keyboard | Matrix C reached $2CC8 and changed $3EC5 from 0 to 1. SPACE reached the pause branch at $2CEC. P and X reached $2D26 without changing the music flag or entering pause. |
| Viewport and IRQ | Stopped at the three IRQ callbacks and stepped the first patched map-row load and screen store. See `work/city-trace.txt` for the register and instruction evidence. |

These short cases test the engine's branch and arithmetic behaviour. The opening title-to-city route is the observed normal gameplay route in `orientation.md`. The supplied park and scoring states make no claim about routes to them.

The unpacker installs the resident map, music, title, actor and course code together. Park entry branches stay in that image. The decoded gameplay code has no calls to the KERNAL LOAD or SAVE entry points. The wide indexed reference search finds the glyph store at $1679 as a theoretical match for those addresses. Its Y loop runs from 7 down to 0. $2459–$2468 retains four short rows of bytes with no decoded reference to their start and an open purpose. They are counted as loaded data.

## The listing's error rate

The independent `gpt-6.2-sol` check drawn with seed 7202026 found 11 wrong comments among 80 sampled from 705. The plain estimate was 13.8%, with a 95% Wilson interval of 7.9% to 23.0%. The weighted estimate was also 13.8%. The check may have missed additional errors. All 11 findings were corrected, including the maximum-level shop debit, timer and animation boundaries, SID instrument offsets, and title-screen and logo details. The draw and verdicts are in `work/reports/coverage/`.
