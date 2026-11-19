# Vigilante — analysis history

## 19 November 2026

Booted the preserved Data East USA G64 in the installed headless VICE with dummy audio. Captured the pre-decode engine handover, title and first stage. Stopping on the stage reload exit and counting the load instruction established a reproducible route to each overlay. The host-side transfer remained in use under `$7B00` after its original file's address was overlaid.

Full-frame capture caused VICE to exit during checkpoint removal. After restarting, smaller non-stopping instruction probes confirmed the raster handlers and the stage reload loop. The work folder retains the local probe scripts and snapshots.

Step 65 did not require a recording. The stage route uses the game's disk loader and a CPU checkpoint. Verification used short input probes from a local snapshot and made no reachability claim that needs a replay.
