# Elvira: The Arcade Game — facts

## Loads and progression

- The selector calls the interlude loader with HL or IL according to the choice byte at $13FA. The addresses to read are $14E6 and $151E in the opening listing.
- Each interlude first requests a B file through $0825 and then an A file through $0875. Stops at KERNAL LOAD showed G1B/G1A, G2B/G2A and G3B/G3A. The A request sets the stack return to $0812, where all three starts were captured. The page copy at $0887 begins with $C700 and $FF00, goes downward, and skips two additional pages at the $C9 boundary.
- The engine uses $094E and $07FF to index the descriptor table at $0A1C. From the loop’s transition path the debugger route with $07FF nonzero reached CL for selector $01 and WIN for selector $0A. The transition path tests the prior-load counter $07FF at $095B and increments it at $098C.
- With the contact handler entered at $2065, a Castle trace for object type $1A stored $FF to the exit request $094F and $0A to selector $094E. Castle with type $19 and Fire with type $1A both branched to $207D before those stores.
- In a controlled trace with spell type seven active, the stores at $2E38 and $2E3D set selector $00 in Fire and $01 in Ice and Castle, and exit request $FF in all three.
- The debugger-driven transition into WIN showed a congratulations screen with Elvira and the king. The ending interrupt vector points to $1515.

## Display and input

| Evidence | Behaviour |
|---|---|
| $13D5, $140E and $1412 in a quest | The raster handler dispatches through two stage addresses. $D019 acknowledges the IRQ and $D012 selects the next raster compare. |
| $1486, $14B0 and $14BF in a quest | The HUD stage switches from bank $C000 to $8000 and selects the HUD’s bitmap and matrix. A $D011 write watch stopped at $1489, directly after the store of $7F. |
| $162E in a quest | The playfield stage sets the bank through $DD00 and writes the fine-scroll and memory-selection registers. Controlled steps at $1635 and $164C in Fire, Ice and Castle showed $04 for the CIA store and $0F for $D018. With bank $C000 that selects the $C000 matrix and $F800 character tiles. The three world tile banks have different glyph drawings. |
| $3BD0 in a quest | CIA 1 scans the keyboard by setting one column low and reading the eight rows. $3C26 is its code table and the routine returns zero in $3C1B on an unchanged decode. |
| $2EC9 and $2F69 in a quest | The spell routine selects CIA keyboard columns $FE and $7F and compares the rows with $FD and $EF respectively. These are Return and Space in the keyboard matrix. Return starts an eligible spell. Space is on the selection path. |
| $1D49, $1D76 and $1DA5 in an interlude | The bitmap interlude uses bank $C000. It copies the supplied screen matrix into RAM under I/O at $D400 and the colour bytes into the colour RAM chip at $D800. |

## Text and values

The quest renderer at $0E1F reads scripts starting at the pointers at $0EA6. The groups select English, German and Italian using $C902. The script supplies a row and column before the text. $FE starts a new segment and $FF ends the script. Values 1 through 26 are alphabet positions for A through Z, with two consecutive character indices per letter. $20 is a space and draws $9A on both rows. $2D is remapped before the same pair calculation. The stored text includes PRESS SPACE TO START QUEST, GAME OVER, disk-side prompts, TRADER and LEVEL COMPLETE. The 24 decoded scripts are named in each quest listing. The text setup writes $BC to $D018 at $139A with VIC bank $8000 selected. In that mode $AC00 is the screen matrix and $B000 is the character set. Stops at $0E7F and $0E96 on Fire’s quest entry showed the E pair starting at $08 and the space value $9A respectively. The glyph bitmaps are inverted.

| Script byte | Top glyph | Bottom glyph |
|---|---|---|
| $01–$1A (A–Z) | $00–$32, even indices in letter order | $01–$33, odd indices in letter order |
| $20 (space) | $9A | $9A |
| $2D (dash) | $4E | $4F |
| $31–$34 (1–4) | $3C, $3E, $40, $42 | $3D, $3F, $41, $43 |

The dash branch loads $28 and jumps over the digit adjustment. Subtracting one and doubling gives $4E. Rendering the inverted pair shows a horizontal stroke in the upper cell and a blank lower cell.

