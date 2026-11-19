# Features

| Part | Feature | Status |
| --- | --- | --- |
| Surface | Title offers fire to start and R to redefine keys | live |
| Surface | Opening spacecraft sequence and status panel with score and lives | live |
| Surface | Traverse the moon to the alien base and receive its access code | open |
| Surface | Walk, jump, duck, fly-kick and fire a laser | open |
| Surface | Avoid or fight the surface creatures and cross gaps on floating islands | traced sprite 7 position and update paths at $C221 and $B366. Creature rules remain open |
| Base | Separate load prompts for the access code | confirmed at $100D with a store watchpoint on $1137 |
| Base | Explore corridors, tunnels and floors linked by lifts | traced floor data and lift position tables at $BB28 and $BB60. The tunnel controls remain open |
| Base | Find terminal information and energy cells to prepare a colour-coded ship | traced readiness display at $A60C. Item and terminal paths remain open |
| Base | Enter the captain's code and launch | open |
| Base | Fight sentinels, inhabitants and robots with laser, kicks or hand-to-hand moves | open |
| Both | Alien kills award points and score thresholds award extra lives | traced surface score and life updates at $C370 and $B59D. The base scoring thresholds remain open |

## Sources

The included C64 title and access-code screenshots identify the two starts.
The [Imagine manual for the CPC release](https://www.gamesdatabase.org/Media/SYSTEM/Amstrad_CPC/Manual/formated/Freddy_Hardest_-_1987_-_Dinamic_Software.pdf)
was consulted on 19 November 2026. Its mechanics are leads for the C64
analysis. C64 key bindings, scoring thresholds and counts need independent
confirmation.

## Open searches

The surface movement switch at `$8345` and collision dispatch at
`$8860` identify input paths. Their remaining control combinations
and creature-specific effects need tracing. Course markers at `$8119`
provide leads for checkpoint and completion timing. The access code was
entered directly for the base, so the surface completion display is open.

The base's ship-position lookup and message code at `$A119`, `$A60C`
and `$AE0A` are mapped. The full launch and combat conditions need
following the remaining control and collision branches in the base
listing. The traces covered prompt acceptance and first-floor play.
