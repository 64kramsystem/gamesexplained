# 720° features

| Feature | Status | Evidence |
|---|---|---|
| Title and seven ranked scores | confirmed | Title capture. $0F25 draws the table, $0BCD shifts entries for a new score and $0C58 edits the eight-glyph name. |
| Port 2 fire starts the game | confirmed | In the title, $0E5A loops until bit 4 of $DC00 clears. Holding fire for 18 frames reached the opening city viewport. |
| Skate City and overview map | confirmed | $3848 renders a 19-row window into the shared tile map. The opening screenshot shows the map markers. $0A1F copies the overview grids at $3B85 and $3D01 and waits for fire. |
| Steering and jumping | confirmed | $310C converts eight direction combinations into facings. A live step at $30C1 with fire clear and held distinguished the steering branch from the airborne store at $30D4. |
| Cash, score, tickets and equipment | confirmed | $155D awarded a ticket at the first score milestone, capped tickets at four and advanced the next threshold. $2E11 accepted an exact cash balance and refused a balance one unit short. |
| Time pressure and chasing actor | traced | $15CC activates the warning and chaser when the city timer expires. $2839 heads toward the skater and requests the end of the session on contact. |
| Park access and repeat limits | confirmed | Controlled single-instruction traces of $1C9B with tile $CA and one ticket reached each of the four park routines. The visit bytes at $3EA4–$3EA7 guard repeat entries in a round. |
| Downhill | traced | $1F51 uses the park timer at $3E8C, a section counter and finish tile $CC. |
| Jump | traced | $1D14 uses the separate clock at $3EAC and the medal gauge increment at $20C3. The clock's mask and decimal decrement were checked at $21D8. |
| Ramp | traced | $220B runs $2300 to process the drop and checks heading and manoeuvre value on landing. |
| Slalom | confirmed | A store watchpoint caught $24D0 changing a nearby $D1 gate tile to $D2 and the next two instructions adding two gauge units. The control case with no $D3 trigger left both values alone. |
| Pause and music toggle | confirmed | Matrix inputs at $2CB2 showed SPACE entering the pause path and C changing the music flag. P and X returned without either action in the same controlled test. |
| Palette and exit shortcuts | open | The matrix handler at $2CB2 has a sound toggle and pause path. At that poll, C toggled sound and X returned without taking either path. A separate handler has not been established. |
| SID music and sound effects | traced | $C000 selects a cue and $C003 updates it. $09FC directly drives the impact tone. The register census and the two groups of track pointers identify the player. |

## Sources

- European Commodore 64 release, catalog and credits, read 20 November 2026. [Lemon64](https://www.lemon64.com/game/720-degrees)
- U.S. Gold cassette inlay, indexed excerpt read 20 November 2026. [720° instructions](https://www.lemon64.com/doc/720-degrees/1373)
- Analysed C64 Comics Group release. [CSDb](https://csdb.dk/release/?id=31075)
- Snapshots captured from the analysed build. [Title](reference/title.png) and [Skate City](reference/skate-city.png).
