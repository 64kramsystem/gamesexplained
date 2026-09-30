# Work toward Silver

- Finish coverage: 49.4% explained, 23,755 of 48,082 tracked bytes. Imported code descriptions cover the code ledger, but tracing/verification are still required.
- Resolve physical `$D000–$DFFF`: `listing.py` reports 4,096 non-fill bytes under I/O. The import calls them prior-phase residue; prove that here before excluding them.
- Capture final loader hand-over and compare with play to identify initialization-only data and all loaded authored data.
- Trace and exercise collection, collisions, guardians, arrows, ropes and winning behavior in `60-verify`.
- Restore and expand the interactive room browser after its claims are verified.
- Obtain the maintainer check required for the unproven run model and unknown imported models.
