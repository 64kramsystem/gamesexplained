# Orientation

New Imports disk, CSDb release 183003, file `BONE CRUN.+ /NEW`. Extract the file with `kit/c64/disk.py extract`. Hard reset the PAL C64, wait two seconds for BASIC, inject the extracted PRG with `vice.inject` and start at its BASIC SYS target, $081D. Injection writes $0801–$86E7. The packer runs before the New Imports intro. Press Space, press N to select No for Unlimited Lives, and press Return. Wait through the New Imports credit screen and second unpacker until the Superior Software title appears. The title screenshot is `reference/title.png`. Hold fire on port 2 for a quarter second, release, and wait for level 1. Save as `work/plain-play.vsf`.

In the title and level 1, processor port $01 reads $37, RAM IRQ vector $0314 points to $CA3C, and NMI vector $0318 points to $3600. Gameplay and title run from the same resident load. The disk contains one PRG. The packed file does not load directly at the gameplay addresses.

VICE v3.14.0 macOS arm64 headless, dummy audio, MCP 23064 and monitor 23065. The emulator check passed 56 cases. Host key input failed, so use the key matrix. The final quirks phase stopped on a missing `checkpoints` field after a reset. The instruction-step, stopping watchpoint, snapshot and joystick port 2 checks passed. Regenerator2000 answers on 23066.

The run stops at $3600 just after the packer hands over, with no JSR frames in the stack backtrace. Save `work/entry.vsf` there. The clean opcode at $3845 is `CE 54 49` (DEC $4954). The enabled trainer changes $3845 to $AD. The listing uses the untrained entry image. The live snapshots show the IRQ and NMI vectors installed by the game after this hand-over.

The title and level 1 both unpack data from the resident pointer table at $C9D3. Its 22 level entries use the same $6000 destination and the unpacker reads resident RAM. These streams are maps in the same game load.
