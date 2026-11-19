# The Trap Door (C64) facts

These are findings from boot and annotation. The separate verification and accuracy sample follow the completed byte ledger.

## CPU and display

- $3800 jumps to $3846. The initial route configures the C64 through $38B9. The main update path starts at $3868 and toggles the drawing workspace between high bytes $CC and $D6 at $3893–$38A3. Writes from $57B4 and $57D8 go to RAM under the chip registers while $01 is $30.
- The hardware IRQ enters at $3937. The handler temporarily selects $35 and checks bit 1 of CIA1's interrupt status at $DC0D. On a Timer B interrupt it goes through the $FFF8 hook. $5C26 sets the hook to $186E for the title music.
- CIA2 port A selects VIC bank $C000. $D018 selects the screen plane at $C800 and bitmap at $E000. $D011 enables bitmap mode and $D016 clears multicolour mode. A write watch on $C800–$CBFF stopped at $628A, with zero reads in that range before the first clear. A write watch on $FD30 stopped at $6272 with $84/$85 pointing to $FD00 and Y=$30. The bytes there that match the hand-off's KERNAL vectors at $0314 already match at the SYS stop. They fall inside the generated bitmap area.
- $5217 scans the draw records starting at $9601. It walks in steps of 14 bytes until the $FF at $9C9F, across six rendering passes. Offset 4 selects the pass and offsets 10 and 11 carry the little-endian shape address. In Learner play a read watch on $C289–$C370 caught a read via $90/$91=$C31C by the fetch at $529E after the renderer selected the record at $9789.
- $529C treats bytes $EE–$FF as shape commands. It dispatches through split vectors at $5357/$5369. Lower values name tiles in the current bank. $F4 changes tile bank and $F2 supplies a style override. $FB draws through a nested stream whose address follows the command. The renderer uses two work planes so $5563 can skip cells with unchanged fields.
- Shape command $FD indexes the inline destination words with $50. A controlled CPU trace at $5556 and $5453 for the command at $B1CC selected the words at $B1CD, $B1CF, $B1D1 and $B1D3 for selectors 0–3, then reached the four return commands at $B202, $B230, $B267 and $B2A7.
- Shape command $F7 increments a stream counter at $54E2. Before reaching the limit, it skips the counted candidates to the existing tile. At the limit, it resets the counter and chooses a candidate tile. At $552E it replaces the destination low byte with candidate count plus one before the $5537 store. In a controlled CPU trace with a test stream at $0920, counter 0 reached the existing tile at $0925 and counter 1 with limit 2 and one candidate wrote the selected tile to $0902. Which authored streams reach this path remains open.

- $5601 and $560D fetch split base bytes from $2000 and $2007. The code adds eight times the tile index and copies eight rows to the bitmap. A Learner play execute checkpoint at $5601 caught bank 3, tile index $0A. The observed bank points to $200E, so those eight source bytes start at $205E.
- The reflected-tile path uses the same computed row address as the direct copy. $560A and $5615 patch the indexed load at $564A. Its eight source bytes become indices into the bit-reversal table generated at $0600 by $3DF4. In a controlled instruction trace, bank 6 tile 60 read $375E–$3765 in both modes. With test rows 1, 3, 5, 7, 9, 11, 13 and 15, only the reflected mode also read those indices at $0600. Selection of tile 60 by an authored stream remains open.
- In a second Learner probe, a read watch covering $36B6–$37FF fired at the tile copy from $36FE, with bank 6 in X and row 7 in Y. The first byte read was $3705. A startup store watch covering $0800–$08FF fired after the store at $3DE7. The startup code computes the high offset byte as the tile index shifted right five times.

- Controlled instruction traces of the renderer at $529C showed the nested stream at $BAEF calling $BAD1 before tail-jumping to $BB59. The extensions at $BAF8, $BAFE and $BB04 each call the preceding stream and use the same tail. At $B80F, style 7 makes tile commands $50 through $57 consume two bytes each. Trace outputs are in `work/shape-gaps-probe.txt`.

## Object state and sequences

