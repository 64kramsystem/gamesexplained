# Elvira: The Arcade Game — facts

## Loads and progression

- The selector calls the interlude loader with HL or IL according to the choice byte at $13FA. The addresses to read are $14E6 and $151E in the opening listing.
- Each interlude first requests a B file through $0825 and then an A file through $0875. Stops at KERNAL LOAD showed G1B/G1A, G2B/G2A and G3B/G3A. The A request sets the stack return to $0812, where all three starts were captured. The page copy at $0887 begins with $C700 and $FF00, goes downward, and skips two additional pages at the $C9 boundary.
- The engine uses $094E and $07FF to index the descriptor table at $0A1C. From the loop’s transition path the debugger route with $07FF nonzero reached CL for selector $01 and WIN for selector $0A. The ordinary condition that raises the world-complete flag is open.
- The patched transition into WIN showed a congratulations screen with Elvira and the king. The ending interrupt vector points to $1515.

## Display and input

| Evidence | Behaviour |
|---|---|
| $13D5, $140E and $1412 in a quest | The raster handler dispatches through two stage addresses. $D019 acknowledges the IRQ and $D012 selects the next raster compare. |
| $1486, $14B0 and $14BF in a quest | The HUD stage switches from bank $C000 to $8000 and selects the HUD’s bitmap and matrix. A $D011 write watch stopped at $1489, directly after the store of $7F. |
| $162E in a quest | The playfield stage sets the bank through $DD00 and writes the fine-scroll and memory-selection registers. A Fire capture at raster zero read $D018=$0F. With bank $C000 that selects the $C000 matrix and $F800 character tiles. The three world tile banks have different glyph drawings. |
| $3BD0 in a quest | CIA 1 scans the keyboard by setting one column low and reading the eight rows. $3C26 is its code table and the routine returns zero in $3C1B on an unchanged decode. |
| $2EC9 and $2F69 in a quest | The spell routine selects CIA keyboard columns $FE and $7F and compares the rows with $FD and $EF respectively. These are Return and Space in the keyboard matrix. Return starts an eligible spell. Space is on the selection path. |
| $1D49, $1D76 and $1DA5 in an interlude | The bitmap interlude uses bank $C000. It copies the supplied screen matrix into RAM under I/O at $D400 and the colour bytes into the colour RAM chip at $D800. |

## Text and values

The quest renderer at $0E1F reads scripts starting at the pointers at $0EA6. The groups select English, German and Italian using $C902. The script supplies a row and column before the text. $FE starts a new segment and $FF ends the script. Values 1 through 26 are alphabet positions for A through Z, with two consecutive character indices per letter. $20 is a space and draws $9A on both rows. $2D is remapped before the same pair calculation. The stored text includes PRESS SPACE TO START QUEST, GAME OVER, disk-side prompts, TRADER and LEVEL COMPLETE. The glyph rendering for the heading and trader has not been mapped exhaustively.

The score adder at $2B8C clears each pending digit on consumption and adds into the digits starting at $C903, least significant first. It subtracts ten and carries to the next digit where needed. The life digit at $C901 is decremented on the ordinary death path at $0893. The spell branch at $2EEF increments it with a cap of nine.

## Open analysis

The exact load ranges, packed stream end conditions, object and level formats, graphics outside the traced tile and interlude blocks, and the SID driver need further analysis. The hardware and string sweeps are in the part work directories. The listings record the range and size of loaded non-fill stretches still outside the ledger.

## Map rendering

The world header supplies a metatile-map base at $4F2E, a character-grid base at $4F2C and a colour lookup at $4F2A. The first two bases in the three quest entries are as follows.

| World | Metatile ID grid | Character grid |
|---|---|---|
| Fire | $6A29 | $5077 |
| Ice | $61DC | $5064 |
| Castle | $685C | $515B |

$452C divides the incoming coordinates by four, saves the remainders and builds the map pointer. $182E reads a map byte through that pointer. Single-stepping it at the first draw after each hand-over read zero at $72A9, $6C99 and $76A6 respectively. A nonzero map ID is decremented to index the split offset table at $4560/$461E. The viewport expands a metatile four characters at a time using row offsets 0, 40, 80 and 120. At $1845 the renderer reads the character codes and looks up their colour bytes through $BC. The full grid bounds remain open.