All three quests carry the same text-screen glyph bank. The glyphs following the alphabet include the exclamation mark, question mark, colon and zero at $B1A0. The digit glyphs for 5 through 9 start at $B220. The tiles at $B4D8–$B7BF contain picture fragments in the same eight-byte tile format.

The score adder at $2B8C clears each pending digit on consumption and adds into the digits starting at $C903, least significant first. It subtracts ten and carries to the next digit where needed. The life digit at $C901 is decremented on the ordinary death path at $0893. The spell branch at $2EEF increments it with a cap of nine.

## Open analysis

The conditions that make the verified exit paths reachable during ordinary play remain open. The feature checklist records the remaining questions about pickups, difficulty and high-score entry.

## Map rendering

The world header supplies a metatile-map base at $4F2E, a character-grid base at $4F2C and a colour lookup at $4F2A. The first two bases in the three quest entries are as follows.

| World | Metatile ID grid | Character grid |
|---|---|---|
| Fire | $6A29 | $5077 |
| Ice | $61DC | $5064 |
| Castle | $685C | $515B |

$452C divides the incoming coordinates by four, saves the remainders and builds the map pointer. $182E reads a map byte through that pointer. Single-stepping it at the first draw after each hand-over read zero at $72A9, $6C99 and $76A6 respectively. A nonzero map ID is decremented to index the split offset table at $4560/$461E. The viewport expands a metatile four characters at a time using row offsets 0, 40, 80 and 120. At $1845 the renderer reads the character codes and looks up their colour bytes through $BC.

The shared split offset table contains 190 offsets. Each world stores 180 metatiles, and reachable IDs in the stored maps are in the range 0 through 180. Each group of ten occupies four 40-byte rows of character codes in the atlas. The map has a 256-byte row stride. Fire has 45 rows ($6A29–$9728), Ice 46 ($61DC–$8FDB), and Castle 46 ($685C–$965B). Each range stays within the metatile ID domain, and the following row-size window contains values outside it. The character colour table has 256 byte indices, one per possible character code. The map, atlas and colour ranges match between the entry and play snapshots.

## Interlude artwork

The interlude setup clears the destination bitmap at $1DC9. The reveal routine at $08DB uses a permutation at $0945 to choose the order in which pixel pairs appear. Instruction stops at $091C showed the source pointer at $1DE3 for Fire and Ice and $1DE5 for Castle. The destination pointer held $E000 and Y was $19 for the first masked write in all three. The matrix copy at $1D81 fills $D400–$D7F7 under I/O, and $1A25–$1A48 write the eight sprite pointers immediately after it.


## Quest sprite storage

The raster sprite writer at $21A4 sets pointers in both $C3F8–$C3FF and $C7F8–$C7FF. In VIC bank $C000 each pointer selects a 64-byte slot. The first 63 bytes give 21 rows of three bytes. The entry images hold sprite shapes at $CA00–$F7FF in Fire and Castle and $CA00–$ED3F and $F300–$F7FF in Ice. Controlled instruction steps through the pointer writer set slots $30, $29 and $31 in Fire, Ice and Castle respectively. Those slots select $CC00, $CA40 and $CC40. The Ice terrain lookup begins at $ED40. These ranges match byte for byte between each quest’s entry and play captures. CPU reads at $D000–$DFFF address I/O when it is banked in, while the VIC fetches the shapes from RAM underneath.

## Terrain probes and player poses

The setup at $0BBB installs pointers to two 180-byte terrain tables. $28A0 indexes them with the metatile ID minus one. A high byte with bit 7 set makes $28D6 use the low byte directly. Otherwise the pair gives an offset into the 16-byte profiles at the address in $4F30. The read at $28C0 uses four times the horizontal character remainder plus $AB as the subindex. Stops on that instruction with the subindex set to nine resolved the first profile to $5D1F in Fire, $EEA8 in Ice, and $5E03 in Castle.

Holding Down in the Fire play capture reached $2392 with input mask $02. That path starts crouch pose seven and initializes its frame to zero. $23A4 advances the crouch while Down is held and walks the animation back toward frame zero on release.

The spell selector scans nine slots and skips those that hold zero. $2FE1 uses sprite 0 in the HUD for the selected spell. With selection index two, a stop at $300C showed $A9 about to be written to the sprite pointer at $AFF8. The nine source shapes are in slots $A7–$AF in VIC bank $8000.

