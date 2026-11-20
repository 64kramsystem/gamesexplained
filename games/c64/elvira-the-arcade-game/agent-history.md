# Elvira: The Arcade Game — agent history

The Legend D64 booted with the prepared headless VICE. Host key presses missed in the health check. Direct matrix holds reached both crack intros and the trainer. The two globe hotspots required moving the cursor down as well as horizontally. The C64 globe pictures advance on joystick fire, then the quest prompt needs Space.

The first direct debugger jump into the interlude dispatcher selected CL but stalled in the serial loader. Letting the active quest take its own teardown path with the three transition bytes set reached Castle and later WIN. The debugger route is in the orientation notes.

A long-running checkpoint on $FFD5 armed after the first interlude request logged nothing. A targeted stop during the next transition reached the calls from $0825 and $0875 and established the B-then-A order. The checkpoint at $0812 must be armed following the A request. Waiting at the quest prompt has already passed that entry. Similarly, the artificial return address on the second LOAD means the stack-derived caller address is not the address of a JSR.

The native VICE memory map with mask `$12` showed writes across $0810–$C7FF in the Fire and Ice transitions. The Ice map missed upper RAM changes that were in the before-and-at-entry comparison, and the server stopped answering before the Castle map returned. After restarting VICE the entry snapshots and targeted instruction stops still worked. The write-map dump is a guide to ownership, alongside the disassembly and the RAM comparison. It does not establish an exclusion where the set is empty. Raw evidence is in `work/write-summary.txt` and the world-specific files it names.

A fresh boot reached the language initializer at $12ED through the trainer jump at $7D1E. The listing uses that entry capture because the selector later overwrites the loader at $C000. The language work files preserve the later capture alongside the hand-over, with the depacker and loader instruction traces.
