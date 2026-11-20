# Stage 3

Loader IDs `04` and `05` begin at track/sector 25/0 and 9/0. They decode to 14,615 bytes at $86E9–$BFFF and 12,288 bytes at $C800–$F7FF. Both payloads match the stage snapshot byte for byte.

The stage layout selects 28 distinct 20-by-10 terrain chunks starting at $A020. Each tile has four character indices in the tables at $BC00–$BFFF. The sprite slots at $C800–$E7FF precede the two terrain character sets at $E800 and $F000.

The resident setup at $2E4D selects the stage hook and the actor placement lists for the two sections. The frame update calls the selected hook via $29CF.

In a debugger probe at $8BD8, setting $CB to five took the call to $2E4D and selected $8BE7 for the following frame. A store watch at $B9A8 stopped at $8BF7 after the first table's entry zero was written. The second hook selects a 32-byte property table at $90E3 below horizontal position $BC and at $9103 from position $BC onward.

With the second frame hook active, setting $BB to three at $8C0F reached the tile update at $8CA0 with X=5. Its store at $8CFB wrote tile $A6 into $B442. The destination was resolved through the current chunk, row and column values.
