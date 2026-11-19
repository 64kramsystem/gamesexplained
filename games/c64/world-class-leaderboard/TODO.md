# Analysis handoff

The ledger accounts for 51,482 of 51,482 tracked bytes. The engine has 49,946 of 49,946 explained and the printer has 1,536 of 1,536. Both rebuilt listings report zero uncounted stretches. Run `python3 kit/scripts/coverage.py games/c64/world-class-leaderboard` for the aggregate. The exact game and part checks are saved in the ignored `work/coverage-*.txt` files.

- The packed layout at $E000–$E0F0 decodes to thirteen thirty-cell rows. Its selector remains open. $F57B–$F5F2 is part of glyph bank 3 and its first cell was read by the bitmap glyph copy in a targeted trace.
- The printer overlay copies $6D20–$6DFF along with the last string page. The traced scorecard accesses stop at $6D1A. The copied tail's original purpose in engine RAM remains open.
- The remaining feature questions include the complete terrain and hazard outcomes, physical printer output, the manual's course editor and saving instructions for this release, and audio provenance across phases.
- The expanded listing sample found 12 inaccurate or incomplete comments in 60, with a 95% interval of 11.8%–31.8% before correction. The earlier sample found eight in 60. Both verdict sets and the settled counts are in the ignored `work/reports/` directory. A full listing audit followed by a fresh sample on a proven model is recommended.
- The branch is Bronze. A proven-model check and the minisite and reader review remain separate Silver requirements. Raw images, part snapshots, annotation logs and targeted instruction and memory traces are in ignored `work/` directories. The verification probes did not establish a new reachability claim that calls for an input recording.
