# The Great Giana Sisters

## Engine and display

- The $0832 entry turns off display, sets up KERNAL LOAD for `ATG`, then runs the attract initialisation at $084F. The $FFD5 breakpoint reported the call from $084C and the three filename bytes `41 54 47`.
- The stage uses screen memory $C800 and characters $C000. CIA2 port A read back $C0, and $D018 read back $21. Eight sprite pointers at $CBF8–$CBFF refer to 64-byte slots within the same VIC bank. The handler at $1393 loads those pointers from $0605–$060C at $13D3.
- The four raster IRQs begin at $1249, $12A3, $1326 and $1393. Execute stops and single steps placed their entry instructions at raster lines 65, 89, 118 and 252. Their writes to $D012 and $FFFE/$FFFF select the next handler. In a separate short Stage 1 sample the trace counted 22 entries at $1249 and 88 writes to the low byte of the hardware IRQ vector.
- The engine reads player input from CIA1 port A at $9F84. The execution breakpoint advanced directly from $9F84 to $9F87, where the read value is complemented before being split into direction state at $0400 and a fire hold counter at $0401. Non-stopping load watches on $DC00 counted 22 reads in the same sample.
- The text writer at $9881 uses the carry flag to select a custom pointer or a built-in message. It draws screen codes into the game charset. The rendered glyphs show blank at $00, A–Z at $01–$1A, the copyright mark at $1B, and 0–9 at $30–$39. The BCD writer at $98D9 adds $30 to each digit and uses colour seven.
- Character animation at $163C selects a destination glyph address through $9D6B/$9D72 and copies the frame chosen from a pointer table. Its final copy reads the eight bytes at $C238 and overwrites the glyph at $C790. The sprite exchange at $1474 swaps $A080–$AA7F with $CC00–$D5FF using underlying RAM.

## Stage data

- A recipe address is selected from $6000 by doubling stage minus one. A five-byte placement gives the template ID, little-endian offset into $AC00, horizontal repeat count and vertical repeat count. $FF in the template ID field terminates the recipe. The table names 39 recipes. Indices 1–33 are the numbered stages and $27 is the attract map.
- The template address table at $9200 names 52 non-null templates. The first two bytes of each template are width minus one and height minus one. The character data follows in row order. Each destination row is 256 bytes. Stage 1 starts with block 1, a 3-by-3 template, repeated 85 times across at offset $1100.
- $9936 clears $AC00–$BFFF before rebuilding the map. When a Stage 1 start was triggered from the menu, a store watch on $AC00 stopped after $9943 with A zero, then a checkpoint at $99E3 reached the first placement read. The source pointer was $926C and the destination was $BD00. The first step loaded $3C at row-column offset 2, and the second step stored it into the destination.
- An independent read of the placement streams reproduced all 5,120 map bytes in the engine hand-over, the running Stage 1 image and the attract image using recipes 1, 1 and 39 respectively. The hand-over already carries a generated copy of the Stage 1 map. This is why $AC00–$BFFF is excluded as a runtime map buffer.
- Scroll exposes a new column using the map's row pages and paints it with the colour lookup at $AB00. The starting display uses $0D54 and self-modified load and store addresses to fetch 40 map cells per row.
- At $2296 the stage number selects a spawn list in the pointer table at $3D20. Entries contain a column, a row and a type. The reader at $22A6 compares the stored column minus one with $21, advances three bytes for a past column and stops on $FF. Type $0B passes through the rotation table at $3032 before the descriptor lookup.

## Movement, scores and transitions

