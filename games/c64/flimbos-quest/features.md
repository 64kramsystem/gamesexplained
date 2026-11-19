# Flimbo's Quest features

| Feature | Status | Evidence |
| --- | --- | --- |
| Rescue Pearly from Franz Dandruff | live | Standalone story viewer and the laboratory ending |
| Seven stage overlays, with a separate ending | confirmed | Numbered loads and captured stage screens |
| Carry scrolls to Dazz Bazian to complete the spell | traced | Shop progress display $26FE and stage requirement comparison $1FE6. Scroll-bearing enemy and pickup conditions are open. |
| Walk horizontally, duck and fire | confirmed | Port-2 input traced to stores at $24D0, $24DC, $2479 and $2516 |
| Jump and drop through platforms | open | The player movement paths are partly annotated |
| Enter or leave rooms | traced | Door comparisons at $25B0 and shop exit branch at $2074. The shop was exercised using the debugger. |
| Toggle music and effects from title | confirmed | Matrix input traced to $6B bit changes at $7B19 |
| RUN/STOP pause | traced | Reads at $1C6B and pause bit at $32. The PAUSED string is in the $7261 banner table. |
| Shop item selection and affordability | confirmed | Down input changed $225A through $205A. The price-rejection path is traced at $226B. |
| Stage skip and automatic move to the next stage | traced | $1F6C sets the progress count and $1FE6 tests the requirement. The transition was exercised from $20FE under the debugger. |
| Collect money and power-ups, stronger shots and temporary underwater breathing | open | The money fields and one timed effect are mapped. Their pickup and purchase effects need further analysis. |
| Five distinct heart colours trade for a life | traced | $1F86 checks stored colours, then calls the extra life path through $272C |
| Shooting changes heart colour | open | C64-Wiki |
| Treasure rooms, differently valued gems | open | C64-Wiki |
| Timer, lives and score | confirmed | HUD in gameplay and breakpoint tests for the timer. Life display and cap are traced. |
| Ending presentation | confirmed | The load count check calls the ending $9080, which installs its own IRQ and draws the laboratory scene |
| High-score screen | open | C64-Wiki |
| Horizontally scrolling foreground and parallax background | confirmed | Maps at $A250 and $9990 and two live instruction checks |
| Title tutorial | live | Title screen text and icon carousel |
| Alternating stage tunes | open | C64-Wiki. Resident SID paths identified. |

## Sources

- [Flimbo's Quest – C64-Wiki](https://www.c64-wiki.com/wiki/Flimbo%27s_Quest), consulted 19 November 2026.
- Game screens and the animated story on the documented disk build.
