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

## Training result and score formatting

- Strength uses a zero-based attempt index and a separate strike outcome. The results handler awards training values when it reaches its award path, scaling the four base values 50, 60, 0 and 14 by the result percentage with rounding up. Targeted execution checkpoints reached all four award stores at $0A9C, $0ABC, $0ADB and $0AFB. The flag at $CE2A plus apprentice index was written for 50 and 100 percent in the tested cases.
- The score screen rewrites an in-memory five-row message before rendering it. The decimal digit routines use $C860–$C863 for lookup offsets. A top score shifts bytes through $C8B9, beyond the five-record save range that ends at $C8A3.

## Display initialization and Combat score

- Balance replaces the display plane before playing. A CPU trace of $18CC read $5800–$77E0 and wrote $A000–$BFE0. The introduction first installs characters at the same base from $ED80.
- Combat clears its bitmap and working plane before decoding a scene. The instruction trace records $2000–$3FE0 and $5180–$5E73 as the clear destinations. On entering that path in VICE, the clear routines executed 7,948 and 3,328 stores respectively. The HUD initializer then read each of its bottom colour strips 21 times.
- The Combat raster IRQ at $1D35 ran 120 times in 24 VICE frames. The phase that waits for line $F1 increments $7816, and separate phases service the HUD bars and redraw the score.
- Combat formats its score by adding one decimal contribution per nibble. Instruction tracing produced the five-digit strings 00000, 09999 and 65535 for the tested scores 0, 9999 and 65535.

## Training carried into Combat

The numbered training loads use two interleaved apprentice records at $CE17–$CE1E. Balance writes the initial award values. Speed and Strength add their own awards. The paired flags at $CE26–$CE2B record the training unlocks. In Combat, the action interpreters at $157D and $1744 consult one flag apiece for each of moves four, six and seven. An instruction test with each flag zero or one checked both interpreters. A zero flag took the exit without reading the script directory. A one flag reached the directory and selected the first pose of the requested move.

Combat uses the training values in three other places. Its opening and recurring timers use $C8 minus $CE17 or $CE18. The opening bars at $0EEE use $CE1D and $CE1E, and the contact handlers add the move score from $CD5A with adjustments from $CE19–$CE1C. In one-apprentice mode the entry supplies the CPU opponent with default values and all three move flags. The code at $09AB increases its thresholds and training values after advancing the arena.

## Combat progression and disk I/O

A controlled combat round check entered $0960 with bar $7831 at $A0 and movement offset $7810 at $FF. In one-apprentice mode, scene index 2 advanced to scene 3 and selected interlude 5. Scene 3 advanced to index 4, selected interlude 1 and set the score-exit flag at $09A3. In two-apprentice mode it selected interlude 6 and set the same flag at $0977. An active movement offset of zero bypassed those endings. The intro then consults the flag at $08B1 and can enter the HIGH load at $C300.

The executable disk calls, including the Speed loader as reconstructed from $EB00–$EFFF, account for the route from LABLE through 1, 2, 3, 4 and HIGH, then back to LABLE. The high-score program separately loads and saves H. The listed calls use fixed filenames and the disk directory contains those files plus the release intro. The multi-platform manual also describes chambers and character storage absent from this disk route.

## The listing's error rate

An independent gpt-6.2-sol checker sampled 65 of 1,114 comments with seed 652. Seven contained wrong details (10.8%, with a Wilson 95% interval of 5.3% to 20.6%). The estimate weighted by stratum size was also 10.8%. The seven corrections cover the Balance bitmap mask and music credit, Speed strip and pointer strides, Strength voice-zero filter fields, Combat bar cadence and expired timer branch, and title command-buffer boundaries. Repeated comments with the same errors were also corrected. The checker may have missed errors in the sample.
