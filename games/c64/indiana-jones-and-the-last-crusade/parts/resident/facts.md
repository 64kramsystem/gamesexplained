# Resident engine

The bootstrap reaches `$7D5C`. The resident code handles both the title and play. During play its two raster handlers alternate at `$809C` and `$81CF` and the serial load path at `$B80F` replaces the map and field charset for the requested stage.

See [facts.md](../../facts.md) for the instruction stops, writes and bank values.

## Startup data and alternate layouts

- The expanded bytes at $1401–$1460 contain six compact sound-effect records, each eight pitch bytes followed by eight SID control bytes. Records zero, three, four and five agree with the active effect streams at $1D74, $1DA7, $1DB8 and $1DC9 after removing each pitch terminator. Record one changes its last pitch, and record two has different pitches and controls. The packed relocation bytes at $FF7D–$FFB8 likewise agree with the expanded sprite at $FC00–$FC3F when the three-byte token at $FFB5 is decoded as seven zero bytes.
- The 128 tile codes at $7AB0 include two copies of the six-tile sequence $36–$3B. That same sequence starts at fifteen addresses in the train map from the saved load. The records at $BB00 include alternate temple room coordinates in the same 20-byte layout used by the active table at $B354. The two regions are unchanged between hand-over and play. Bounded read watches from the boot hand-over and five saved stage entries recorded no reads of either region or the compact effect records. This evidence establishes format and origin. Their runtime consumers remain open.

## Instruction watchpoints

- Starting from the five saved play states at $AEE1, write watchpoints stopped after $AEE7 and $AEED. The combined lookup operand was $3100 in the caves, $0096 on the train, $3200 in the catacombs, $3300 in the airship and $0000 in the temple. The train path branches away at $A627 before the lookup at $A64F.
- Starting from $9C54 with stage indices 0–3, a watchpoint after $9C6A captured $FF, $00, $00 and $FF at $9BF3. At $99F7–$99F9 the title printer treats zero as a blank row before the prompt and $FF as the end of the page.
- With the cave phase set to three and the subtick at $10, the watch at $7BFA stopped after the store at $8BA7 with $11. This wrap of the four-phase clock adds one to the subtick. The subtick carry at $8BAA is a separate condition for advancing the dimming index.
- With train phase zero and timer $12FF, the watch at $7A35 stopped after $8C64 with $13. In the caves, setting the decoded fire bit and starting at $9E6E with the fire latch clear stopped after $9E89 with player mode $08.
- A watchpoint on panel pointer zero at $C3F8 stopped after the raster's clear at $80E3. The later loop at $8163 copies the eight pointer values from $7C10. In the temple, the store at $8C2D was observed advancing the timer's low byte to four.
