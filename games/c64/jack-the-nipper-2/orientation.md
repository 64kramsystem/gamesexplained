# Orientation

The [Beastie Boys release](https://csdb.dk/release/?id=19968) runs in headless VICE-MCP v3.14.0 with dummy sound. The kit's emulator check passed 56 tests. Host-key injection failed, while keyboard matrix input passed. The remaining failure was a checkpoint-list response missing its `checkpoints` key in the last quirks phase. The session used MCP port 18516 and disassembler port 18518.

The input, `work/jack.d64`, is a 174,848-byte sector image with no GCR signature or error suffix. Its 167-block PRG, `JACK THE NIPPER`, has a two-byte load header for $0801 followed by 42,257 payload bytes. The disk directory has no other files and the BAM has no allocated stray sectors.

1. Hard-reset a PAL C64 and autostart the disk. Wait for the Beastie Boys intro with the striped scroller. The native load took tens of seconds in this setup.
2. Hold SPACE through the keyboard matrix for about one second and release it. The next screen initially shows the Beastie Boys credit while the remaining unpacker runs. Wait for the game's yellow title frame and score panel. Save this state as `work/game-title.vsf`.
3. Hold port 2 fire for ten frames, release it and advance sixty frames. Jack appears beside the vertical yellow climbable surface. Save `work/play-round1.vsf`.
4. To rebuild `work/entry.vsf`, arm a stopping execution checkpoint at $801A during the black Beastie Boys credit screen, before the depacker finishes. If the checkpoint is armed earlier, filter out the intro and packed bytes. The last depacker transfers at $012E to $801A. Save its stop before advancing. Use this snapshot for regenerator2000 and the listing.

The BASIC wrapper enters at $0812. Two backwards unpacking stages precede the crack intro at $1900. On leaving the intro, a final stage copies its decoder to $011C and moves the packed stream high in RAM. The decoder starts writing at $0F00 and advances its output pointer through $FFFF. At handover the raw PRG no longer matches at $0801. The bytes at $0800–$0EFF are identical immediately before and after final unpacking and lie below its output base.

The game enters with CPU port $37. The IRQ setup at $8113 changes the output latch to $05, with DDR $2F. During play the effective port reads $15, exposing RAM in the BASIC and KERNAL ranges and leaving I/O visible. The hardware IRQ vector at $FFFE points to $80A0, which pushes A, X and Y and jumps through $0314. In the captured play snapshot $0314 points to $8302. The four handlers at $814C, $823A, $8259 and $8302 write the next handler and raster line into $0314 and $D012.

The title and first playable area share the same loaded image. The media ledger assigns the one packed PRG to that image.