## Music on the opening and ending screens

The language, globe selector and ending captures contain the same player at $0884, the same three track lists, and the same 20 pattern pointers. Each track’s $FF loops the track. A $FF in a pattern advances to the next track entry. The decoder reads note numbers below $60, changes the duration for $60–$7F, selects an instrument for $80–$9F, and dispatches $A0–$A7 through the eight-address table at $0CCC. The tick update at $0C93 stores the two frequency and two pulse-width bytes for each SID voice. The three listings identify the parsed pattern limits and the 16 stored instrument records. A controlled trace of command $88 in the ending player indexed instrument eight at offset $48. The reads at $0A04 and $0A0A supplied $08 and $40 for the SID attack-decay and sustain-release writes.

Two passages of duration and note tokens sit between the indexed patterns. The pattern directory skips $0FD8–$0FE4 and $1063–$1078. The latter contains two copies of the same eleven-byte phrase. Pattern $06 crosses $1000 and ends at $1032.

The interludes use another player. Its track headers have the same three-voice layout, with five headers per interlude. The command handlers differ. The Castle player exposes two additional commands for changing the tick reload and requesting a fade. The decoded tables are in the interlude listings.

The quest sound-effect code at $0405 handles two queues. The first uses a sixteen-byte record starting at $05A5 and drives SID voices one and three. The second uses an eight-byte record starting at $073C and drives voice two. Each request has a priority. The active effect’s duration and modulation state are separate from the queue bytes. The driver code and both parameter tables match across the three quest entries.

## Map actions and colour scrolling

The quest probe at $3202 uses the current map column to fetch an action ID. It uses the ID to select a 16-byte descriptor, then uses the low nibble of the first descriptor byte to select one of 16 addresses at $3298. In a controlled Fire instruction trace with X set to four at $3285, the two table reads supplied $14 and $33. The indirect jump entered $3314, which reads descriptor byte two and stores it at $1932 before setting up the two position words for $1940.

The colour RAM dispatch at $4971 uses the low nibble of the scroll mask in $A5 when that byte is nonzero. A controlled trace with X set to four at $4979 entered $4A2A and stepped through the first indexed load and store, copying colour RAM from $D84F to $D827. This handler shifts 19 rows up and fills the exposed row from $4EC8. The other table entries select downward, sideways or diagonal shifts. Both dispatch tables match across the three quest entry images.

The energy update at $2CD0 applies a signed pending change from $2CCE to the energy byte at $2CCD, one unit per call. It bounds energy at zero and 40, then uses the remaining energy to redraw the HUD bar. The pickup handler queues four units for pickup ID $11.

## Object motion scripts

The routine at $1AC5 uses a per-object pointer and record index to read
four bytes at a time. When bit 7 of the first byte is clear, it starts a
motion segment at $1BCA. In a controlled Fire instruction trace, slot
zero read the bytes $03 $FE $02 $05. The first went into the segment
timer. The next two became signed increments of −16 and 16, and the
fourth reached the slot field at $BFBE. At $1C65 the routine decrements
the timer and applies both increments to the three-byte positions. The
code through the position updates matches across the three quest entry
images except for the immediate operand at $1B83 on the restart path.

## Lives and animated tiles

The quest HUD setup copies 200 screen-matrix colour bytes from $0D15 to $AF20. In the Fire capture, instruction stops at $0D09 and $0D0C showed the first byte, $AE, passing from the source to the destination. The lives renderer uses $C901 times sixteen to select two eight-byte strips. With three lives, stops at $2C19 and $2C1E showed X=$30 and the reads from $2C5A and $2C62. The stores target the HUD bitmap at $BA98 and $BBD8. The matrix and glyph sources match in all three quest entries.

Fire and Ice rotate the rows of animated characters in three bands at $FF78, $FF98 and $FFB8. Four offsets, 0, 8, 16 and 24, select the four columns. Fire moves two rows per call and Ice moves one. Instruction steps through $972E–$973B in Fire and $8FE1–$8FE9 in Ice showed the first source and destination accesses. Fire also has a three-phase frame copy at $695E. A controlled trace at $699E with phase zero selected $5EAF, $5F0F and $5F6F for the 32-byte copies to $FFD8, $FF08 and $FF28 respectively.

