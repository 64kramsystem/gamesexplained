# Pac-Land facts

The address references are for the Madonna Cracking Group disk, using the packed game's handover image at $033C. See [orientation.md](orientation.md) for the image hash and boot sequence.

## Resident map and round progression

- The game selects processor port $35 at $035D and VIC bank $C000 at $3754. The graphics under $D000-$DFFF are physical RAM visible to the VIC. The CPU sees chip registers there during normal play.
- The renderer combines $C400 character cells and $D800 colour cells with two character sets. $382A swaps eight pages between $A800 and $C800. A byte-for-byte comparison of entry and Round 1 shows both sets exchanged, all 2,048 bytes in each direction. $386B can replace the $CA78-$CBE7 tile subset with one of two $170-byte patches at $78D2 and $7A42.
- The working round index $1D runs from 1 to 16. $0C6D adds one and changes $11 to 1. It separately increments the decimal display count at $1C. Stepping the transition instructions from $1C=$16 and $1D=$10 produced $1C=$17 and $1D=$01 at $0C81.
- $EF46 selects the round's recipe through the split pointer table at $7D08/$7D1C. A positive byte selects a strip. A negative byte goes straight into the expanded high-byte stream as an event marker. Zero ends the recipe.
- A strip consists of paired source lists selected by $7855/$7874 and $7893/$78B2. The high list's zero ends the strip. Each normal pair gives a pointer into $4000-$6FFF. The sixteen recipes reach 807 distinct, consecutive column records in that range. The records each decode to 20 glyphs.
- In a column record, bytes $00-$07 select colour, $FF terminates, and $F2-$FE repeat the preceding glyph by the low nibble. Ordinary bytes in between emit a glyph. The runtime decoder has an additional colour case for glyph $82 at $9D47 and $9E3A. The Round 1 right-edge decoder executed $9E2D with its operand patched to $4561. At $4561 the first eight bytes are `06 BE 21 FE 81 20 F2 FF`.
- $EF46 also expands the selected round's object layout and its separate run-length event map. $F023 reads count and value pairs until count zero and writes the result beginning at $A5E0. In Round 1, eleven pairs at $939C expand to 503 bytes.
- The main loop compares the 16-bit world coordinate at $9D/$9E with the finish coordinate at $9F/$A0. When equal it calls the finish sequence and then the round transition. $0DCD dispatches ending sequences using the round modulo four. These paths are traced from the code.

## HUD and alphabets

- The VIC split switches from $D018=$12 for the playfield to $10 for the panel while retaining the screen base at $C400. The custom panel glyphs begin at $C000, eight bytes per glyph. The rendered letter codes $02-$0F read C, D, E, G, H, I, M, N, O, P, R, S, T, U in that order. $10-$19 are 0–9 and $1A is blank.
- $C120, $C126 and $C12B provide the panel legends CREDIT, ROUND and HIGH SCORE. $07F2 maps the nibbles of the BCD credit byte into custom digit codes. $389A uses decimal arithmetic for the three score bytes and updates the high-score bytes when exceeded.
- The title lettering starts at $C800 in the entry image. Its alphabet uses the C64 order with A–Z at $01-$1A, digits at $30-$39 and space at $20. $3AFC also reads this encoding in its text streams. $92A9 holds GAME OVER, $92C6 starts PLAYER and $92D7 starts READY. $CEDA holds the title text and logo stream.
- $3AFC takes the stream address on the stack. Its zero ends the stream. The bytes $FF, $FE, $FD, $FC and $FB dispatch to position, colour, clear, positioned string and glyph-repeat commands respectively. Ordinary glyphs pass to $3BCD.

## Controls and movement

- In the title at $074C, the game drives CIA1 row 0 with $FE and reads $DC01 until two consecutive samples agree. F1 adds a credit. F3 consumes one credit and F5 consumes two. F1 and F3 were exercised on the title.
- Gameplay polls joystick port 2 at $F29E, testing bits 2–4 after inverting the input. When these are inactive it scans the keyboard via $F2DD, $F2EA and $F2F7. Those instructions sample P, O and CTRL respectively. F7 in $7FAD sets the IRQ maintenance skip operand at $040F and mutes the SID. A subsequent input clears the skip and restores volume.
- Single-instruction steps at the input reads gave the following results for $32/$33/$34. Neutral produced `00 01 01`. O produced `FF 01 01`, P produced `01 01 01` and zero produced `00 01 01`. CTRL or joystick fire held after the latch was set made $33 and $34 zero. Joystick right plus fire read $E7 at $F29E and produced `01 00 00`.
- The ground and air paths at $1436 and $1564 use $31 as the horizontal speed tier, $32 as requested direction, $35 as previous request and $3A as a timer. $1523 initiates a jump from the active-low test of $33, checks state and height and selects an initial vertical phase from $889A. A breakpoint before and after the motion call measured $BC changing from 0 to 1 on joystick fire in Round 1.
- $98E0 adjusts the fine scroll in $36 by $37. When the result crosses eight pixels, it shifts screen and colour rows by one cell and decodes another column in the appropriate direction.
- The chase sprite path at $09B0 seeds and moves a trailing sprite. Its contact branch sets the life-loss byte $FD when the power flag $23 is clear, or switches to a score pose and delay when power is active.

