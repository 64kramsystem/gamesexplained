# Analysis log

- Created the game branch from the prepared batch checkout. Used the installed headless VICE release with dummy audio.
- Booted the X-Ray disk, declined the trainer, captured the title and forest play, and stopped a fresh boot immediately after the trainer. Kept the image and snapshots in ignored work directories.
- Used execution checkpoints and write watchpoints to locate the resident hand-over and five overlay loads. Captured each stage through the resident loader with a debugger-selected stage number. The screen buffer exclusion follows the zero read counts before its first clear.
- Exported the six part maps. The snapshot, frame capture, disassembler journals and short CPU traces remain in local work directories.
- Compared the upper-memory gap against the Censor release, rendered the shared eight-byte glyphs, and traced the X-Ray bootstrap store at $0819 to determine the provenance of its retained high-page bytes.
- Ran the exact ledger before verification. An independent same-model checker sampled the listing, and the checked corrections are in the exported map. The draw, verdicts and count stay in ignored `work/reports/`.
