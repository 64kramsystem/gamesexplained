# Analysis record

- Booted the D64 directly through file `2` using the batch's headless VICE with dummy audio. Captured the presentation, main entry, menu, Stage 1 banner and running Stage 1.
- Captured an execution map in Stage 1, a KERNAL LOAD breakpoint for `ATG`, and targeted instruction traces for the raster handlers, joystick and stage builder. The full frame-capture utility exited when VICE crashed, so the emulator was restarted from the Stage 1 snapshot.
- Rendered the character and sprite sheets in ignored `work/`. Expanded the stage recipe and terrain table and checked the expanded bytes against the snapshots. Used the native Rust port's public source as an address reference and checked annotations against the disk snapshot and instruction traces.
