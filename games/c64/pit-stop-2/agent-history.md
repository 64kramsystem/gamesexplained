# Pitstop II — analysis record

- Captured the decompressor handoff at $C000, the title, the setup
  menu, the grid and the moving race using the assigned VICE instance.
  The grid requires fire from both selected drivers before the countdown.
- Reconstructed the decoder input window and its run commands in
  `work/unpack.py`. A zero run count wraps to 256 before the loop
  exits. The exact output agrees with the full 57,344-byte game block.
- The kit media scanner identifies the T64 container as unread. The
  ledger records its one occupied entry directly from the directory and
  records the exact unpacked match. The input image remains in `work/`.
- Rendered glyphs and 64-byte sprite slots to identify visual data,
  seeded the disassembler with a live execution map, then exported the
  annotations from the assigned Regenerator2000 session.
- Captured the race IRQ chain and used instruction and store
  checkpoints to check the vector handoff and port-2 acceleration.
  The scripts, snapshots, frame captures and trace logs are in `work/`.
- The CSDb X-OR disk comparison has the same packed format. Its
  reconstructed payload differs from the T64 in two bytes at $B204 and
  $B20A. Both comparison files stay in `work/`.
- A frame advance with the two broad load/store watches active closed
  VICE's connection. Restarting the assigned headless instance and
  resuming normally let both watches answer. The failed and successful
  probes are retained in `work/`.
- The frozen listing sample and verdicts are in
  `work/reports/sample-1984/`. Input, timer, pit-window and standings
  probes are in `work/verify-*.py` with their output beside them.
