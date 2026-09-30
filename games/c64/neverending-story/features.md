# The NeverEnding Story — features

Sources: [game documentation](https://www.lemon64.com/doc/neverending-story/412) and the contributor’s annotated listing, consulted 30 September 2026. The documentation supplies the feature inventory; technical status comes from the listing.

| Feature | Status | Evidence or open work |
|---|---|---|
| Text commands and adventure rules | traced | $122F parser, $0DE3 actions, $1193 conditions |
| Illustrated locations | traced | $05BF; 21 captured pictures rendered on the page |
| Objects and inventory | traced | $0D4F room table and $A560 icon storage |
| Multipart progression | open | Runtime loader is present; PART2/PART3 content is outside the capture |
| Save/load behavior | open | Release-specific handlers require live round-trip verification |

“Traced” means supported by the imported analysis. It does not imply a fresh live replay in this publication pass. Scope exclusions are described in `orientation.md`.
