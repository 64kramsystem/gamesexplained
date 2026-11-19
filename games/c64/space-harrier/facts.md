# Space Harrier facts

## Build and memory

This is the Elite PAL C64 game from the Jazzcat Cracking Team D64. The
unpacked game enters at $0850. The listing uses the RAM from that entry
checkpoint. The live observations use the same release in VICE C64SC
with 6569 PAL timing.

| Range | Contents |
| --- | --- |
| $0850–$1EBA | Initialization, game loop, title, score table, movement, projectiles, collision and video setup, interleaved with their tables |
| $1EBB–$38FF | Object dispatcher, movement streams, stage spawn tables, perspective renderer and beginning of the raster chain |
| $395C–$4E8A | Character rectangles, including title logos, projectile graphics and object frames |
| $4E8B–$4EEA | Working state for input, stage, wave, score, projectile velocities and raster synchronization |
| $7000–$9FFF | Five terrain character banks and a separate boss bank at $7800 |
| $A000–$BFB2 | SID driver state, music interpreter, four tune groups and sound effects |
| $C000–$C7FF | Live playfield character bank, populated by $1E14 |
| $C800–$CFFF | Fixed title and status-panel character bank |
| $D000–$EDFF | Physical RAM behind CPU I/O and KERNAL addresses, used by the VIC for sprite shapes $40–$B7 |
| $F800–$FBFF | Live screen cells, HUD and sprite pointers |
| $FFFA–$FFFF | Hardware vectors. $3817 installs NMI at $3855 and IRQ at $3856. |

The disk has one PRG containing the wrapper and packed resident engine.
Stage advance changes pointers and copies one of the resident 2 KiB
character banks. The listing's stage and object dispatch trees exposed
no additional load or banked program. There was no execution checkpoint
hit at KERNAL LOAD ($FFD5) in 120 tested active Moot frames.

## CIA and VIC

| Register | Game use and code |
| --- | --- |
| $01 | $3827–$382B clears HIRAM. The effective port in play is $35 with DDR $2F, so hardware IRQ dispatches through RAM while I/O is visible. |
| $DD02, $DD00 | $1DB5–$1DC2 makes CIA2 port A's low two bits outputs and sets both low, choosing VIC bank $C000. |
| $D016, $D018 | $1DB5 enables multicolour and selects the $F800 screen. The raster phases at $38B7 and $38E7 change the character pointer without moving that screen. |
| $D011, $D012, $D019, $D01A | $3817 enables VIC raster IRQs. The four phases program the next line and acknowledge through $D019. |
| $D000–$D010, $D015, $D027–$D02E | $38E7 applies movement to the paired player sprites. $3317 and $33FA assign and position the six other slots. |
| $D01B, $D01C, $D025, $D026 | $1DB5 configures player priority, sprite multicolour and the two sprite colours shared by all multicolour sprites. |
| $D020–$D023 | Title setup and the raster phases select border and background colours. The stage advance reads sky and ground palettes at $14F2 and $1506. |
| $DC00 | Active-low port 2 directions and fire in $1BC1, title and score-table input. |
| $DC01 | The main loop checks for $EF at $0952. Space produced this value in the matrix-key test. |
| $DC0E | $3823 stops CIA1 timer A before installing the raster handler. |
| $D400–$D414, $D415–$D418 | Voice pitch, pulse width, envelope and gate, plus filter and volume. $A2F8 uses a register offset of 0, 7 or 14. $A7FF and $AAEB set filter or volume state. Sound effects can borrow the first two voices. |

The IRQ entry at $3856 stores A, X and Y in $08–$0A and dispatches
through $4E95. Four execute stops in active Moot observed these phases.

