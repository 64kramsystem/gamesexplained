# The Trap Door (C64) facts

These are findings from boot and annotation. The separate verification and accuracy sample follow the completed byte ledger.

## CPU and display

- $3800 jumps to $3846. The initial route configures the C64 through $38B9. The main update path starts at $3868 and toggles the drawing workspace between high bytes $CC and $D6 at $3893–$38A3. Writes from $57B4 and $57D8 go to RAM under the chip registers while $01 is $30.
- The hardware IRQ enters at $3937. The handler temporarily selects $35 and checks bit 1 of CIA1's interrupt status at $DC0D. On a Timer B interrupt it goes through the $FFF8 hook. $5C26 sets the hook to $186E for the title music.
- CIA2 port A selects VIC bank $C000. $D018 selects the screen plane at $C800 and bitmap at $E000. $D011 enables bitmap mode and $D016 clears multicolour mode. A write watch on $C800–$CBFF stopped at $628A, with zero reads in that range before the first clear. A write watch on $FD30 stopped at $6272 with $84/$85 pointing to $FD00 and Y=$30. The bytes there that match the hand-off's KERNAL vectors at $0314 already match at the SYS stop. They fall inside the generated bitmap area.
- $5217 scans the draw records starting at $9601. It walks in steps of 14 bytes until the $FF at $9C9F, across six rendering passes. Offset 4 selects the pass and offsets 10 and 11 carry the little-endian shape address. In Learner play a read watch on $C289–$C370 caught a read via $90/$91=$C31C by the fetch at $529E after the renderer selected the record at $9789.
- $529C treats bytes $EE–$FF as shape commands. It dispatches through split vectors at $5357/$5369. Lower values name tiles in the current bank. $F4 changes tile bank and $F2 supplies a style override. $FB draws through a nested stream whose address follows the command. The renderer uses two work planes so $5563 can skip cells with unchanged fields.
- $5601 and $560D fetch split base bytes from $2000 and $2007. The code adds eight times the tile index and copies eight rows to the bitmap. A Learner play execute checkpoint at $5601 caught bank 3, tile index $0A. The observed bank points to $200E, so those eight source bytes start at $205E.

## Input

The menu gives X / Z for right / left, A / Q for down / up, C for drop and T for tip, and joystick port 2. S starts, then L selects Learner or S selects Super.

At $58BB the scan saves the CPU port and banks I/O in. It walks seven row and column masks, then merges the keyboard bits with the active-low joystick bits from $DC00. A breakpoint at $58E8 with port 2 right held caught A=$F7 immediately after that read and A=$08 after the low five bits were inverted and masked. The nonzero result was stored at $7C.

A stop at the self-modifying JMP at $6497 and one CPU instruction per case showed the following destinations from the same Learner snapshot. The destinations establish the control dispatch. Object eligibility, collisions and the post-dispatch state changes remain open for individual mechanics.

| Matrix key | Mask at $74 | Jump destination |
|---|---|---|
| Q | $01 | $65E5 |
| A | $02 | $682A |
| Z | $04 | $69CF |
| X | $08 | $6ADB |
| C | $10 | $64DC |
| T | $20 | $659D |

## Text

- The controls screen and ordinary text support the C64 ROM font. $5914 selects that font when the custom base in $60/$61 is zero. The glyph copier reads eight rows. The inline text reader at $59E0 resumes execution after the $5D terminator. $26 introduces another run with new position and colour bytes.
- The response renderer at $4C05 uses a separate face at $4D00 with sixteen bytes per glyph. Digits 0–9 use indices $00–$09, period, comma, apostrophe and exclamation use $0A–$0D, and A–Z use $11–$2A. $4C32 computes the alphanumeric index from the stored byte minus $30. The row copy also handles blank and punctuation cases. The local rendering sheet is `work/response-font-16.png`.
- $3DFF selects the custom panel glyph base $C744. Its border uses index $04, a square outline. The rendered cells at that base are panel motifs. The local rendering sheet is `work/custom-font.png`.
- The raw text sweep finds the four recipe requests. The response parser at $4AC9 resolves conditions before copying text to $CC00. Its word renderer recognizes $2B and $24 as boundaries and $5D as the text terminator.

## Sound

- The title IRQ routine dispatches events through a patched JMP at $1506. An execute checkpoint there caught the first five stream bytes selected as events, $E9, $E6, $00, $00 and $86, from $1A3A, $1A40, $1A43, $1A44 and $1A45.
- The kit CPU simulator, starting from the title music IRQ snapshot, reads 1,453 contiguous bytes at $1A39–$1FE5 and dispatches 521 distinct event positions. The last event is $57, which jumps to $1557 to restore the saved pointer and begin the sequence again. The high-level event payload lengths can vary with the voice state. The trace used the actual instructions to find event boundaries.
- The sound service at $61B2 writes the three voice register groups using record stride $37 and register stride 7. It also writes the SID filter state. The register census and instruction trace outputs are in `work/`.

## Register census landmarks

| Register | Use | Instruction |
|---|---|---|
| $0001 | Selects RAM and I/O for the caller's operation | $38BC, $393D, $5219, $591D |
| $D011 / $D016 / $D018 | Bitmap mode, colour mode and plane selectors | $3923–$3933 |
| $D012 | Raster samples seed software state | $51E9, $51F2 |
| $D020 | Border colour | $5210 |
| $D400–$D414 | SID frequency, pulse, control and envelopes | $1604–$1610, $6217–$6247 |
| $D415–$D418 | SID shared filter and volume | $61DD–$6204, $5C51 |
| $DC00 / $DC01 | Keyboard matrix and joystick port 2 | $58CA–$58E8 |
| $DC04–$DC07 / $DC0D–$DC0F | CIA1 timer setup, interrupt selection and dispatch | $38C8–$38FC, $393F |
| $DD00 / $DD02 | VIC bank selection | $390C–$3919 |

Indexed writes to $D000–$DFFF in the workspace loops are RAM writes. They appear in the address census next to hardware registers because the addresses overlap.
