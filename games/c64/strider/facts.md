# Strider technical facts

## Build and memory

The analysis uses the Five Immortals D64 described in [orientation.md](orientation.md).
Addresses in this file refer to the resident engine unless a stage overlay is named.

| Region | Role |
|---|---|
| $0400 and $0800–$0A92 | Resident file reader and stage bridge. $093C dispatches files by $FF and $0871 patches the next engine stage into $8101. |
| $1600–$47FF, $5A00–$67FF, $E400–$E7FF, $F500–$F6FF | Four replaceable stage payloads. A few files end one byte short. See the stage facts for exact extents. |
| $6C00–$80FE | Three-voice music sequencer, sound-effects player and their streams. |
| $8100–$BEFF | Engine and title code. |
| $C000–$CFFF | Object descriptors, coordinate and movement tables, title data and text. |
| $D000–$DFFF | RAM beneath I/O. $09BF relocates all of file B here from $4000 before the stage loads. |
| $E000 and $E800 | Panel and title matrices in VIC bank $C000. The engine also uses parts of those pages for generated tables and sprite state. |

The title calls $B5B3 for a six-slot raster schedule. Gameplay chains $8210 and $8269, with raster compare values $26 and $AD. The first handler chooses one of the two playfield matrices in bank $4000 and calls the SID updater at $6C12. The second selects the panel in bank $C000 and publishes the prepared sprite state.

The map read at $A0F0 takes a byte index from a 144-byte-stride map. Four stage pages at $E400, $E500, $E600 and $E700 resolve the character codes of that index's 2×2 block. The collision lookup uses the same map and reads the stage property table at $F500.

The gameplay input read at $8BE4 takes the five active-low port 2 bits from CIA1. Neutral, right, and right with fire produced table indices $00, $08 and $18 in a stepped VICE trace, and $C7C8 translated them to $00, $01 and $11.

## The listing's error rate

The independent gpt-6.2-sol sample drew 80 of 665 comments with seed 6510 and found six wrong details. The observed rate was 7.5%, with a 95% Wilson interval of 3.5% to 15.4%. The estimate weighted by stratum size was 8.3%. The checker may have missed other errors. Corrections covered the slide clamp, music repeat state, traversal transition, particle glyph terminator and the starting coordinate byte order across all five stages.

## Live tests

- The loader was stopped at $0840 before stage 1 and at $8100 for each stage. The later stage routes hit the file reader's KERNAL call site at $041F four times each. All 89,595 stage payload bytes match their entry snapshots.
- Step from $A0F0 with a map byte of $7A. The first three quadrant lookups returned $67, $2B and $6B and the instruction trace reached the fourth lookup.
- A ten-frame advance through gameplay from the tile probe recorded nine hits each at $8210, $8269 and $8260 and 72 hits at $871B, the eight-sprite pointer store.
- The grounded input probe restored the same $8BE4 stop for each of four 12-frame cases. Neutral held player X/Y at $8E/$7C. Right moved X to $9A and kept Y at $7C. Up changed Y to $56, wrote action 1 and hit the jump displacement instruction at $8EAB six times. Fire hit the sword sound-request instruction at $9BB5 once. The $8269 control counted 12 hits in each case.
- The timer's $8B23 entry was stopped with the two BCD bytes set to $0100. Eight instruction steps through the two decimal subtracts wrote $0099. Neutral grounded play produced six timer decrements in 12 frames. The timer measures update passes and the count changes when work such as a sword redraw takes longer.
- The same neutral grounded probe hit $6C12 11 times and recorded 181 stores in $D400–$D418. The probe began partway through the first raster frame.
- With stage 1 stopped at $A292, a nonnegative value at $148D took the completion path. The execute stop at $A2AC found X = 1 and stepping its store wrote 1 to $FF. Later stage loads were verified by entering the actual loader with each selector.

The [resident facts](parts/resident/facts.md) describe the control, display and sound paths used by all five stages.