| Handler | Observed raster line | Work |
| --- | --- | --- |
| $3862 | 185 | Change $D021 to the ground colour and schedule line 205. Its own line is $31 plus eight times the horizon row. |
| $388E | 205 | Increment the main loop's wait byte $4E97 and schedule line 242. |
| $38B7 | 242 | Select the fixed $C800 character bank and schedule line 20. |
| $38E7 | 20 | Select the $C000 playfield bank, apply sprite movement, restore the sky colour and schedule the moving horizon. Call $A9B7 on even synchronization counts. |

$D018 read $E1 at the $38B7 entry and $E3 at the $38E7 entry, with an
unchanged screen pointer. On this snapshot, 120 PAL frames caused 120
passes through $388E, 60 calls to $A9B7 and 30 stores to $D404.
Those SID stores confirm software activity with dummy audio.

## Controls, time and scoring

- $1BC1 polls active-low port 2 bits 0 through 4 for up, down, left,
  right and fire. Instruction stepping from $1BCF to $1C39 on the same
  active Moot snapshot produced motion bytes $FA/$00 for left,
  $06/$00 for right, $00/$FB for up, and $00/$05 for down. The
  no-input case gave $00/$00. The handler checks position bounds
  before storing each increment.
- The fire path uses $4E8B as a pressed latch and scans four shot slots
  from the highest index down. A store watch on $B5–$B8 stopped at
  PC $1C57, immediately after $1C54 activated slot 3. $1A9A uses
  $1B6C to turn a shot phase into a character rectangle.
- The main loop checks for pause after drawing the status panel.
  Single-stepping $0952 with Space held loaded $EF and reached
  $0955. Holding Space stopped at $095C. Releasing, pressing and
  releasing again took the CPU through the latch waits and to $0982.
  The tested matrix key was Space for both entry and resume.
- The HUD starts at TIME 60. $16C3 subtracts one in decimal after 20
  calls and leaves the timer at $99 once it gets there. At the zero
  boundary, a store watch confirmed $16DB writes $99. In 120 observed
  PAL frames, $16C3 was called ten times. A second run of 244 frames
  with the divider initialized to 20 reached the subtraction store
  twice, changing $59 to $57. The displayed unit follows
  gameplay-loop calls and should not be read as a real-time second.
- $4EBA starts at ten. In the impact routine's life-loss branch, an
  execute stop after the check found ten lives when the timer was
  $59 and nine when it was $99, both starting from ten. The HUD at
  $1625 uses $99 to switch from the decimal timer to the life icons.
  $0944 tests for a negative life count, so zero remains playable
  until a further decrement routes it to the high-score check.
- $16E0 adds packed-decimal score units across $4EB5–$4EB6.
  $16F5 converts the resulting four digits to glyph codes. The
  six-column HUD template at $169B supplies two trailing zero glyphs.
  A direct CPU check stopped at $16F4 with $1302 after adding $03
  to the packed-decimal value $1299.
- $0EA4 compares scores and shifts the ranked names and values.
  $104A draws the entry screen and $1147 selects letters by joystick
  fire. $FC erases the preceding glyph and $FD is the finish glyph.
  $11AE produces seven scoreboard rows from rank, name and score
  fields. Entry-screen flow is traced through the listing.

## Objects, stages and graphics

$1E9E indexes the update handler by object type using the table at
$1EBB. $281F selects wave handlers through $291E and alternate
spawns through $28A4. The object update routines add signed position
and depth deltas, often through $2386. The player collision test
at $17A5 checks near depth, a recovery countdown and two projected
axes. $1A29 checks the projectile's depth and a separate tolerance
table at $1A86. Hits may destroy the object ($1A0A), deflect the
projectile ($19E5), or move a boss's health state toward its terminal
value, depending on the update handler.

In the escort-head last-hit tail, $231C scans the linked body slots
using Y, then $233C uses that same index as the projectile-store
index. In a direct CPU check with no linked body types, the stop
at $233F showed Y=$FF and the instruction had cleared $01B4,
leaving the four projectile flags untouched. The check establishes
the store address for that state. Its effect in a full encounter
remains open.

