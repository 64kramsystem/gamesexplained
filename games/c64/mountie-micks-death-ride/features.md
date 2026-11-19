# Features

## Sources

- [C64-Wiki](https://www.c64-wiki.com/wiki/Mountie_Mick%27s_Deathride), consulted 19 November 2026.
- [Lemon64 documentation scan](https://www.lemon64.com/doc/mountie-micks-death-ride/1083), consulted 19 November 2026.
- The Mega Team disk build in the media ledger. See [the title](reference/title.png), [loading picture](reference/loading.png) and [Train 1](reference/train-1.png).

| Status | Feature |
|---|---|
| live | The title page displays a score table. Fire starts Train 1. |
| live | Train, lives, score, supplies and train diagram occupy the panel below the playfield. |
| live | The playfield scrolls the mountains, train and foreground fence. |
| confirmed | Nine trains have resident scripts with distinct layouts. Each initialiser ran with its selected script. |
| traced | The handcar connects the departing train and the already selected next train. $1AAA advances the script before the rider boards through the path at $3E42. |
| confirmed | Joystick and A/Z/O/P/Space decode to the same five control bits. Left, jump and duck paths ran from the stopped Train 1 snapshot. |
| traced | The movement handlers use contact classes for climbing. See $32B9 and the vertical movement case at $2C87. |
| confirmed | Standing fire consumes ammunition and starts a projectile. Ducking fire reaches the grenade path and consumes supply type two when seeded into a slot. |
| traced | Vertical contact with bandits can transition the other actor to state $2C. See $356B. |
| traced | Pickups alter ammo, torch charge or item slots in the routines at $33AB and $344E. |
| confirmed | T and G reach the torch and mask handlers. Synthetic charge, terrain flag and mask inventory isolate the equipment branches. |
| traced | Terrain classes, train hazard tag $50, bandit spawn at $3703 and paired foreground templates at $227A gate hazards. The titles and pictures identify the documented tunnels, obstacles, boats and elk. |
| confirmed | S activates the damage state and debits a retry. H pauses the playfield updates. |
| traced | Q jumps to the title. The right-edge paths at $2B42 and $3B5A route outlying actors to replacement states. |
| confirmed | M clears the active music flag on repeated samples and the SID-copy routine ran. The C64 documentation credits Ben Daglish. |
| open | The reported Train 7 obstruction and left-boundary bypass are unresolved. The script, opening display and boundary paths were identified. The exact collision cell and whether the route works in this release remain open. |
