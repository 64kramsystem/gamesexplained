# Basketball match

## Raster split and sprite queue

The hardware IRQ vector points to $575B during ordinary match frames. Starting from the live school match, a stopping watchpoint on $D018 repeatedly caught the store at $5792 on raster line $F2. A held $34 and the register read back $35. The next stop was the store at $57D5 on line $FC, with A=$36 and $D018 reading $37. Both settings select screen RAM at $CC00 in the $C000 VIC bank. The first selects the generated score glyphs at $D000 and the second selects the court glyphs at $D800.

The vector store watch stopped just after $574B. The low byte had changed from $F8 to $5B while the high byte still read $56. The next store at $5750 installs $57 and completes the switch back to $575B. The driver at $56F8 takes target lines from $03C3 and sprite operations from $03DB. Some requests set sprite Y, and others change a sprite pointer in both screen matrices. The return to the main handler schedules $F0.

## Court and sprite data

- A CPU load watch on $C000–$C57F hit the indexed read at $3C7E from both the setup and a live match. The pointer table beginning at $468E advances by 17 bytes for each column. The reader halves $0550 and subtracts eight for its row, then dispatches by the code it found. The file provides 80 columns covering $C000–$C54F. The last 47 bytes in G, H, I and J match consecutive slices of file B beginning at $1651, $1BD1, $2151 and $26D1 respectively. Setup writes clamp values at $C550/$C551 and clears a counter at $C559. A range watch from the school hand-over caught those stores returning to $1353, $1358 and $10A1 respectively.
- A CPU load watch on $6A00–$BFFF hit $2CF0 in a school match. It reads the six slot pointers beginning at $7002. The base-pose table at $700E is indexed through $0322,X. The body at $70F4–$95EC parses as 106 consecutive variable-length records. Every record consumes 129 minus its first byte, and the final record ends exactly before the first character-specific catalogue. The part's annotations record each run of equal headers.
- A CPU load watch on $FD80–$FEFF hit the recolour loop at $3334. An earlier setup step patches that instruction's source operand from $3355. The six templates are spaced by 64 bytes and rendered as 21 rows of three multicolour bitmap bytes, with a padding byte per template.

## Match panel encoding

The printer at $17DD reads zero-terminated strings. It maps digits to indices $00–$09, space to $0A, uppercase letters to $0B–$24, and colon, exclamation mark, question mark and period to $25–$28. Each screen index goes to $CFC0 plus the column. Its colour goes to $DBC0 plus the column.

| Hardware | Use | Evidence |
| --- | --- | --- |
| $01 | Hides KERNAL for the match, exposes character ROM during score font preparation | $0EC2, $0F31 |
| $D012, $D018, $D019 | Raster schedules, display split and IRQ acknowledgement | $572C, $5733, $5792, $57D5 |
| $D021 | Restores the court background colour from the selected court's $EFFD byte | $57A6 |
| $DD00, $DD02 | Select VIC bank $C000 | $0EEC, $0EF4 |
| $DC00, $DC01 | Match input and confirmation | $17C0, $1FCB, $1FD1 |

## Target score and award

With the match paused on the target prompt, port 2 right hit the execution checkpoint at $164C with A=$22 and decimal mode set. Stepping exactly one instruction changed the low BCD byte at $EA from $20 to $22. The paired branch at $162B subtracts two and has a lower bound guard. The right path stops increasing the target when the hundreds byte at $EB becomes nonzero.

The award routine at $558F adds two to one of the BCD totals at $37–$3A. Setting the ball action to $50 in a saved school match reached the CPU checkpoint at $55B0 with A=$02. One instruction changed the blue total from zero to two. In a separate controlled check, entering the contact handler at $3F6F with negative contact result, phase and possession zero, and height $40 reached $3FB1. Stepping that store wrote $50 to the ball phase at $20.

The court asset has a character bank at $D800, screen-code halves at $E000 and $E400, and 24 rows of 80 colour codes at $E800. The routine at $3667 copies four ten-cell strips per row from a moving source column. The palette is stored separately at $EFFD–$EFFF.

## Ball velocity

A controlled entry at $508E with target index $07 reached the variation entry at $516B. The code between $51B3 and $5264 reads the SID oscillator and uses separate bit groups to scale and sign the perturbation of each horizontal velocity word. The second checkpoint reached $5264 after both components had been written. VICE ran with dummy audio for this check. The observation establishes the executed path and stores.

## Match sound effects