$1D64 sorts eight object-slot indices by depth. $3272 and $32B8
project position using the sixteen decreasing factors at $3262.
$33FA chooses a frame through $1F2B, then indexes its frame directory
by depth. A high byte of $FF is a tag, with the low byte holding
a sprite slot. A non-tagged entry points to a width byte, a height
byte and row-major screen codes. The character renderer $378D skips
zero cells and applies the object's colour to the cells it writes.
Player sprites occupy slots 0 and 1, with six VIC sprite slots
available for nearby objects. $099B draws two horizon rows from
stage-specific scrolling screen-code strips.

The stage-card names at $15B0 decode in this order. Moot, Geeza,
Amar, Ceiciel, Ida, Revi, Minea, Drail, Asute, Vicel, Nark, Absymbel.
The counter at $4E8F selects the content. The separate packed-decimal
stage number at $4E90 supplies the on-screen label. An execute stop
at $14D2 on the forced stage-advance path observed index 0 and
label 01 advance to index 1 and label 02. Starting from index 11
and label 12 reached index 0 and label 13. $14C6 reads the $FF
high byte in the next alternate-spawn pointer to detect the wrap.
A load watch during the stage charset copy triggered at $9800 for
Moot. $2BE4 and $2FAF select the separate $7800 character bank
during their boss setup.

## Text encoding

The fixed character set at $C800 was rendered as 256 eight-pixel
glyphs with eight bytes each. $D6 is the blank cell, $D7–$F0
represent A–Z, $F1–$FA represent 0–9, $FB is a dot, $FC is the
left-arrow glyph, and $FE is copyright. $FD is the selectable finish
glyph on the high-score grid. The stage-card strings terminate with
$FF. The score-entry layout at $10C4 gives $FF a different role
as a newline and ends at $80. The title logo and Elite logo are
character rectangles at $4599 and $4651.

## Audio

The IRQ drives $A9B7. $AAB5 initializes the main music, $B060 and
$B356 initialize two boss themes selected by their respective
spawners, and $B5B1 initializes the score-entry tune. Each supplies
three voice order lists and event pointers. $A5B4 reads the next
pattern pointer and rewinds at a zero pointer high byte. $A74F
dispatches event commands from $C8, and $A635 looks up instruments
for bytes $F0 and higher. $BAEE is the pending effect request.
$BAF6 selects the stream through $BC3E. $BBCD runs the effect at
its own divider and restores the music mask and filter state on
terminator. Tune names and register-level timing outside the
sampled Moot interval are traced only.

## Remaining data coverage

The two booted disk builds agree byte for byte at $4EEB–$6FFF.
Its role is open. The active Moot comparison found no read of
$4F2B–$6FFF in 12 frames. Neither the direct operand census nor the
decoded stage, object and motion dispatch tables assigned it a
consumer. These checks leave indirect reads and unobserved phases
open. The bytes are counted in the ledger. $BFB3–$C7FF and several
small high-RAM runs also remain unclassified.

The JCT RLE source starts at $2FBC and its destination begins at
$FF50. The stop at its final jump ($0129) caught the destination
cursor at $FF4B. The 175 bytes from $FF4B to $FFF9 are
byte-for-byte the same at RLE entry and game handover and differ
from the alternate disk's material there. They are retained
packing material and are outside the ledger. Static vector and
asset data are counted separately.

## The listing's error rate

The gpt-6.2-sol checker marked 6 of 65 sampled comments wrong in
detail, from 661 comments with seed 20261119. The observed rate
was 9.2% (95% Wilson interval 4.3%–18.7%). The rate weighted
by the two strata was 8.3%. The sample is an estimate and the
checker may have missed errors. Corrections cover ranking and
name entry, inactive versus expired projectiles, boss movement
delta cadence, pitch-slide setup and the pattern-order start.
The individual verdicts are in the local `work/reports/` handoff.