- An actor sequence is read in two-byte units by $7B4B. A word with a nonzero high byte supplies the renderer pointer for object offsets 10 and 11. A zero high byte selects a command through the split vectors at $8689 and $86DB. The two halves have 82 entries each.
- In a controlled CPU trace from the Learner snapshot, the sequence at $AA44 dispatched commands $09, $06, $0A and $15. With bit 4 of Berk's actor flags clear, it then used frame $B2B7 from $AA4E. With bit 4 set, the branch read its target from $AA4C, dispatched command $11 at $AA88 and used frame $B302 from $AA8A.
- A startup read watch on $C508 caught the load at $3F69, with the next instruction set to store to $0010. A read watch on $C570 and a separate write watch on $9981 caught the same patched copy loop with source $C570 and destination $9981. The first descriptor copies 462 bytes into the active object table.
- The task request list at $46A2 is selected by the task index at $10. It contains the four dish requests, the tidy-up request and grading text. At delivery, task 5 follows a special path from $4A6B. Bit 7 of $15 selects the wages text at $4A93 when set and the untidy-room text at $4A83 when clear.

- The overlap search at $8464 walks backward from $9B25 in steps of 14 bytes. It filters candidate types and flags before comparing drawing passes and rectangle bounds. In a controlled CPU trace with equal bounds, matching pass 2 reached $84DC, returned type $02 with carry clear and stored $9B25 in $5C/$5D. Changing the candidate to pass 3 took the $FF terminator exit with carry set. The trace is in `work/overlap-probe.txt`.
- With a nonzero type at $9AED and a nonzero $20, $6E0B counts up at left $20 and top $84, and counts down away from that position. CPU traces from the Learner snapshot hit the shape-pointer store at $6E4F on four transitions. Counting up to 50 and 200 selected $B832 and $B827. Counting down to 200 and 50 selected $B832 and $B856. The trace is in `work/timed-shape-probe.txt`.

- In a controlled CPU trace, $7242 installed sequence $A6F3 for the record at $9A8B. The interpreter issued the opening frame $A780, repeated it six times, reached frame $A7AC, then jumped to $A713. After the following four repeat groups, the jump at $A745 selected $A70B. See `work/actor-a6f3-probe.txt`.

## Tasks and timing

- $3961 waits for the delay at $55 before selecting or updating a request. The first request is worms. Subsequent selections examine completion flags at $2A–$2D. The cleanup request at $39CB requires at least four completed tasks at $13 and Super mode at $12. The low and high hint pointer loads at $4121 and $4126 resolve task 5 to $44FC.
- For an active request with the door stage at $2F clear, $3A1F increments the tick count at $27. When it reaches 20, $3A44 resets it and $3A46 increments anger at $53. The range $9C–$9F sets the flashing flag at $3B55. At $A0 the routine takes the timeout path. A controlled VICE store watch on $53 caught $3A46 advancing $9B to $9C. A CPU instruction trace with the door stage set returned at $3A41 before incrementing the counter.
- At $3D56, the score transfer repeatedly subtracts from remaining time at $3E/$3F and adds to the score at $40/$41. At $3D40 the mode test selects $19 for Learner and doubles it to $32 in Super for this bonus path.
- The actor update at $751C checks mode before inspecting record $9A99. With an inactive record and bit 1 of $14 set, a controlled instruction trace reached the random call at $7547 in Super mode and returned at $753E in Learner mode. The zero-result branch sets type $22 and sequence $A92B.
- $8434 assigns the opening shape at $C268 to record $9823 and sets the stage at $2F to one. $3BEA moves the door and any linked object through successive stages. The midpoint handler at $3CAE passes the delivery type to the response logic when the task and linked object permit it. The stage $1C path restores the closed shape.

## Input

The menu gives X / Z for right / left, A / Q for down / up, C for drop and T for tip, and joystick port 2. The instruction trace stopped at $5B49 and $5BDA with A=$5D, the terminator of each preceding inline text block. S starts, then L selects Learner or S selects Super. At $5BE8 the Learner trace had X=$01. Stepping the store put $01 in $12. The Super branch reaches the same store with X=$00.

At $58BB the scan saves the CPU port and banks I/O in. It walks seven row and column masks, then merges the keyboard bits with the active-low joystick bits from $DC00. A breakpoint at $58E8 with port 2 right held caught A=$F7 immediately after that read and A=$08 after the low five bits were inverted and masked. The nonzero result was stored at $7C.

The menu scans the CIA1 keyboard matrix at $5C8E. It waits for two consecutive equal reads per row, counts the active-low bits and looks up each pressed position in the character table at $5863. It takes the last character for up to two pressed positions and takes zero for three or more. The comparison at $5CD6 suppresses duplicate detections and $5CD8 saves the current detection for the next scan. In a controlled instruction trace, supplying $FE, $FC and $F8 for the row selected by $FD gave returned values $33, $57 and $00 at $5CE0 on fresh snapshots. Two identical scans with $FE returned $33 and then zero, with $33 retained at operand $5CD7.

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

