# Orientation

The input is the DCS disk release, a standard 174,848-byte, 35-track D64.
The directory is titled `NINJA SPIRIT/DCS`, disk ID `10`. SHA-256
`5db796b510abc90b9aaf905ba86207c717f7c7c5a88d0aa5d1be7002d514f3c7`.
[Release record](https://csdb.dk/release/?id=191343).

## Boot

Autostart the image on drive 8. At the DCS intro, hold Space using the
C64 key matrix. At the tape-counter prompt, press Space again. The disk
loader runs while the display is black with coloured lines. Warp can
shorten the wait. At the title screen, turn off warp and press fire on
joystick port 2. Advance about one second to see the player in Round 1.
The listing snapshot is `work/play-round1.vsf`, without ROMs or disk data.

The PAL emulator is vice-mcp v3.14.0, macOS arm64 headless, with dummy
audio. Its check passed 56 tests including exact instruction stepping
and store and load watches. Host key names failed. A checkpoint-list
reply without a `checkpoints` field interrupted the final quirks probe.
The boot uses matrix keys and does not depend on that probe.

The gameplay hardware IRQ vector at `$FFFE` points to `$2405`.
The KERNAL RAM vector at `$0314` retains `$EA31`. At `$2405` the
handler saves A, X and Y in `$02-$04` and jumps through `$0012`.

## Parts and disk files

| Disk file | Role |
|---|---|
| `NINJA SPIRIT/DCS` | Boot PRG. Its intro precedes the tape-counter prompt. |
| `ANOTHER NOTE/DCS` | Standalone DCS release note, confirmed by starting directory entry 2. |
| `A.NINJA SPIRIT..` | Load A, reached through `$BA00`. Round 1 and its successor share this load. |
| `B.NINJA SPIRIT..` | Load B, reached through `$BA03`. |
| `C.NINJA SPIRIT..` | Load C, reached through `$BA06`. |
| `D.NINJA SPIRIT..` | Load D, reached through `$BA09`. |

The part folders contain `work/entry.vsf` at `$2780` and
`work/play.vsf` during play. The engine uses the load A snapshots.
To capture A's entry, set an execute checkpoint at `$2780` before
answering the tape-counter prompt. The title follows initialization.
To capture B, C or D, stop during play, leave the D64 in drive 8 and
set PC to the corresponding loader entry above. Resume to the
`$2780` checkpoint, save the entry and advance about 80 frames.
This enters the game's loader directly and bypasses the previous
round's completion sequence.

The trace in local `work/trace-load.log` stops at the header read
(`$BC73`) and decoder exit (`$BC38`) for each packet. The decoder's
destination starts at `$A000` and ends at `$2780` for the first packet,
then starts at `$F800` and ends at `$DB40` for the second. It writes
backward. Every stage load replaces `$2780–$9FFF` and `$DB40–$F7FF`.
The part folders own those two ranges. The remaining address space
belongs to the shared engine, subject to its coverage exclusions.

A frame capture with the kit's multi-checkpoint capture command lost
the emulator while cleaning up the checkpoints. A restart on the
same port restored access. The single-address store trace in
`work/irq-watch.log` captured the individual handler pointer writes.

If autostart leaves the disk program loaded at a BASIC READY prompt,
type `RUN` through the KERNAL keyboard buffer before using the matrix
Space presses. The tool ports for this worktree are VICE 17476, VICE
monitor 17477 and Regenerator2000 17478. The kit convention places
symbol maps and listings in the five part folders for a multipart game.
