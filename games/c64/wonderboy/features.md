# Wonder Boy features

Sources read on 19 November 2026.

- [Wonder Boy, C64-Wiki](https://www.c64-wiki.com/wiki/Wonder_Boy). Gameplay and boss animations in reference/ come from this page.
- [Wonder Boy, Lemon64](https://www.lemon64.com/game/wonderboy). Credits and release identification.
- The instructions bundled with the Remember disk, seen after pressing fire at its intro.
- [Manual transcription](https://www.c64x.no/games/wonderboy_manual.php). The controls in this transcription describe the Spectrum version. Use the C64 sources for controls.

| Feature | Status | Evidence or question |
|---|---|---|
| Rescue Tina across seven territories | open | Find the ending and territory limits. |
| Four rounds per territory, four signposts per round | open | Locate the round data and retry checkpoint. |
| Woods, waterfront, caves, and mixed terrain | traced | Row pointers at `$1EC1` and character streams at `$AB17`. Opening forest observed live. |
| One or two players, music toggle, pause | traced | F1 starts play live. Title choice at `$F737`, music toggle at `$09DE` and pause handler at `$3D00`. |
| Walk, run, jump and throw | traced | Matrix and port-2 joystick at `$24F3`, movement at `$29B6`, axe at `$2D2C`. Jump and fire edges confirmed by instruction checkpoints. |
| Vitality drains with time, food replenishes it | traced | Drain and exhaustion confirmed live at `$F38D`. Meter at `$F33C`. Food effects remain open. |
| Rocks, fire, pits and moving platforms | open | Distinguish terrain and object collisions. |
| Snail, snake, wasp, blue runner, spider, frogs, bat and squid | open | Identify movement and hit states. |
| Break eggs by kicking or shooting | open | Identify contents selection and axe prerequisites. |
| Axe, skateboard, mushroom, guardian and Death | open | Locate timers, transformation and collision rules. |
| Potion, extra life, spring, doll and clover | open | Locate pick-up and score effects. |
| Boss shots, scaling, defeated head and collectible | traced | Boss initialization at `$23F2`, phase handling and shot spawning at `$393A`. Full progression remains open. |
| HUD shows lives, axe, boss items, scores and vitality | open | Identify draw path and score encoding. |
| Round-end vitality bonus and doll multiplier | traced | Bonus at `$F473` and BCD transfer to score at `$F5BA`. Doll modifier remains open. |
| Death, retry and game over | open | Compare vitality exhaustion with collision and fall outcomes. |
| Background music and effects | traced | Selector requests at `$E000`, tick at `$E003`, music interpreter at `$E870`. |

The bundled C64 documents also describe quitting while paused, an extra life at area completion, and score-based extra lives. The pause quit path is traced at `$3D71` and score carry at `$F661`.
