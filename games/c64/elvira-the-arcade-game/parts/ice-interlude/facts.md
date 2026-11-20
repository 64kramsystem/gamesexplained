# Ice interlude

The IL overlay sets up its illustrated screen at $1800. The raster IRQ at $1945 increments the tick at $19A4 and calls the driver at $0CDB on odd ticks. The screen matrix copy starts at $3DE3 and lands in RAM at $D400.

The next transition runs $0810 to request the B file. $0887 relocates loaded pages, then $0875 jumps to LOAD for the A file. The synthetic return enters the quest at $0812. See the game’s orientation for the two names and breakpoint evidence.
