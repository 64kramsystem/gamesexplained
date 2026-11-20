# Stage 1

Loader IDs `00` and `01` begin at track/sector 19/1 and 21/2. They decode to 14,615 bytes at $86E9–$BFFF and 12,288 bytes at $C800–$F7FF. Both payloads match the stage snapshot byte for byte.

The stage layout selects 22 distinct 20-by-10 terrain chunks starting at $A020. Each tile has four character indices in the tables at $BC00–$BFFF. The sprite slots at $C800–$E7FF precede the two terrain character sets at $E800 and $F000.

The resident setup at $2E4D selects the stage hook and the actor placement lists for the two sections. The frame update calls the selected hook via $29CF.
