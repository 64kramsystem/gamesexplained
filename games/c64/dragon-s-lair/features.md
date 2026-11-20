# Dragon's Lair — documented features

| Feature | Status | Expected behavior |
|---|---|---|
| Scrolling prologue | confirmed | After the castle picture, the game scrolls its opening story and credits on a custom character screen. |
| Joystick | confirmed | The external title picture uses port 1 fire. The inter-scene prompt uses port 2 fire. Both were instruction-stepped. |
| Falling platforms | live | Jump onto a descending disc and jump off at a ledge. |
| Skull Hallway | live | Cross platforms and resist the wind. |
| Burning Ropes | live | Time jumps between swinging ropes while avoiding flame. |
| Weapons Room | live | Dodge and strike flying weapons and armour. |
| Giddy Goons | open | Use evasive jumps and sword attacks. |
| Tentacle Room | live | Evade attacks from floor and ceiling on the way out. |
| The Ramps | live | Cross disappearing platforms and fend off attackers. |
| Phantom Knight | live | Ride another descending disc, then cross a board that the knight sets alight. |
| The Dragon | live | Use rock cover, collect the magic sword, defeat Singe and release Daphne. |
| Attempts | traced | The resident failure display consumes an attempt at $27. The successful scene-return path adds an attempt on scene indices 4–7 when the count is below four. |
| Music and effects | traced | The resident SID driver at $C004 processes five logical channels on three voices. The prologue credits Colin Porch. |

## Sources

Consulted 20 November 2026. [Dragon's Lair — C64-Wiki](https://www.c64-wiki.com/wiki/Dragon%27s_Lair), [Dragon's Lair — Lemon64](https://www.lemon64.com/game/dragons-lair) and the [C64 walkthrough](https://gamefaqs.gamespot.com/c64/580546-dragons-lair/faqs/20267). The walkthrough counts the initial falling platforms separately from Skull Hallway.

The scene captures establish that the pictured scenes load and run. Individual success, failure and bonus claims remain open unless traced in facts.md.
