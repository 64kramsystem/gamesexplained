# Terramex features

| Feature | Evidence | Status |
|---|---|---|
| Choose one of five explorers | The pointing hand's hit regions are tested at selector `$5A00` and validated at `$59C5`. Port-2 up entered the movement path 24 times, and a valid fire reached the `MAIN` disk load. | confirmed |
| Start the expedition | The title says “Fire Starts Game”. Fire polling at main `$A0CF` exits the title and the opening desert was observed. | confirmed |
| Horizontal movement | The title lists Z/X. A port-2 right probe reached main `$CC7A` and wrote the player X coordinate 11 times in 11 game passes. The idle control produced zero stores. | confirmed |
| Climb or move vertically | Main `$CCDF` and `$CCFC` examine down and up and consult terrain before accepting a move. The opening desert position provides the movement control snapshot. A climbable location was outside the measured cases. | traced |
| Leap | The title lists Space. Port-2 fire reached the action entry at main `$CC53` and ran the leap handler at `$DB0D`. | confirmed |
| Think | The title lists T. Main `$DE47` requests action `$0A` and the action handler at `$D842` selects the scene-dependent response. | traced |
| Swap and scroll items | The title lists S and 1/2. Main `$BCDD`/ `$BD2D` drive the exchange and inventory navigation. `$9505` draws the scrolled window and held item. A gameplay probe observed 33 palette reads through `$9526` and 33 corresponding VIC colour stores at `$9529`. | traced |
| Collect objects by walking onto them | The instructions describe proximity pickup. The main proximity handler at `$BEA9` finds a free inventory slot and processes the pickup's ID. | traced |
| Item puzzles | The instructions say items found or supplied by an explorer solve obstacles and help the professor. Scene-specific tests begin at main `$BB1B` and compare held IDs. Exact item names and puzzle outcomes remain open for many IDs. | traced |
| Status panel | The expedition screenshot shows score, high score, day and time, and portraits. Main `$86D2` wrote the minute byte six times in an 11-pass probe. Main `$E43B` and `$E456` update score fields in the HUD. | confirmed |
| Title music and effects option | The legend credits Ben Daglish and shows a mode indicator. Main `$A095–$A0CC` update the status label, and instruction checkpoints verify the title's voice event decoder and SID stores run. | confirmed |
| Hazards and companions | The instructions mention dangerous animals, acid rain and other hazards. The engine dispatches general actors at main `$C45F` and scene-specific ones at `$BB1B`. The one-to-one mapping to documented creatures and loss conditions is open. | traced |
| Find Professor Eyestrain and prevent an asteroid impact | The manual supplies this objective. At main `$B87F` a successful matching item transfer increments a count and the sixth invokes `$B9BE`. The broader ending route and its conditions remain open. | open |
| Request for the other side | A side-2 message exists at main `$A273` and is selected by `$A2E8`. The RCS/HCC load entered the expedition with two files on one side. The prompt's reachable conditions in this release are open. | open |

## Sources

- [Terramex on Lemon64](https://www.lemon64.com/game/terramex), consulted 19 November 2026.
- [Zafiro Terramex instructions](https://spa2.speccy.org/Instructions/t/Terramex%28Zafiro%29.pdf), consulted 19 November 2026.
- C64 title, portrait and gameplay screens in `reference/`, captured from the RCS/HCC disk.
