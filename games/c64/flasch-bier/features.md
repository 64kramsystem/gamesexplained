# Features

The [64'er review](https://www.winz.run/c64/games/testberichte/C64_Testbericht_Werner.pdf) documents the bottle objective, falling rocks, enemies, the timer and lives. The [C64 longplay](https://www.youtube.com/watch?v=Q_wHggsT9mc) shows the animated title and played caves. The emulator captures in `reference/` show the analysed tape copy.

| Feature | Status | Evidence |
|---|---|---|
| Animated Werner Soft and FlaschBier title | live | `reference/title.png` and title animation observed in VICE |
| Start with port 2 fire | confirmed | Title tests CIA port A bit 4 at $5AB4–$5ABB. Holding fire reached the score interlude and first cave. |
| Single-screen rock and dirt caves | live | `reference/round-1.png` |
| Reach the bottle | confirmed | The controlled adjacency test reached $2602 and copied the following cave. |
| Falling rocks and enemy contact cost a life | confirmed | Both contact fixtures stop at $2308. The life-loss continuation is $26EB. |
| Time limit | confirmed | A step at $2739 decremented the time byte. The main loop tests it for zero at $25F5. |
| Score and lives interlude | live | `reference/score-lives.png` |
| Title and game sound | traced | Both SID pitch sequences and effect writes are traced. The gameplay pitch table read was stepped in VICE. Dummy audio was used. |
