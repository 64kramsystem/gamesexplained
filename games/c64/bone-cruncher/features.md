# Features

| Feature | Status | Evidence |
|---|---|---|
| Title names Andreas Kemnitz and musician Michael Winterberg | live | Title screen |
| Fire starts a game and joystick directions move Bono | confirmed | Level 1 opens on port 2 fire. A right press reaches $3CC4 with Y=$61. |
| Fire with a direction clears adjacent mould without moving Bono | confirmed | Instruction stops at $3E71 and $3E7F and store watches on $618A distinguish the two branch results. |
| Clearing mould, collecting skeletons and keys, making soap and delivering it score 1, 10, 100 and 1000 points respectively, with keys and skeletons both worth 10 | traced | $44B3 dispatches by the decimal place stored at $4541. |
| The kettle turns skeletons into soap for the monsters reached by stairs | traced | $3D08 spends five skeletons. Tile handlers $3D33–$3DEB decrement carried soap before the bathing scenes. |
| Fozzy, Glooks, goblins and spiders interact with Bono and the maze | open | C64-Wiki |
| Keys open gates. Trapdoors can catch Bono. | traced | $3E49 spends one key and rewrites a gate tile. The exact trapdoor tile transitions remain open. |
| F1 accepts passwords for later levels, F3 restarts, F5 sacrifices a life | confirmed | Matrix-key input reached $4610, $3988 and $398F respectively. The password table is at $CB40. |
| Panel tracks score, level, bonuses and supplies | live | Level 1 screenshot |
| 22 named levels | traced | The 22 maze streams selected by $C9D3 correspond to the 22 twelve-byte passwords at $CB40. |

## Sources

- Game title and level 1 captured from the New Imports disk.
- [BoneCruncher – C64-Wiki](https://www.c64-wiki.com/wiki/Bone_Cruncher), read 19 November 2026.
