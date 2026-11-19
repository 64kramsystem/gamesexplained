# Golf engine technical facts

## Display and memory

The first tee is a VIC-II multicolour bitmap with bank $4000, bitmap $4000 and screen matrix $6000. At capture, the VIC memory register was $81 and CIA2 port A ended in binary 10. CPU port $01 read $35 during play and the indirect IRQ vector at $0314 held $0E39. The RAM IRQ stub at $FF48 preserves A, X and Y and routes ordinary IRQs through that vector. The initializer at $14BA sets the VIC and copies the ROM pages that hold the interrupt entry. The initializer at $19F5 writes the separate game stub at $FF58. The tee snapshot matches KERNAL revision 901227-03 byte for byte at $FE00–$FF57 and $FF62–$FFFF. The ledger retains the interrupt entry at $FF48 and the RTI byte at $FEC1, where the initializer explicitly installs the NMI target. The ledger excludes the remaining ROM copy. At $FDF9–$FDFF, the physical RAM matches the hard-reset fill in the entry and tee captures. The keyboard and disk paths select system ROM for KERNAL calls.

| Registers | Use and evidence |
|---|---|
| $00–$01 | CPU port mapping. $12A3 selects $36 for KERNAL keyboard calls and $35 on return. $BF50 selects $24 during the staged terrain copy, then $25. |
| $D000–$D00B, $D027–$D02C | The golfer's six sprite positions and colours. Indexed stores appear at $17F7 and $180A. |
| $D00C–$D010, $D015 | Ball and marker sprites, their high X bits and sprite enables. The aiming output writes sprite 7 at $37A9 and $37BC. |
| $D011, $D012, $D019, $D01A | Raster interrupt line $FB and dispatch through $0E39. The handler checks and acknowledges the VIC interrupt request. |
| $D016, $D018, $DD00 | Bitmap mode and memory placement. The initializer writes these at $1503, $14FE and $14F9. The resident loader also uses $DD00 for disk transfers. |
| $D400–$D414 | SID voice registers. $ABD2 indexes frequency, pulse width, ADSR and control with a seven-register stride. |
| $D415–$D418 | SID cutoff, routing and output level. The filter cutoff update writes the low and high bytes at $ABC3 and $ABBD. |
| $DC00, $DC02–$DC03 | Port 2 polling and temporary input direction selection at $12C6. The keyboard path restores a different port configuration before SCNKEY. |
| $DC04–$DC05, $DC0D–$DC0E | CIA1 timer A and its interrupt handling. $101D advances the swing meter during timer interrupts. |
| $DC08–$DC0B | CIA time of day. The player menu clears it at $A2A5 and polls minutes at $A1C6 for the demo timeout. |
| $DD00, $DD02 | Drive transfer bits and direction control in the resident loader at $CCA7 and $CDD1. |

The VIC bitmap spans $4000–$5F3F. A store watch at $4000 stopped after $B9DD wrote $FF during the course-name fill. The ledger excludes the bitmap output and retains the glyphs and packed layouts that produce it.

The course screen is painted from polygon boundaries and a mask bank. $20B0 expands signed boundary deltas. $247F transforms coordinate pairs and $97B5 projects the ball or aim into screen coordinates. $2DE5 steps along a projected segment and clips against 120 multicolour X positions and 200 Y positions. $AFB5 selects mask addresses from $BF7E/$BF9A. The sixteen swing-frame streams and the putting packet at $6E00–$925F use byte-and-offset pairs separated into pages by zero sentinels. Decoding frame packet zero yielded exactly the three pages at $6800–$6AFF in the tee snapshot.

The disk intro builds its decompression lookup tables in page three. A store watch on $03A8 first caught KERNAL RAM initialization and later stopped at boot PC $2EB0 with $41 just written by the indexed store at $2EAD. Range watches caught the same instruction writing the remaining nonzero bytes of the table in $03A2–$03E8. The engine ledger excludes that boot workspace. The engine BIT instructions referencing $00A2, $00A9, $02A2, $02A9, $03A2 and $03A9 use overlapping immediate loads. They preserve the selected register and fall through to a store, skipping the alternate entry.

