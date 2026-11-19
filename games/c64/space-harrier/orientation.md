# Orientation

The input is the [Jazzcat Cracking Team D64](https://csdb.dk/release/?id=160848), a 174,848-byte, 35-track sector image (SHA-256 `9312362b419ff7d40801783862a934be04bffa9f8ea369a17a8ae7937ae28ab5`). Its only file is `SPACE HARRIER`, a 47,951-byte PRG at $0801 including its two-byte load address. The directory reports no allocated sectors outside the file.

Use the C64 kit launcher with the installed v3.14.0 macOS arm64 headless release and dummy audio. The assigned ports are 18500 (MCP), 18501 (monitor) and 18502 (regenerator2000 0.9.18). The health check passed 56 checks. Host-key F1 failed, and the final quirks phase stopped at a missing `checkpoints` field. Use matrix input and the joystick tool. The full-frame capture terminated at checkpoint cleanup when VICE stopped answering; smaller watchpoint runs below answered after restarting.

1. Hard reset, arm an execution stop at $0850 and autostart the disk's first file. Wait for the cracker's credit screen and both unpacking stages. The first stop at $0850 was reached without input, within 35 seconds. Save `work/entry.vsf` there and remove the stop.
2. Continue to the title logo and its fire prompt. Pause and save `work/title-clean.vsf`. Hold port 2 fire for six PAL frames, release, then advance 320 frames. `work/active-moot.vsf` shows moving obstacles with TIME 59 in Stage 01.
3. Build the listing from `work/entry.vsf`, taken at the engine's first instruction. Comparing it to the earlier Stage 01 intro snapshot (`work/play-round1.vsf`) found 2,756 changed RAM bytes. The engine's startup instructions at $0850 are present at handover.

The BASIC stub starts with SYS 2065 ($0811). The wrapper relocates an unpacking loop into the stack page, and the loop expands runs identified by $C5 before jumping to $0850. The first $0850 execution starts the game initializer. No trainer choices appeared. Searching the disk payload in unique 16-byte pieces produced only small matches: 11 at payload-base $0149 and 9 at offset −$01B1, in both snapshots. No direct whole-file mapping survived unpacking.

At handover the effective CPU port reads $37 and the DDR $2F. A store watchpoint on $FFFE–$FFFF stopped after the low IRQ byte was installed, with PC $383C and port $35. The next store at $383E writes the high byte. In play the RAM vectors at $FFFA–$FFFF are $3855, $49C5 and $3856. The KERNAL RAM indirect IRQ vector still contains $EA31. With KERNAL banked out in play, the CPU enters $3856 directly. The entry saves A/X/Y and dispatches through ($4E95). An active Moot frame counted four entries to $3856 and zero stores to either hardware IRQ vector byte or $0314.

The title, stage banner and Moot share one resident image. The only disk file contains the cracker wrapper and the packed resident game. No additional program part was identified in orientation.

The comparison input was the [Non Stop Cracker D64](https://csdb.dk/release/?id=34041).
Its wrapper stopped in a KERNAL key poll at $036B–$036F; Space released
that wait. The local comparison snapshot was taken at the title, after
that wrapper, for a byte comparison only. It is not a listing input.
