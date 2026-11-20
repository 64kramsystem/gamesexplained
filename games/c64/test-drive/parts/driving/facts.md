# Driving engine

The Lotus capture contains the common RD driver, the original D1 instrument module for this route, and the graphics data used by the first road. The other four cars load different instrument modules at the same addresses. Each road stage loads its own module at `$3600` and installs the three road-data pointers.

The driving IRQ entry is `$8AB3`. It banks I/O in, acknowledges the interrupt and updates VIC bank selection and the next compare line. The input watchpoint and the trace of up with fire reached `$8EA5` and the gear store at `$8EF4` respectively. See the root facts for the traced values and the road graphics format.

The listing uses `work/analysis.vsf`, the stage-one loader-return snapshot, because the `##` graphics payload at `$A286` is fully present there. `work/entry.vsf` is the earlier RD hand-over at `$6A1B` and `work/play.vsf` shows the road after drawing. The snapshot comparison distinguishes loaded instrument-panel art from the blank windshield the renderer fills.
