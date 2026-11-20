# Ghouls 'n Ghosts analysis history

The initial TWT boot reached a wait at $C2AD/$C2B0. CPU history showed the serial input loop. The installed headless VICE build was kept and restarted with true 1541 emulation. A fresh process was also needed for repeatable handover capture.

The stage route was developed by stopping at $29FE and exercising its stage-outcome branch with a debugger write. Checkpoints at $5B5F and $5B6A separated the two stage requests. After the direct comparison left ambiguous areas under ROM and I/O, the sector chains and run-length decoder gave exact payload boundaries. The executor maps were collected for the title and each stage and seeded into the disassembler.
