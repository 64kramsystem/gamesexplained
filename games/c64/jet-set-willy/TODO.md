# Work toward Silver

- The tracked ledger includes the retained high-RAM bootstrap, its room templates and all 102 rope sprites. The entry/play audit still reports loaded regions outside that ledger; resolve these before claiming complete coverage.
- Identify the loaded copyright/loader region, remaining title-music stream extent, title-text continuation and retained lower-memory bytes. Do not treat unexplained prior-phase bytes as padding.
- Capture final loader hand-over and compare with play to identify initialization-only data and all loaded authored data.
- Trace and exercise collection, collisions, guardians, arrows, ropes and winning behavior in `60-verify`.
- Restore and expand the interactive room browser after its claims are verified.
- Obtain the maintainer check required for the unproven run model and unknown imported models.