- The six pitch arguments read at $191C patch the three noise presets at $1943, $1950 and $195D. Each preset copies two high pitch bytes to $1714 and $1720 before starting the noise note. Title pitch index 63 reads the zero pair at $1A2E. A VICE read watch stopped just after the fetch in the pitch lookup at $18A3, and the instruction trace identified the first argument at $1A8A.
- The title IRQ routine dispatches events through a patched JMP at $1506. An execute checkpoint there caught the first five stream bytes selected as events, $E9, $E6, $00, $00 and $86, from $1A3A, $1A40, $1A43, $1A44 and $1A45.
- The kit CPU simulator, starting from the title music IRQ snapshot, reads 1,453 contiguous bytes at $1A39–$1FE5 and dispatches 521 distinct event positions. The last event is $57, which jumps to $1557 to restore the saved pointer and begin the sequence again. The high-level event payload lengths can vary with the voice state. The trace used the actual instructions to find event boundaries.
- The sound service at $61B2 writes the three voice register groups using record stride $37 and register stride 7. It also writes the SID filter state. The register census and instruction trace outputs are in `work/`.
- The effect driver at $5DED masks the sound request to seven bits and indexes the relative-offset table at $9000. In Learner play, a read watch caught $5E0D reading the low byte of entry $0C. The instruction trace resolved the effect address to $9176. An execute checkpoint at $5FED caught that effect's first step with $94/$95 pointing to $9180. The local decoder follows the header and step lengths used by $5D81, $5FD8 and $606A. It accounts for the 20 offsets and their contiguous records through $928E.

## Ledger scope

- $CC00–$CEFF is zero at hand-off. The stores at $57DC, $57DF and $57E2 clear these pages. A Learner play store watch on $CD00–$CEFF fired at $57DF with the CPU port at $30. The renderer computes destinations in that workspace from $58 and its row and column tables at $52BC–$52DE. $4B39 also stages response text at $CC00.
- The bytes at $FFF8–$FFFF are runtime copies of the authored vector template at $3959–$3960. A hand-off store watch fired on the first write at $38D5 with X=$07. The timer service pointer at $FFF8/$FFF9 is replaced when the music and sound services install their hooks.

- From the original cassette LOAD command to the execute checkpoint at $3800, write watches on $0900–$14FF and $9400–$95FF stayed at zero. Those bytes retained the power-on pattern. The disk expansion wrote zeroes there. A separate watch at $9600 stopped immediately after $03C0 executed `STA ($FB),Y` with $FB/$FC holding $9600 and Y zero. The $1500 and $9601 controls also registered writes before $3800.
- Cassette write watches counted 336, 365, 721 and 369 stores in $4FB0–$50FF, $6293–$63FF, $8D2F–$8FFF and $928F–$93FF respectively. Both cassette captures agree with all the disk bytes in those intervals at $3800. Their use remains open. [Ultimate Tape Archive](https://uta.pokefinder.org/list.php?p=t&s=1)

## Register census landmarks

| Register | Use | Instruction |
|---|---|---|
| $0001 | Selects RAM and I/O for the caller's operation | $38BC, $393D, $5219, $591D |
| $D011 / $D016 / $D018 | Bitmap mode, colour mode and plane selectors | $3923–$3933 |
| $D012 | Raster reads seed $51FE and $51FD. A third read is shifted right and made odd for $51FF | $51E9–$51F8 |
| $D020 | Border colour | $5210 |
| $D400–$D414 | SID frequency, pulse, control and envelopes | $1604–$1610, $6217–$6247 |
| $D415–$D418 | SID shared filter and volume | $61DD–$6204, $5C51 |
| $DC00 / $DC01 | Keyboard matrix and joystick port 2 | $58CA–$58E8 |
| $DC04–$DC07 / $DC0D–$DC0F | CIA1 timer setup, interrupt selection and dispatch | $38C8–$38FC, $393F |
| $DD00 / $DD02 | VIC bank selection | $390C–$3919 |

Indexed writes to $D000–$DFFF in the workspace loops are RAM writes. They appear in the address census next to hardware registers because the addresses overlap.


## The listing's error rate

An independent `gpt-6.2-sol` checker sampled 70 of 1,375 comments with seed 20261119. Ten had incorrect or incomplete details and all ten were corrected, along with related comments. The corrections cover the crack-intro screen residue, patchable noise presets, the task 5 hint pointer, the space glyph, raster seeding, keyboard repeat suppression, two object updates and actor sequence commands. The estimated error rate of the sampled listing is 14.3% with a 95% Wilson interval of 7.9% to 24.3%. Weighting by stratum size gives 12.3%. The checker may have missed errors.
