# Features

## Sources

- [Firebird instructions, transcribed by Lemon64](https://www.lemon64.com/doc/freak-factory/1432)
- [Zzap!64 review, reprinted by GameBase64](https://gb64.com/oldsite/gameofweek/17/gotw_freakfactory.htm)
- [GameBase64 screenshot](https://gb64.com/game.php?id=2911)
- Captures from the DCS release in VICE, listed in `orientation.md`.

| Feature | Status | Evidence |
| --- | --- | --- |
| Enter the factory by lift | live | `reference/entry-lift.png` |
| Two visible floors, doors and energy display | live | `reference/factory-floor.png` |
| Port 2 directional movement | confirmed | Instruction checkpoints at $4136, $453B and $45CC |
| Crawl with down and fire | confirmed | $4456 reaches the crawl setup and shifts Y by $15 |
| Gargoyles, spikes and lasers consume energy | open | $5972 and $59E1 qualify background contact by floor, position and room flags. The visible hazard corresponding to each interval remains open. |
| Find five laboratories and shut down their machinery | traced | The factory sets five lab numbers in its room routines. $9CFC marks a lab cleared. $9DF1–$9E0C tests all five flags. |
| Each laboratory has four assistants and machinery on floors connected by gaps | traced | $8C59–$8D35 set the four raster strips. $92F9, $9430, $955B and $9686 update four assistants. $9CBE moves the player down and advances the floor. |
| Fight assistants and replenish energy with alternating left and right | confirmed | $9B7F counts any port-byte change. A fire transition also triggered recharge in the targeted probe. |
| Previously defeated assistants return after a delay | traced | $8D79 with restore branches at $8E03–$8E20 |
| Shutting down a laboratory requires removing all its assistants | confirmed | Store watch on $BFF1 with and without an active assistant flag |
| Completing the five labs and leaving by the lift brings up congratulations | confirmed | Targeted probes reached $9E0C with all five flags set and separately reached $CBDE and $CF37 from the completed lift branch at $5FA3. |
| Energy reaching zero ends the attempt | confirmed | $6455 sets $40E0 when the gauge becomes empty and $40E4 dispatches death |

The five individually initialised lab selections are shown in `reference/laboratory-1.png` through `reference/laboratory-5.png`.
