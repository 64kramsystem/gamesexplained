# Rygar on the Commodore 64

## Image

The [Softrambo and Wanderer Group release](https://csdb.dk/release/?id=249447) is a 174,848-byte D64. The first track contains sector data and has no GCR container signature. The directory has one 164-block PRG, `RYGAR`, with a `$0801` load address and a 41,570-byte payload. No allocated sector falls outside the file. The [retail preservation image](https://preservation64.de/index.php?title=File:Csd_Rygar_Tecmo_s0.g64) returned HTTP 401, so changes from the retail build are unverified.

## Rebuild the snapshots

1. Use PAL on the installed macOS ARM64 headless vice-mcp v3.14.0 with dummy audio. Hard-reset, arm a stopping execute checkpoint at `$0820`, and autostart `work/rygar.d64`. The BASIC line runs `SYS 2080`. Let the load finish in warp. The emulator check reported 56 passes and two failures, `keys-host` and `no-exception` in the remote-monitor quirks phase. Matrix input, exact execute stops, watchpoints and frame advance passed.
2. Resume to the Softrambo intro. A stop at `$C350` catches the first decompressor's exit. On the intro, hold the Space key using the keyboard matrix for 60 frames. Release it, then allow 180 frames to reach the Wanderer Group intro.
3. Hold Space again at the Wanderer Group intro. Release it after 74 frames. With the final unpacker running, arm `$0915` before resuming. The preceding checkpoints at `$00AF` and `$0812` distinguish the jump through `$0334` from the last depacker. The `JMP $0915` at `$03A2` hands control to the engine. Save the stop at `$0915` as `work/entry.vsf`, without ROMs.
4. With warp off, advance 65 frames for the title. Press fire in port 2 for five frames and release it. The text prologue types itself onto the playfield. Once it has finished, press fire in port 2 for 30 frames and release it. After 12 further frames the first landscape and player sprite are visible. Save it as `work/play-round1.vsf`, without ROMs.

## Steady state

The CPU port reads `$35` in play. The hardware IRQ vector at `$FFFE` reads `$0E84` at the saved frame boundary, and the NMI and RESET vectors both read `$0F9C`. The KERNAL's RAM IRQ vector at `$0314` still reads `$EA31`. The low two bits of CIA2 port A are 2, selecting the VIC bank at `$4000`.

## Loading

The PRG contains repacked introductions and the game. The initial BASIC stub starts a depacker from the stack page. The Softrambo and Wanderer screens precede later unpacking stages. The final depacker at `$0812` relocates its own executable to the stack page and page 3, unpacks backwards, and leaves via `$03A2`. The handover capture contains the expanded game, so there is no direct placement of the packed PRG at that point. The selected disk has no separate stage files. The round initializer at `$11D5` indexes the sixteen resident terrain maps.

The alternate [Triton release](https://csdb.dk/release/?id=154177) supplied a comparison handover at `$0915`. Both trainer options were off. It is a comparison image only. The selected D64 is the source of the media ledger and listing.

Rebuild the listing from the repository root with the handover as the byte source and the play snapshot as the comparison.

```sh
python3 kit/scripts/listing.py games/c64/rygar games/c64/rygar/work/entry.vsf --entry games/c64/rygar/work/play-round1.vsf
python3 kit/scripts/coverage.py games/c64/rygar
```