The routine at $270E uses $6C to select a voice 1 effect phase. The phase sets a waveform, changes frequency or closes the gate. In a controlled match snapshot, phase six entered $27E1 and stepping $27F4 executed the store of $60 to $D400, the low byte of the starting frequency $0960. Phase seven entered $280A. With the same starting frequency, the store at $2811 took $2E, the low byte after subtracting $0032.

The voice 2 dispatcher at $288B uses $6D and a separate table at $289E. Its sweep helper at $2B5A adds the step at $72/$73 to the accumulated offset at $74/$75 and writes the sum of the new offset and the base at $70/$71 to the two SID frequency registers.

## Roster overlays and return to selection

The loader reads the catalogue bounds and pointer counts from file A at $1000, $1020 and $1040. It adds the destination base to each relative pointer at $1207 and $1213, then copies the shape bytes. At $1299 a checkpoint caught Y=$0A and A=$ED with the source pointer $95ED at $1702. Stepping the store wrote $ED to $700C, the low byte of the sixth slot's pointer.

In the live school match, $2CFF read from $9BEA for slot 1. The next header reads at $2D0A and $2D0F selected the record at $9C72 and read placement $09 and payload length $1E. Stopping and stepping the base-pose loads at $2D30 and $2D3A read $24 and $00 from the record at $71AE. The first byte sets the starting copy index and the second adjusts the placement of the overlay. The overlay loop at $2E11 reads from the adjusted pointer at $D9 and combines the recoloured overlay with masked base pixels. A separate stop there caught a bitmap fetch at $AED7 for slot 2.

At the match hand-over, $F500–$FD1B still contains the menu backdrop bytes. A store watch from the saved school match stopped after the compositor instruction at $31F8 wrote into that range. The selection listing accounts for the backdrop bytes.

The loader exposes the saved low RAM as three pages at $0B00–$0DFF. Those images hold zero page and pages two and three. A store watch on $0B42 stopped immediately after $FFD6 copied the saved byte in from the parked overlay. In a controlled run with PC set to the return entry at $0E06, a load watch on $0B42 stopped after the source read at $0E23 with A=$08 and X=$42. The next store writes the byte to $0042. The remaining two pages are restored by the same routine before it installs the disk reload stub at $0334.

## Initial court view

During match setup, the store at $1144 writes the left 20 screen cells of each row from $E014 to $CC00. The store at $1156 uses $E814 and $D800 as its first-row colour source and destination. The right-half store at $119E starts with $E400 and $CC14. Stopping on all three instructions from the school hand-over confirmed those pointer pairs.

## Court camera

The routine at $33F6 compares ball X at $0210/$0219 with the 16-bit camera origin at $0F/$10. It scrolls up to two pixels toward the ball when its offset leaves the $94–$C5 band, with the camera clamped to $0000–$014E. When the tile column changes, the routine calls $3667 to rebuild the court strips. In a controlled school-match check, setting ball X to $0190 with camera X at $00A6 reached $3425 with X=$EA. At $3452, stepping the store wrote $A8 to $11 as the new camera low byte.

The actor contact dispatcher at $411D uses a separate 71-entry table at $414D. It doubles the map cell code and writes the handler address into the jump at $414A. The handlers return carry and can also update the current actor's counter at $07D2. Separately, the placement dispatcher at $6443 doubles $8A to select one of 23 entries at $6459, then loads the selected actor's offset index at $027E,Y. Its handlers separate position offsets from velocity transfer. For example, $652C clears the two horizontal velocity words and $655E copies them using the same position offsets.

At $1D71 the actor dispatcher takes the active index from $0E. The side bit and assigned indices at $08/$09 select one of four input bytes at $54–$57. From a saved school match the execution checkpoint at $1D8E caught the selected byte $06. One instruction later it was in $8B.

## Velocity damping and actor selection

The routine at $24DF subtracts one arithmetic eighth from the signed ball velocity words. In a controlled entry with vertical velocity $0180, a breakpoint at $24EE found $0030 in $E3–$E4 after the shift. The next stop at $24FF found $0150 in $0262/$0269. A low-height branch can clear vertical motion and use the oscillator to skip the remaining horizontal updates.

The target scan at $336B compares same-side actors through the coarse direction routine at $23A0. It ranks candidates using the returned distance and direction relative to the candidate's facing. In a controlled school match entry with X=$01, the execution checkpoint at $33ED found $0C in $B2 and $05 in $B4. Stepping the following four instructions transferred these values to $59 and $62, the selected distance and actor index.

