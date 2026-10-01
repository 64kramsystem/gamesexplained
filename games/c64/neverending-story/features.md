# The NeverEnding Story — features

Inventory: [game documentation](https://www.lemon64.com/doc/neverending-story/412), consulted 30 September 2026. Imported annotations guide searches.

| Feature | Status | Evidence or open work |
|---|---|---|
| Boot and first command prompt | live | Fresh Ocean disk boot; reference capture |
| Picture/text display | traced | $A7E3/$A80A register writes and fresh font; full rendering comparison open |
| Commands and rules | open | Dispatch patching traced; exercise parser and handler outcomes |
| Illustrated locations | live | All 21 captured records: native $05BF output matches decoded bitmap, screen and colour bytes; browser pixels independently compared |
| Objects and inventory | open | Trace and test routes through imported $0D4F/$A560 leads |
| Multipart progression | open | $03A0 exchange and $9700 loader traced; later parts need captures |
| Save/load | open | Trace release-specific dispatch and test actual disk behavior |
