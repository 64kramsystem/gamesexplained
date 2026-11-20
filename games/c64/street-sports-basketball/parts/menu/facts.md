# Court and team selection

## Title and option panels

At the $0800 hand-over the title bitmap at $6000–$7F3F and all 1,000 colour cells at $5C00–$5FE7 already match the title screen. At the title, $DD00 reads $96 and $D018 reads $7D. The menu replaces the bottom 16 bitmap rows with data expanded from the value/count pairs at $EFE8–$FD1B. The loop at $0CBC adds one to the count and stops at $7F40. The expanded image changes 5,120 bytes of bitmap address space.

A checkpoint at $12B7 caught X=$00, Y=$84 when port 2 moved right once from School. The routine draws the Alley preview from $8400. The first four bytes give width, height, column and row. Each following cell has eight multicolour bitmap bytes, one byte carrying two screen colours and one for colour RAM. Court previews are at $8000–$8FE1. The ten draft portraits occupy page-aligned slots starting at $2000 and ending with Dana at $4400. The $192B table points to undrafted figures and $193F points to the roster figures.

## Draft cursor and coin frames

From the draft snapshot, a right input on port 2 reached $1E5C with A=$00, X=$4C, Y=$96 and carry clear. The checkpoint at $1EA9 caught $D000/$D001 holding $4C/$96 after the two stores. Bit zero of $D010 was clear. The cursor's X and Y come from the three-byte character entries at $1969. Bit zero of the third byte supplies the ninth X bit.

The coin frame loop starts at $4E00 and advances its coordinate pointer by 32 after each frame. In a controlled call to $1EC0, the comparison at $1F96 reached X=$10 with its next pointer at $5000. The compare and branch exited at $1F9E. The coordinate records at $5000–$50F8 continue the same stride beyond that frame limit.

In a controlled draft snapshot, the two indexed loads at $1D2E and $1D32 read $F6 and $CE from the last populated biography pointer. The three following words are zero.

## Text

The menu renders bitmap glyphs from $091E plus eight times the character index. Rendered glyphs confirm screen-code letters $01–$1A, space $20 and digits $30–$39. Apostrophe is $27, hyphen $2D and the name-entry cursor is $40. The normal writer at $0DF8 ORs the shape with $55, and the highlighted writer at $0E35 inverts the shape before that operation. Menu panels at $C000–$CFBC are made of 28-cell rows and use $FF to terminate a panel.

## Registers

| Hardware | Use | Evidence |
| --- | --- | --- |
| $01 | CPU banking for SID player, KERNAL I/O and image reads | $086F, $08EB, $0C90, $12D2 |
| $DD00, $DD02 | Select VIC bank $4000 | $0B3A |
| $D011, $D016, $D018 | Multicolour bitmap, display blanking and layout | $0B4A–$0B5F, $08CB |
| $DC00, $DC01 | Active-low joystick inputs | $1236, $1259 |
| $DC0D | CIA interrupt acknowledgement | $090E |
| $D400–$D418 | SID voices and volume | Reset at $E0AB. The music tick enters at $E000. |

## Opening music

The IRQ calls $E000, which jumps to the three-voice player. The tune table at $E495 assigns separate streams beginning at $E4CB, $E6BD and $E755. The dispatch table at $E43A points to 29 commands for waveform, filter, repeats and other settings. Bytes below $C0 are note events with a duration byte, and $FF ends a stream. The three active opening streams terminate at $E6BC, $E754 and $E80D. Walking both possible exits of the stream branches from each of the four starting pointers gives those three stops and $E4CA for the volume stream. Two further parseable event sequences begin at $E80E and $EA0D and end at $EA0C and $EB69. Controlled entries to the event dispatcher confirmed that fetching each of $E80D, $EA0C and $EB69 clears the active stream pointer high byte at $E0F3.

In the title snapshot an execution checkpoint hit $E3DF with note $35 and X=$6A. One instruction loaded the low frequency byte $60 from $FE6A and stopped at the SID write. The voice register offset was $0E, selecting voice 3.

## Parked loader and packed-image residue

At the menu hand-over, $D400–$D5FF matches $0200–$03FF byte for byte. The disk overlay exchanges those two pages with $0C00–$0DFF. The return-to-selection code reads them back to low RAM. The next page starts with two loader entry jumps, whose operands target the relocated addresses $0E06 and $0E19.

A store watch on $D700 during the boot of M hit the initial page move at $082A, the unpacker's literal copy at $017E and the page relocation at $01DD, all with I/O hidden. At the last stop the source operand was $C700. The full source page in that stopped snapshot matches $D700–$D7FF at the menu hand-over. The page is outside the later overlay exchange and the banked colour sources.

