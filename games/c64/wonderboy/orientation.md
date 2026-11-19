# Wonder Boy orientation

This is the 1987 Activision conversion of Sega's first Wonder Boy arcade game. The input is Remember's April 2005 disk release, `Wonder_Boy_(REM).d64`, from the [C64Games.de disk download](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=200). Its shipped documentation lists changes to pause, quit, display and several game behaviors. Interpret addresses and behavior as specific to this build.

## Boot on PAL C64

1. Power-cycle and autostart the D64's sole file, `WONDER B.+10/REM`. The image is a 174,848-byte, 35-track sector image. The PRG starts with little-endian load address `01 08`. Wait for the Remember intro.
2. Hold joystick port 2 fire to enter the documents. Press the C64 matrix Run/Stop key (row 7, column 7) to leave. The illustrated loading screen follows.
3. Hold port 2 fire again. Let the depacker finish. The trainer menu shows N for all cheat switches and 1/1 for the stage. Press Space with these defaults. A checkpoint at `$082A` stops at the first instruction of game initialization. Save `work/entry.vsf` here.
4. Resume to the text title with the F1/F3 prompt. Hold F1 (matrix key) for 12 frames. Release and advance 180 frames to the round banner, then another 95 frames to the active opening of Area 1, Round 1. Save `work/play-live.vsf`. Use this snapshot for listing and `work/entry.vsf` for the comparison. Both omit ROMs.

The loader runs an intro and a document reader before the illustrated screen and decrunch. At the trainer exit, a store watch on `$FFFE–$FFFF` stopped startup at `$08E6` with `$FFFE = $E5`. The earlier execute checkpoint at `$082A` captures intact initializer code before that store. Entry and play agree across `$2000–$2FFF`, `$5000–$5FFF` and `$8000–$DFFF` apart from the row cursors and related working bytes on the `$BCxx` page. The loader's packed image is inventoried in [media.json](media.json). The file count, four in-memory terrain pointers, and in-memory round setup support one game image for the rounds covered by that setup.

## Machine state

- VICE headless release v3.14.0 on macOS arm64 with the dummy sound device. The kit check passed 55 of 57 tests. Host-key delivery and 1,600 unpaced calls failed. Matrix input, stopping checkpoints, store watchpoints and instruction stepping passed. The kit's all-frame capture lost the server and the initial snapshot still loaded after restarting it.
- Game CPU port is `$35` with DDR `$2F`. It maps the RAM vectors at `$FFFA` and `$FFFE` and leaves I/O visible for gameplay. The ROM-dispatched vector at `$0314` held `$EA31`.
- Live execute checkpoints hit raster handlers `$0D4B` and `$0DE5`, with those addresses respectively in `$FFFE/$FFFF`. The former can route through `$1101` during the banner. The VIC bank from `$DD00` is `$4000`. `$D018 = $0C/$0E` selects the common screen at `$4000` and character sets at `$7000/$7800`.
- Regenerator2000 0.9.18 opened the snapshot on the assigned port. It was seeded with the title-to-play execution map, initialization at `$082A`, and handlers from the two object dispatch tables.
