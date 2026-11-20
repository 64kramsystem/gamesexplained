# Ending

The WIN load shows Elvira facing the king under the congratulations message. The reset target at $1A7F sets the stack and processor port before jumping to $12ED. Its raster handler is at $1515. The capture was made by setting the transition values during Castle and letting the normal teardown and load path run.

The display setup at $1BBA selects bank $C000, matrix $C400 and bitmap $E000. It installs the first 1016 matrix bytes from $3C44. The raster display's sprite pointers occupy the last eight bytes of the matrix. $1C2A clears the bitmap before the reveal at $1870. At the first $18B1 write the source pointer was $1C44, the destination pointer was $E000 and Y was $19. The running capture’s displayed bitmap through $FE7F matches the corresponding source bytes.

A RAM write trace from Castle play through the WIN hand-over at $12ED recorded zero writes to underlying RAM at $D000–$DFFF. All 4096 bytes match across Castle play, the WIN hand-over and the ending picture. This range belongs to the Castle sprite set. For the ending, $135F–$137B select sprite slots $00–$07, which point into $C000–$C1FF.

The same trace shows the Castle voice-two effect records at $0741–$07F0 and terrain and map data at $5E03–$7FFF and $8009–$965B carrying over unchanged. The trace contains writes to the nine-byte header at $8000–$8008.

The ending clears two pages of sprite RAM at $134F and $1352. In a controlled reveal trace with $186F zero, the instruction at $1911 read through the pointer $4444 and the store at $1917 used the pointer $C000, with Y=$19 at both instructions. The routine moves both pointers by 48 for each of ten groups and uses the permutation at $1945 to select the byte and pixel pair. With $186F nonzero the loop clears the same pairs.

The sprite position routine at $157F writes two rows of four sprites. The
columns are 24 pixels apart and the rows are 21 pixels apart. A controlled
instruction trace from the ending capture found $50 and $68 before the
first two X stores and $4D and $62 before the two row Y stores. The
movement controller at $13BC indexes four-byte records at $15E9. It reads
the stop flag first, then the repeat counter and the X and Y increments
when the record calls for motion. The first record loaded a repeat
counter of eight in the trace. Bit 7 of the fourth byte ends the motion
at the record at $1655.

The side prompt renderer at $1724 selects one of six 24-character rows
using the offset table at $1806. The rows give the side A and side B
prompts in English, German and Italian. In a controlled instruction
trace with A zero, the renderer selected the first row, read a character
ROM byte at $175E, and reached the indirect sprite store at $1763 with
Y=$15. The eight rows of each glyph are placed three bytes apart in
sprite RAM. The setup at $1659 clears all eight 64-byte sprite slots.
The trace reached both the first and last slot stores with X=$3F and
A zero.

The colour-copy loop also copies $3AC4–$3BC3 to $FE80–$FF7F. In a
controlled trace with X=$41, $1C20 read $E2 from $3B05 and $1C23 wrote
the same byte to $FEC1. The full destination page matches the source in
the ending capture.

The matrix source occupies $3C44–$4043. Instruction steps at $1BFC and
$1BFF with X=$FF confirm that the fourth indexed load reads $403B and
writes $C7F7. The eight stored $FB bytes at $403C–$4043 occupy the original
matrix positions corresponding to the sprite pointer cells.

The vector installer at $1A45 copies the nine-byte CBM80 header from
$1A76 to $8000. Steps at $1A50 and $1A53 covered all nine writes. The two
entry words are $1A7F. Steps at $1A5B and $1A69 also showed the low and
high bytes of the NMI vector being written to RAM.

The stored bytes at $4624–$4643 follow the ten sprite reveal groups.
The load-only write map shows that WIN wrote $4625–$4643. The subsequent
range $4644–$5058 matches the bytes at the KERNAL LOAD checkpoint, at
WIN entry and on the ending screen, with no writes during the load.

A controlled raster IRQ stop at $1572 showed the opcode `BD F7 07` with SP and X both $F2. The indexed read loaded $8D from $08E9. $1575 then tests bit four, and a set bit transfers to $1A7F.

On the disk exit, $1428 selects processor-port banking value six before the KERNAL calls. A controlled S-marker run stopped at $FFBA with a ROM jump visible to the processor and three zero bytes in the underlying RAM.
