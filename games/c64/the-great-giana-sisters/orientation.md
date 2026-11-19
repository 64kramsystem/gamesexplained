# The Great Giana Sisters on the Commodore 64

The analysis uses Zibri's [D64 with reset scores](https://github.com/Zibri/The-Great-Giana-Sisters-C64-D64/tree/f99e2b9477badce359ad068d7b3f5f981082a73c), kept as `work/giana.d64`. Its SHA-256 is `5383164abc583db3b6f56822b22792f51cd7cd8c4a80ad90df317733f8984adb`. The image has 174,848 bytes, the size of a 35-track D64 without an error-code trailer. The sector directory is `GIANA-GAME`, ID `GG`, with no allocated sectors outside its files and directory.

## Reproduce the snapshots

1. Start the installed VICE-MCP v3.14.0 macOS ARM64 headless build with dummy audio using the kit launcher. The assigned VICE MCP and monitor ports are 23052 and 23053. regenerator2000 0.9.18 answers on port 23054.
2. Hard-reset, allow about two seconds for BASIC startup and autostart filename `2` from the image. Its BASIC wrapper starts the depacker at $0810. A stopping checkpoint at $0823 catches its patched hand-over into the loading presentation, saved as `work/loader-entry.vsf`.
3. Continue to the Time Warp Productions logo. Hold SPACE through the logo wait, whose loop at $0AB2 polls bit four of $DC01. The observed boot used matrix key holds of about 300 ms for SPACE and then 1. The loader calls KERNAL LOAD for `1` on device 8, secondary address 1. An execute checkpoint at $0832 catches entry into the loaded engine. Save this as `work/entry.vsf` with ROMs omitted. The hand-over is also kept locally as `work/engine-entry.vsf`. The 63,441 payload bytes of `1` match main RAM at $0820–$FFF0 byte for byte, including pre-existing buffer contents in the file.
4. Continue to the scrolling menu with the `PRESS 1` and `2` banner and save `work/menu.vsf`. On the stopped machine hold the matrix key `1` for 12 frames, release it and advance 75 frames for `work/play-stage1.vsf` at the stage banner. Advance 100 further frames for `work/play-stage1-live.vsf`, with Giana at the Stage 01 start. The tempo for these frame counts is PAL.
5. Open regenerator2000 on `work/entry.vsf`. Use this hand-over when building the listing. The menu and gameplay substitute score records, alter character and sprite data, and overwrite the screen and game workspace.

The emulator check passed 56 with two failures. Host-named keys failed and the server-quirk phase raised `KeyError('checkpoints')` after reset. Direct keyboard matrix input, checkpoint stops, instruction stepping and load/store watches passed. Restarting recovered the emulator after a later crash during the frame-capture script. The four IRQ entry breakpoints and instruction steps supplied the raster-chain evidence instead.

## Disk files and load boundaries

| File | Payload | Role |
|---|---:|---|
| `LADER` | 98 bytes at $02A2 | Alternate first-file bootstrap. The `2` autostart route bypasses it. |
| `F` | 992 bytes at $CC00 | Fast-load helper. Its first routine installs a handler in the KERNAL LOAD vector at $0330/$0331. |
| `2` | 20,086 bytes at $0801 | BASIC wrapper, packed loading presentation and boot path. It displays the Time Warp logo before the main engine arrives. |
| `1` | 63,441 bytes at $0820 | Main program image. Disk entry code at $0823 jumps to $0832. |
| `ATG` | 120 bytes at $36F7 | Persistent all-time scores. A breakpoint at $FFD5 confirmed the filename and load parameters from the call at $084C. |

Stage 1 and the attract state use the same engine and build different maps through $9936. The stage, bonus and score code traced in the engine uses resident routines and tables. The observed file overlap is the load of the main program over the boot presentation. No separate gameplay part has been established.

## Banking and interrupts

At the loading screen the processor-port readback was $37 and the KERNAL IRQ RAM vector pointed to $0846. In Stage 1 the processor port read back $35 with DDR $2F. The active RAM NMI vector is $084F. IRQ breakpoints reached $1249, $12A3, $1326 and $1393 at raster lines 65, 89, 118 and 252 respectively. The handlers write $FFFE/$FFFF and $D012 to advance the chain. CIA2 port A read back $C0 and $D018 read back $21, selecting video bank $C000, character set $C000 and screen $C800.
