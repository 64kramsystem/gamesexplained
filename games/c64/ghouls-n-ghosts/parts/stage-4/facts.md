# Stage 4

Loader IDs `06` and `07` begin at track/sector 27/5 and 7/0. They decode to 14,615 bytes at $86E9–$BFFF and 12,288 bytes at $C800–$F7FF. Both payloads match the stage snapshot byte for byte.

The stage layout selects 27 distinct 20-by-10 terrain chunks starting at $A020. Each tile has four character indices in the tables at $BC00–$BFFF. The sprite slots at $C800–$E7FF precede the two terrain character sets at $E800 and $F000.

The resident setup at $2E4D selects the stage hook and the actor placement lists for the two sections. The frame update calls the selected hook via $29CF.

In a debugger probe with slot $17 set to type $63 and descriptor-owner entry three free, instruction stops reached $8C9A and the allocation branch at $8CAA. A watch on $8E94 caught it storing owner slot $17. The shape write that followed used $E1, the shape associated with descriptor entry three.
