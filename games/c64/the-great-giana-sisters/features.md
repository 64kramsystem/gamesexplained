# Features

| Feature | Status | Evidence or question |
|---|---|---|
| Time Warp loading screen | live | The boot program displays the Time Warp Productions logo while the main program loads. See `reference/loading.png`. |
| One- and two-player menu | live | The attract banner offers keys 1 and 2. Key 1 reaches Stage 01. |
| Alternating Giana and Maria | traced | $09E9 saves fields by active player before toggling the index at $0A17. Both active flags are left clear by the key 2 branch. |
| Port 2 input and jumping | confirmed | Stepping $9F84 gave $FF centred and $FE with up held. After ten frames the up trial moved from Y $CB to $B0 and the control stayed at $CB. |
| 33 numbered stages | traced | Layout pointers 1–33 select the numbered maps. The ending flag at $157E is written by the crossing test at $301A and consumed at $0ABF. |
| Stage introduction and status panel | live | The screen shows the player's name and stage before play. In play the panel lists score, bonus, lives, stage and time. |
| Lives and retry | confirmed | The Stage 01 frame displays 03 and the start code sets $043C to three. $2041 decrements that byte and $0C46 tests its sign for the retry decision. |
| Dreamcrystals | confirmed | A controlled entry at $1C4F with crystal count $99 reached the carry branch, changed the life count from three to four and added 25 points. |
| Hidden prizes and powers | open | The tile contact code at $1A17 dispatches to block and pickup paths, and $14DC swaps player shapes based on $22. The full progression and per-pickup rules need a separate field-by-field trace. |
| Holes, nails, fire and collapsing bridges | traced | $1D67 tests the bottom edge and tile category flags for fatal contacts. The bridge dispatcher and tile-removal slot update are visible at $1C6E and $19CF. The precise tile art for each hazardous category is open. |
| Creatures, flattened shells and dreambubbles | open | $288A reads sprite collisions, $29B2 processes ordinary object hits and $2A69 tests the weapon level and free projectile slot. The individual exceptions for shells and the dragon need a targeted contact trace. |
| Secret rooms and the route through Stage 32 | traced | The branch at $1E19 selects resident bonus recipes and treats stage $20 specially by selecting $21. A player route through that branch is open. |
| Pause or return to menu | confirmed | Matrix row 1, column 7 took the pause store at $21F3, and release took the clear at $21FD. The hardware NMI target is the menu entry at $084F. |
| Today's scores and all-time scores | traced | Entry at $325D compares and prints the two tables. The name-entry and SAVE paths are at $3348 and $3459. Startup KERNAL LOAD for ATG was confirmed with a breakpoint. |
| Music and sound effects | confirmed | The periodic driver runs at $439E and the effect entry is $4987. Stage 1 produced 616 SID stores in a 24-frame test. Track identities beyond the code-indexed selections remain open. |

## Sources

- [Original Commodore 64 manual](https://c64online.com/wp-content/uploads/2021/03/The-Great-Giana-Sisters.pdf), consulted 19 November 2026.
- Attract screen and Stage 01 in the disk image identified in `orientation.md`.

- [Native Rust port](https://github.com/kvnshroom/giana-sisters-native), consulted 19 November 2026 for candidate routine addresses. The comments and findings derive from the D64 snapshot and C64 disassembly.
