# Loading presentation

The listing snapshot is stopped at the first poll at $ACA2. The title bitmap in $E000–$FF3F matches the first 8,000 bytes produced by unpacking record 376. The original stream consists of single-byte controls followed by literal runs or repeated bytes. The low seven bits of a negative control give the repeat count, and a zero control ends the stream.

The sound player starts at $1001 and ticks at $1004 under the CIA1 timer IRQ at $AFE6. $AF79 joins 1,314 bytes from $B011 with 3,360 more from $7000. The packet stream expands to 5,846 bytes at $1000, of which 5,843 match the title input snapshot after the player begins. The other sound path uses CIA2 timer B and produces amplitude changes via $D418. The title script at $AA00 selects speech items two and three.

The speech driver uses writable wave buffers in page $08. A store watch over $0800–$087F stopped immediately after $A7F7 while running the title's voice call at $AC86. The first 128 bytes of that page are identical across the title and engine hand-over snapshots. They are speech workspace left by startup.

The first voice's control write at $1501 patches the immediate operand at $14DA. A write watchpoint stopped at $1504 with Y and that operand both $08. The next pass loads the saved byte at $14D9 and clears bit 0 before writing the gate-off control to $D404. The corresponding stores for voices two and three are at $15E9 and $16D1.

The speech NMI uses the low byte of the RAM NMI vector to switch between wave phases. The path at $A583 walks the wave buffer forward and $A5A4 walks it backward. $A5C3 writes the hold amplitude and $A5D9 acknowledges the following timer interrupts until the hold count runs out. $A5F2 loads the next phase and its counters. The timer-stop path at $A5E1 writes $90 to $DD0F and seven to $D418.

Record 462 ends with a 160-byte duplicate of sprite data from record 267. The bytes at $AA7D–$AB1C match $C500–$C59F of the resident graphics at the same offsets within their respective tape records. The match covers two full 64-byte sprite slots and the first 32 bytes of the next slot.
