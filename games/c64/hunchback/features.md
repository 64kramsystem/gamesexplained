# Hunchback features

| Feature | Status | Evidence |
| --- | --- | --- |
| Cross the castle walls and rescue Esmeralda | traced | The stage index wraps at 48 and every sixteenth layout sends completion to the rescue sequence at `$55D3`. |
| Title, instructions and start | live | SPACE opened the input selection and J opened the port 2 prompt. `$46AD` dispatches F1 to the instructions at `$46D0`. |
| Move and jump | confirmed | The live port 2 poll writes the three action bits at `$03FF`. At `$49BA`, left and right moved X by two, while fire started a jump in place. The keyboard matrix path is traced at `$4930`. |
| Wall layouts | confirmed | The first three stage indices were traced live through the indirect wall renderer at `$425F`. The masks at `$7011` compose wall, gaps, decorations and guarded positions. |
| Arrows and fireballs | traced | IRQ paths at `$4D59-$525E` select projectile type, height and direction through the stage's hazard bits. Fall and collision checks begin at `$56F3`. |
| Swinging rope and platforms | traced | `$539E` selects the rope phase and `$5406` tests contact. A forced lookup exposed an out-of-table pitch selection. Its reachability in play remains open. |
| Pursuing guard | confirmed | Guard draw calls were counted at `$530B` while the gameplay IRQ ran, and `$5733` tests his X against the player's once he reaches the top. |
| Bells and scoring | confirmed | The completion path calls the bell sound at `$3EA7`. Instruction breakpoints at `$5583` confirmed the award based on timer band and stage. |
| Super bonus and bonus life | traced | At five markers the completion code awards 5000 for each marker at `$4A84`. The bonus life test at `$4AC9` checks the ten-thousands digit and a latch. |
| Lives, retry and high score | traced | The death routine spends one life and can restart the same wall. The final score comparison and three-letter registration begin at `$581D` and `$588E`. |
| Attract music and effects | traced | `$3CEF` plays the attract tune from 64-entry frequency and delay tables. Separate SID paths handle jumps, projectiles, wall completion and death. |

## Sources

- [Hunchback – C64-Wiki](https://www.c64-wiki.de/wiki/Hunchback), consulted 19 November 2026. The title and first-wall comparison captures come from this page.
- [C64Games.de, game 74](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=74), consulted 19 November 2026. Source of the Ocean TAP used for the analysis.
- The title and instructions stored in the TAP name the game, give the controls and explain the bonus marker rules.
