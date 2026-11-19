# Bone Cruncher technical facts

## Build and memory

The New Imports disk contains a single packed PRG. The trainer's No path leaves `DEC $4954` at $3845. The game starts at $3600. The hand-over snapshot is `work/entry.vsf`. The level 1 snapshot is `work/plain-play.vsf`.

| Address | Role |
|---|---|
| $3600 | Startup, title screen setup and KERNAL NMI restart |
| $6000 | Output buffer for expanded mazes |
| $7000 | Work area for the tile-to-character conversion before clipping to the viewport |
| $8400 | VIC screen matrix. The upper 20 rows show the maze and the bottom five show the panel during play. |
| $87F8–$87FF | Eight hardware sprite pointer slots |
| $8800, $A000, $B800 | Panel, maze and title character sets |
| $A800–$B7FF | Sprite shape bank addressed by pointers $A0 through $DF |
| $C000 | Saved maze cells used around the bathing scenes |
| $D000–$DFFF | RAM contains the same 4,096 bytes as $E000–$EFFF in both snapshots. These bytes are accounted for separately in the ledger. |
| $E000 and other entries of $C9D3 | Packed screens and mazes |

The New Imports loader credit screen at $0400–$07E7 remains in RAM after the game selects $8400. The 24 bytes after it match hard-reset RAM. The hand-over's title and panel data at $8400 are included because they already contain game artwork.

## Resident maps and screens

$C900 uses A as the index into the 30 pointers at $C9D3. The first eight select screen records. Indices eight through 29 select the 22 mazes. Each record supplies the output address and an offset to its run-count list, both as little-endian words. The packed stream uses one flag byte per eight values. Low bits come out first. A clear bit emits one literal. A set bit consumes the next repeat count and expands the associated value by that count. Count zero ends the stream.

$C9C5 stores $35 in the processor port to make the data beneath KERNAL visible. $C9B7 restores $37 after unpacking. At the title, an execution breakpoint observed A=0 at $C900. A store watch at $8400 fired after $C947 with glyph $DC. The return to $C9B7 observed A=0 on the count terminator. The first maze stream at $3368 expands to 1,408 bytes. The gameplay scan indexes maze rows with a 48-byte stride.

Two fragments after $FD6D reproduce sections of the packing used by levels 3 and 4. Specifically, $FD76–$FE32 matches $EAD0–$EB8C, and $FEAC–$FFFE matches $EC10–$ED62. This establishes the data format and overlap. Its original role remains open. The retained code at $9E69–$9FF3 contains parts of a filename parser and an assembler-style byte output routine. A number of its call targets now hold the second music bank's note data.

## Text and passwords

The visible letter codes follow screen-code order. $01–$1A are A–Z, $20 is space, $30–$39 are 0–9 and $3A is the colon used by the panel. Glyphs from $80 upward include artwork as well as text fragments. The title and level panel use separate 2 KB glyph banks. Each entry is eight rows of eight bits. Local contacts for all three banks are in `work/glyphs-*.png`.

$4610 reads the KERNAL keyboard buffer. It accepts letters and spaces, handles Delete, and compares twelve codes at $852B. The password records start at $CB40 at a stride of twelve. Subtract $36 from a table byte to get its displayed character code. A pad byte is $56, which becomes a space. For example, the first record decodes to GOLEMSTENCH and a trailing space. Screen 7 asks the player to enter the password. Screen 6 displays the final congratulations after the last maze.

## Input and rules

The gameplay port 2 read is at $39B0. It sets bit 4 in A before comparing the active-low directions. Code $77 invokes $3CC4 with Y=$61 for right. Other comparisons are $7B for left, $7D for down and $7E for up. The direction handlers use $7C61 to select the corresponding fine-scroll animation.

When a target cell contains mould ($02), $3E6A reads CIA1 port A again. In a level 1 snapshot with the same target cell $618A set to $02 for both cases, a right press stopped at $3E71 with A=$77 and the store watch observed tile $03 after $3E73. Right plus fire stopped at $3E7F with A=$67 and the watch observed tile $01 after $3E81. The right-only branch returns one. The fire branch returns zero, so Bono stays in place.

$3D08 consumes five skeletons to produce one soap when the soap count is below nine. $3DEE and $3E1D increment skeleton or key inventory respectively up to nine. $3E49 spends a key to turn a gate into a clear tile. $3D33 and the following bath branches require soap and spend one. $476E and $4844 increment the level's delivery count. The fifth delivery calls the password-award path and advances the internal level selector.

The score is six decimal characters starting at $8767. $4541 selects the place advanced by $44B3. The selectors for mould, skeleton or key, soap making and soap delivery are one, two, three and four. Carries use the glyphs for decimal digits.

## Graphics and audio I/O

| Register | Access and role |
|---|---|
| $DD00 | $3627 selects VIC bank $8000. |
| $D018 | $CA4F and $CA69 switch character banks in the raster handler. The level 1 trace stopped at the two writes with A=$12 and $18. |
| $D012, $D019, $D01A | $CA20 and $CA3C set the raster compare, switch between $01 and $D2, acknowledge and enable raster interrupts. |
| $D000–$D00F, $D015, $D027–$D02E | The level and interludes position, enable and colour the VIC sprites. The interludes save and restore these values. |
| $D800–$DBE7 | $3F30 recolours the whole screen via $C800. $3BC5 updates the maze viewport through a separate table at $8300. |
| $DC00 | Joystick port 2 input read at $39B0 and $3E6A, among other polling sites. |
| $DC0D, $DC0E | The raster setup masks CIA interrupt sources. The unpacker stops and restarts timer A. |
| $D400–$D414 | Drivers write pitch, width, waveform and envelopes in seven-byte voice slots. |
| $D416, $D417, $D418, $D41C | Global SID filter and volume accesses, including modulation from the voice 3 envelope read in $6D22 and $9422. |

The raster copies 128-byte character frames using the twelve source and destination pairs at $CAFF–$CB2E. A separate copy selects one of three 64-byte frames for $A1A0 via the event mode at $CFFF. The viewport expands each maze tile into a four-by-four matrix of screen codes. Each tile indexes the pointers at $7600 and $767A.

Two resident SID drivers start through $6CE8 and $9E5E. Each driver selects piece-specific tables, with state slots indexed by zero, seven and fourteen. It advances note patterns through a split pointer list and uses an indirect dispatch for per-voice effects. The mute output configuration was the dummy audio device, so the analysis of those drivers uses the code and register accesses.

## Function keys

Separate execution breakpoints with matrix-key input observed F1 reaching $4610 with $CB=$04, F3 at $3988 with $CB=$05, and F5 at $398F with $CB=$06. F3 jumps back to $3600. F5 sets the death request at $7C66. The hazard probe at $3C64 also sets that flag. It typically compares tile $05 at offsets $30, $5F, $5F, $61 and $90 relative to the biased maze pointer. Its last comparison uses a profile-dependent offset and tile value.

## The listing's error rate

Seed 3617 sampled 65 of 708 comments with an independent gpt-6.2-sol checker. Eight contained errors and all eight were corrected. Corrections cover the indexed maze scan and special marker address, hazard offsets, the music row counter, an instrument-table patch address, a pulse-width initialisation case, a voice helper and a bypassed return. Related comments in the parallel player were corrected at the same time. The estimated sample error rate was 12.3%, with a 95% Wilson interval of 6.4% to 22.5%. The estimate weighted by the strata was 12.1%. The checker may have missed errors.
