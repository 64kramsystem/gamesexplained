# Space Harrier features

| Feature | Status | Evidence |
| --- | --- | --- |
| Title screen and fire to start | confirmed | The port 2 fire prompt at $1303 reads CIA1 port A. Fire led to STAGE 01 / MOOT in VICE. |
| Move and shoot with the port 2 joystick | confirmed | Stepping $1BC1 produced the signed motion increments for all four directions. The fire path's store at $1C54 activated a player projectile slot. |
| Pause and resume | differs | The C64-Wiki lists RUN/STOP for pause. The Space matrix key produced $EF at $0952, took the pause branch and resumed after the second press and release. The manual names Space. |
| Stage intro and time, stage and score HUD | confirmed | $151A draws the stage card. $1625 prints the HUD with time, stage and score. The title and active Stage 01 captures show both initial and ticking time. |
| Apparent scaling and approach from the horizon | confirmed | $33FA selects sprite or rectangle frames by depth. The Moot capture shows both character-cell objects and hardware sprites. |
| Hit enemies and obstacles for points | traced | $1A29 tests projectile overlap. $1A0A scores destructive hits and $19E5 deflects shots and adds a smaller score. The isolated BCD carry check exercised $16E0. |
| Collision, knockdown and recovery | traced | $17A5 checks the position and recovery countdown and invokes $172A. The impact routine's life branch was tested separately. |
| Transition from training timer to ten lives | confirmed | A watch on the timer store captured $00 wrapping to $99. The HUD changes to lives at $99. The life branch preserved ten lives during training and deducted one at $99. |
| Stage-specific obstacles, waves and boss targets | traced | The stage tables at $28A4 and $291E select wave schedules and object types. Their dispatch and motion data are in the listing. The exact encounter contents beyond the observed opening remain open. |
| Twelve stage names and a loop of stage content | confirmed | The $15B0 names decode twelve stages. Starting the advance routine at label 12 and index 11 produced label 13 and index 0. |
| Main, boss and score-entry music and effects | traced | $AAB5, $B060, $B356 and $B5B1 initialize four tune groups. Active Moot wrote the SID registers. Dummy audio leaves the identification of the score-entry tune as a documented lead. |
| Game over and high-score entry | traced | $0944 tests for negative lives and routes to $0EA4. $104A, $1147 and $11AE handle qualifying entry and the scoreboard. The external screenshot shows the ranked table. |

## Sources

Read on 19 November 2026.

- [Elite Space Harrier instruction leaflet](https://idpixel.ru/games/s/spaceharrier/files/spaceharriermulti-lang.pdf). The English C64 instructions are on page 2.
- [Space Harrier on C64-Wiki](https://www.c64-wiki.com/wiki/Space_Harrier). The Amar and high-score reference images come from this page.
- Local VICE reference captures show the title and active Stage 01 in the analysed release.
