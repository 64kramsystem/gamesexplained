# The Trap Door (C64) orientation

## Image

The [Cleveland Cracking Service disk](https://csdb.dk/release/?id=199140) is a 174,848-byte, 35-track D64 with one PRG, `THE TRAP DOOR`, and zero allocated orphan sectors. The PRG header is `01 08`. All 45,471 payload bytes match RAM starting at $0801 at the BASIC SYS stop. The intro credits Ian and gives the date 20 November 1986.

## Reproduce the snapshots

1. Start the kit's headless VICE build with dummy audio. Power cycle and autostart the first file of `work/cleveland.d64`, in PAL. Set an execute checkpoint on $080E, the target of BASIC's SYS 2062, and save `work/sys.vsf` there.
2. Arm $3800 and resume. The intro plays automatically and needs no input. Warp can shorten the wait. Save `work/entry.vsf` when the checkpoint fires, with neither disks nor ROMs included. The effective CPU port is $37 at hand-off.
3. Delete the checkpoints, disable warp and advance about 130 frames to the controls screen. Hold S on the C64 keyboard matrix for 30 frames. At the next screen hold L on the matrix for 12 frames and advance another 85 with the key released.
4. The game is in the trapdoor room with Berk, Boni and Drutt. Save `work/play.vsf` without ROMs or disks. The accompanying captures are [the controls](reference/controls.png), [mode selection](reference/modes.png) and [early play](reference/learner.png).

The startup code writes $3937 to the RAM hardware IRQ vector at $FFFE/$FFFF. In play the effective CPU port was $30 at the sampled instruction, so the CPU saw RAM there. The KERNAL RAM vector at $0314/$0315 still read $EA31. The direct IRQ banks I/O in to read CIA1 interrupt status and uses a software service pointer at $FFF8. During play its value was $3936, an RTS. During the controls menu the pointer reaches the music routine at $186E.

## Loader and image selection

The SYS stub at $080E enters the crack intro at $B800. After four colour cycles it jumps back to $0818, which banks out ROMs and enters $B439. That stub copies the depacker to the stack page and the escape-byte fixups to $0334. The depacker walks backward from $B438, expanding literals and $D9 runs into $0820–$CFFF. It fixes 14 literal escape bytes and jumps from $01A6 to $3800. An independent expansion matched all 51,168 bytes at hand-off. The loaded PRG accounts for the single media item. Title and early play both run within its expanded image.

The hand-off snapshot is the listing input. It preserves the menu prelude and the contents overwritten by display and work buffers. Use the play snapshot for comparison when rebuilding:

```sh
python3 kit/scripts/listing.py games/c64/the-trapdoor games/c64/the-trapdoor/work/entry.vsf --entry games/c64/the-trapdoor/work/play.vsf
```

## Tool checks

VICE MCP v3.14.0 passed 56 checks, including instruction stepping, stopping store watchpoints and exact frame advance. Host-key input failed. Keyboard matrix input passed and reaches the game. The server-quirks phase ended with a missing `checkpoints` key after its paused-reset probe. Starting with a fresh server allowed orientation, stepping and watchpoints to proceed. Regenerator2000 0.9.18 answered on the hand-off snapshot.
