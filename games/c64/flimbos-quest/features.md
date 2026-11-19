# Flimbo's Quest features

| Feature | Status | Evidence |
| --- | --- | --- |
| Rescue Pearly from Franz Dandruff | live | Standalone story viewer and the laboratory ending |
| Seven stage overlays, with a separate ending | confirmed | Numbered loads and captured stage screens |
| Carry scrolls to Dazz Bazian to complete the spell | traced | Shop progress display $26FE and stage requirement comparison $1FE6. Scroll-bearing enemy and pickup conditions are open. |
| Walk horizontally, duck and fire | confirmed | Port-2 input traced to stores at $24D0, $24DC, $2479 and $2516 |
| Jump and drop through platforms | open | The resident paths at $2541 and $2635 add signed displacements to player Y. The terrain gate at $263F tests bit seven of the saved cell property. Jump and drop trigger conditions remain open. |
| Enter or leave rooms | traced | Door comparisons at $25B0 and shop exit branch at $2074. The shop was exercised using the debugger. |
| Toggle music and effects from title | confirmed | Matrix input traced to $6B bit changes at $7B19 |
| RUN/STOP pause | traced | Reads at $1C6B and pause bit at $32. The PAUSED string is in the $7261 banner table. |
| Shop item selection and affordability | confirmed | Down input changed $225A through $205A. The price-rejection path is traced at $226B. |
| Stage skip and automatic move to the next stage | traced | $1F6C sets the progress count and $1FE6 tests the requirement. The transition was exercised from $20FE under the debugger. |
| Collect money and power-ups, stronger shots and temporary underwater breathing | open | The money fields and one timed effect are mapped. Their pickup and purchase effects need further analysis. |
| Five distinct heart colours trade for a life | traced | $1F86 checks stored colours, then calls the extra life path through $272C |
| Shooting changes heart colour | open | The shop heart-colour reader is at $1F86 and the panel colour cycles via $293D. The shot-to-heart colour transition remains open. |
| Treasure rooms, differently valued gems | open | The $29A2 selector marks a room object slot, and the actor handler at $42E1–$42FE adds packed-decimal awards from four descriptor bytes. Which award entries correspond to each displayed gem remains open. |
| Timer, lives and score | confirmed | HUD in gameplay and breakpoint tests for the timer. Life display and cap are traced. |
| Ending presentation | confirmed | The load count check calls the ending $9080, which installs its own IRQ and draws the laboratory scene |
| High-score screen | traced | The title code edits initials at $7F72–$7F89 and formats the scores at $8155–$8168. Record offsets are at $83D2. |
| Horizontally scrolling foreground and parallax background | confirmed | Maps at $A250 and $9990 and two live instruction checks |
| Title tutorial | live | Title screen text and icon carousel |
| Alternating stage tunes | live | Stepping $29EB–$29F2 to the call vector selected music entries 3, 2, 3, 2, 3, 2, 3 for the seven stage indices. |

## Sources

- [Flimbo's Quest – C64-Wiki](https://www.c64-wiki.com/wiki/Flimbo%27s_Quest), consulted 19 November 2026.
- Game screens and the animated story on the documented disk build.
