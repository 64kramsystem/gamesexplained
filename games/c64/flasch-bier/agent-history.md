# Agent history

VICE-MCP ran headless on port 23188 with dummy audio. The disassembler was assigned port 23190. The C64 emulator checks used the existing build. The host-key test failed and the initial boot attempt overlapped with the unpaced transport phase. A serial boot succeeded after the checks.

The hand-over snapshot preserved the whole loaded program. Regenerator2000 initially interpreted the RAM under ROM entry points as code. The final project and export use only the game code blocks and explicitly typed loaded data. `work/annotate.py` can regenerate the hand-written labels and data classifications from `work/initial-symbols.json` and the entry snapshot. `work/verify_live.py` uses the original `work/cave.vsf` snapshot filename because VICE already had an earlier capture registered as play-round1.

The analysis scope ended at verification. Step 65 was considered. The fixture tests establish direct code behavior and the orientation recipe gets to the first cave, so no input recording was needed for the agreed deliverables.
