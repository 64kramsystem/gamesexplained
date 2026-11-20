# Shinobi (C64) orientation

The input is X-Large's disk release [Shinobi](https://csdb.dk/release/?id=146950). The 174,848-byte image is a plain 35-track D64, as confirmed by the directory and sector reader. Its SHA-256 is `b1ec16035ac6fd04550286c3a4ae82f1ff8d9e7feb8a97419a7f5c880f172ebb`.

## Boot

1. Power-cycle the PAL machine and autostart `SHINOBI/XL` from drive 8. At the scrolling X-Large intro, hold Space briefly to leave it.
2. The loader displays a masked face. Press port 2 fire at that screen. Allow the drive to finish reading. Warp speeds up the serial transfer. The loading routine then waits 255 raster frames at `$3F8B`.
3. The game shows an attract sequence with a fire prompt. Press port 2 fire, release it, then wait through the opening message. `work/gameplay.vsf` shows the ninja standing at the left with the timer running. `work/round1-check.vsf` holds the fire prompt.
4. For the first mission overlay, stop at `$3F22` before the loader closes the input channel. `work/mission1-entry.vsf` is the snapshot at this instruction.

## Interrupts and tools

During Mission 1 play, the processor port is `$35` and the hardware IRQ vector at `$FFFE` points to `$1E87`. An execution checkpoint hit it once at PC `$1E87` and a single instruction step reached `$1E88`. The RAM vector at `$0314` retains `$EA31`. The hardware NMI vector reads `$284F`.

VICE MCP v3.14.0 headless for macOS arm64, with dummy audio, answered on port 23092. The kit probe passed 56 checks, including exact instruction stops, stepping and load and store watchpoints. Host-name F1 failed. The final quirks probe ended on a checkpoint-list response without the expected key. Matrix input worked. Regenerator2000 answered on port 23094 on the mission 1 entry snapshot.

## Disk files and memory

| File | Evidence |
|---|---|
| `SHINOBI/XL` | First PRG. The BASIC stub invokes SYS 2268 and the release boots into the X-Large intro. |
| `SHINOBI` | 47,100 of 47,103 payload bytes match RAM from `$0801` in the loader snapshot `work/later.vsf`. The differences are at `$081B`, `$3F2B` and `$3F3F`. The last two are written by the mission loader. |
| `MISSION1` through `MISSION5` | Each carries a 17,664-byte payload. The loader constructs a name from the mission number and reads a sequential stream into two separate regions. |
| Directory decoration | Entries after the five mission files point to 1,014-byte payloads with a nominal address of `$0041`. |

The resident loader at `$3E97` adds ASCII zero to the mission index at `$FCC0` and writes the result to `$3E45`, the digit in `MISSION1,P,R`. The read loop calls KERNAL CHRIN at `$3F58` and stores at `$3F60` with RAM enabled under ROM and I/O. A nonstopping watch at the store recorded 768 hits over about two seconds and the destination advanced from `$EC0A` to `$EF13` across the enclosing observation. The entry snapshot matches the first `$0500` payload bytes at `$6400-$68FF` and the following `$3EF0` at `$C000-$FEEF`.

## Mission overlays

All five files matched in full at the two destinations at `$3F22`, for 17,392 bytes per mission. The destination operand, payload comparison and the loader's two explicit lengths delimit what belongs to each overlay. The remaining 272 payload bytes per file are outside this read loop.

To reproduce the later captures, restore the paused first-mission gameplay snapshot, attach the same image to drive 8 and set `$FCC0` to one less than the intended mission number. Set PC to `$B008`. The game clears its transition state and increments `$FCC0` at `$B00F` before calling `$3E97`. Arm an execution breakpoint at `$3F22`, run in warp and save the entry snapshot on the stop. To reach a later mission in play, restore that mission entry. Hold port 2 fire while running to a stop at the transition return instruction `$B074`. Release fire, set SP to `$FF` and PC to the engine player initializer `$19B5`. Advance 380 PAL frames. This uses a fresh player state on the loaded mission, with no carryover from the preceding mission.

A fresh boot stopped on its first execution of `$1904`. The snapshot in `parts/engine/work/entry.vsf` holds all 47,103 bytes of the resident PRG unchanged. Use this image for the engine listing because gameplay overwrites the setup routines at `$4C00` and `$4C2F` with screen data.

Later overlays use `parts/missionN/work/entry.vsf` for their listings. The companion `play.vsf` files hold playable first-stage states. Missions 2–5 use the controlled entry above. The captures show each mission with the player active and the timer running.
