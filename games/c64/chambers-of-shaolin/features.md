# Features

The printed guide covers three platforms. Its general training and fighting instructions are leads for the C64 disk. References to selecting a stored fighter need a separate check against the C64 code.

| Feature | Status | What to look for |
| --- | --- | --- |
| Stick | open | Read the master's attack height and jump, duck, or change distance before the blow. |
| Agility | open | Avoid moving hazards and collect yin-yang symbols to recover power. Up triggers a flic-flac, while fire modifies the stick for jumping and ducking. |
| Balance | live | Disk file 1 opened the Balance chamber. Live play showed four poles, a time counter and a sign counter. The manual describes collecting ten signs and restarting after a fall. |
| Speed | live | Disk file 2 displayed the Speed instructions and a playable chamber with the suspended ball. The kick and water rules still need instruction tracing. |
| Strength | live | Disk file 3 displayed the Strength instructions and the playable board chamber with a hand panel. The aiming and alternating-stick rules remain to be traced. |
| Fire | open | Use a low sweeping kick to drive away burning baskets on a bridge. |
| Combat | live | Disk file 4 displayed the combat introduction and two fighters in the mountain arena. The route from training and the effect of training scores still need instruction traces. |
| End sequence | open | The guide mentions another test after beating four opponents. Its presence on the C64 remains open. |
| Character storage | open | The guide describes a separate character disk. Look for C64 character loading and saving independently of high scores. |
| Score table | confirmed | The score screen requested H at $FFD5 and displayed five records. Fire led to LOAD for LABLE. The score-save call uses the replacement name @:H. |
| Music and sound effects | open | Check the title, training and combat independently for music and sound effects. |

## Sources

- [Chambers of Shaolin printed manual](https://db.hfsplay.fr/files/2018/10/06/cefaf35f-cfde-419b-a20d-cf990ade2c95.pdf), consulted 20 November 2026. The English training and combat instructions are on pp. 6–15.
- [Overdrive release record](https://csdb.dk/release/?id=241287), consulted 20 November 2026.
- [Chambers of Shaolin – C64-Wiki](https://www.c64-wiki.de/wiki/Chambers_of_Shaolin), consulted 20 November 2026. Its C64 description lists Balance, Speed and Strength. The other chambers in the multi-platform manual remain open until the load paths and relevant code are checked.
