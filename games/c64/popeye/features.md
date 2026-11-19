# Popeye — features

The [Alternative Software manual](https://www.lemon64.com/doc/popeye/459) describes this game's mechanics and matches the C64 control menu. Lemon64's footer links to the Parker Brothers game, while the manual text itself credits Alternative Software and describes the 25-heart adventure. The [Macmillan release record](https://www.lemon64.com/game/popeye-piranha) identifies the 1986 C64 edition.

| Feature | Status | Evidence |
|---|---|---|
| Start and movement with S, A, Z, X and Q | Observed | [Menu](reference/title.png), keyboard matrix input and the route to the lighthouse |
| Redefine keys, H to hold, port-2 joystick | Documented | Menu and manual |
| Connected locations and movement in depth | Observed at the starting stairs and lighthouse | [Olive's house](reference/olives-house.png), [lighthouse](reference/lighthouse.png) |
| Collect and deliver 25 hearts to Olive | Documented | Manual. The remaining-heart display starts at 25. Heart pickup traced at $5601 |
| Love meter declines and deliveries restore it | Countdown and restoration verified live | Execution checkpoints and store watches at the countdown boundary and inside the delivery handler. See [facts](facts.md) |
| Eight inventory slots shared by hearts, keys and spinach | Visible and traced | Manual and screenshots |
| Keyed doors, coin-operated fruit machine, fuse and cannon, and a ride on a passing saucer | Documented | Manual |
| Bluto changes depth. Birds, witches, dragons and sharks are hazards | Documented | Manual |
| A hit can consume spinach | Documented | Manual |
| 1,000 points per delivered heart, time bonus and ending reward | Documented | Manual |
| SID music and effects | Traced with isolated watchpoints | Six music pattern headers at `$85C0/$85C6` and twenty effect offsets at `$9000`. [Facts](facts.md) |
