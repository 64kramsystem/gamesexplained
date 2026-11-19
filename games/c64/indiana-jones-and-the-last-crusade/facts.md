# Facts

| Observation | Evidence |
|---|---|
| The common engine uses one character set and one map per asset load. | An execution stop at `$B85E` captured each filename, and store watchpoints at the slot boundaries recorded the writes before `$B861`. The load selector is in `$B80F`. See [orientation.md](orientation.md) for the five ranges. |
| The engine builds the map row pointers at runtime. | `$AD05/$AD0A` write the low and high bytes. The additions at `$AD10/$AD17` use the stage stride. The play snapshots show a first pointer of `$3600` and a stride of 150 in the catacombs or 256 elsewhere. |
| The scroll renderer reads map tiles and copies them into a field buffer. | A read watch over `$3600–$75FF` stopped at PC `$895A`, just after a patched `LDA abs,Y` at `$8957`. `$883C` selects the destination page and the code at `$889E` patches the sources from the row tables. |
| The cave VIC raster split uses two banks. | The captured PAL frame shows `$DD00=$3C` and `$D018=$03` at line 168, then `$D018=$3A` and `$DD00=$3F` around lines 259–260. The panel selects the bank at `$C000`; the field returns to bank 0 with `$0C00` screen RAM and `$2800` patterns in this frame. |
| Gameplay sprites are copied from a sheet in RAM underneath the chips and ROMs. | Holding right hit `$9635`, then `$9CD5` with `X=$3F`, operand `$D200` and `$01=$34`. In the unmodified caves snapshot the four visible player-layer patterns in `$0A00–$0AFF` match sources `$D740`, `$E400`, `$D900` and `$E440` for their 63 pixel bytes. |
| The IRQ translates joystick input into an action code. | `$816F` reads CIA1 port A, masks to the five stick bits, inverts the active-low values and looks up the result through `$7A8D`. `$817A` stores the code at `$7A3F`. The title samples the fire bit directly at `$9867`. |

## Cave light

With the cave timer set to $FF and its phase set to zero, a write watch on $3000–$30FF stopped after the store at $8BDD, with PC=$8BE0, X=$34 and A=$0C. The timer and phase read $01/$01. The dimming path replaces selected palette values, so it can change the colour of many map cells without replacing their character codes. The pickup path at $A6CE clears both counters and reloads the base palette through $B7C0.

## Title text

The title's display uses the character set at `$0800`, with `$D018=$12` in bank 0. The copy at `$97EF` brings six pages from `$BB48`. The text records stored at `$9A3E`, `$9A92`, `$9B64` and `$9BC9` have a column byte, then a colour byte, then the text terminated by `$FF`. Zero in place of the column skips a row. A negative byte in that position terminates the page. The printer masks characters with `$3F`. Letters A–Z take glyphs `$7D–$96`. Digits 0–9 take glyphs `$6C–$75`. Stored bytes `$40` and `$20` select the blank glyphs `$7C` and `$9C` respectively.

## Hardware census anchors

| Register | Use | Instruction |
|---|---|---|
| `$01` | Expose KERNAL for serial reads, then restore the game map. Banking value `$34` exposes sprite data underneath the chips. | `$24B1`, `$24D0`, `$9637` |
| `$D011/$D012/$D019/$D01A` | Configure and reschedule VIC raster IRQs and acknowledge the IRQ. | `$804F`, `$81C0`, `$82A9`, `$82AE` |
| `$D016/$D018/$DD00` | Scroll and select the screen, character set and video bank for the field and panel. | `$80C7`, `$80CC`, `$80F8`, `$8261`, `$826B`, `$8271` |
| `$D800–$DBE7` | Field colour comes from the screen's character codes via the current palette at `$3000`. | `$8302–$8308` |
| `$DC00` | Port 2 input during play and on the title. | `$816F`, `$9867` |
| `$D404/$D40B/$D412` | Clear all three voice control registers when the driver is idle. | `$1012–$1018` |

## Foreground and raster hand-off

A store watchpoint at `$7E71` stopped twice in the saved caves state. The foreground store at `$7E76` left `$01`, with PC `$7E79`. The raster store at `$820C` left zero, with PC `$820F`. The watched byte is the immediate operand of `LDA` at `$7E70`, which the foreground tests while waiting for the raster handler.

## Additional resident routines

The resident image contains a second effects sequencer at `$2208` and a matching setup routine at `$225C`. They use a three-slot state layout at `$1EFD–$1F0E`. Setup reads four pointer bytes per effect from `$21BC`. In the saved image, the records for effects 17 and 18 point into `$2134–$2184`. The IRQ's effects dispatch at `$101E` instead jumps to `$206D`.

The code at `$C628` draws the banner from `$C603`, sets the CIA2 data direction registers to input and uses `$C6FC` to read port B on a strobe from bit 2 of port A. The receiver fills a destination pointer, length and command from the header. Its use by any release and the operation that would occupy `$C6D1` before the patched destination operand remain open. The Electric Boyz stage loading observed in VICE takes the separate serial path at `$24A7`.

## Sprite mirroring

The setup at $B930 builds two 256-entry reversal tables. Bit reversal goes to $0EE8 and reversal of the order of two-bit pixels goes to $06E8. Execution stops at $9D06 after the indexed read confirmed that the preceding instruction at $9D03 uses each of those bases after patching.

In the saved cave gameplay state the single-bit table matches all 256 calculated values. Two entries in the two-bit table differ. The map probe's stores at $A580 and $A58B overwrite the entries at $0754 and $0756 with digits derived from the player's low Y and X bits. Store watchpoints captured $37 and $31 respectively. For source bytes $6C and $6E the copier therefore reads those digits in place of the two-bit reversals $39 and $B9.

## Resident startup

A store watchpoint at $FF7D caught the loader's relocation instruction at $0836. The next unpacking pass runs at $0100. A separate watchpoint at $FC7F stopped immediately after the unpacker's store at $0166, which left $3A, the stride byte for a blank sprite record. An instruction trace from the saved state at $0100 reached $7D5C after 669,251 instructions and wrote the continuous RAM range $1000–$FFEB. The traced bytes in that range matched the VICE hand-over snapshot. The loader's copied bytes at $FFEC–$FFFF survive this unpacking pass. The hardware vectors occupy part of that area once the game initializes interrupts.

The unpacker writes separate copies of the pages at $2500 and $3300 during startup. In the hand-over snapshot 251 of 256 bytes match. Stage setup selects $3300 for the airship contact table through $B197 and the patched operand at $A651. A consumer for the variant at $2500 remains open.

## The listing's error rate

An independent gpt-6.2-sol checker reviewed 60 of 1,075 comments drawn with seed 62. It found six incorrect details, an estimated 10.0% error rate with a 95% Wilson interval of 4.7% to 20.1%. The checker may have missed other errors. All six findings were corrected. They concerned the airship's bypass of the initial map table, the cave light clock's two carries, continue-prompt visibility, the stage contact-table operand, the heart sprite silhouette and the packed sprite's literal byte count. This was a sample of the pre-correction listing. A full audit is still due.
