# Mission A.D. features

| Feature | Status | Evidence or question |
|---|---|---|
| Joystick in port 1 | live | Fire opens the first briefing and a second press enters the room. |
| Keyboard mode and redefinable keys | open | The title offers both options. |
| Music toggle | open | The title displays MUSIC ON. |
| Numbered mission briefings | live | The first briefing displays 001 and waits for fire. |
| Targets and time limit | live | The first briefing asks the player to liquidate five targets in 16 minutes. |
| Platform movement, room transitions and shooting | traced | The player controller and its direction dispatch are at `$B1B0` and `$B190`. Fire reaches the shot path at `$B595`. |
| Enemy respawn | open | Reported in a Lemon64 player review. |
| Status panel | live | A panel with counters and icons sits below the first room. Its individual fields need tracing. |
| Later objectives, mission failure and retry | traced | Forced time, energy and quota cases took distinct result stores. The time and energy handlers branch on remaining lives. Later objective details are open. |
| Music and effects | open | Lemon64 catalogs 13 SID tracks. Identify each from its caller. |

| Lifts | open | The release instructions say to stand in the centre and press up or down. |
| Teleport selection | traced | The up/down/fire menu at `$C847` selects from eight destinations. The location condition needs a live check. |
| Status map and bars | traced | `$C31F` packs two-bit map marks. `$C3A7` and `$C3E2` draw the two bars. |
| Score bonus and civilian penalty | traced | The bonus calls its time and ally adders once per input unit in the forced-state trace. The friendly-hit handler at `$C0F0` decrements the ally count. |

## Sources

- In-game [title](reference/title.png), [first briefing](reference/briefing.png) and [first room](reference/first-room.png), captured in VICE on 19 November 2026.
- [Lemon64 release listing and reviews](https://www.lemon64.com/game/mission-ad), search extract read on 19 November 2026.
- [C64.COM credits and inlay listing](https://www.c64.com/games/209), search extract read on 19 November 2026.

- [Retro Games release instructions](https://retrogames.biz/games/c64/mission-ad/) and [Zzap!64 issue 17](https://datassette.s3.us-west-004.backblazeb2.com/revistas/zzap64_017_set86.pdf), consulted on 19 November 2026.
