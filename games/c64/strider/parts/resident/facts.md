# Resident engine and title

All addresses refer to the resident part unless an overlay is named.

## Display and controls

| Hardware register | Use |
|---|---|
| $D011, $D012, $D019, $D01A | Raster mode, position, acknowledgment and interrupt enable. The stage handlers are $8210 and $8269. |
| $DD00, $D018, $D016 | VIC bank, matrix and charset selection, multicolour and horizontal scroll. $8210 chooses $4800 or $6800 for the playfield. $8269 selects $E000 and charset $D000 for the panel. |
| $D000–$D010, $D015, $D017, $D01C, $D01D, $D025–$D02E | Draw positions, enable and mode masks, and sprite colours. The preparation routine publishes them at $8716. |
| $DC00 and $DC01 | Port 2 at $8BE4 and keyboard matrix scanning at $8895. The front end also reads up, down and fire at $B303. |
| $D400–$D418 | SID frequency, pulse width, control, envelopes, filter and volume. Music and effects share the entry at $6C12. |

Title strings use PETSCII, then the display copies their low six bits as screen codes, for example at $B28B–$B2A0. The gameplay panel uses its own glyph IDs. $8B0E maps decimal digit 0 to glyph $B9 and digits 1–9 to $BA–$C2. It draws the BCD timer and score in the panel and takes the lives digit from $0201. The health routine at $896D paints a paired-glyph bar at $E37E–$E389.

## Player and stage flow

Jumping, falling and edge movement are action states at $1480. $8C21 chooses a state from the current action, the directional input and terrain samples around the player. $94A2 applies table-driven position changes and then dispatches the camera rules. Those rules place the player and camera together through stage seams so a region transition can keep their relative offset.

The fire edge at $9BA2 compares the decoded fire bit with the previous latch at $28. A new press draws a temporary 6×2 glyph patch. The draw routine keeps the old screen codes and copies their pixel patterns before combining these with the sword masks. $9CBD checks the sword glyph range when applying contact against the selected object.

$896D handles zero health and the death sequence consumes one life at $89BB. The restart reloads the current area's spawn and object data at $8ADF and $8851. At zero lives it puts the score into the title's insertion buffer, sets $0200 and leaves the engine. Stage completion is a separate test at $A292, with an ending text path for the fifth stage.

## Sound

A at $6C00 selects a music preset. Each preset points to three streams, then seeds SID registers and duration and modulation state. $6C4E reads notes followed by durations or commands with the high bit set. $FE stops and $FF restarts the preset. The title choices select whether to play music or allow effect requests through $6C03. Each effect has a stream of frequency indices stopping with $FF and a parallel stream of SID control bytes.
