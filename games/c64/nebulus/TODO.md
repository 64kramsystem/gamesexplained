# Nebulus analysis handoff

The resident C64 listing uses `work/play-tower1.vsf`, with `work/entry.vsf` as the hand-over comparison. The exact step 50 ledger is **43,013 of 43,013 bytes explained**. It covers 17,498 code bytes and 25,515 data bytes. The rebuilt listing reports no uncounted stretches. The same resident image contains all eight tower maps and the submarine scene. The separate documentation file is classified in `media.json`.

- The follow-up's independent sample found six errors in 60 comments. All six sampled errors were corrected. The estimated error rate before those corrections was 10.0%, with a 95% Wilson interval of 4.7% to 20.1%. The sample can miss errors. A listing-wide audit is due. The kit classifies `gpt-6.2-sol` as unproven, so Silver also requires its proven-model check.
- The full lift and door transitions and the mapping from individual music events to named tunes remain open. The traced predicates and music entry points are in `facts.md`.
- Step 65 required no recording. The verification cases replay controlled debugger states and make no route reachability claim.

The branch is an analysis handoff. Its metadata keeps the entry out of site builds until site work begins.
