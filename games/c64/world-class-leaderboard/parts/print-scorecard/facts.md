# Scorecard printer technical facts

The golf engine requests PRNT after the print prompt. At $CC3C, the loader uses port $01 = $38 to expose RAM, then copies pages $DC–$DF and $FB–$FC into $68–$6D. Store watches fired once at $6800, $6D1F, $6D20 and $6DFF before the execution checkpoint at $6800. All six loaded pages matched their source ranges byte for byte. The printer uses the same addresses as the golfer sprite work area during play.

The printer entry banks in the KERNAL and calls $6810. The code selects device and logical file 4, secondary address 7, and opens the output channel with KERNAL OPEN and CHKOUT. The print loop has front and back nine columns, per-round scoring totals, the player name and skill, and blank form fields for the date, signature, attestation and caddy. $680D jumps to $BA82 with the result in carry, where a set carry branches to the retry path. The local capture stopped at entry before opening the printer channel.

The loader’s full-page copy carries $FC20–$FCFF into $6D20–$6DFF. The scorecard’s only indirect read is the string walker at $6A3A. Its 15 call sites pass constant pointers to strings whose last terminator is at $6D1A. Instruction-level simulations with KERNAL output calls stubbed covered one to four players, a rejected OPEN and a rejected CHKOUT. The success cases reached $6D1A and the twelve cases left the copied tail untouched. The source RAM’s original use is open.

The number formatter at $6A66 accepts a two-byte value but mishandles some totals. An instruction-level simulation with CHROUT hooked emitted `1 5` for 105, `144` for 400 and `256` for 512. The tens-field check at $6AA8 checks the sign of a stored digit, and the high-byte path subtracts 100 from the low byte without accounting for the full high byte.
