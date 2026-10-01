# Last Ninja Remix — features

Sources: [game documentation](https://www.lemon64.com/game/last-ninja-remix) and the contributor’s annotated listing, consulted 30 September 2026. The documentation supplies the feature inventory; the annotations supply leads for verification.

| Feature | Status | Evidence or open work |
|---|---|---|
| Isometric Central Park exploration | open | $8A52 recursive scenery renderer |
| Movement and combat | partly verified | Live `$B54A` damage and `$B767` collision boundary tests; full combat/control outcomes remain open |
| Objects and puzzles | open | $C0D0 trigger table |
| Animation and music | partly verified | 157 commands parsed; live `$A802` first step and changing SID state; all event/track outcomes remain open |
| Later levels | open | Replacement occupants are outside this Central Park listing |

The imported annotations remain leads until traced or exercised in this run. Central Park’s boot and initialized gameplay are observed live.
