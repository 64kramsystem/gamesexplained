# Tower engine

The listing is based on the snapshot immediately before the loader transfers to $0880. The played snapshot preserves the first elevator and the loaded first-tower resource at $A520. The hand-over retains initialization instructions at addresses that are rewritten after startup.

$0AD4 bypasses the saved-game question when $A1D1 is nonzero. $A1D1 is one in this tape's hand-over. $0A4A would otherwise draw messages at $B9C2 and $BA12 and scan the keyboard for Y. The title and engine use different raster and sound setup. See the watchpoint results in [the game facts](../../facts.md).

A separate load probe used the resident call at $0A0A to request record 315. All 3,120 tape bytes matched at $A520. A store watch at $F400 stopped after $6232 during the backward copy from that buffer. The natural opening checkpoints instead recorded requests 000, 130 and 328.

A targeted run entered $7C26 on the hand-over snapshot. The $EC80 store watch stopped just after $7C2A, and the execution breakpoint at the return showed all 64 bytes set. The first seven matched $7C20–$7C26, including the entry opcode $A2, and the remaining 57 were zero.

With A set to layout zero at $59E2, the $E788 store watch fired just after $5A41. Execution to $5A56 produced all 120 glyph bytes at $E788–$E7FF. They matched the fifteen IDs in the list at $9641, taking eight bytes per ID from $9D54.
