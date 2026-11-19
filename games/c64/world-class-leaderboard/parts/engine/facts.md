# Golf engine technical facts

## Display and memory

The first tee is a VIC-II multicolour bitmap with bank $4000, bitmap $4000 and screen matrix $6000. At capture, the VIC memory register was $81 and CIA2 port A ended in binary 10. CPU port $01 read $35 during play and the indirect IRQ vector at $0314 held $0E39. The RAM IRQ stub at $FF48 preserves A, X and Y and routes ordinary IRQs through that vector. The initializer at $14BA sets the VIC and copies the ROM pages that hold the interrupt entry. The initializer at $19F5 writes the separate game stub at $FF58.

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

The course screen is painted from polygon boundaries and a mask bank. $20B0 expands signed boundary deltas. $247F transforms coordinate pairs and $97B5 projects the ball or aim into screen coordinates. $2DE5 steps along a projected segment and clips against 120 multicolour X positions and 200 Y positions. $AFB5 selects mask addresses from $BF7E/$BF9A. The sixteen swing-frame streams and the putting packet at $6E00–$925F use byte-and-offset pairs separated into pages by zero sentinels. Decoding frame packet zero yielded exactly the three pages at $6800–$6AFF in the tee snapshot.

## Text

Bitmap output locates glyphs at eight times the index plus the base selected by $8E. $121B derives the bases from $5FD5 and $5FD9. The three nonzero bases are $EDAB, $E8AB and $EFAB. Local font grids were rendered from the tee snapshot.

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

$15C5 cycles the club index through 0–12. $1662 captures release and $160F latches the later snap press from the timer. The ball integration routine at $3B18 keeps a remainder per axis and uses it to carry fractional movement across updates. The documented skill-specific rules beyond the traced branches remain open in [features.md](../../features.md).
