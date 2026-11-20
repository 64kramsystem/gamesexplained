# Final sequence

The engine invokes the overlay through five consecutive JMP vectors at $7800, $7803, $7806, $7809 and $780C. It loads record 402 into $7800 and picture record 409 into $A800 before the first call. After its return, record 428 replaces the encoded picture while the overlay instructions remain in place. All three loads were confirmed by byte comparisons against live snapshots.

$7993 expands either picture to $8000. Each expands to 10,002 bytes. The first 8,000 form the bitmap, and the next 2,000 comprise screen and colour attributes. The background byte is read at $A710. The [ending screenshot](../../reference/ending.png) comes from the forced load route described in the orientation.

A read, write and execute checkpoint over each of $7DB5–$7DB9 and $7E03–$7E8F counted zero hits between the overlay entry and the final input wait at $35EA. Both ranges remain tracked as part of the initial load.
