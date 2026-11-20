# Stage 2

Loader IDs `02` and `03` begin at track/sector 23/1 and 11/2. They decode to 14,615 bytes at $86E9–$BFFF and 12,288 bytes at $C800–$F7FF. Both payloads match the stage snapshot byte for byte.

The stage layout selects 28 distinct 20-by-10 terrain chunks starting at $A020. Each tile has four character indices in the tables at $BC00–$BFFF. The sprite slots at $C800–$E7FF precede the two terrain character sets at $E800 and $F000.

The resident setup at $2E4D selects the stage hook and the actor placement lists for the two sections. The frame update calls the selected hook via $29CF.

The phase-two routine swaps ten complete character patterns at $F4C0 with ten at $F510. A store watch on the first glyph range stopped at $8F4B, just after the indexed write at $8F48 with X=$4F.

Setting the horizontal position to $BC at $8EB5 reached $2E4D and selected $9052 as the next frame hook. A store watch at $B92D stopped at $908D after the new hook wrote zero to the terrain property for character $2D.

A probe set slot $17 to type $3B with its motion state clear and set bit two of $2945. The dispatcher reached $8984. The actor entered $89BA, and a watch caught the motion-state increment at $89BD. The next shape store selected $DC for the side of Arthur tested.
