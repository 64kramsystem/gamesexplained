# Mouse Trap analysis log

- Booted the ATC / Brute Force PRG on the provided VICE MCP 3.14.0
  headless build with dummy audio. The C64Games ATC T64 payload
  matches the complete Edicola 8 Bit PRG payload byte for byte.
- Used a hardware keyboard matrix press for Normal selection and saved
  the handover at PC $8E00, the illustrated title and a real room.
  Raw RAM copies, VICE probes, the regenerator project and annotation
  logs are in `work/`.
- Captured the instruction-start map after clearing it and restarting
  from the engine handover. Used this and the decoded call graph to
  seed Regenerator2000, then described the routines and their data.
- Decoded the room directory and record lengths. Targeted breakpoints
  observed the descriptor cursor and the packed tile count in room 21.
  A short JSR trampoline exercised room setup at all 22 directory
  entries to test the read bounds. This was an instruction probe.
- Traced the second-stage loader with stopping store watchpoints.
  `lastwrite.log` separates the relocation store from subsequent unpacker stores. It records
  the PCs following the two stores, $082F and $009F. `resident-watch.log` contains the
  range-watch controls. `probe.log` records the title bitmap transfer
  instructions and the two readings of the joystick instruction.
- Compared the BBC disk's engine files with short exact matching
  windows to identify preserved BBC source and data. The unmatched
  C64 page at $4700 remains tracked while its original role is open.
