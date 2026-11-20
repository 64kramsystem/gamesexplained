# Orientation

## Disk and machine

The analysis uses the [Overdrive disk release](https://csdb.dk/release/?id=241287). The image in the local work directory is a 174,848-byte, 35-track D64 with 683 readable sectors and no unowned allocated sectors. Its SHA-256 is `9dfa7ef008715922d4b2c21440969754dddbff88d661af5c97704850202269a7`. The boot program is `CHAMP.OF SHAOLIN` at $0801, with BASIC SYS 2082. Autostarting it produced the Overdrive introduction.

VICE MCP v3.14.0 ran headless on macOS arm64 with dummy audio, PAL C64SC, an MCP listener on 23068 and a monitor on 23069. Regenerator2000 answered on 23070. The emulator check passed 56 tests. The two failures were `keys-host`, which did not deliver F1 by host key name, and `no-exception`, which raised `KeyError('checkpoints')` in the quirk probe. Matrix key input and stopping execution checkpoints worked in the game.

## Reproduce the hand-overs

1. Extract the six packed PRGs listed below with `python3 kit/c64/disk.py extract`. Each begins at $0801 with BASIC SYS 2063. A direct disk autostart of `LABLE` remained on BASIC's `LOADING` screen during the capture attempt, so the snapshots use debugger-assisted loading.
2. Hard-reset VICE and let BASIC initialize. Use the kit's `vice.inject` to load the **packed** PRG, then set $AE/$AF to the first address after its payload, the end pointer normally supplied by LOAD. With the CPU paused, set PC to $080F and set an execution checkpoint at $0150.
3. Run to $0150, remove the checkpoint and step the JMP once. Save the resulting machine as `work/entry.vsf` in the part's folder. The listing uses this snapshot because later initialization reuses some authored addresses as output and state.
4. For `LABLE`, run to the Thalion logo, then press and release port-2 fire to cycle through the title pictures to the apprentice form. Use the matrix keys: press 1, release it, enter a name and press Return. A breakpoint at $C33C caught the 1 key with A=$38. At $FFD5, the stack identified the game call at $C9DA, requesting filename `1` from device 8, secondary 1.
5. For the Balance entry used by the listing, load the local `before-load1.vsf` taken at that call. Mount the original disk in unit 8, set the breakpoint at $0150 and run the disk load in warp. Step the JMP when the breakpoint hits. The result preserves the name and resident bytes from `LABLE` and matches the debugger-assisted capture throughout the depacker output. At each of the first two $097F input gates, release fire long enough for the code to clear its latch, then press fire. Each press reaches $0995. After the second press the main loop reaches $08C4. Advance 20 frames and save the playable state as `parts/load-1/work/play.vsf`. The machine reads processor port $35, the KERNAL IRQ vector remains $EA31, and the active hardware vector points to $198A.

The later listings use native disk loads. Starting from the Balance gameplay snapshot, enter the game's transition routines at $C900 (Balance), $08B1 (Speed), $C900 (Strength) and $C300 (Combat). At each step, break at $FFD5 to identify the requested file, then resume in warp to $0150 and step once. This route runs the game's own load and depack code for `2`, `3`, `4` and `HIGH`. It skips the result logic by entering the transition directly. The per-part load ranges match the independent captures byte for byte. The local Speed, Strength and Combat `play.vsf` files were captured independently after setting the apprentice count to 1 and the name to A. The corresponding input checkpoints were $0A3E/$0A54, $097F/$0995, and $EC4C/$EC62. Release and press port-2 fire at the input gates. The game installs IRQs at $1C09, $143F and $1D35 respectively. The independent capture has no prior training results. The score capture mounts a writable copy of the disk, runs from $C200 through the KERNAL LOAD of H, and stops when the completed score panel reaches its fire poll at $C231.

## Disk files and output ranges

The packed file byte counts exclude its two-byte PRG address. Instruction tracing with the kit CPU identified the stores through ($FA),Y that write the depacker output. Two simulated runs per file started with RAM filled with $00 and $55. Every output byte matched both runs and the VICE hand-over. The initial staging copy uses ($FE),Y and leaves packed bytes below $0800.

| File | Packed bytes | Part | Entry | Depacker output |
| --- | ---: | --- | --- | --- |
| CHAMP.OF SHAOLIN | 8,030 | Overdrive loader | $0822 | Open before the publisher image |
| LABLE | 23,330 | title | $C200 | $0800–$CFFF, $E000–$FFFF |
| 1 | 31,260 | load-1 | $0810 | $0800–$C9FE, $E000–$EFFF |
| 2 | 31,776 | load-2 | $0810 | $0800–$CDFE, $D000–$FFFF |
| 3 | 21,965 | load-3 | $0810 | $0800–$C9FE, $E000–$E2FF |
| 4 | 43,136 | load-4 | $0810 | $0800–$CDFE, $D000–$FFFF |
| HIGH | 6,920 | scores | $C200 | $0800–$CDFE, $E000–$EFFF |
| H | 60 | score save | — | $C868–$C8A3 |

The packed first pass relocates the stream to $0334 for backwards decoding. Each $CC escape introduces a literal $CC, an end marker, a new output pointer or a repeated byte. The depacker restores the KERNAL and I/O mapping before its final JMP. `LABLE` installs a RAM LOAD vector into its block at $CA00. The Balance overlay preserves it and calls it again on exit. `HIGH` supplies a byte-for-byte copy of the same block at $CA00–$CDFE. Speed reconstructs the shared loader before the load of Strength. The resident result-border templates at $CF00–$CF9F survive all five later loads verbatim. Their data belongs to the title listing, which supplies the shared memory below those parts.

## Local handoff files

`work/capture.py` contains the direct-load capture procedure. `work/title-trace.py` and the Balance trace scripts show the execution checkpoints. `work/depack.cjs` produces the two-fill write trace, and the fitted annotation projects, census, strings and ledger transcripts are in each part's `work/` directory. These files and the image are local.
