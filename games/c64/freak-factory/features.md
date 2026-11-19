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
| Gargoyles, spikes and lasers consume energy | open | Zzap!64 review |
| Find five laboratories and shut down their machinery | open | Firebird instructions |
| Each laboratory has four assistants and machinery on floors connected by gaps | open | Firebird instructions |
| Fight assistants and replenish energy with alternating left and right | confirmed | $9B7F counts any port-byte change. A fire transition also triggered recharge in the targeted probe. |
| Previously defeated assistants return after a delay | traced | $8D79 with restore branches at $8E03–$8E20 |
| Shutting down a laboratory requires removing all its assistants | confirmed | Store watch on $BFF1 with and without an active assistant flag |
| Energy reaching zero ends the attempt | confirmed | $6455 sets $40E0 when the gauge becomes empty and $40E4 dispatches death |

The five individually initialised lab selections are shown in `reference/laboratory-1.png` through `reference/laboratory-5.png`.
