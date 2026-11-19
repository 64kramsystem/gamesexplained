# Nebulus analysis log

## 19 November 2026

The Danish Gold intro took port 2 fire. The trainer displayed LIMITED LIVES with a spelling error and passed to the game on matrix Space. A stopping breakpoint at $8017 caught the hand-over. The separate file labelled NEBULA DOCS booted into documentation for Hades Nebula.

VICE's headless macOS v3.14.0 build used dummy audio on the assigned worktree ports. The emulator check passed 56 checks. Host-key input failed and a quirk probe ended on a missing checkpoint-list field. Matrix keys reached the trainer, and targeted stops, watchpoints and single stepping worked. The frame recorder lost the server connection during a step. Restarting on the same ports restored the saved PC and let the IRQ trace run through individual checkpoints.

An initial description treated the tower output as one page per row. The VICE decoder comparison at $B0A1 exposed the transpose. Comparing column-major data matched all eight levels. The comparison script and raw trace are in work/.

In the submarine scene, stopping at $A1C4 after setup showed the twenty destination addresses in the back screen, $74C8 through $77C0. Regenerator had interpreted the unpatched operand bytes in the tower snapshot as references into the engine and message records. The live comparison supported removing those placeholder field labels. The annotated project can be rebuilt with symbols_import.py.

Watchpoints tested the retained high RAM for 150 frames from hand-over and for 120 from the first tower. There were zero hits in $FE00-$FEFE and $FF40-$FFF9 in both windows. The sound descriptor watch at $F800-$FD3F recorded 1,020 and 80 hits respectively. The object phase tables at $CA00-$CDFF recorded 28 hits in the tower window. The negative windows leave the high-RAM payload's role open.

The independent gpt-6.2-sol checker sampled 60 of 460 listing comments, draw seed 20261119. It identified two issues, at $9066 and $C1B4. Simulated blocked motion confirmed that door alignment can fail while the animation advances. A second simulator case moved the camera without touching the screen. Both comments and the camera's jump-entry description were corrected. The draw and settled verdicts are in work/reports/handoff/.
