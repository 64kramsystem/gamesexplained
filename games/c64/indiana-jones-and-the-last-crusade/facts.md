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
