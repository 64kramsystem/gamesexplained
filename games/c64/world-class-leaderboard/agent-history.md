# World Class Leaderboard analysis log

The installed headless VICE build on port 18504 passed exact stops, CPU stepping and memory watchpoints. Host key presses failed the tool self-check. Direct keyboard matrix events supplied F1. The self-check's optional server-quirk report stopped at a checkpoint-list response without a `checkpoints` field. The game traces used checkpoints successfully after the emulator restarted.

The code map first included KERNAL addresses hit while the keyboard reader briefly selected $36. The engine map keeps execution below the ROM window and the known RAM interrupt entry at $FF48. The raw capture remains in `work/tee-codemap-unfiltered.json`. Disassembler port 18506 was reused sequentially for the engine and printer.

The directory gave no PRNT file. The load breakpoint and stores at the overlay endpoints showed the resident side of the loader supplying it from RAM. The initially misclassified instructions at $6800 in the engine listing were interpreted from the golfer sprite bytes. Typing them as sprite data and giving the printer its own snapshot resolved the conflicting use of the addresses.
