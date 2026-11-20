# Orientation

The source is the OUG disk edition from the Internet Archive, kept locally as
`work/oug.d64`. It is a 174,848-byte, 35-track sector image, with SHA-256
`c0dc130bc0a33251242d66c7766555c472b589afe2d6c0cbda5e5ab773b20463`.
The kit disk reader reported 683 sectors and zero used sectors outside the
directory and file chains. It extracted directory files to `work/disk/`.

## Boot

1. Start the installed VICE MCP v3.14.0 macOS arm64 headless build with dummy
   audio. The restored worktree uses MCP port 23040 and monitor port 23041.
   The original emulator check reported 56 passes and two failures. Host key names failed,
   and the quirks probe hit a missing `checkpoints` result. Matrix keys,
   stopping execute and store checkpoints, stepping and snapshots passed.
2. Autostart `R. GHOSTBUSTERS+` by name from the disk. Wait for the blue
   OUG screen with the sunglasses logo. Press fire on control port 1. The
   intro code at `$2062` reads `$DC01` and jumps to `$3502` when the
   value is `$EF`. The CPU history after the transition showed a decode
   loop at `$0022`–`$002D` copying bytes with an index-dependent XOR.
3. Answer N twice on the keyboard matrix for the two unlimited-lives
   prompts. Pause at “PRESS 1 or 2” and save `work/title.vsf`.
4. Press 1 and wait at “Press any key to continue”. Press Space. The
   subsequent disk load can take tens of seconds at normal speed. Wait
   for Stage 1 and save `work/play.vsf`. Turn warp off when timing play.

At the title, `$0314/$0315` reads `$EA31`. In play it still reads
`$EA31`, while the processor port reads `$35` and the hardware IRQ
vector in RAM at `$FFFE/$FFFF` points to `$0C31` in the captured state.
The handler at `$0C31` acknowledges the VIC raster interrupt at
`$D019` and then reads the CIA1 interrupt control register at `$DC0D`.

## Disk files in memory

| File | Evidence |
| --- | --- |
| R. GHOSTBUSTERS+ | The boot program is not present as a contiguous image in title or play. A 16-byte chunk search found four matches at the best alignment of each snapshot. |
| LEVELA–LEVELK | The eleven KERNAL-return snapshots `work/stage1-packed.vsf` through `work/stage11-packed.vsf` hold each complete disk payload at `$6000`. The stage expansion snapshots hold the decoded overlays. |
| Picture and demo extras | Separate BASIC-startable files on the same disk. The directory entries and load evidence are in `media.json`. |

During the first level load the CPU was in the KERNAL serial receive code
with a return stack through `$5610` and `$3367`. The KERNAL filename
pointer at `$BB/$BC` was `$3387`, whose six bytes were `LEVELA`.
The call at `$3367` branches on successful load to `$337A` and restores
game banking before returning.

## Overlay capture

The resident layout is in `parts/resident/`. The kit requires symbol maps
and listings to live in the part folders for a game with overlays. Start
the later captures at the title snapshot. Press 1, wait for the prompt,
arm a stopping execute checkpoint at `$32FC` and press Space. Save this
state locally as `work/stage-select.vsf`.

At that checkpoint, set `$11` to the zero-based disk suffix
(`0` for A through `10` for K), and use the game's own loader.
The ignored script `work/capture-stage.py` captures the return from
KERNAL LOAD at `$5613`, the return from the first unpacker at
`$337A` and the completed expansion at `$3302`. The script
`work/trace-stage-setup.py` captures the first setup dispatch and
advances eight frames from that point. This route uses the loader
directly and does not establish how the player reaches each stage.

The captured expansion windows begin at `$6000`. Their ends differ
because the stage files produce different amounts of code and data.
The expanded snapshots are the sources of the overlay listings.
`parts/resident/work/stage-1.vsf` is the resident listing source.
The audited hand-over is `parts/resident/work/entry.vsf`. Set a stopping
checkpoint at `$0820` once the trainer prompt is visible and answer N to
both prompts. At the hand-over, the instruction bytes at `$0820` begin
`AD 11 D0 29 4F 8D`. The depacker also executes at `$0820` earlier,
when the instruction begins `A5 AC`, so an early address hit captures
the wrong image. The resident startup then clears screen RAM at
`$4000` and sets up the raster IRQ.
