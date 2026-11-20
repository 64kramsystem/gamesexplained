# Stage 5

Loader IDs `08` and `09` begin at track/sector 6/17 and 30/0. They decode to 14,615 bytes at $86E9–$BFFF and 12,288 bytes at $C800–$F7FF. Both payloads match the stage snapshot byte for byte.

The stage layout selects 27 distinct 20-by-10 terrain chunks starting at $A020. Each tile has four character indices in the tables at $BC00–$BFFF. The sprite slots at $C800–$E7FF precede the two terrain character sets at $E800 and $F000.

The resident setup at $2E4D selects the stage hook and the actor placement lists for the two sections. The frame update calls the selected hook via $29CF.

A debugger probe traced the first section’s frame call at $29CF into $92FE. Setting $FD=$2F and $FB=$3C just before its transition test took the call to $2E4D. The later frame hook at $936E reached the indexed load at $93AF and the following store instruction at $93B2 with X=$0B and A=$FF, selecting the second preset from $940D–$9418.

The setup routine at $95A2 calls the column writer at $94A7 and passes the terrain edit script at $95D1 to $2FCD. The script contains ten records of six bytes followed by $FF at $960D. Each record selects a chunk and a starting column and row, then gives a count of one and two replacement tile indices. The decoder treats the count as one less than the number of bytes to write.

Type $3C dispatches to $8731. A probe put this type in slot $17 with a zero shape. Stops at $8731 and $88B4 followed by a watch on the slot’s shape confirmed the initial shape write. The same probe reached the same instructions and wrote the same value from the stage 2 snapshot.

Type $6B first checks the linked type $30 companion. In a probe with the companion inactive and $8C81 set to one, the handler stopped at $8B6D, the counter watch fired after the decrement at $8B7C, and the next stop at $94A7 had X=$0B. That selects the second set of terrain-column edits.
