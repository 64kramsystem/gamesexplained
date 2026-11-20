# Ghosts 'n Goblins (C64) — orientation

## Disk and boot

The analysis uses the PAL sector image `Ghosts'n_Goblins_(PAL).d64` from
[C64Games.de](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=62).
It is a 174,848-byte D64 with SHA-256
`b04f4ce4edb9ab729795b63bb297cbcfa8bbfcc63f1a067fc0309f60cd9416e3`.
The archive also offers a patched NTSC image. The PAL bytes match the
boot and gameplay snapshots described below.

1. Start headless VICE with dummy audio and autostart the first directory
   entry, `GHOSTS N GOBLINS`, on unit 8. Turn on warp once the disk is
   loading. The title takes several disk reads.
2. Arm an execute checkpoint at `$0850` while the disk loads. Save
   `work/entry.vsf` at the stop before the first instruction. Delete
   the checkpoint, disable warp and resume.
3. The title has the Elite credit at the top and the score panel at the
   bottom. Press joystick port 2 fire to start stage one. The snapshot
   `work/play.vsf` shows Arthur in the graveyard. `work/title.vsf`
   preserves the attract screen before the fire press.

## What the disk loads

| File | Location and evidence |
| --- | --- |
| `GHOSTS N GOBLINS` | Boot program at `$01F8–$0303`. The bootstrap leaves its load filename at `$0302–$0303`, with the suffix updated in place. |
| `.1` | Loading picture at `$0C00–$3FFF`. The loader selects screen RAM at `$0C00` and bitmap mode with the bitmap at `$2000`. |
| `.2` | Loading picture colour RAM at `$D800–$DBE9`. The PRG header addresses I/O with the normal KERNAL mapping in force. |
| `.3` | Load at `$4000–$718E`. Execution at `$7148` was observed once. That routine copies `$4000–$6FF7` to the underlying RAM at `$D000–$FFF7`. All 12,280 copied bytes match the entry snapshot. |
| `.4` | Gameplay load at `$4000–$D000`. All 36,865 bytes match the entry snapshot. |
| `.5` | Gameplay load at `$0850–$3FFF`. All 14,256 bytes match the entry snapshot. |

The bootstrap increments the numeric suffix at `$0303` in the load
helper at `$02E5` before each KERNAL LOAD. It displays the bitmap
during the early loads and calls the relocation routine before loading
over its source. The five files constitute a single gameplay image.
The game's main loop increments `$3536` and reads the next stage
from resident RAM via `$2F3F`.

## Steady state and tools

At handoff the processor port reads `$37`. The game's raster setup at
`$31A6` clears bit 1, leaving `$35` during play. The hardware IRQ vector
points to `$31E5`, whose indirect jump selects a handler via `$3446`.
The NMI vector points to the RTI at `$31E4`. The captured graveyard
frame switched `$D018` from `$DC` to `$DE` near the top and back at
the score panel. The VIC reads the `$C000` bank.

VICE release v3.14.0, macOS arm64 headless. The emulator check returned
55 passes and three failures on dummy audio. These were `keys-host`,
`unpaced-calls` and `no-exception` (checkpoint-list response in the
quirk probe after restart). Exact stops, store and load watchpoints,
frame stepping, joystick writes and snapshot restoration passed.
Regenerator2000 was started on `work/entry.vsf` and seeded with the
executed-instruction map from the title and gameplay.
