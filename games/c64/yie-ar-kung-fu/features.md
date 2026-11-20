# Yie Ar Kung-Fu — feature checklist

| Feature | Status | Evidence or question |
|---|---|---|
| Oolong fights one opponent at a time to become Grand Master | traced | The setup loads one opponent record at `$A47C`. `$A205` advances through the ten opponents and wraps the index. The exact Grand Master award condition remains open. |
| One- and two-player modes | confirmed | The menu shows both options. The fight initializer receives the selected mode and the turn path at `$BE4A` consults it. |
| Walking, ducking and vertical or diagonal jumps | traced | The port-2 input trace at `$BB8C` shows active-low directions. `$BAC1` tests up and the side bits for jumping without fire. The pose lookup at `$1A99` selects the displayed move. |
| Face punch and leaping punch without fire | open | The branch at `$BBC3` translates direction and fire codes for facing. The attack labels in the manual have not been matched individually against the pose and contact tables at `$1A99` and `$1B29`. |
| Eight attacks with fire held | open | The manual names high kick, roundhouse kick, ground kick, leg sweep, ankle kick, flying kick, lunge punch and rising kick. The five-bit input and pose tables at `$BBC3` and `$1A99` are traced, and the eight names remain to be matched to the poses. |
| Ten opponents | confirmed | The opening preview shows Buchu followed by Star and Nuncha. The complete roster is in the addressed text records at `$C02C–$C085` and the ten stage records reached through `$A498`. |
| Opponent movement and weapons | open | The instructions describe Buchu's flight, Star's shuriken, long weapons, Club's shield, Fan's fans and Blues' speed. The behavior dispatch at `$B22F` and auxiliary sprite contact routine at `$A5D1` are traced. Per-weapon damage cases remain open. |
| Separate KO meters and move displays | traced | Both meters are visible in the first fight. `$B81C` initializes them, `$B86F` and `$B8C4` remove filled cells, and `$B8E0` updates the direction icon. |
| Five starting attempts and a bonus at 20,000 | live | `$BD5A` initializes the counter to four and `$A41F` decrements it on a loss. The negative count ends play. Stepping `$C635` showed how changes of the 20,000 bit in the high BCD byte award another life below the cap. |
| Current score and high score | live | Both are visible with six digits. `$C5C3` adds to the BCD score and `$C5E7` draws it. `$C608` draws the high score. A targeted trace followed a contact score-table entry into the decimal adder. The full list of attack names and awards remains open. |
| Tape loading display and music | live | The Ocean–Imagine loader shows a warning about attached peripherals and runs its own SID routine. |

## Sources

- Imagine's revised C64/128 instructions, as transcribed in the manual archive, consulted on 20 November 2026. [C64Games game entry](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=206)
