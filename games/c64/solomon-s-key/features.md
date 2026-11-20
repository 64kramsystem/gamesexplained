# Solomon's Key features

| Feature | Status | Evidence or question |
|---|---|---|
| Title and one- or two-player selection | live | The title shows the selected player count. The menu at `$0A59` toggles and accepts it. The turn swap at `$1160` is traced from the saved zero-page image. |
| Single-screen rooms, key and exit | traced | The room loader at `$14B8` populates the grids. The key path at `$1EB0` opens the exit and the exit handler at `$1D50` flags room completion. |
| Walk, duck and jump with the stick | live | A step at `$1989` and a watch on `$0410` confirm walking right. Ducking and jumping are traced from the player dispatch at `$36DC`. |
| Create or remove blocks with fire | traced | `$37CC` selects a target by stance and facing. `$3A53` animates the cast and selects the final tile from the impact table. The blocking probes at `$1C3B` and the upward hit path at `$3ADD` use separate remaps. |
| Fireball stock and Commodore action | traced | Keyboard mapping at `$19B7` selects logical bit 5 from the Commodore key. `$3877` allocates a shot and `$2293` removes a stock entry. |
| Monsters, overlap and death | traced | Actor handlers use the dispatch at `$2900`. `$21CE` checks frame-dependent hit boxes. `$37AE` and `$3B50` start and complete death. Enemies are visible in Round 1. |
| Buried and invisible items, fairies, points and lives | traced | The cell renderer translates encoded items through `$2600`. The tile action table dispatches score and life pickups, and `$2220` handles fairy contact. |
| Score, time and HUD | live | The Round 1 display shows the stocked icons and counter strips. A timer fixture confirms BCD subtraction and the paused-death case. Counts from Round 1 are in `facts.md`. |
| High-score name entry | traced | `$0F94` accepts the selected glyph from `$10A8`. Delete and finish use separate codes. `$10ED` sorts the resulting rows. |
| Alternate key and secret rooms | confirmed | The alternate key is stored as `$31` in four authored rooms. Targeted stops confirm the spell remap and the separate two-slot increment. The displayed room labels and the conditions are in `facts.md`. |
| Music and sound effects | traced | The fourth raster phase calls both SID drivers. The tune and effect directories start at `$C720` and `$CC2A`. |
| Built-in room editor | confirmed | The original score-name comparison accepts `ASSISTANCE` in the fixture. The gate at `$3C03` also checks logical bit 7. The normal score-entry route was not exercised. |

## Sources

- [Solomon's Key — C64-Wiki](https://www.c64-wiki.com/wiki/Solomon%27s_Key), consulted 20 November 2026.
- [Solomon's Key — Documentation](https://www.lemon64.com/doc/solomons-key/1232), consulted 20 November 2026. Lemon64 identifies the C64 release as U.S. Gold, 1987, and lists both player modes.
- Title and Round 1 screenshots from the Scouse Cracking Group disk in VICE.
