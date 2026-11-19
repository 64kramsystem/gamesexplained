# Blood Money orientation

## Disk images

The boot disk is the [Accept release](https://csdb.dk/release/?id=149504), stored locally as `work/blood-money.d64`. It is a 174,848-byte sector image with 683 sectors and no error trailer or GCR header. Its SHA-256 is `72af9983e06ed274ced9f0b80001f576e2bb45675833ab16f2b19acb359221ba`.

For level 4, attach the [Syntax Designs release](https://csdb.dk/release/?id=200335) in drive 8. Its local name is `work/syntax.d64` and its SHA-256 is `eddd95402860a35d87ad445e49e4d2d626c22e6709717db29f0b30bf6261a3df`. All 14 level payload files present on both disks are byte-identical. Syntax adds the `CHARS4` and `DATA4` files that the Accept disk lacks.

## From power-on to level 1

1. Start the prepared VICE v3.14.0 macOS arm64 headless build, with PAL timing and dummy audio. The assigned VICE MCP and monitor ports are 23040 and 23041. The regenerator2000 bridge uses 23042.
2. Hard reset, autostart the first directory entry of the Accept disk and wait for the ACCEPT intro. Hold SPACE through the keyboard matrix for about one second. Wait for the animated Blood Money title and options. A load can spend tens of seconds on a grey screen or a black frame.
3. To capture the engine handover, arm an execution breakpoint at `$1CD6` after the ACCEPT intro appears and before holding SPACE. Save `parts/engine/work/entry.vsf` on that stop. Resume and save the title state as `parts/engine/work/title.vsf`. Use the matrix key 1 to select one player. The game shows the level number while it loads from drive 8.
4. To capture the overlay before it is modified by gameplay, stop at the return instruction at `$C9B6` and save `parts/level-1/work/entry.vsf`. Resume through the startup and save the live level. `parts/level-1/work/play-level1.vsf` shows the helicopter, terrain and score panel. In play the processor port was `$35`. The RAM IRQ vector was `$2034` in that snapshot, and the frame trace places its panel split at raster line 202.

The emulator check reported 56 passes and two failures. The host-key F1 path did not deliver a key. The last test phase aborted at checkpoint-list parsing. Direct matrix input and stopping load and store checkpoints worked in the game. An instruction-step request disconnected VICE during a play snapshot probe. The run restarted the same headless build and used execution breakpoints and load and store watchpoints for targeted tracing.

## Levels 2 through 4

For levels 2 and 3, restore the options-screen snapshot in `work/menu.vsf`, attach the Accept disk, start one player, and stop at `$C8BC`. Set `$0442` to the requested level number before the filename digit is formed. Resume to `$C9B6` and save the part's `work/entry.vsf`. Save play separately.

For level 4, follow the same options-screen route as levels 2 and 3 with the Syntax disk and set `$0442` to 4. The listing uses `parts/level-4/work/menu-entry.vsf`, saved at the return checkpoint. The play snapshot is `parts/level-4/work/menu-play.vsf`. The `from-3-*` files preserve the separate probe that used the Accept disk and left the previous level's sprite payload in place.

## Loader and file correspondence

The Accept intro precedes the resident engine. 16-byte chunk matches link the file `A` to several resident ranges, including `$3210–$36FF` and `$D676–$DC75`. This establishes partial correspondence with the unpacked image. The engine's loader at `$C8B0` banks in the KERNAL and requests four files by name. Execution checkpoints at its four SETNAM calls each hit once for level 1, and a store watchpoint at `$C9BD` hit when the digit was installed.

| Filename family | Load range | Bytes matching at the loader return |
|---|---|---|
| `BLOCKS1` through `BLOCKS4` | `$EF70–$FFEF` | 4,224 per level |
| `CHARS1`, `CHARS2`, `CHARS4` | `$5000–$5BFE` | 3,071 per level |
| `CHARS3` | `$5000–$5BFF` | 3,072 |
| `LEVEL1` through `LEVEL4` | `$8000–$9D7F` | 7,552 per level |
| `DATA1` through `DATA4` | `$A000–$BFFF` | 8,192 per level |

The Accept disk's deleted directory entry and the Syntax release's two boot-time files are recorded in the media inventory.
