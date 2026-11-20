# Opening and globe selector

The left globe opens Fire and the right globe opens Ice. The centre hotspot opens the high-score screen. The loader at $14E6 uses $13FA to choose HL or IL. Its two descriptors both return from LOAD to $1800. The difficulty prompts for the two globes use the screen-code table starting at $1AF9.

The title copy from $2895 and the globe copy from $5925 both target bitmap RAM at $E000. Stops at $2222 and $1F9F showed the two source pointers and the common destination pointer. The globe copy at $1F47 installs its matrix at $CC00, and $2025 installs the cursor shape from $8125 and the sprite pointers at the end of that matrix. The running snapshot’s first 1016 matrix bytes and its bitmap through $FE7F match the stored sources.

The copy at $1FAC installs the title sprite shapes in RAM from $C000. Single-stepping $1FC0 and $1FC2 confirmed the first stored shape byte. A stop at $1FCE showed all 2048 bytes matched the source at $51A5, including the first 128 bytes of the globe bitmap at the end of the transfer.

$2006 installs the title sound-effect image with indexed stores to $0400, $0500, $0600 and $06F0. The last two copies overlap by 16 bytes. Instruction steps at all four stores confirmed the source pages. The installed driver and its effect records through $07BB match the quest entry images.

$2510 blends two 16-byte glyph strips with the stored title bitmap. A controlled instruction trace at $2586 read the upper strips at $4895–$48A4 for glyph $00 and $4C45–$4C54 for glyph $27. The glyph bytes index the mask and foreground tables at $25ED and $26ED.

The title sprite text starts at $17E9. The loop calculates a source pointer by multiplying the row index by eight. In a controlled read of row ten, $1757 fetched $1D from its eighth slot. The stored text includes FLAIR SOFTWARE PRESENTS and PRESS FIRE TO START.

$2492 selects one of three groups of nine script pointers at $1C73. With language and script index both zero, a stop at $24AB showed the script pointer at $1CAD and single-stepping read $09 as the first position byte.

The RAM at $CA00–$CBFF, $D000–$DFFF and $FF83–$FFB7 matches across the language selector, OPEN entry and the globe screen. The trace from language selection to the OPEN checkpoint recorded no underlying RAM accesses in those ranges. The copy at $1F82 separately installs a page at $FE80, whose slice at $FEE8–$FF07 matches $780D–$782C in the stored image.
