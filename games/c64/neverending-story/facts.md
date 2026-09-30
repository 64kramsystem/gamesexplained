# The NeverEnding Story — facts

## Live state

A fresh Ocean disk boot reaches the Part-1 command prompt after Space through the title and opening narrative. The reference screenshot records the clearing in the Great Forest. The narrative capture matches all 4,277 imported code bytes and 142 word bytes; 29 byte-data bytes differ.

## Display

$A7E3 writes $D018=$38 for the bitmap picture. $A80A writes $D018=$3E for character text. With VIC bank $C000 this selects screen $CC00, bitmap $E000 and font $F800. Comparing its 2,048 bytes with the character ROM halves finds 157 and 215 matching bytes respectively; neither matches. This authored font is absent from the imported address space.

## Text and dispatch

All 94 pointers at $25DD-$2698 were checked against packed records $2699-$28B8. Each record is a length byte followed by that many ASCII bytes; each pointer equals the next record start computed from the preceding record. Capitalization is preserved.

$1638/$163E patch condition-call operand $1642/$1643; handler carry selects continuation or skipped actions. $1690/$1696 patch action-call operand $169A/$169B. Their imported offcut labels now retain the actual operand addresses.

## Display workspace and loader

$0730-$073D copies staged pages $C000/$C100 to $9700/$9800. $0743-$0757 copies $0FA0 bytes from the display bundle at $E000 to $BC00, overwriting those staging pages. Saved display bytes are runtime output excluded from coverage.

$03A0 calls the exchange at $03A6, calls relocated loader $CC00, then falls through into the exchange again. The exchange exposes RAM with processor port $38 and swaps $CC00-$CFFF with $DC00-$DFFF. The parked loader contains non-fill bytes through $DCE3; internal calls name relocated $CCxx addresses.

## Open evidence

The consumer and ownership of hidden page $D000-$D0FF remain unresolved; it is unexplained in coverage. Loader hand-over comparison, parser outcomes, picture reconstruction, objects, save/load and part transitions remain open. The earlier technical article is a private draft until its claims are checked.

## Provenance

Imported `neverending_story_full_listing.txt`, SHA-256 `ef4cadfc4fb0bbe410a3a0881d8ca9da6c877c19ef9579ce2f07147c66f90e12`. Original models are unknown. Source comes from fresh regenerator2000 exports and `listing.py` on the declared snapshot.
