# Resident engine

The resident snapshot is `work/play-round1.vsf`. The handover
comparison is `work/entry.vsf`. The IRQ vector points to $53BD, the
playfield NMI handlers are $5419 and $5464, and the main game loop
waits at $4051 for CIA 1 timer A. The timer latch installed at
$4D6B and $4D70 is $998F. $4059 and $4061 wait on raster position
as part of the same update loop.

| Register or range | Code | Role |
|---|---|---|
| $0000–$0001 | $3C18, $8073–$8077 | Banks ROM or I/O out for particular memory operations |
| $D000–$D01D | $5663 and following | Programs positions, hardware enables and sprite attributes for the next group |
| $D011, $D012, $D018 | $5419, $5464 and the raster IRQ chain | Fine scrolling, raster scheduling and display split |
| $D019, $D01A | $53C9, $5316 | Acknowledges and enables VIC interrupts |
| $D020–$D026 | $4D92 and following, $5494 | Panel, playfield and shared sprite colours |
| $D400–$D418 | $F9EB–$FFF9 | SID voices, filter and volume |
| $D800–$DBFF | $8264 and following | Scrolls the colour cells alongside character rows |
| $DC00–$DC01 | $4BBF, $4CD6 | Controller direction and fire reads, and pause keys |
| $DC04–$DC05, $DC0D–$DC0E | $4D6B, $4051, $4F10 | Sets timer A period, polls its flag and starts the timer |
| $DD00, $DD02 | $4DB4 | Selects VIC bank $C000 |
| $DD0D | $5419 and $5464 | Acknowledges the two playfield NMI phases |

$3C0D temporarily banks out I/O and swaps 160 bytes between $D358
and $3F5A. This is a RAM access even though the operand lies within
the I/O address range. The listing leaves other unattributed RAM under
the I/O area in the coverage ledger.
