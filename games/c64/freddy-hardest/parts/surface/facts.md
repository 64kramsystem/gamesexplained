# Surface

The title IRQ installer at `$AFF5` sets the compare to `$8D` and
hooks `$B021`. Its bank-zero phase starts at `$B052` and uses
sprites as the marquee font. `$A9AA` reads its data at `$2328` and
assigns nonzero, non-`$FF` bytes directly to the sprite pointer slots
at `$07F8`. Zero advances the script without a sprite and `$FF`
returns the cursor to `$2328`. Rendered sprite pointers
`$A5–$BE` give A–Z, `$BF–$C8` give 0–9, `$C9` is a dot and
`$CA` a copyright mark. The alphabet designs start at `$2940`.

The small title font at `$5000` uses `$00` for blank,
`$4C–$63` for A–X, `$64–$6D` for 0–9, `$6E` for colon,
`$6F` for dot, `$70` for Y, `$71` for Z and `$72` for the
copyright mark. The code at `$AF76` copies title cell and colour
runs from `$4000–$422F` and the five text rows from `$B60E–$B685`.

## Surface map and panel

The cursor at `$3B6B–$3B6C` starts at `$32D6` when `$8065`
initializes the course. Each byte selects a vertical 11-cell record
from `$357C` via `$C100`. `$C1A7` builds forty columns, and
`$C11F` and `$C163` draw the entering right and left columns
from the cursor helpers `$C0AA` and `$C0CD`. The measured map
band from `$32D6` to `$357B` contains 678 column IDs. Its
highest index is 56. The position limits tested by `$C1EE` are
`$0008` and `$09F9`. Five restart marker comparisons are at
`$8119`. The meanings of all restart paths are open.

The reverse reader subtracts 41 from the forward cursor before
fetching an ID. In an isolated trace with the forward cursor at
`$32F1`, the load at `$C0E6` read `$0C` from `$32C8` and
triggered a watchpoint there. The fourteen IDs at `$32C8–$32D5`
precede the forward start and use the same column dictionary.

`$C370` increments the six score glyphs using `$3BBB` as a count
and `$3BBC` as its starting digit. It carries by wrapping a 9
glyph at `$6D` to 0 at `$64`. `$B59D` awards a life when
the last four digits are zero and the second digit is odd, provided
the life count is below five. `$B50B` updates the live panel tiles
for the new life count and sets the terminal flag on losing the
last one. These paths are traced in the listing.

## Register census

| Hardware | Evidence |
| --- | --- |
| CPU port $01 | $800B–$800D clears LORAM in the banking setup. |
| CIA1 keyboard and stick $DC00–$DC01 | $B1AB scans the keyboard. $B24E reads the stick. $A857 or $A867 chooses the input path in $3C1D after the title reads fire. |
| CIA1 timer $DC04–$DC05 and $DC0E | The title tune loads the timer at $0F3E and $0F44. The play IRQ setup stops timer A at $A006. |
| CIA2 $DD00 and VIC $D018 | The title multiplexes the banks at $B067 and $B0AD vicinity. The play IRQ toggles between character bases at $A070 and $A0D5. |
| VIC $D011–$D012, $D019–$D01A | $A000 installs raster IRQs and $A02C acknowledges the interrupt. $A27D sets the next compare from the phase table. |
| VIC $D016 | $A2D3 and $A308 write the fine scroll field while stepping course position. |
| VIC $D000–$D010, $D015, $D027–$D02E | $C8F9 and the sprite helpers send coordinates and masks from shadows. $CBF9 seeds the crash sprites. |
| VIC $D01E–$D01F | $A052 and $A058 sample the two collision latches into $3B93 and $3B94. |
| SID $D400–$D418 | $C3F6 flushes the gameplay shadow. $0EC9 sets the title instrument envelopes, pulse and filters. |

## Instruction evidence

A watchpoint on `$3C1C` in the natural play snapshot stopped at
`$B1F3`, immediately after the keyboard path's default write.
The raster control checkpoint at `$A02C` hit during all runs.
To isolate the joystick routine, load the same snapshot, set the I
flag and start at `$B24E`. Step the three instructions through the
store. Neutral, right, left and fire read `$7F`, `$77`, `$7B`
and `$6F` from `$DC00` and store `$1F`, `$17`, `$1B`
and `$0F` in `$3C1C`. The original snapshot reached the keyboard path. The isolated trace confirms
that the port-2 joystick path reads the injected directions and fire.

In an isolated sprite update at `$C8F9`, the store at `$C8FE`
copied sprite 0's Y shadow to `$D001`. A voice-one initialization
with the pointer set to `$956E` hit the execute checkpoint at
`$C57E` and triggered three load-watchpoint hits in the stream's
first seven bytes during the following 17 instructions.
