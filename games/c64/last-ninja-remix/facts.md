# Last Ninja Remix — checked facts

- **Boot (live):** first I-TAL disk reaches TSM intro; port 1 fire exits it. Space exits the I+T intro. F7 at the trainer starts the game with unlimited lives and unlimited power both NO. After the Central Park presentation, Space loads the level, and port 2 fire at the credits starts active play. The screenshot is `reference/central-park.png`.
- **Initialized machine (live):** gameplay processor port `$35`, DDR `$2F`; IRQ `$0314=$1E06`, NMI `$0318=$1582`. CIA2 port `$C7` selects VIC bank `$0000`; bitmap mode with `$D018=$19` selects screen `$0400` and bitmap `$2000`.
- **Composition differs (byte comparison):** of 15,889 imported code bytes, 288 differ in the gameplay snapshot: 286 in `$0E00–$0F2B`, one at `$1F5B`, and one at `$8A0F`. Of 45,809 imported data bytes, 4,247 differ. Source bytes therefore come from gameplay, never the composition.
- **Overwritten startup (live trace):** a store checkpoint over `$0E00–$0FFF` fires during movement after four frames, immediately after `$BF02` stores through pointer `$04/$05`. Tracing `$BEC1` reads eight sprite bases from `$169D/$16A5`: `$0C00,$0C40,…,$0DC0`; flag bit 0 adds `$0200`, selecting the other bank. `$BED7/$BEF8` copies decoded sprite masks there. Thus `$0C00–$0FFF` is runtime sprite output in play, including the composition’s former `$0E00` startup code. Stale startup annotations and code typing are removed.

## Verification work

Scenery format, sprite packing, animation, combat, object records and music remain imported leads. Their previous checks do not verify them here. Later disk loads are out of this declared Central Park scope and remain open under the interim policy in RFC #124.
