# Rainbow Islands features

The C64-Wiki page was read on 20 November 2026. Its claims about later islands are leads for this disk build. [Rainbow Islands, C64-Wiki](https://www.c64-wiki.com/wiki/Rainbow_Islands)

| Feature | Status | Evidence |
|---|---|---|
| Attract screens show credits, high score and the title | live | Title screen and Rainbow Project credits captured in VICE |
| F7 adds a credit and F1 starts one player | confirmed | F7 increments the attract count at $4156. F1 then started Round 1 through the separate selection screen. |
| F3 selects alternating two-player play | open | C64-Wiki |
| Run/Stop pauses or unpauses, and Clear/Home ends a paused game | open | C64-Wiki |
| Stick movement, jump and rainbow cast | confirmed | Right changed X in the comparison run. Up reached the phase and velocity stores at $746F and $748B, and fire reached the allocation decrement at $7D02. |
| Gameplay controller accepts either joystick port | confirmed | $4BC4 and $4BC7 combine the ports. Instruction stepping produced identical right-plus-fire results on both. |
| Rainbows serve as platforms and weapons | open | C64-Wiki |
| The playfield scrolls vertically toward the goal | traced | $F805 issues a row change to the scrolling update at $8148. The time and goal transitions remain open. |
| Seven island resource pairs and four rounds per island | traced | $62DA advances the island every four rounds. All seven pairs loaded through the tested resident loader. |
| Island bosses and their defeat conditions | open | C64-Wiki |
| A hurry warning precedes rising water | open | C64-Wiki |
| Shoes raise speed, red potions increase the rainbow count to three and yellow potions speed up casts | open | C64-Wiki |
| The way an enemy dies affects its drop | open | C64-Wiki |
| Small diamond colour depends on horizontal position | open | C64-Wiki |
| All seven colours yield a large diamond, collection order can open a room, and large diamonds affect the ending | open | C64-Wiki |
| Stars kill enemies, and rainbows reveal and collect items | open | C64-Wiki |
| Credits can be spent to continue | open | C64-Wiki |
| Lives and score appear in the play display | confirmed | Round 1 screenshot, packed score adder at $4D14 and life glyph writer at $8537. |
| Ending shows a congratulations page and treasure | live | Ending snapshot after the $0810 handover. |
