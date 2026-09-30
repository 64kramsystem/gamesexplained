# The NeverEnding Story — orientation

## Route and captures

Ocean disk release. Hard reset and autostart the first entry, NEVERENDING. Space leaves the title and starts loading Part 1. Allow the load to finish, then disable warp. Space dismisses the opening narrative and reaches the command prompt in the Great Forest.

`work/part1.vsf` is the opening narrative: all 4,277 imported code bytes and 142 word bytes match the supplied RAM image; 29 byte-data bytes differ as state. `work/part1-command.vsf` is the Source snapshot after dismissing the narrative. C64MEM RAM starts at offset 209. `reference/part1-command.png` records that state.

## Machine and scope

Processor port $36, direction $2F; IRQ $0314 points to $A7E0, NMI $0318 to $FE47. $DD00=$C4 selects VIC bank $C000. Picture phase $A7E3 uses screen $CC00 and bitmap $E000 with $D018=$38. Text phase $A80A uses $D018=$3E and authored charset $F800-$FFFF, which matches neither character-ROM half.

The wrapper $03A0-$03E0 exchanges $CC00-$CFFF with hidden RAM $DC00-$DFFF, calls the loader at $CC00, then exchanges back. Non-fill page $D000-$D0FF is unresolved. Parts 2 and 3 are separate loads outside the capture.

## Rebuild

Use `symbols_import.py` on the symbol map and `work/part1-command.vsf`, start its private project through `tools.py`, export with `symbols_export.py`, and generate Source with `listing.py` on the same snapshot. The Ghidra export supplies annotations; it does not generate Source directly. No binary or snapshot is published.
