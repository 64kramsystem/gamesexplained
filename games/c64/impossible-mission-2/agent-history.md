# Impossible Mission II analysis history

The installed VICE-MCP headless executable and its dummy audio wrapper were kept. The Sharks D64 reached the intro but the custom serial reader stayed around $BE40–$BE6E polling CIA2. The Nostalgia D64 reached NOSDOS and stayed in its serial loading path. The publisher G64 passed control to its boot code at $02E0 but did not reach a playable display in this setup. The tape release worked after pressing Play when the bootstrap was waiting for pulses.

The kit's TAP reader provisionally divided stretches of this recording into generic turbo pages. The decoded pages did not match the RAM at the reported addresses. Reading the pulse reader and testing the two measured pulse widths against the snapshots recovered the actual named format. The private decoder, alignment diagnostics and original generic extract are in `work/`.

A trial seek after restoring a snapshot without an attached TAP crashed VICE. Reattaching the tape before seeking restored reliable positioning. The final sequence and scoreboard were then reached by setting the program counter to their original resident load paths. A forced record 315 probe at offset 649298 skipped the header while the monitor resumed the live machine. Moving the seek back to 646000 and disabling warp until the probe was armed caught the copy and matched all 3,120 bytes.

The disassembler initially walked code beyond the logged addresses and created false entries in the boot screen. That region was reset to undefined after matching it to the BASIC startup screen. The high-RAM character sets were identified by live writes to the VIC memory selector. The resident listing is built from the $0880 hand-over because it preserves startup code overwritten by subsequent screen setup.

Retyping the resident compiler's inline frames and jump tables removed false operands emitted by linear decoding. Reimporting that map also dropped an automatic span at $03D7–$03DE. Those eight bytes match the title's bootstrap cassette fragment at the same addresses and lie outside the recorded resident load ranges.
