# Scene graphics and speech

A forced call at $0A0A reached the original record 315 loader. The store watch on $F400 stopped at $6234, after the final store of the backward copy at $6232. All 3,072 bytes at $F400–$FFFF matched the start of tape record 315. Its 48-byte suffix was still at $B120–$B14F. The source at $A520–$B11F is the staging copy of the same 3,072 bytes.

- The agent animation reads the first VIC sprite pointer from $4EA2 and uses the next two consecutive values for the rest of the frame. At the opening elevator snapshot, a controlled call to $4E69 with $48 set to $1C hit store watchpoints on $F3FE, $F3FF and $F3FD. The three writes installed $D0, $D1 and $D2. In VIC bank $C000 these address $F400, $F440 and $F480. The following two groups start at $F4C0 and $F580.
- $63A2 moves three 64-byte sprite cells into writable storage beginning at $F640. The engine's compositor also writes to $F640, $F680 and $F6C0. The bytes in the listing are the versions delivered by the tape.
- The resident entry at $3606 calls the speech setup at $FA87. With RAM vectors selected, execution checkpoints caught $FA87 and the first timer NMI at $F8C0. A store watch on $D418 stopped immediately after $F8C3 wrote volume seven. The decoder uses the base word at $FAFA, which is $0740 in the captured record. The installed vector uses page $F8, with its low byte changing as the playback phase advances.
- $FFC0 holds sprite-shaped data at copy completion. Later engine code reuses the space for special room actor fields and interrupt vectors. The column write is at $3985, the row write is at $398B, and the class writes are at $3967 and $3991. The engine sets its NMI vector at $2ECF and $2ED4 and its IRQ vector at $2EC4 and $2EC9.

The bytes at $B120–$B14F match exactly the 48 bytes beginning at offset $800 in record 306. The 192 bytes at $F740–$F7FF are copied from record 315. The first slot repeats the byte pattern $04 $00 $FF $FB with two variations. The last two slots predominantly repeat $00 $04 $FB $FF. Sixteen-byte matches occur in records 264, 267 and 306. The composer at $6358 uses bounded byte offsets within the three writable slots at $F640–$F6FF. The repeated slots remain tracked and their use is open.

The bytes after the speech driver at $FB06–$FB3F begin with a zero and decode as a fragment of 16-bit x86 code. Both relative calls, at $FB08 and $FB32, resolve to the same destination. Each is followed by a test of AX. Two branch paths reach the same BP-relative load at $FB3D. The offsets identify addresses in the C64 tape copy. The fragment’s original load address and purpose are unknown. It remains listed as cassette data.

The input probes are controlled instruction-entry tests.
