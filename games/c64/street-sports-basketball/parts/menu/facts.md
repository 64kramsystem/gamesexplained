# Court and team selection

## Title and option panels

At the $0800 hand-over the title bitmap at $6000–$7F3F and all 1,000 colour cells at $5C00–$5FE7 already match the title screen. At the title, $DD00 reads $96 and $D018 reads $7D. The menu replaces the bottom 16 bitmap rows with data expanded from the value/count pairs at $EFE8–$FD1B. The loop at $0CBC adds one to the count and stops at $7F40. The expanded image changes 5,120 bytes of bitmap address space.

A checkpoint at $12B7 caught X=$00, Y=$84 when port 2 moved right once from School. The routine draws the Alley preview from $8400. The first four bytes give width, height, column and row. Each following cell has eight multicolour bitmap bytes, one byte carrying two screen colours and one for colour RAM. Court previews are at $8000–$8FE1. The ten draft portraits occupy page-aligned slots starting at $2000 and ending with Dana at $4400. The $192B table points to undrafted figures and $193F points to the roster figures.

## Text

The menu renders bitmap glyphs from $091E plus eight times the character index. Rendered glyphs confirm screen-code letters $01–$1A, space $20 and digits $30–$39. Apostrophe is $27, hyphen $2D and the name-entry cursor is $40. The normal writer at $0DF8 ORs the shape with $55, and the highlighted writer at $0E35 inverts the shape before that operation. Menu panels at $C000–$CFBC are made of 28-cell rows and use $FF to terminate a panel.

## Registers

| Hardware | Use | Evidence |
| --- | --- | --- |
| $01 | CPU banking for SID player, KERNAL I/O and image reads | $086F, $08EB, $0C90, $12D2 |
| $DD00, $DD02 | Select VIC bank $4000 | $0B3A |
| $D011, $D016, $D018 | Multicolour bitmap, display blanking and layout | $0B4A–$0B5F, $08CB |
| $DC00, $DC01 | Active-low joystick inputs | $1236, $1259 |
| $DC0D | CIA interrupt acknowledgement | $090E |
| $D400–$D418 | SID voices and volume | Reset at $E0AB. The music tick enters at $E000. |

## Opening music

The IRQ calls $E000, which jumps to the three-voice player. The tune table at $E495 assigns separate streams beginning at $E4CB, $E6BD and $E755. The dispatch table at $E43A points to 29 commands for waveform, filter, repeats and other settings. Bytes below $C0 are note events with a duration byte, and $FF ends a stream. The three opening streams terminate at $E6BC, $E754 and $EB69.

In the title snapshot an execution checkpoint hit $E3DF with note $35 and X=$6A. One instruction loaded the low frequency byte $60 from $FE6A and stopped at the SID write. The voice register offset was $0E, selecting voice 3.

The draft's computer choice, parts of the match transition and several retained RAM ranges still need coverage.
