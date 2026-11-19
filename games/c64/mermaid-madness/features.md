# Features

| Feature | Status | Evidence |
|---|---|---|
| Title, credits, fire to start, promenade sequence with Myrtle and Gordon | live | Title and promenade captures. |
| Port 2 directions swim in four directions. Fire handles objects and stout. | confirmed | Right was stepped from the CIA1 read to the X write. Fire was stepped through the drop path. Stout is traced at `$5101`. |
| Space toggles sound during play. Music changes with location. | confirmed | Space stepped through the toggle write at `$43CC`. The location-dependent requests are traced at `$4765` and `$477D`. |
| Adjacent screens form a 4 × 8 map. Some passages require opening. | traced | Map geometry at `$5592` and passage changes at `$5B36`. Several rooms were observed while swimming. |
| Screen visits and puzzle actions advance the percentage score. High score appears below it and the held object appears underneath. | traced | Visit awards at `$559E`, score rendering at `$4FA1`, held-item label at `$52A3`. |
| Gordon's air runs down and can end the game. | confirmed | Stepped through air exhaustion at `$5228`. |
| Myrtle's heart pulses faster near Gordon and breaks on death. | traced | Position-indexed delay table at `$5C38`; end animation at `$53A2`. The table follows room position. |
| Stout gauge measures energy. Sea creatures drain it and bottles replenish it. Bottle placement can vary. | traced | `$52EF`, `$533C`, `$5101` and the randomized bitset at `$5080`. |
| Carry one item and drop it in rooms with space. Similar objects can have distinct effects. | confirmed | The item count and drop traced through `$523C–$529C`. The three dynamite records have different target rooms. |
| Lantern lights a dark cavern. Dynamite detonates after a delay, opens a passage and is lethal while Myrtle remains there. | confirmed | Lantern lighting and blast damage verified with branch-specific emulator fixtures. Passage edits are traced at `$5B36`. |
| Ankh, chest, tire and other objects solve location-specific obstacles. A ship ghost is lethal and can be removed with the chest. | open | C64 walkthrough. |
| Rescue sequence, ending, retry and high-score persistence | traced | Rescue at `$514A`, ending sentinel at `$51B7`, restart at `$539E`, high-score retention at `$C047`. |

## Sources

- [Mermaid Madness – C64-Wiki](https://www.c64-wiki.de/wiki/Mermaid_Madness), read 19 November 2026.
- [Mermaid Madness Guide and Walkthrough for Commodore 64](https://gamefaqs.gamespot.com/c64/576408-mermaid-madness/faqs/55153), read 19 November 2026. The reproduced manual section uses Spectrum control names. The C64 control descriptions are from the walkthrough itself.
- VICE captures in `reference/` are from the Kurt disk variant.
- The C64-Wiki title image is included as `reference/wiki-title.png`. The Remember entry carries a separate instruction screen that describes the objective and the stout supply.
