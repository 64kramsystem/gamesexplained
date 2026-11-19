# Wonder Boy features

Sources read on 19 November 2026.

- [Wonder Boy, C64-Wiki](https://www.c64-wiki.com/wiki/Wonder_Boy). Gameplay and boss animations in reference/ come from this page.
- [Wonder Boy, Lemon64](https://www.lemon64.com/game/wonderboy). Credits and release identification.
- The instructions bundled with the Remember disk, seen after pressing fire at its intro.
- [Manual transcription](https://www.c64x.no/games/wonderboy_manual.php). The controls in this transcription describe the Spectrum version. Use the C64 sources for controls.

| Feature | Status | Evidence or question |
|---|---|---|
| Rescue Tina across seven territories | traced, ending open | The area mask wraps to $80 after Area 7 at $0C8B. The instruction trace reaches the exit branch at $0C8F. The display path it enters has not been traced through the ending presentation. |
| Four rounds per territory, four signposts per round | traced | The round counter wraps at $0C85. Four world-X entries per round begin at $0C2D. The restart scan at $0BDC selects the greatest entry at or below the player X, checked by instruction tracing in all four rounds. |
| Woods, waterfront, caves, and mixed terrain | traced | Row pointers at `$1EC1` and character streams at `$AB17`. Opening forest observed live. |
| One or two players, music toggle, pause | live and traced | F1 starts play live. The title at $F737 stores mode 0 for one player or 1 for two. Music toggle at $09DE and pause at $3D00 are traced. |
| Walk, run, jump and throw | traced | Matrix and port-2 joystick at `$24F3`, movement at `$29B6`, axe at `$2D2C`. Jump and fire edges confirmed by instruction checkpoints. |
| Vitality drains with time, food replenishes it | live and traced | Drain and exhaustion confirmed live at $F38D. The meter is at $F33C. The overlap path at $334F fills the meter. The food variant at $309B changes actor state. Individual food values remain open. |
| Rocks, fire, pits and moving platforms | open | The terrain probes at $254D–$2662 classify tile codes and the actor table at $35EA selects separate contact handlers. The mapping from individual screen shapes to these outcomes remains open. |
| Snail, snake, wasp, blue runner, spider, frogs, bat and squid | open | The dispatch table at $35EA groups enemies by type and the renderer reads shapes from $BCB2. Matching each named enemy to its types and variants remains open. |
| Break eggs by kicking or shooting | traced | The handler at $2F61 checks axe contact and player overlap. The initializer at $2FBB reads the contents type and substitutes type $3D for $72 or $6B without the axe. The full contents-to-shape mapping remains open. |
| Axe, skateboard, mushroom, guardian and Death | traced, identities open | Axe pickup at $30C8 enables the launcher at $2D2C. The skateboard state paths include $28D8. The timer at $310B tests the guardian state before following or departing. The actor type and shape tables still need to be matched to every named variant. |
| Potion, extra life, spring, doll and clover | traced, identities open | Overlap paths at $333C, $334F, $3367 and $337B set the round item flag, refill vitality, add a life and enable protection. The item shapes and spring motion still need to be matched to their handlers. |
| Boss shots, scaling, defeated head and collectible | traced | Boss setup at $23F2 selects shot intervals and hit targets. CPU traces checked Areas 1, 2 and 7. The phase machine and shot paths run through $393A. The head and collectible artwork associations remain open. |
| HUD shows lives, axe, boss items, scores and vitality | traced | Lives at $F685, axe test at $F801, badges at $F7B6, score digits at $F2E9 and vitality at $F33C. The badge trace covered all seven area masks. |
| Round-end vitality bonus and doll multiplier | traced | The first payout at $F569 uses the bonus accrued at $F4FF. The item flag at $0660 controls whether the restored amount is paid again at $F5AB. Area 7, Round 4 adds a separate increment at $F58E. |
| Death, retry and game over | live and traced | The vitality-exhaustion watch observed outcome $0B. Actor contact can write $0C at $2EFC. The loss path decrements lives at $0A74 and branches to retry or the title path. The restart scan at $0BDC chooses the checkpoint. |
| Background music and effects | traced | Selector requests at `$E000`, tick at `$E003`, music interpreter at `$E870`. |

The bundled C64 documents also describe quitting while paused, an extra life at area completion, and score-based extra lives. The pause quit path is traced at `$3D71` and score carry at `$F661`.
