# Orientation

## Image and tools

- Electric Boyz release of the C64 action game. [CSDb release record](https://csdb.dk/release/?id=83398)
- Local disk image `work/electric.d64` is a 174,848-byte, 683-sector D64. The sector reader found six PRGs and no allocated sectors outside the files. The first PRG is `INDIANA JONES`, with load address `$0801`.
- VICE MCP v3.14.0 macOS arm64 headless with dummy audio, PAL, MCP port 18520. The emulator check passed exact instruction stops and execution, load and store watchpoints. Host-key F1 failed and matrix F1 passed. The unpaced-call portion had no final result before the emulator was restarted.
- Regenerator2000 on port 18522. Use the assigned port for one part at a time.

## Title and caves

1. Power-cycle the PAL C64. Autostart the first program of `work/electric.d64` in drive 8. Allow roughly 45 seconds at normal speed for the disk and startup code. The title displays **PRESS FIRE TO START**.
2. Save `work/title.vsf`. Hold port 2 fire for 40 PAL frames, release it, then save `work/play-caves.vsf`. Indy starts on a ledge at the left side of the caves.
3. On a second cold boot, arm an execution stop at `$7D5C` before autostarting the same file. Save there as `work/entry.vsf`. The initial program has expanded into resident RAM. The first play snapshot shows the numbered cave assets in their slots. Use `parts/resident/work/play.vsf` for the resident listing, with `parts/resident/work/entry.vsf` as its hand-over probe.

Both title and play use the processor port `$01 = $35`, with DDR `$00 = $2F`. The default KERNAL IRQ vector at `$0314` reads `$EA31` and the KERNAL is banked out. The title's hardware IRQ vector is `$993B`. In play `$809C` and `$81CF` alternate in `$FFFE`, as shown by the stores at `$81B8/$81BB` and `$829F/$82A4`. The hardware NMI vector is `$809B`.

## Asset loads

The resident setup calls `$B80F`, which derives a zero-based asset selector from the main stage `$7D2D` and the train subsection `$7A5F`. It skips the disk when the selector equals the cache byte at `$B80D`. Otherwise it edits the digit of the filename at `$B87B` and passes the resulting name at `$B874` to SETNAM. The subroutine at `$24A7` reads serial bytes through KERNAL and expands the packed stream directly into RAM. The first PRG's file bytes are packed and do not match the expanded engine as one contiguous run.

| Disk component | Part | Observed destination of expanded assets |
|---|---|---|
| `INDIANA JONES` | Resident engine | Engine entry at `$7D5C`, music entry at `$1000`, shared fonts, sprites and tables |
| `INDIANA1  (EBES)` | Caves | `$2800–$2FFF`, `$3600–$75FF` |
| `INDIANA2  (EBES)` | Train | `$2800–$2FFF`, `$3600–$4FFF` |
| `INDIANA3  (EBES)` | Catacombs | `$2800–$2FFF`, `$3600–$7600` |
| `INDIANA4  (EBES)` | Airship | `$2800–$2FFF`, `$3000`, `$3600–$7600` |
| `INDIANA5  (EBES)` | Temple | `$2800–$2FFF`, `$3000`, `$3600–$7600` |

For each numbered load, restore `work/play-caves.vsf` with the Electric Boyz disk attached. Set `$7D2D/$7A5F` to `0/0`, `0/1`, `1/0`, `2/0`, or `3/0` respectively and force a disk read by setting `$B80D = $FF`. Set PC to the game's stage initializer at `$7DD6`. The local script `work/enter-stage.py` stops on `$B85E` to read the filename, on `$B861` after the disk call to save the part's `entry.vsf`, and on `$7E68` to save `play.vsf` after initialization. It also records the end-of-range store watchpoints between the disk call and return. The five screenshots in `reference/` were taken 50 PAL frames after the final stop.

The train leaves bytes above `$4FFF` from the preceding load intact. The catacombs map uses rows of 150 bytes. The other maps use rows of 256. All five character sets are at `$2800`; the map renderer uses the generated pointers at `$3400/$3500` rather than the filename or stage number to fetch each row.

## Release comparison

The separate Shaolin Monastery disk booted its intro. After leaving the intro it produced a blank screen in this setup. It is kept in ignored `work/` as a byte comparison. Its A and B files matched the corresponding Electric Boyz map and glyph ranges byte for byte, except that the shared part of the catacombs map matched through `$75DD`; the 32 bytes at `$75DE–$75FD` differed. VICE store watchpoints, rather than that release's file lengths, establish the Electric Boyz write boundaries above.
