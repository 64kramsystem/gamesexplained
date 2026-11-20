# Test of Balance

- Two fire gates reached the acceptance branch at $0995 before execution reached the chamber loop at $08C4. Release clears a press latch, so one held press cannot accept both.
- $18CC produces the playfield bitmap and screen colours from the sources at $5800 and $7800. The initial instruction matrix at $8C00 is authored data and is overwritten when the bitmap display starts.
- The active IRQ vector was $198A with the processor port at $35. Six sprite pointers alternate between buffers as each pose is copied into the inactive one.
- The transition at $C900 calls LOAD for file 2. The new hand-over at $0810 retains the apprentice and the common result templates.
