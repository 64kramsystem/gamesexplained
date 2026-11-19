# Pac-Land analysis history

19 November 2026. The supplied Mac batch worktree used VICE-MCP 3.14.0 headless with dummy audio on port 17408 and regenerator2000 0.9.18 on 17410. No installation was needed. VICE passed 56 checks. Matrix keys replaced host-key translation. The quirks probe aborted on a missing checkpoint-list key, and the text monitor's memmap reset subsequently terminated the emulator. I restarted it and used execute breakpoints, instruction steps and memory watches for the live evidence. The executed-address map and play recordings are not dependencies of the listing.

The primary D64 came from the CSDb MCG release; its hash and unpacking route are in orientation.md. The Wanderer Group D64 and its title snapshot served as a local comparison of the game code and the retained bytes. Neither image nor any snapshot is tracked.

Regenerator2000 followed the direct calls from the entry and raster handlers. I added targets for the table-dispatched raster, text, object setup, object update and music routines. The terrain column notes and selected screen, map and operand annotations were generated from the decoded structures. The scripts and their inputs are under work/. The symbol map was exported from the live disassembler and the source listing built from the entry snapshot.

The sample and verdicts are under `work/reports/sample-20261119/`. The installed build reproduced the startup clear-loop finding with the CPU stopped after each instruction. Step 65 required no recorded play because the verification uses instruction-level interventions. The site, reader review and retrospective are outside this handoff.
