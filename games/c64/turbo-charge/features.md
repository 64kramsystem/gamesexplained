# Turbo Charge — feature checklist

| Feature | Status | Evidence or question |
|---|---|---|
| Start a single-player chase | live | Port 2 fire at the title loads the first driving scene on the captured release route. The title option and opening sequence are described in [the technical facts](facts.md). |
| Recover the stolen weapons | traced | The opening satellite and garage scenes set up the pursuit. The sequence of cards ends with [Game complete](parts/picture-18/facts.md). |
| Steering, braking and acceleration | confirmed | Checkpoints at `$6E9A/$6ED5` distinguish left and right. `$6F73` and `$6F80` are the accelerate and brake calls. |
| Handgun and missiles | confirmed | A hold hits the initial press branch once, changes the sight, then spends one missile on release. See [driving facts](facts.md). |
| Turbo boost | confirmed | Space hits the countdown setup at `$6FAB`. The active path spends fuel and advances speed. |
| Pause | confirmed | RUN/STOP reaches the three waits at `$6B38`, `$6B42` and `$6B4C`. A second press and release returns at `$6B56`. |
| Abort | live | Pressing RESTORE in round one reached the external NMI at `$937F`. The store wrote return reason one to `$A7BB`. |
| Damage, fuel and pickups | live | The crash-status store at `$6C5D` reported the final car. The fuel-contact path at `$9D0F` added three whole units. Turbo and normal acceleration draw on the fractional fuel reserve at `$A73B`. |
| Traffic, hills, bends and forks | traced | The driving script dispatches the road profiles at `$7A1F`. The fork handlers at `$7A4B/$7A7E` carry an inline destination. VICE probes confirmed the pitch table stores and the round-two traffic sprite composition. |
| Border countdown and scoring | live | Round-one countdown underflow at `$6992` wrote reason three and copied the expiry message. The score path at `$78A1` carried between two packed decimal bytes. |
| Multi-load stages and transitions | confirmed | Ten driving images form five chapters. The finish cards alternate border-smash and villain-capture scenes. The last capture card says Game complete. |
| Music and effects | traced | The title runs a three-voice driver. Five driving cue images supply two-voice order and pattern streams. The common effect player at `$BC4C` selects from 16 scripts, exercised in the kit CPU simulator. |
| Title and high scores | live | The title cycles through a scores display. The insertion probe reached the initials editor with the new score in the table. The save path at `$0F44` was traced to the drive wrapper, and disk persistence remains open. |

## Sources

Consulted 19 November 2026.

- [System 3 instruction manual](https://archive.org/details/Turbo_Charge_1991_System_3_M3/page/n1/mode/2up)
- [Turbo Charge gameplay summary](https://en.wikipedia.org/wiki/Turbo_Charge)
- [Sean Connolly interview](https://www.c64.com/gt_display_interview.php?interview=44)
- [Nostalgia disk release](https://csdb.dk/release/?id=230212&show=notes)
- VICE title and first-round observations. See `reference/` and `orientation.md`.