File M unpacks in two passes. The first pass enters $0100 with source $4B57 and destination $0801, and reaches $0196 with source $FFFF and destination $F000. The relocation loop at $01DA then copies pages $BF00–$EFFF to $CF00–$FFFF. At menu entry, $D700–$D7FF, $EB6D–$EBFD and $FD1C–$FD3F exactly match the first pass at $C700–$C7FF, $DB6D–$DBFD and $ED1C–$ED3F respectively.

The second pass enters $0100 with source $4770 and destination $0800. At the second stop at $0196, both pointers are $CFBE. A scripted decode matches all bytes through $CFBD in the stopped snapshot. This pass supplies the menu-entry bytes at $4CDE–$4DDE, $7F5E–$7FFF, $ACAC–$AFDE and $BB1F–$BFC0. Their patterns repeat at similar offsets across several pages. All four stretches, the three first-pass stretches and the parked overlay tail at $D16D–$D1FE match the hand-over from LCX’s differently packed M. The selection listing excludes the gaps outside the addressed sprite, bitmap, image, text, and sound data.

The old overlay bytes at $D628–$D680 match 89 consecutive bytes in M starting at file offset $0840. The retained loops move six eleven-byte blocks apiece, targeting page $F5 in one loop and higher offsets in page $F9 in the other. In the menu image, those offsets lie within the backdrop's value/count stream read by $0CBC.


The parked overlay at $D000–$D2FF matches $0800–$0AFF in the match entry except for the filename byte at $0A00. The exchange loop at $FFCE places it there. The match listing describes the overlay at its execution address and identifies the open range at $096D–$09FE. The next parked page is the zero-page save image, which appears at $0B00 while the overlay is active.

## Menu interrupt vector

The hand-over's RAM vectors at $0314–$0333 match the saved vector table at $FD30 in the match image. A store watch on $FD30 from menu entry stopped at the KERNAL VECTOR routine at ROM PC $FD29, with $C3/$C4 pointing to $FD30 and the saved IRQ vector low byte $31 already written. The title and match snapshots contain the same full 32-byte table at $FD30–$FD4F. During menu startup, the checkpoint at $0849 caught the incoming NMI high byte $FE with A=$08. Stepping the store changed the RAM vector at $0318/$0319 to $08D7.

## Draft roster and coin display registers

The draft commit branches on bit seven of $1928. It stores the character index from $1919 in $038D indexed by $1929 for a clear bit, or at $0390 indexed by $192A for a set bit. The branch increments the corresponding pick count. In a controlled draft state, the checkpoint at $1B2A caught A=$07 and X=$01. Stepping the indexed store wrote $07 to $038E.

The coin loop adds $44 to each sprite selector before storing its VIC pointer in $5FF8–$5FFF. Across the 16 active records, the selectors at even offsets in the $5B00 attribute table range from $00 through $27. In bank $4000 these select sprite slots $5100–$5AC0. In the same loop, the indexed expansion access at $D017,Y reaches $D018 when Y is one. A store watchpoint caught $1F6C writing $7D to $D018 with Y=$01. Both branches change only bit one for this index, preserving the screen and bitmap address fields.

The menu's two control gates read the sign bits at $03A0 and $03A1 before reading the two CIA joystick ports. A controlled watch stopped after the reads at $1231 and $1254. The RAM entry at $FF80 jumps to $FF86, as confirmed by an instruction step with the KERNAL banked out. With KERNAL visible, $FF81 is the screen initialization entry called at $0825.

At the four match hand-overs, the first CPU access to each byte at $FD1C–$FD2F is a write from the sprite compositor at $2D95. This classifies the match destination as generated sprite storage.

A controlled entry at $0CA8 reached the breakpoint at $0CE4 with source pointer $FD1C and destination pointer $7F40. The backdrop decoder consumes $EFE8–$FD1B and writes through $7F3F. The $FD1C–$FD2F bytes lie beyond that stream.

The menu and all four court hand-overs have identical bytes at $D700–$D7FF. In a controlled entry at $FFDF with the page counter set to $D7, stepping the load, compare and branch reached $FFE5 with carry set. The page exchange ends before touching $D700.

Load watchpoints in the selection image decoder stopped after $13FA read $ACA7 and $BB17, the last colour bytes for the figures starting at $AB14 and $B9FC. The next cell-advance call in each case sent the decoder to its exit at $137C. The draft sprite pointers are $30–$32 in bank $4000. Their slots end at $4CBF, below the packed gap that starts at $4CDE.
