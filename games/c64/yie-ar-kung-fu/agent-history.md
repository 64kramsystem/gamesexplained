# Yie Ar Kung-Fu · analysis log

The PAL tape booted in VICE 3.14.0 headless with dummy audio. A CPU trace of the default configuration reached `$EA68` as a JAM after the serial-line check at `$0524`. A cold boot with the virtual peripherals disabled stepped the same BIT with its N flag set. The no-drive boot reached the first fight without a game-memory patch.

The hand-over source was compared with the first-fight image and the nine extracted turbo blocks. The loader's source copy beneath I/O remains tracked. The regenerated on-screen character cells at `$4000` replace the relocated tape reader and its workspace.

Local handoff evidence is in `work/`:

- `entry.vsf` and `entry-nodrive.vsf` stop at `$0400`. `play-round1.vsf` shows the first fight.
- `jam-history.txt` and `joystick-trace.txt` hold the CPU observations. `round-frame.json` records one early fight frame's video writes, including the patch to the IRQ handler's phase target.
- `assets.py` renders the two glyph sets and the candidate sprite banks. `decode-streams.py` decodes screen streams. `music-data.py` walks SID stream and instrument pointers; `music-data-summary.txt` names its remaining gaps.
- `stage-read-watchpoints.txt` has the stage initialization read checks. Every case hit `$A498–$A4AB` twice and executed the hardware IRQ. The single broad watchpoint hit in `$307F–$35FF` stopped at `$80EC` after the sound setup's overlapping BIT at `$80E9`. The instruction reads `$35A0` as part of the skip used to enter the common selector setup.
- `compare-excess.vsf` is a disk-edition comparison snapshot with all trainer options declined. Matching tails are evidence that the editions carry the same data. The comparisons do not establish the tails' consumers.
- `annotations.jsonl` is the Regenerator2000 client log. The canonical export and listing are in the game directory.
