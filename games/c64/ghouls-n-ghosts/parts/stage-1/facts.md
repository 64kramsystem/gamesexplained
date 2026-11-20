# Stage 1

Loader IDs `00` and `01` begin at track/sector 19/1 and 21/2. They decode to 14,615 bytes at $86E9–$BFFF and 12,288 bytes at $C800–$F7FF. Both payloads match the stage snapshot byte for byte.

The stage layout selects 22 distinct 20-by-10 terrain chunks starting at $A020. Each tile has four character indices in the tables at $BC00–$BFFF. The sprite slots at $C800–$E7FF precede the two terrain character sets at $E800 and $F000.

The resident setup at $2E4D selects the stage hook and the actor placement lists for the two sections. The frame update calls the selected hook via $29CF.

A probe at $91FD set $CB to eight. The next instruction stops were at the resident section setup $2E4D and the new frame hook $920E. The store watch at $B901 then caught the write of $80 at $9246. The same instruction writes $20 when joystick bit two is set at row $12.

A debugger probe set slot $17 to type $2E at the resident dispatch. Entry $8A26 wrote five to $5D07 before allocating linked type $30 slots $16 and $15. The parent advanced to type $2F and the linked position path reached its second shape store at $8BB1.
