# Live and Let Die — orientation

## Disk and machine

Use the [Fantasy release](https://csdb.dk/release/?id=42805), extracted as `work/fantasy_live_and_let_die.d64`. The image is a 174,848-byte sector dump with a valid 35-track directory and disk name `FANTASY LIVE AND`. Its SHA-256 is `de4c216fbee56754fd5475bbdcb53eda51d639eb96009704a9c34755453d1bd5`.

VICE v3.14.0 headless for macOS arm64, PAL, dummy audio. The kit emulator check passed 56 probes. `keys-host` failed, while keyboard matrix input worked. `no-exception` was a missing `checkpoints` key in the final quirk probe after a reset. The exact stopping, instruction step and memory watchpoint tests passed.

## Startup

Hard reset and autostart the first file, `LIVE AND LET DIE`. When the Fantasy intro appears, press Space through the keyboard matrix. The startup loader calls KERNAL LOAD on device 8 and ends with `JMP $0803` at `$44F1`. Arm the hand-over checkpoint on `$0803` before pressing Space.

| File | Header | Loader and destination |
| --- | --- | --- |
| LIVE AND LET DIE | `$0801` | BASIC line calls `SYS 2064` for the Fantasy intro. The phase loader executes at `$4400`. |
| PHASE1 | `$5000` | LOAD at `$441E`, then `$4439` copies 32 pages to `$E000–$FFFF` with ROM banked out. |
| PHASE2 | `$5000` | LOAD at `$4466`, then `$4481` copies 16 pages to `$D000–$DFFF` with I/O banked out. |
| PHASE3 | `$4800` | LOAD at `$44B2`, spanning `$4800–$CFFE` before PHASE4 overwrites part of it. |
| PHASE4 | `$8000` | LOAD at `$44CC` replaces `$8000–$8FFF`. |
| PHASE5 | `$0800` | LOAD at `$44EE`, then the loader jumps to `$0803`. |
| PIC | `$2000` | Separate picture file. Its use is open. |

These phase calls run in one uninterrupted startup routine. The disk's phase names identify files within the startup image. The loader's instructions and the KERNAL breakpoint trace are the evidence for the table.

## Snapshots and course selection

- `work/entry.vsf` is the listing image, saved at `$0803` before the first game instruction. Read RAM beneath the ROMs and I/O. The CPU initially sees KERNAL ROM at `$E000`. The ROM's IRQ vector in RAM at `$0314` reads `$EA31`; the game installs and then uses hardware vectors directly when it maps out KERNAL.
- Run past the title with joystick port 2 fire. The briefing screen has a globe and a course label. Release fire. Down advances the selection and Up moves backwards, with wraparound. Practice is 0, North Pole 1, Sahara 2 and New Orleans 3. The game compares the whole port value in the menu, so use only the direction button for selection.
- On the chosen course, press fire and wait for the briefing text or start sequence to finish. For Practice and New Orleans, the text scrolls at `$46FA` before the next fire can start play. A stopping checkpoint on `$2A00` catches the transfer to the course. Release fire and advance a few frames for the first live picture. `work/play-practice.vsf` was saved 25 frames after the first instruction at `$2A00`. `work/practice-underway.vsf` was saved later in the same session.
- `work/menu.vsf` holds the briefing before confirmation. From that state, a breakpoint at `$0D47` catches a Down selection before the increment. `$0D5E` catches Up before the decrement. The script `work/course-probe.py` uses those points and saves `north-pole.vsf`, `sahara.vsf` and `new-orleans.vsf`. The course-selection snapshots differ in state and scenery. Each runs through `$2A00` in the same program.
- During Practice, the visible processor port was `$35`, the RAM vector at `$FFFE` held `$1829` at the end of frame 25, and a store trace caught the chain through `$16F5`, `$1802`, `$1397`, `$1535` and back to `$1829`. VIC bank 1 and `$D018 = $1F` give screen memory at `$4400`, the bitmap base at `$6000`, and character images at `$7800`.

The hand-over matches PHASE1, PHASE2, PHASE4 and PHASE5 in full. For PHASE3, both runs outside the overwritten window match in full, 30,719 bytes in all. The boot program and its copied loader are replaced by the game screen at `$4400`. The hand-over retains both copies of each resource the game later exchanges in RAM. That allows one address-space listing of the loaded image.

`work/loads.jsonl` records the five KERNAL LOAD calls after the intro in sequence. `work/play-watchpoints.txt` holds the vector store trace and `work/control-trace.txt` holds the instruction sequences for acceleration and the missile input branch. The VICE text monitor connection dropped during a later high-volume watch. Its first reads were captured in `work/hidden-ram-watches.txt`. The game snapshots were saved before that trace.

Regenerator2000 0.9.18 serves the analysis through the kit's assigned port. The disassembly starts at `$0803` and also uses the executed-address map from the four courses. The kit's default sixty-entry seed batch timed out. Five-entry batches reached every recorded start.
