# Impossible Mission II orientation

The analysed image is the PAL cassette `Impossible_Mission_II.tap`, extracted as `work/im2.tap` from the C64Games tape archive. Its header is `C64-TAPE-RAW`, version 1. It has 1,331,581 pulses and SHA-256 `3fcf532f08f01d4c9df52f331a0c5274bbd5e73949ac2fd5f01047d74983959e`. [C64Games release page](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=333).

## Boot and snapshots

Start the installed VICE-MCP v3.14.0 macOS arm64 headless executable through `tools.py --platform c64 vice`. Its local wrapper enables dummy audio. The assigned ports are 23024 for VICE, 23025 for its monitor and 23026 for Regenerator. The emulator check passed 56 tests. Host-key injection failed and the last quirk probe raised `KeyError('checkpoints')`. Direct matrix keys, watchpoints, exact stops and snapshots passed. Regenerator 0.9.18 answered through the kit's stdio bridge.

1. Hard-reset, then autostart the TAP. KERNAL loads `POSSIBLE` at $0801. When the loader is polling at $02EB or $02ED, ensure Play is pressed through the datasette monitor command `tapectrl 1`. Use warp while the tape runs. The KERNAL loader can switch warp off at its run hand-over, so set it again for the turbo loads.
2. The first turbo reader at $0370 transfers G-LOADER. The second loader runs at $AC00–$BFFF and reveals the title in bitmap mode. A stopping checkpoint at $ACA2 captures the first title input poll. This is `parts/title/work/entry.vsf`. The corresponding screenshot is in [reference/title.png](reference/title.png).
3. The title path advances on input or the flag at $1000. Allow loading to proceed. Stop at $0880, the destination of the jump at $ACFD. The banking setup in effect is $01 = $35. Save without ROMs as `parts/resident/work/entry.vsf`.
4. Resume and allow the next three tape requests to complete. An opening elevator with a live countdown appears. Disable warp, pause and save `parts/resident/work/play-elevator.vsf`. The hardware IRQ at $FFFE reads $2F86 and NMI at $FFFA reads $2ED8. The KERNAL RAM IRQ vector at $0314 still reads $EA31. $01 reads $25 after the loader, with the processor direction register at $2F. The $2F86 entry saves registers and follows a changing absolute jump. Store watchpoints on $D018 caught $2F08 writing $C6 and $2F32 writing $C4 on alternating raster passes.

The first turbo load has two byte-width classes. The loading program's interrupt measures the interval on CIA1 timer A and shifts in one bit at a time. It reads the 16-character PETSCII name and a two-word header. The numbered loader at $BE72 uses the difference between the two header words as the payload length and places bytes at the caller's requested destination. The title's resource table is $AC03, and the engine's is $2332. Both select tape records by three decimal digits.

## Replacement loads

The ending and scoreboard snapshots below were produced by directing VICE to the game's loading paths. They establish the loads and show their display routines. They do not establish the player's prerequisites for triggering the paths.

| Part | Route from the opening elevator | Listing snapshot |
|---|---|---|
| Final sequence | Restore the elevator snapshot, reattach the TAP and seek to byte offset 1190466 with Play pressed. With the CPU paused, set PC to $0C25 and arm a stop on $7800. The game reads records 402 and 409 before entering the overlay. Continue to $0C6A to capture the image after record 428 replaced 409, and to $35EA for the completed display. | `parts/ending/work/entry.vsf`. The later snapshots are `ending-drawn.vsf` and `ending-wait.vsf`. |
| Scoreboard | Restore the elevator snapshot, reattach the TAP and seek to byte offset 1280862 with Play pressed. Set PC to $2C65 and stop at $A520. Save the snapshot. The score code later calls back into the resident loader for records 264 and 358. | `parts/scores/work/entry.vsf`. The subsequent name-entry state is `scores-name-entry.vsf`. |

The snapshot restores RAM and registers. Reattach the tape before seeking from a restored state. A seek on a disconnected tape crashed this VICE build. The exact runnable probes and extracted records are in the ignored top-level `work/` directory.

## Tape inventory and memory matches

The kit's generic tape reader recognized the KERNAL block and split stretches of the turbo stream into tentative page blocks. The 33 numbered and named records in `media.json` come from decoding the bit order and sync sequence used by this loader. The local decoder and its mapping report are `work/raw-tape.py` and `work/tape-blocks.txt`.

| Record | Destination | Comparison |
|---|---|---|
| G-LOADER | $9FC0 on tape, relocated to $AC00 | 5,115 of 5,120 bytes match in the title snapshot. |
| 376 | $1000 initially, expands into $4000 | The 6,240-byte stream expands to 10,002 bytes. Its first 8,000 match the title bitmap at $E000. |
| 448 | $7000 | All 3,360 bytes match in the title snapshot. This is the second segment of the packed music stream. |
| 462 | $A57D | 1,439 of 1,440 match in the title snapshot. This is the speech driver. |
| 468 | $8000 | All 5,280 match in the title snapshot. The speech pointer table starts here. |
| 267 | $C000 | 9,218 of 9,360 match in the engine hand-over. |
| 306 | $E800 | All 2,160 match in the engine hand-over. |
| 490 | $0880 | All 39,840 match in the engine hand-over. |
| 130 | $A520 | 3,808 of 3,840 match in the opening elevator snapshot. |
| 402 and 409 | $7800 and $A800 | All 1,680 and 4,560 match at the final sequence hand-over. |
| 428 | $A800 | All 4,800 match after the subsequent overlay call. |
| 664 | $A520 | All 4,560 match at the scoreboard hand-over. |
| 264 and 358 | $F000 and $C000 | In the scoreboard name-entry state, 740 of 1,024 screen bytes and all 512 glyph bytes match. |
