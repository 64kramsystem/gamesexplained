# The Trap Door (C64) agent history

The first disk download endpoint returned a web page. The Cleveland Cracking Service image from CSDb arrived as a valid D64. VICE's supplied headless build kept exact CPU stops in the kit check. The apparent title loop was the timed crack intro. Tracing $B8DE showed how it exits without a button press. A checkpoint on $3800 caught the hand-off after the actual depack.

I saved separate early-play and hand-off snapshots. The hand-off retained the tape prompt bytes and the original pre-play data. The play snapshot preserved the bitmap produced after startup. The comparison initially flagged $FD30 as a moved copy of the KERNAL vectors. That byte pattern was already present before expansion and the startup clear-loop watchpoint explained the mismatch.

The first static music scan lost synchronization with a voice-dependent event. I traced the dispatch in VICE and used the kit CPU runner on the title routine to find the loop boundary and actual byte reads. A separate early-play code map seeded code missed by direct control-flow decoding. The graphics sweeps found atlas bases, fixed-width object records and a shape interpreter. Some shape data is self-modifying. The local shape walk leaves cases requiring more state open.

Tools used were the installed VICE MCP v3.14.0 headless wrapper and regenerator2000 0.9.18 on assigned ports. Work snapshots, the original disk, scripts and raw captures remain under `work/`. The exported coverage is the result of the ledger run, including the expanded payload where the classification is incomplete.
