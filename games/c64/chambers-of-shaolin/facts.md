# Analysis facts

## Disk progression and controls

- The title accepts one or two apprentices. The count select at $C333 calls SCNKEY and compares $CB with $38 and $3B. A live CPU checkpoint at $C33C caught the 1 case with A=$38. The name routine at $C3BD maps matrix codes through pairs from $C94F, suppresses repeats, supports delete and requires a non-empty name before accepting Return. The title copies ten characters per name to $CE03 and $CE0D.
- The title requests disk file `1` from device 8. The KERNAL LOAD breakpoint at $FFD5 identified call site $C9DA, name byte $31 and secondary address 1. The next file is the Test of Balance. Entering each transition directly produced further native LOAD calls for `2`, `3`, `4` and `HIGH` in that order. Disk files `2`, `3` and `4` start the Test of Speed, Test of Strength and combat.
- Balance's introductory gates both poll CIA1 port A at $097F for the exact byte $6F. The accept path at $0995 sets $CE23 to 1. A neutral read clears it at $0988. Both accepts were caught with execution checkpoints before the game reached its main loop at $08C4.
- The score screen loads `H` into $C868 and saves through $C8A3 under the replacement name `@:H`. The five records occupy 12 bytes apiece, a ten-character name followed by low and high score bytes. Code at $C268 compares the high byte first. The shipped `H` has 60 payload bytes. In VICE, the $FFD5 checkpoint caught the score screen's call at $C42E for H with secondary address 0 and destination $C868. Pressing fire at $C231 subsequently reached LOAD for LABLE from $C921.

## Video and sound

| Part | Register or address | Use |
| --- | --- | --- |
| Title | $D018, $D011 | $C5A4 copies a selected bitmap/matrix to $2000/$0400. $C4A7 enables bitmap mode. |
| Title | $D012, $D019, $FFFE | $C4DA installs $C500, which acknowledges IRQs and alternates raster compares $00 and $8C. |
| Title | $D418, $E050, $E053 | The presentation mutes the SID at transitions, starts the tune at $E053, and services its player through $E050 from the IRQ. |
| Balance | $DD00, $D018 | The initialization at $0828 selects VIC bank $8000. $18CC copies the background bitmap and screen colours to $A000 and $8C00. |
| Balance | $D015, $D01C, $8FF8–$8FFD | $12A3 enables sprites and multicolour for six body sprites. $11E7 copies the new pose in chunks and swaps the six sprite pointers. |
| Balance | $D012, $FFFE | $1964 installs hardware IRQ $198A. Observed in the live snapshot with processor port $35. $08C4 separately waits for line $FA. |
| Speed | $D018, $D011 | $0E28 selects the instructional screen matrix at $A400 and character RAM at $A000. |
| Strength | $D018, $D011 | $1244 selects the introductory matrix at $8C00 and copies the font to $A000. $1358 later puts the board chamber bitmap at $A000. |
| Strength | $D01A, $FFFE | $1414 enables the raster IRQ and sets the hardware vector to $143F. |
| Combat | $DD00, $D018 | $0884 selects bank $0000 and $D018=$1B. The intro temporarily switches to character mode for its text. |

## Text

The title's form renderer takes a list of message IDs ending in $FF. A message starts with column and row and continues with text. $FE starts another positioned row and $FF ends the message. It subtracts $40 from bytes at or above $40 before writing the screen code. This maps PETSCII capitals $41–$5A to glyphs $01–$1A, leaves $30–$39 for digits and $20 for space, and uses the game's own ornamental border glyphs from $40 onward. The glyph sheet in local `work/title-glyphs.png` renders $00–$5F. It shows blank glyphs at $00 and $20, letters at $01–$1A, digits at $30–$39 and the line pieces at $40–$4F. The font begins at $0800 in the title image. Speed's source at $FA00 matches its first three pages byte for byte.

## Overlay and data evidence

- The Speed exit rebuilds the loader at $C900–$CDFF from $EB00–$EFFF before jumping to its relocated entry at $C900. In the hand-over image, $C900 holds data that the copy replaces.
- The Combat scene decoder at $1E9E selects one of four ten-byte descriptors at $7832. CPU instruction tracing consumed four source streams, $D000–$DB6E, $6B96–$778C, $6000–$6B95 and $4000–$4AA8. They each write the scene's colour matrix at $0428–$062F and bitmap portion at $2140–$317F. The first stream is read with I/O banked out.
- The large zero-filled score gap at $1400–$9FFF produced no stores or execution hits between hand-over and requesting the next load. The two reads stopped in the KERNAL serial routines after `BIT $2009` and `BIT $3FA9`. These instructions use a three-byte BIT to skip an alternate instruction. The operands do not supply score data.

## Open analysis

The exported maps identify traced starts, authored display planes and several tables. They leave the remaining routines and data bare. The end conditions, training-to-combat rules, combat dispatch and unlabelled music data still need analysis. The listings use hand-over images, so indirect accesses and bytes installed or changed by the game still need tracing.