## Restart, poses and rebound velocity

In a controlled call to the phase-$91 handler at $66C5, slot two was selected with the delay clear. At $66D5 the accumulator held $4F. Stepping the two stores at $66D5 and $66DA set that actor's X coordinate to $024F.

The pose dispatcher at $5B94 reads an actor's state and patches the jump at $5BA7. In controlled calls with actor slot one, selectors $02, $03 and $0B entered $5CBA, $5DE6 and $6060 respectively. The first advances the actor's moving pose counter or selects one of two stationary ball poses. The second picks a follow-through state from the selected target slot and movement conditions. The third selects a ball placement from the actor and ball heights and uses the actor's timer to advance the state.

The rebound handlers at $42ED–$4505 mix signed halves of ball velocity on two axes. With X velocity $0400 and vertical velocity $FE00, the $42ED handler reached $4334 with X velocity $0300 and vertical velocity $FF00, before the two calls that add half back to each component.

Match initialization copies a sprite slot from $6950 to $F400. The stop at $10B5 with X=$3F showed that the last copied byte was $A5 from $698F, the next routine's first opcode. The 63 sprite bytes occupy $6950–$698E.

## Actor distance and pose state one

The distance routine at $2697 returns the larger of the absolute Y displacement and a halved horizontal displacement in X. For a negative horizontal difference whose high byte is $FF, the routine complements the low byte before halving it. A controlled call for actor 2 at ($0100,$66) against target ($0120,$70) reached the return at $26CA with X=$0F. The scan at $3B12 writes each result at $02E9,Y and records the best slot on each side.

A controlled actor-state dispatch from $5B94 with state $01 in slot 1 reached $5C64. Three instructions later, the indexed store at $5C68 had cleared $0795.

In controlled entries with actor slot one, stepping $5D9C stored state ten at $0201 after the $0552 value passed the comparison with $023D. Stepping $5DC0 in the pose-fourteen handler stored one at $0795.

## Return load request

Entering the return routine at $0E06 in the saved school match reached the KERNAL LOAD checkpoint at $FFD5. The request specified device 8, secondary address 1 and the 16-byte filename `M*REET BASKETBAL`. This is the request made by the copy of the stub at $0334. The boot request is M. In the menu transition the exchanged loader at $0E22 selects A. From file A’s $1100 entry, the reachable external transfers are $12BE, $1300, $130A and $1316, through $0803. They request the court character file C–F, the map file G–J, file K and file B respectively. The separate load at $1612 has its caller at $1441 outside that entry flow. File B replaces both addresses. The observed boot, all four court entries and the return request leave file L unused on this disk.

The retained serial LOAD path at $088E updates the filename at $096C. In a controlled trace, stepping $0893 wrote $30 at $096C and left the adjacent byte intact. At $08AB, A=$01 and X:Y=$6C:$09 supplied SETNAM with the address and length one. The numbered match requests use the separate loader at $080D.


## Draft mapping and pose tables

A controlled call to file A's sorter at $1178 stopped immediately after $11AE wrote rank four to $FF2C for draft slot five. The six ranks beginning at $FF27 select the catalogue pointers copied into $7002. The six selected 50-entry pointer tables in the School hand-over match their file A offsets plus the corresponding relocated table bases. Two surviving unselected tables retain their relative offsets.

At $121D a read watch on $FF26 caught match setup loading difficulty two into X. In the menu, stepping $1616 wrote the translated difficulty value one to $0396 for highlighted row one. The settings transfer at $0D5F copies $0396 to $FF26.

Controlled entries for actor slot one stepped $5D88 to store pose state $0B at $0201 and $605A to clear the pose flag at $0795 at timer zero. An independent entry at $61B0 used normalized heading two and selector zero, then stepped $61B6 to write pose index $2E. The ball-possessor target selection at $62FA returned $FF for table index zero, and stepping $62FD stored that result at $07C6.

A controlled ball-height test stepped $4C57 to raise $023D from $20 to $38. In the edge-column copy, stepping $3616 with X=24 loaded zero from $3646 as the first low-byte row offset.

The contact path at $60B5 multiplies the actor's heading by four to select the ball's horizontal velocity record at $2126. A store watch stopped after $60D0 with the heading-zero record's final byte, $FF, in $025B. A separate watch on $0269 stopped after $5165, where subtracting a step of one from $0200 left the vertical velocity at $01FF.

