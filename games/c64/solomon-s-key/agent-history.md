# Analysis history

- Booted the SCG D64 with the preinstalled headless VICE and dummy audio. The exact execution stop at the jump target established the handover snapshot independently of saved title and Round 1 states.
- Compared the handover with a cold BASIC state and Round 1. Seeded the disassembler from the VICE execution map, then from statically resolved sprite IRQ, tile, actor, player-state, editor and music dispatch tables. The map is a sample of executed instructions from the observed boot-to-first-room path.
- Checked the control path with instruction steps and hardware, room-record and sprite-related accesses with memory watches. The frame recorder and store watch independently located the four sprite bands. Raw recordings and scripts are in ignored `work/`.
- Rendered the RAM font and sprite bank in `work/` to distinguish the stored glyph codes and sprite bitmap ranges from text and room tables.
