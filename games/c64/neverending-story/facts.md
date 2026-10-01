# The NeverEnding Story — facts

## Live state

A fresh Ocean disk boot reaches the Part-1 command prompt after Space through the title and opening narrative. The reference screenshot records the clearing in the Great Forest. The narrative capture matches all 4,277 imported code bytes and 142 word bytes; 29 byte-data bytes differ.

## Display

$A7E3 writes $D018=$38 for the bitmap picture. $A80A writes $D018=$3E for character text. With VIC bank $C000 this selects screen $CC00, bitmap $E000 and font $F800. Comparing its 2,048 bytes with the character ROM halves finds 157 and 215 matching bytes respectively; neither matches. This authored font is absent from the imported address space.

## Room illustrations

The 21 captured descriptors at $0BF9-$0C76 specify row, column, a little-endian source pointer, height and width. Picture 0 spans $A100-$A55F (1120 bytes). Pictures 1–20 span $4300-$93E5 consecutively. Each source row contains width*8 bitmap bytes, then width screen bytes, then width colour bytes.

A direct live call to $05BF was run for each of the 21 descriptors with interrupts disabled and processor port $35. Every bitmap byte, screen byte and colour-RAM low nibble matched the independent record decoder. The calls returned to the injected caller and consumed height*width*10 source bytes. The browser uses the fresh command-prompt snapshot’s sources.

## Text and dispatch

All 94 pointers at $25DD-$2698 were checked against packed records $2699-$28B8. Each record is a length byte followed by that many ASCII bytes; each pointer equals the next record start computed from the preceding record. Capitalization is preserved.

$1638/$163E patch condition-call operand $1642/$1643; handler carry selects continuation or skipped actions. $1690/$1696 patch action-call operand $169A/$169B. Their imported offcut labels now retain the actual operand addresses.

## Display workspace and loader

$0730-$073D copies staged pages $C000/$C100 to $9700/$9800. $0743-$0757 copies $0FA0 bytes from the display bundle at $E000 to $BC00, overwriting those staging pages. Saved display bytes are runtime output excluded from coverage.

$03A0 calls the exchange at $03A6, calls relocated loader $CC00, then falls through into the exchange again. The exchange exposes RAM with processor port $38 and swaps $CC00-$CFFF with $DC00-$DFFF. The parked loader contains non-fill bytes through $DCE3; internal calls name relocated $CCxx addresses.

## Visible graphic records

The six records at $2943-$2966 have a six-byte stride. The source pointer occupies offsets 2 and 3: the scan at $0EDA-$0EF3 starts with X=2 and adds six between records. Consequently record 4 has pointer $295D/$295E and record 5 has pointer $2963/$2964. $1156/$115B write the computed low/high bytes into the final pointer; $1146/$1149 clear them.

## Hidden-page observation

Bank-conditioned watchpoints on physical RAM $D000-$D0FF observed the restored title loading Part 1, reaching its narrative screen, and proceeding to the command prompt. Neither a RAM read nor a RAM store was observed on that trajectory, and all 256 bytes remained equal to the title capture. Injected LDA $D000 and STA $D000 with processor port $34 each stopped at the instruction following the access, confirming both watchpoints were active. This observation does not establish ownership or rule out use by other commands or parts, so the page remains unexplained in coverage.

A second watched load stopped at $0400 before the Part-1 entry instructions. Comparing this hand-over snapshot with the command-prompt snapshot exposes four untracked non-fill runs: $68D7-$6905 (47 bytes), $9D00-$9EF2 (499), $9FEF-$9FFF (17), and $A500-$A55F (96). Their owners still need to be traced.

## Open evidence

The consumer and ownership of hidden page $D000-$D0FF remain unresolved; it is unexplained in coverage. Ownership of the hand-over ranges, parser outcomes, picture reconstruction, objects, save/load and part transitions remain open. The earlier technical article is a private draft until its claims are checked.

## Provenance

Imported `neverending_story_full_listing.txt`, SHA-256 `ef4cadfc4fb0bbe410a3a0881d8ca9da6c877c19ef9579ce2f07147c66f90e12`. Original models are unknown. Source comes from fresh regenerator2000 exports and `listing.py` on the declared snapshot.