## Map action rows and object tables

The action grid is separate from the metatile grid. $37AD uses a per-world table of 47 little-endian offsets. The stream bases are $98D7 for Fire, $9182 for Ice and $96C0 for Castle. The last directory entry points back to the first stream. Each stored row expands to 256 action IDs. Bytes $00 and $FF introduce a run whose length is the following byte plus one. Other values are literal IDs. Store checkpoints on $B280 resolved the first write for row eight in all three quests. The 256 decoded bytes matched the parser at the routine's return. A Fire store watch confirmed that the row writer at $3811 can put a new ID into the six zero bytes reserved at the end of a packed row.

The 16-byte action descriptors follow the row streams. The dispatch at $3242 applies a world-specific remap to the raw ID before multiplying it by sixteen. Controlled traces of raw ID $FF read type nine from descriptor addresses $A936 in Fire, $A991 in Ice and $A89E in Castle.

The quest constructor at $1940 reads the object's starting offsets and an eight-byte type entry. A high bit in the second byte rejects the slot. The entry ends with the motion pointer written to $BFC4 and $BFCA. A Fire trace for type four stored $6786 from entry $6356. Ice type one stored $5CF7 from $5C5B, and Castle type one stored $6470 from $6264. Stepping $1AEB in each capture read the first command byte through that pointer.

The viewport scan at $2AA1 uses another set of world tables for positioned items. Five equal-stride arrays hold the low and high bytes of each axis and the sprite type offset. The low X arrays start at $6000, $EFF9 and $5F74 in Fire, Ice and Castle. Instruction steps at $2AB3 and $2ABA verified the first coordinate words $1340, $0CE0 and $1700 respectively. $2ABD rejects a high X byte with its sign bit set. The placement routine at $2B03 uses the visible indices from the scan to build sprite entries.

## Interlude loading text

The three text pointers at $0B20 select English, German and Italian.
Each of the scripts at $0B26, $0B57 and $0B82 contains a title and a
loading message. The first two bytes of each segment give its row and
column, $FE introduces the second segment, and $FF ends the script.
The English text is ELVIRAS MAGICAL QUEENDOM and LOADING PLEASE WAIT.

## Viewport edge columns

The scroll dispatcher at $40A9 uses the low four bits of $C4 to
choose which edge buffers to prepare. The right-column routine at
$4358 samples at viewport X plus 39. The left-column routine at $4442
samples at viewport X. Both expand 20 character cells down from the
viewport's Y position. Controlled Fire store watches stopped after
$440A and $44F4 wrote the first characters to $4949 and $495D.
Single-stepping then showed the colour lookup through $BC and the
matching stores of $19 to $4EF0 and $4F04. The Castle copies use one
background offset per cycle where Fire and Ice cycle through three.

Fire and Ice both store nine-byte instrument records through index
$10. A controlled event $90 stepped through the first indexed load at
$0E02 in Fire and $0E05 in Ice. It read the record at $1714 and $172E,
respectively, and returned the first control byte $41. Fire stores a
23-byte repeat of $1703–$1719 after that record, shifted one byte from
the start of instrument $0E.

## Spell exchange display

In Fire, Ice and Castle, instruction stops at $126A, $12D9 and $12DE showed the fill byte $AA for slot $CA and the two pointer writes for the first sprite pair. The first pointer came from the spell selection at $4F26 plus $A7. The paired pointer was $CA in all three captures. To restore the playfield, $12E7 tests bit four of $B0. The traced branch read character indices from $C000 at $12EF, looked up each colour through ($BC), and wrote it to colour RAM at $12F4.

## The listing's error rate

An independent gpt-6.2-sol checker examined 65 of 4,558 comments drawn with seed 20261120. It found 11 wrong details, or 16.9% of the sample, with a 95% Wilson interval of 9.7% to 27.8%. Weighting by the sizes of the sampled groups gives an estimate of 26.7% for the listing at the time of the draw. The checker may have missed errors. The 11 identified comments account for 0.24% of the listing at that point. All 11 were corrected along with matching claims in other parts. The corrections cover sound-effect fields, a SID pulse-width nibble, clipping and input operands, the crouch bound, the packed run count, two reused zero-page scratch bytes, a screen operand and the effect of an initialization store on the processor flags.
