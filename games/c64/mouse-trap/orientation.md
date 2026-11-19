# Mouse Trap orientation

The input is the Commodore 64 PRG advertised under the original title on
[Edicola 8 Bit's Squeal page](https://www.edicola8bit.com/gioco?id=2364).
Its header specifies load address `$0801`. The BASIC line invokes
`SYS (2064)`, or `$0810`. The payload is 37,729 bytes.

1. Hard reset a PAL C64 in VICE, autostart `work/mouse-trap.prg`, and let
   the virtual drive finish loading. The ATC / Brute Force trainer offers
   1 Normal, 2 9 Lives, and 3 Trainer. Select 1 using keyboard matrix row 7,
   column 0. The menu is preserved locally as `work/trainer.vsf`.
2. For the listing image, stop on `$8E00` while selecting Normal. The
   trainer's `JMP $8E00` at `$0938` transfers control there.
   Save `work/entry.vsf` without ROMs. The CPU port reads `$2F/$37` at
   the stop. Option 1 writes `$05` to `$18D0` and `$C6` to `$18FB`
   before transferring control.
3. Run 162 frames from the trainer selection with the key released after
   12 frames. The illustrated title is `reference/title.png` and the
   corresponding snapshot is `work/attract.vsf`.
4. Press fire on port 2 to leave the title. The first playable room is
   `reference/play.png` and `work/gameplay.vsf`. The CPU port reads
   `$3F/$05` in play. With the ROMs banked out and I/O visible, the
   hardware NMI, reset and IRQ vectors point to `$8E93`, `$6060` and
   `$8E99` respectively. The KERNAL RAM IRQ vector at `$0314` reads
   `$C020` in the title snapshot.

The BASIC stub copies its depacker to the hardware stack page and jumps to
`$0100`. The resulting trainer and game are in RAM at the menu. The
trainer applies the selected settings, restores the processor port, then
jumps to the game's startup code. The game starts from an unpacked image,
so a linear address offset from the PRG would conflate packed input with its
output. The supplied medium has one PRG. No additional medium or bank is
required to reach the title and first room.

VICE MCP 3.14.0 ran headless on port 23056 with the dummy sound device.
The emulator check passed 56 checks, including exact instruction stepping,
watchpoints and frame advance. Host key names did not reach the keypad
matrix and the final quirks phase raised `KeyError('checkpoints')`. Use
matrix coordinates for keyboard input. Regenerator2000 answers on port
23058.
