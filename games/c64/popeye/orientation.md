# Popeye — orientation

## Image and release

Use the disk compilation from [C64.COM's Popeye 86 entry](https://www.c64.com/games/no-frame.php?showid=582). The extracted file is `work/Popeye 86.d64` (SHA-256 `25a4c18a1255c130208524f1904d5f8788beb1607916beb2fd9eada18e29b4ad`). Select the PRG named `POPEYE 86`. The catalog attributes this release to Macmillan Ltd., 1986.

Autostart the companion `POPEYE PIC` file to see the [copyright title](reference/copyright.png). It shows ©1986 Macmillan Ltd. and ©1986 King Features Syndicate, Inc. The playable PRG presents a separate controls screen. The [controls screen](reference/title.png) has a repeated Popeye logotype and shows the redefine, start, movement, hold and port-2 controls. Starting the game leads to [Olive's house](reference/olives-house.png). From the starting position, walking down the stairs and moving left leads to the [lighthouse](reference/lighthouse.png) under player control. The two screenshots show different room layouts and the same inventory and heart panel.

## From power-on to play

1. Autostart the D64 using the program name `POPEYE 86`. Allow the disk load and drawing to finish until the control menu is visible.
2. For the hand-over snapshot, arm an execution stop at `$4000` immediately after requesting autostart. Save `work/entry.vsf` when the CPU stops there. Clear the checkpoint and resume.
3. Press S through the C64 keyboard matrix for about 400 ms and release it. Wait for the initial room to finish drawing.
4. Save a snapshot with no ROMs or disks while Popeye is in the initial room. The analysis snapshot is `work/play.vsf`.
5. To reach the lighthouse from this snapshot, hold A for about two seconds, release it, then hold Z for about five seconds.

The disk is a compilation. The named PRG starts the game without requiring a selection menu. Its packed disk representation and the resident image are considered separately in the media ledger.

VICE used the installed v3.14.0 headless build and dummy audio on port 17464. Regenerator2000 0.9.18 served the play snapshot on port 17466. The room-change trace and the resident placement stream support a single gameplay image for the observed rooms. The companion picture is a media item.
