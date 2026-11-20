# Pitstop II — features

| Feature | Status | Evidence or open question |
|---|---|---|
| Title and credits | confirmed | Title capture. Space advances to setup. |
| Setup | confirmed | The menu shows number of drivers, course, lap count and difficulty. Port 2 down and fire selected Start the Race. |
| Driver names | confirmed | Both prompts accepted Return with the defaults. |
| Two-driver starting grid | confirmed | The prompt requires both ports in two-driver mode. $4FA1 records the first port to fire and $4FCE waits for the other. |
| Split-screen race | confirmed | Both road views, course maps and lap counters appear in the race capture. |
| Solo race | traced | The driver-count option at $039E routes the second driver to the synthetic controls at $4E4A. The live run used two drivers. |
| Course selection | traced | The pointer list at $980D names all six entries. $3346 indexes the matching course data. Brands Hatch was the live test course. |
| Grand Circuit | live | Forced branch values $83 and $85 at $A134. The first advanced to $84 and $3300. The second cleared the option and entered $9439. |
| Steering, acceleration, braking and turbo | confirmed | Steering uses the direction bits at $395B and $3989. Live checkpoints at $388C and $39D2 established the five longitudinal speed changes in facts.md. |
| Fuel and tyres | traced | Fuel usage runs at $471B and the four tyre states are capped by $3B2B. The checkpoint observations covered normal driving without forcing depletion or blowout. |
| Pit entry | live | At the position-qualified branch $3AFA, the four edge probes accepted $15 and $1E and rejected $14 and $1F. |
| Refuelling | open | The crew input and service paths start at $6F14 and $702C. The precise hose-overflow path is still open. |
| Tyre change | traced | The wheel-contact tests at $77FF dispatch to the four picture and colour updates. No full pit stop was driven. |
| Pit exit | traced | The cursor action checks coordinates and crew state at $6FBD onward, then $4B90 restores road graphics in phases. No full pit stop was driven. |
| Results and restart | traced | The ranking array at $28–$31 indexes the score table at $A14B. The fire continuation at $A134 reaches $9439 for a single course. Restore also vectors to $9439. |
| Sound | traced | Grid tones at $503E, engine pitch at $3C8E, pit effects at $7B7E and standings tones at $A0BE. The SID register census establishes the writes with dummy audio. |

## Sources

- [Epyx C64/128 manual](https://evercade.info/wp-content/uploads/2023/02/Pitstop_II_1984_Epyx_en-de.pdf), accessed 20 November 2026.
- [C64-Wiki](https://www.c64-wiki.com/wiki/Pitstop_II), accessed 20 November 2026.
- VICE captures in `reference/` and snapshots in `work/`.
