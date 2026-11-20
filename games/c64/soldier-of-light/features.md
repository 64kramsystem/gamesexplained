# Soldier of Light features

| Feature | Status | Evidence or question |
|---|---|---|
| Title credits and three animated planets | live | The title names Reptilia Design, Ian and Mic, Rob Whitaker and the Maniacs of Noise. |
| Start and destination selection | live | Port 2 fire opens the selector. The stick moves the ship and fire over Cleemalt selects it. The three displayed destinations are Cleemalt, Lagto and Cleedos. |
| Ground movement | live | Up reached the jump-accept branch at `$1067` and the state write at `$0BE1`. The second ascent is traced through `$116C` and `$1183`. Air steering and the prone pose need further tracing. |
| Ground combat | open | The port 2 fire check at `$2000` enters the slot action logic at `$1F88`. Sprite-latch and per-slot coordinate comparisons are traced. The ducking effect on hits and the attack behavior of specific enemies remain open. |
| Pickups and weapons | open | The object shape dispatch at `$8A4E` distinguishes several sprite shapes. The sequence that produces the upgrades reported in reviews, including double fire, remains open. |
| Three terrain sets | live | Cleemalt begins under a jagged skyline, Lagto among green vegetation and Cleedos against a cyan sky with light grey rocks. Each is captured in `reference/`. |
| Scrolling and terrain hazards | open | The position-to-tile lookup at `$15A6` and movement-state checks beginning at `$1200` trace the support and fall decisions. The moving platforms reported on Cleemalt remain open. |
| Get Ready | live | The wait at `$3C45` reads port 2 after the raster-timed sound call. Fire advanced to play. |
| Score, damage, time and lives | live | The HUD displays SCORE, DAMAGE, LAST, TIME and MEN. The least-significant score rolls into `$8483` and `$8482`. A VICE watch observed the timer units digit roll from zero to nine at `$0830`. Some field update conditions remain open. |
| Planet bosses and completion | open | The collision branch at `$200F` identifies the special masks `$83` and `$C3`. The result renderer at `$2F3B` draws the base and mission messages. Exact boss attack and reuse rules across planets remain open. |
| Spaceflight between worlds | live | A targeted CPU entry at `$0C63` stopped at `$E800` and produced the space display. Legal input reachability, later waves and the exit remain open. |
| Retry, game over and overall completion | open | The game-over display is drawn at `$0F26`. The counter at `$0691` gates the completion path at `$069F`. State retention across retries and legal-play completion remain open. |
| Music and effects | live | Cue start and tick at `$C001/$C007`, effect update at `$FE12`. A watchpoint confirmed the SID control write at `$C645`. The listing identifies cue tracks, note patterns and effect parameters. |

## Sources

- C64 title, selector and Cleemalt in the F.S.N. release, captured 20 November 2026.
- [Lemon64 C64 game record](https://www.lemon64.com/game/soldier-of-light), search excerpt, 20 November 2026.
- [Lemon64 C64 review](https://www.lemon64.com/review/soldier-of-light/1187), search excerpt, 20 November 2026. The review also discusses the arcade's five planets.
- [Vintage Is The New Old C64 and Amiga review](https://vitno.org/2020/06/07/soldier-of-light-c64-and-commodore-amiga-review/), search excerpt, 20 November 2026.
- [Soldier of Light C64 review and screenshots](https://www.retrogames-maniacs.com/games/commodore-64/1988/ace-software/soldier-of-light/), 20 November 2026.
