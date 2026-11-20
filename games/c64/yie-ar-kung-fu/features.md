# Yie Ar Kung-Fu — feature checklist

| Feature | Status | Evidence or question |
|---|---|---|
| Oolong fights one opponent at a time to become Grand Master | open | Imagine instructions. Find the fight setup and completion tests. |
| One- and two-player modes | confirmed | The menu shows both options. The fight initializer receives the selected mode and the turn path at `$BE4A` consults it. |
| Walking, ducking and vertical or diagonal jumps | open | Imagine joystick diagram. Test which direction codes the game reads. |
| Face punch and leaping punch without fire | open | Imagine joystick diagram. Check facing and input priority. |
| Eight attacks with fire held | open | High kick, roundhouse kick, ground kick, leg sweep, ankle kick, flying kick, lunge punch and rising kick. |
| Ten opponents | confirmed | The opening preview shows Buchu followed by Star and Nuncha. The complete roster is in the addressed text records at `$C02C–$C085` and the ten stage records reached through `$A498`. |
| Opponent movement and weapons | open | The instructions describe Buchu's flight, Star's shuriken, long weapons, Club's shield, Fan's fans and Blues' speed. Check how these affect collision and damage. |
| Separate KO meters and move displays | traced | Both meters are visible in the first fight. `$B81C` initializes them, `$B86F` and `$B8C4` remove filled cells, and `$B8E0` updates the direction icon. |
| Five starting lives and a bonus at 20,000 | open | Imagine instructions. Find initialization, life loss, retry and bonus tests. |
| Current score and high score | traced | Both are visible with six digits. `$C5C3` adds to the BCD score and `$C5E7` draws it. `$C608` draws the high score. Individual attack awards remain open. |
| Tape loading display and music | live | The Ocean–Imagine loader shows a warning about attached peripherals and runs its own SID routine. |

## Sources

- Imagine's revised C64/128 instructions, as transcribed in the manual archive, consulted on 20 November 2026. [C64Games game entry](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=206)
