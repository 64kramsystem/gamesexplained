# Ghosts 'n Goblins (C64) — analysis log

## 20 November 2026

The installed macOS arm64 headless VICE build ran on its assigned port
with dummy audio. Host key mapping and an unpaced stress probe failed
its setup check. A later unpaced request during a stopping checkpoint
also dropped the server. Restarting headless VICE and pacing the same
operations succeeded.

The Newcomers crack reached a modified title picture, and direct PRG
injection did not reach stable play. The PAL retail disk worked through
its own loader. The breakpoint at $0850 captured the handoff and the
boot trace hit the relocation entry at $7148 before that. Regenerator2000
used the handoff snapshot as its source.

The title and graveyard instruction map seeded the first trace.
The stage probes added evidence for dynamically selected terrain and
encounter paths. The disk bytes and graphics relocation fixed the
ledger's authored ranges. Stage-start memory watchpoints and bounded
table readers established the exclusions described in the ledger.

An independent gpt-6.2-sol sample checked 60 comments. The script
`work/check_phrases.py` parses every indexed music phrase after the
sample found that the common template overstated its contents.
The two disable-pulse-sweep command paths were checked live with
execute checkpoints and store watches. No input recording was needed
for these direct mechanic and data checks.
