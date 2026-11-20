# Test of Balance

- Two fire gates reached the acceptance branch at $0995 before execution reached the chamber loop at $08C4. Release clears a press latch, so one held press cannot accept both.
- $18CC produces the playfield bitmap and screen colours from the sources at $5800 and $7800. The initial instruction matrix at $8C00 is authored data and is overwritten when the bitmap display starts.
- The active IRQ vector was $198A with the processor port at $35. Six sprite pointers alternate between buffers as each pose is copied into the inactive one.
- The transition at $C900 calls LOAD for file 2. The new hand-over at $0810 retains the apprentice and the common result templates.
- The instruction trace of $18CC read $5800–$77E0 and wrote every byte of $A000–$BFE0, replacing the introductory character display with the playfield bitmap. It also wrote $8C00–$8FFC from the separate colour source. The introduction had copied its glyphs to $A000–$A2FF at $0C81, $0C87 and $0C8D.
- The action at $0E5E reads six rows from each of eight frame sources. The rows are 64 bytes wide within a 320-byte stride, and the loaded scene bytes equal to $9F are retained by the writer. $1684 draws six digit glyphs to $BEA0, $BEB8 and $BF30.
- The result test entered $086D with result mode 4, elapsed value 35, award input 60 and a new best target count. It reached the flag store at $0A90 and the four award stores once. The elapsed penalty brought the percentage to 55, setting the flag and writing 14, 0, 30 and 29 to the interleaved training record.
- The music initializer at $E173 sets three track pointers and a tempo. Calls through $E170 reached the phrase and track lists and used the resident SID parameter tables.