## Hardware and timing

| Register or range | Use | Evidence |
| --- | --- | --- |
| $01 | Switch to RAM with I/O visible | $035D writes $35 |
| $D000-$D010, $D015, $D017, $D01B-$D01D, $D027-$D02E | Copy position, enable, expansion, priority, colour and mode shadows to sprites | $0432, $04B7, $0544, $05BB |
| $D011/$D012/$D019/$D01A | Select the raster line, enable and acknowledge the raster IRQ and synchronize the main loop with line $A0 | $037C, $03E3, $062F, $F334 |
| $D016/$D018, $D020-$D026 | Set scroll phase, select character set, change the background at raster splits and choose multi-colour values | $03F1, $04B7, $05B3, $3754, $EBC2 |
| $D400-$D417 | Write music frequency, waveform, envelopes and pulse widths. Voice 1 also plays effects | $B069, $B0E7, $B2A8 |
| $D418 | Set volume during music setup and mute and restore it during pause | $B21C, $B2AA, $7FC0, $7FF1 |
| $D41C | Sample SID voice 3's envelope output as an input to the lower-band spawn position | $2AE1 |
| $DC00/$DC01 | Read joystick and scan the keyboard matrix | $074C, $7FAD, $F295 |
| $DC0D | Disable CIA1 interrupt sources when installing the raster dispatcher | $0384 |
| $DD00/$DD02 | Set the VIC bank | $3754 |
| $D800-$DBE7 | Colour RAM for the panel, playfield and text | $3754, $3BCD, $EE16, $9932 |

A store watchpoint on $D012 caught six successive writes with the PC stopped after the store at $03E6. The old slot byte at $0E advanced through $00-$05 and the IRQ vector stayed $03D1. The stock schedule at $886C is $31, $49, $81, $C2, $C8, $EB. Round initialization and object markers can rewrite parts of that schedule. The Round 1 frame capture showed the playfield character set selected at raster 77 and the panel character set restored at raster 237 in that frame.

## Sound

- $B214 selects a seven-byte descriptor from $B676 with the tune number in A. The first byte selects the tick divisor and the next three little-endian words select the channel order lists.
- The pattern reader at $B399 advances each channel when its duration expires. It decodes commands through a stack dispatch table and keeps independent stream pointers. $B2BB loads the next pattern by following the order list. A zero pointer restarts that list.
- $B1DC copies a 20-byte effect descriptor into $B1C4-$B1D7. The SID update uses voice 1 for the active effect and resumes music voice 1 once the effect state clears. Dummy audio was selected and the SID claims here describe the game instructions and register destinations.

## Scope of the live checks

The boot reached the handover and Round 1. Additional checks used execute breakpoints, instruction stepping and a store watchpoint at the points above. The ready screen and Round 1 were reached through the ordinary controls. The round wrap was exercised by setting inputs to the transition routine. No analyzed claim uses a recorded play route.

## Additional instruction checks

- $F345 clears zero page from $FF through $02. It then stores zero at $0298 and returns. Single-stepping $F34E-$F356 showed X change from $88 to $87 and the negative flag remain set at BPL. A deliberately nonzero byte at $0210 survived the call fragment.
- A write watch on the pause operand at $040F fired after $7FBB when F7 was held. The operand was 1 and the PC had advanced to $7FBE.
- From the eligible power pill contact branch at $2853, stepping $2857-$285D set the flag at $23 and passed A=$09 to the tune selector. The check isolates the result of a successful contact. Object-specific collision windows remain open.
- $7F0B and $EE0B use the round number to index $BFFF. The sixteen bytes read are also the first two glyph definitions of the panel character set. The two zero entries leave the normal scroll path active for rounds 7 and 15. A nonzero entry selects the alternate path.

## Resident bytes with open purpose

$3FEA-$3FFF and $BFEE-$BFFE are present in both the MCG handover and the Wanderer Group title snapshot. A load watch on each interval recorded zero hits while running each of the sixteen round initializers from $EBC2 to $ED5F. The terrain dictionary watch recorded 495–562 reads on those same paths. The intervals remain in the coverage denominator.

## Listing error rate

An independent `gpt-6.2-sol` checker sampled 80 comments with seed 20261119. Nine findings held, and all nine sampled comments were corrected. The raw sample rate was 11.2%. The estimate weighted by the sampled strata was 6.4%. A full audit and a fresh sample are open.