- From the same Stage 1 snapshot, the instruction at $9F84 read $FF with the stick centred and $FE with up held on port 2. At the following movement entry $1138, $0400 held $00 or $01 respectively. Giana began both trials at sprite Y $CB. Ten frames later the control remained at $CB and the up trial reached $B0.
- The shot entry at $2A69 requires a fire hold, a free sprite-three slot, and $22 at least two. It requests the homing lookup at $2CDC for a value of four or higher. The colour and sprite shape number are set before the slot is enabled.
- The pause path begins at $21F1. The keyboard matrix test at row 1, column 7 reached $21F3 with X $FF. Stepping the store set $157D to $FF. Releasing that matrix position reached $21FD and its store cleared $157D. The raster handlers use the flag to skip game updates. The RAM NMI vector returns to the menu entry $084F.
- The menu seeds three lives for each player in $1573/$1574. Key 2 leaves both active. Key 1 and menu fire mark Maria inactive through $1576. The attempt change at $09E9 saves the active player's score, form, stage, lives and start variant in paired fields, then toggles the index and restores the selected player's fields.
- The dreamcrystal branch at $1C4F adds one to the packed decimal byte at $0434. A controlled run with $99 crystals and three lives reached the carry branch at $1C5C with the crystal count at $00. Stepping the increment changed $043C from three to four. The score add returned with packed decimal bytes $25,$00,$00 from zero.
- The clock decrement at $1D0A reloads prescaler $28 when it underflows, then subtracts one in decimal mode. A byte sum of three reaches the timeout store. In a controlled run starting with time bytes $04,$00 and a zero prescaler, the clock reached $03,$00 and the step at $1D42 set the outcome byte $0465 to two.
- A warp request at $2169 takes the branch at $0B70, where the routine eventually adds two to $20. The common successful exit adds one more at $09B1. The bonus-room path at $1E19 uses resident layout recipes. Stage $20 selects layout $21 directly while the other branch rotates through the five bonus layouts $22–$26.
- The score screen at $325D compares six converted score digits, draws five records from each of the tables at $36F7 and $376F and enters the name prompt when a score qualifies. The save path supplies the three-character filename ATG and the memory bounds to KERNAL SAVE at $3459.

## Sound and hardware accesses

| Registers | Use in the listing |
|---|---|
| $01, $0314/$0315, $FFFA/$FFFB, $FFFE/$FFFF | Main gameplay exposes RAM vectors at $0E39. The score screen uses the KERNAL vector at $3566. |
| $D000–$D010, $D015, $D01B, $D01C, $D027–$D02E | Sprite shadow transfer at $13C4, layer colours at $1443 and object visibility and priority at $2444. |
| $D011/$D012, $D016, $D018, $D019/$D01A | Display enable and raster scheduling at $0E39 and its handlers. $08B3 selects the character and screen bases. |
| $D01E | The object-contact path at $288A reads the VIC sprite collision latch and decides which slots require further checks. |
| $D020–$D023, $D025/$D026, $D800–$DBE7 | Stage palette at $0D39, sprite multicolours at $1443 and per-character tile colours with $AB00. |
| $DC00/$DC01 | Joystick scanner at $9F77 and separate matrix scans at $0940 and $21BB. |
| $DD00 and CIA interrupt controls | Video bank is set at $086E. Interrupt setup and the packed sample and transfer code also access CIA registers. |
| $D400–$D418 | SID updates at $439E and $43E0. Across 24 Stage 1 frames a control breakpoint counted 24 entries at $1249, the driver entry counted 24 calls and the SID store watch counted 616 writes. |

The tune selector at $49E6 uses the index in A, the carry flag and lookup columns at $4A7A–$4ACA. The order advance at $4901 selects the pattern number, transpose and instrument offset in separate arrays. The driver decodes note flags, optional arpeggio and timing through $440A. A tune-specific enable at $41EC selects the packed sample path. SID activity was checked with instruction and store counts under dummy audio.

## Bytes carried over from boot

The loaded payload includes an unused-in-the-observed-boot parallel transfer utility at $9000–$91B8 and editor text fragments around it. The fragments decode enough to read assembly mnemonics and directives. The listing counts these as authored bytes. At the top of memory, the boot-time watch caught the loader's write to $FFF1 at $0AEE. The 15 bytes in the main hand-over match the preceding logo's bitmap at $3FF1–$3FFF. File 1 stops at $FFF0 and the engine later installs its RAM vectors, so the ledger excludes the top 15 bytes as loader residue and vector storage.

## Open questions

The full weapon progression and exceptions for individual creatures remain open in the feature checklist. The level and object tables establish their formats and the corresponding handlers, with controlled tests for individual state changes. There is no claim of a recorded route through the late stages or the hidden rooms.

## The listing's error rate

Seed 141987 drew 60 of 903 comments. The independent checker ran on gpt-6.2-sol and found four wrong details in the written stratum and none in generated comments. The unweighted estimate was 6.7% with a 95% Wilson interval of 2.6–15.9%. The stratum-weighted estimate was 6.0%. The findings were the parenthesised stage index at $13F0, the order of type substitution at $22CD, the instrument-offset array at $4269 and the shape shading at $EC00. All four were corrected. This sample estimates the pre-correction error rate, and the checker may have missed other errors.
