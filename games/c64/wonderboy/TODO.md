# Wonder Boy analysis handoff

The game builds one listing from `work/play-live.vsf` with the startup
comparison in `work/entry.vsf`. The image, both snapshots, the annotation
log, full census, and targeted trace scripts remain in local `work/`.
The media ledger has one answered item.

## Remaining Silver analysis

- Continue the step 50 queue. The final measured coverage is 49,684 of
  53,585 tracked bytes (92.7%). The listing also reports 1,527 bytes in
  eight ranges outside the ledger. Confirm ownership and consumers
  before typing or excluding them. The largest unresolved loaded ranges
  are `$CE03–$CFFF` and `$EFE1–$F1FF`.
- The installed headless VICE lost its MCP connection in both the stock
  and paced full-frame capture at checkpoint cleanup. The process
  exited in both cases. Individual execute checkpoints, store
  watchpoints and instruction steps worked after a restart.
  In particular, the ordinary IRQ branches were sampled individually.
  The full raster trace and later sprite-reload paths still need evidence.
- Once the coverage queue is closed, complete the step 60 feature checks
  and independent listing sample. The traces in facts.md are from the
  analysis pass. The kit treats `gpt-6.2-sol` as unproven, so a proven
  model check is also required for a Silver designation.
- Step 65 applies if a subsequent verification requires a replayable
  route. The analyzed states were reached with checkpoint-driven probes
  and the boot recipe. No recording was required for those probes.