The computer decision path compares a seven-bit oscillator sample against a lower bound at $69DA,Y and an exclusive upper bound at $69E3,Y. With Y set to one, instruction traces sent sample 97 to $69D8, sample 105 to $69C4, and sample 113 to $69DA.


## Restart steering and ball recovery

In controlled instruction steps, the restart lookup at $1E66 mapped fine bearings three, four and five to headings one, one and two. The corresponding flags read at $1E79 were one, zero and zero. The adjacent branches use the flag to choose between the rounded heading and the actor's current heading when both are close.

At $4A17, index eight read heading five from the 5-by-5 matrix at $4B1F. Stepping $4A1A stored five at $4B18. The successful height check takes that heading from $4B18 and puts it in the new possessor's field at $027E. Controlled loads at $61BB returned zero for pose selector one and one for selector four. A zero lets the compositor update the actor's secondary heading.

The ground check at $45C0 returned carry set for height zero with a negative vertical velocity. Controlled steps returned carry clear for height zero with zero velocity and for height one with a negative velocity.

## Sprite buffer overwrite at match setup

For each of the four court hand-overs, a stopping load and store watchpoint on each of the 20 bytes at $FD1C–$FD2F first hit after the store at $2D95. The match builds its own sprite data over the bytes inherited from the selection program. A controlled run of the alternate-buffer synchronization at $30F4 confirmed that $3114 later reads one of those generated bytes at $FD20 with Y=$0A and $3117 copies it to $FD60.

CPU execute, load and store watchpoints covering $096D–$09FE and $D700–$D7FF did not hit during 60 frames from each of the four court hand-overs or 60 frames from the saved School match. The test covers those windows. The role of the initial bytes remains open.

## Roster parameters and shape responses

Controlled indexed loads at $2069 and $205A read $03 from $13A0 and $05 from $13AB. The latter path adds ten before indexing the ball carrier's group of speed words. At $5184, $518E and $5198, indexed loads read $06, $05 and $09 respectively for the three selected roster entries. Those bytes set the starting index of the velocity variation loop at $51A1. At $6640, Y=$07 selected $05 from $13CE, where the following instructions double the value to index the vertical launch speed.

In a controlled restart entry the load at $1CD9 with X=$02 read $24 from $1D05, one of the opposite-side rows. The seven-slot setup also uses X=$03. A controlled step with that index read $0F from $1D06. In the collision dispatch, local coordinates (2,5) led the $3EDD handler to read $01 from $400D. Local coordinates (2,1) led the $3EEF handler to read $00 from $402D. Both lookups used index five, from different shape halves.

A controlled call to the signed-shift helper at $25A0 with X=$00 and $E3/$E4 holding $FFFE stepped the patch at $25A4, which set the operand at $25AB to $80. The shift loop left $FFFF at $E3/$E4.

In a controlled entry to the ball integrator at $3C22, ball X began at $01FFF0 and the X velocity at $0010, with the three X bytes holding integer and fractional components. Ten instructions later, the fractional and low integer bytes had both wrapped to zero and the high integer byte had advanced from $01 to $02. At $6536, starting with A=$40 and heading four, the indexed addition of the flat placement offset $FC produced $3C with carry for the following high-byte addition.


## Verification of control, draw bounds and distance

- A controlled call to the movement decoder at $1FF2 passed the active-low right direction in X. The store at $2086 wrote $02 as the high byte of X velocity for slot one. In the team-switch path at $222D, a controlled third fire detection while slot one lacked possession selected slot three and set the hold counter at $033D to $80.
- The colour copier at $3667 adds nine to the camera column and starts with that offset at Y. At camera column 41, a load watch on $E850 stopped immediately after $369B with Y=50. The fourth strip of the first row reads the first byte of the next source row at that extreme.
- The base-pose copy stops at Y=$3F, advances again and takes its next source byte at Y=$40. Instruction stepping verified the skip for the record at $8561.
- In the heading distance helpers at $24C6 and $267E, component magnitudes 1 and 10 produce 8. Components 8 and 10 leave the estimate at 10. Both helpers keep the smaller of the larger component and the three-quarter sum when the intermediate arithmetic fits.
- The parked tail at $096D–$09FF matches $D16D–$D1FF in all four match hand-overs. Individual instruction stepping confirmed that the retained indexed store at $092F can overwrite its first byte using X=$0B. A controlled entry to the legacy SETNAM path supplies only the one byte at $096C. The tail did not stop execution, load or store watches in the setup and play windows.