## Text

Bitmap output locates glyphs at eight times the index plus the base selected by $8E. $121B derives the bases from $5FD5 and $5FD9. The three nonzero bases are $EDAB, $E8AB and $EFAB. Local font grids were rendered from the tee snapshot. In targeted calls from the tee state, $121B resolved bank 2 glyph $3C to $EA8B and bank 3 glyph $BA to $F57B. A read watchpoint on each address fired at the bitmap copy loop at $1328. The bytes at $EA87 are glyph data with the KERNAL hidden and the SCNKEY implementation is visible at the same address with the KERNAL selected.

$E000–$E0F0 decodes into thirteen rows of thirty glyph values with the same literal and $FF,count,value forms as the adjacent course layout. No encoded run crosses a row boundary. The code that selects this stream is open. $F57B–$F5F2 holds fifteen eight-byte frame and fill cells before the packed setup prompt at $F5F3.

| Encoded value | Meaning in the setup bitmap text |
|---|---|
| $96–$9F | 0–9 |
| $A0–$B9 | A–Z |
| $94 | Space in the name entry conversion |
| $11 | Blank used in the disk prompt rows |
| $0D | Slash in the prompt Y/N field |

The stored course title and load filenames are PETSCII. $B9CC translates the title into glyph indices for its on-course display. The name entry path stores A–Z as 30–55 in the player record and uses 10 for a space. The printer has a separate text encoding path.

## Targeted instruction traces

| Test | Observed |
|---|---|
| Left aim from the tee using port 2 | A store watch at $003F conditioned on PC $371F fired once. The low byte changed from $00 to $FF. Stepping $3721, $3724 and $3726 changed the high byte from $18 to $17. |
| Swing start using port 2 fire | The $15C1 store watch fired once and set $0D00 to 1. |
| Power release | After releasing fire, the $1682 store watch fired once. The timer value at $85 and captured value at $0D07 were both $06 in that run. |
| Course selection | A trace of the setup keyboard handler through $B860 and the load at $A291 showed BCT being selected by the letter B and updating the course descriptor. |
| Polygon edge modes | Two CPU steps from each of $31F3, $31F6 and $31F9 showed that the overlapping BIT instructions preserve the selected accumulator value. The common store at $31FB receives 1, 2 or 3. |
| Hole coordinate offset at $22AE | Instruction steps with the input word at $21A5 set to $11FE produced $1201 for offset $03, $11FE for $FF and $11FB for $FC. The negative path subtracts the ones' complement of the offset. |
| Boundary and score field entry points | CPU steps beginning at $20AA, $20AD and $20B0 reached $20B2 with X equal to 0, 1 and 2. Steps from $9F8A, $9F8D, $9F90 and $9F93 reached $9F95 with X equal to 0, 1, 2 and 3. |
| Alternate club scale | For club index zero, CPU steps through $3FEC gave A=$3E at $3FF8 with the putting option clear. Setting the option took the shift-and-add path and returned $13. |
| Status panel matrix rows | The stores at $1FEE and $200F wrote $E7 to $E37B and $E3E0. After all twelve row starts held $E7, the decoder's first load at $11CA read $44 from $E379. |
| Scorecard subtotals | Stops at $9B71, $9B84 and $9B9F confirmed back nine, front nine and combined totals. An injected score record of 1–18 gave 126, 45 and 171. Nine 31s followed by nine 35s gave 315, 279 and 594, including the carry into each high byte. |
| Skill-dependent lateral adjustment | CPU steps from $3807 with club zero and meter index six reached $382C with $0D3D equal to 0 for Kids and 16 for Amateur and Professional. The Kids branch replaces the incoming meter index with seven. |

$15C5 cycles the club index through 0–12. $1662 captures release and $160F latches the later snap press from the timer. The ball integration routine at $3B18 keeps a remainder per axis and uses it to carry fractional movement across updates. The documented skill-specific rules beyond the traced branches remain open in [features.md](../../features.md).
