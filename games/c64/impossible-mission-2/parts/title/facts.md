# Loading presentation

The listing snapshot is stopped at the first poll at $ACA2. The title bitmap in $E000–$FF3F matches the first 8,000 bytes produced by unpacking record 376. The original stream consists of single-byte controls followed by literal runs or repeated bytes. The low seven bits of a negative control give the repeat count, and a zero control ends the stream.

The sound player starts at $1001 and ticks at $1004 under the CIA1 timer IRQ at $AFE6. $AF79 joins 1,314 bytes from $B011 with 3,360 more from $7000. The packet stream expands to 5,846 bytes at $1000, of which 5,843 match the title input snapshot after the player begins. The other sound path uses CIA2 timer B and produces amplitude changes via $D418. The title script at $AA00 selects speech items two and three.

The speech driver uses writable wave buffers in page $08. A store watch over $0800–$087F stopped immediately after $A7F7 while running the title's voice call at $AC86. The first 128 bytes of that page are identical across the title and engine hand-over snapshots. They are speech workspace left by startup.
