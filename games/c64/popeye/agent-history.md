# Popeye — agent history

The run selected the named `POPEYE 86` PRG from the C64.COM compilation and captured the separate 1986 copyright picture. It confirmed player control in Olive's house and at the lighthouse before analysis. A later entry capture stopped at `$4000`.

Coverage began with VICE's executed-address map and took a second pass across start-up and the controls screen. The static seeds followed the drawing, actor and room dispatch tables. The game uses its own bitmap glyphs. The string sweep also turned up retained BASIC text, which was compared against the ROM. The independent comment sample identified the scenery command and other descriptions corrected in the exported listing.

Step 65 did not need a recording. Release identity was established from direct play and the verification evidence consists of execution traces, watches and isolated instruction stops. No portable input track is needed by the handoff.

The follow-up rebuilt the committed listing byte for byte from the saved play snapshot before resuming the annotation ledger. It recovered bounded song voices, sound effect descriptors, drawing substreams, secondary actor scripts and earlier copies of code. The range decisions used load and store watchpoints and compared two disk entries at hand-over. The ledger reached exact equality for tracked bytes while the stable ranges in `TODO.md` stayed open. No new portable input recording was needed.

The next resume matched 42 previously uncounted bytes to drawing and sound fragments and added them to the symbol map. A decompressor store trace and isolated drawing and actor interpreter probes narrowed the remaining three stretches.

The final coverage pass added the three unpacked tails as retained data and recovered the short gaps between records. The exact ledger reached 50,336 explained bytes of 50,336 tracked, with no uncounted stretches or short-gap warnings. Targeted VICE stops and watchpoints checked drawing operands, voice terminators, the tile-bank boundary and a delivery in progress. These isolated checks established instruction behavior without requiring a Step 65 input recording.
