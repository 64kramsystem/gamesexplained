# Terry's Big Adventure features

## Sources

- The [C64 instruction sheet](https://www.lemon64.com/doc/terrys-big-adventure/1403) describes the controls and the goal across twelve levels. Read 19 November 2026.
- The [Lemon64 C64 release record](https://www.lemon64.com/game/terrys-big-adventure) identifies joystick port 2 and credits Gary Walton and Allister Brimble. Read 19 November 2026.

| Feature | Status | Evidence or question |
|---|---|---|
| One player, stages scroll horizontally | confirmed | $7A8B advances the pixel and map cursors. The raster code at $79F0 services the playfield matrix exchange. |
| Port 2 left and right | confirmed | The trace at $97C6 followed Right from the CIA read through the input store. $9858 updates signed momentum. |
| Up jumps | confirmed | The $9822 trace captured writes to the jump state and the Up latch. |
| Fire uses a yo-yo or throws rocks | confirmed | The $9915 trace distinguished the baseline launch from rock mode and found the single ammo decrement. |
| Hedgehogs and snails | open | Sprite frames are identifiable. Which spawn lists and collision paths belong to each creature? |
| Bridges, rivers and mushrooms | traced | Tile handler dispatch and a hazard tested at $73F3. The visual-to-tile mapping and mushroom timing remain open. |
| Twelve levels | confirmed | Fourteen map initializations were instrumented, covering the twelve regular scenes and two alternate entries. |
| Bonus and secret scenes | traced | $B374 selects the bonus transition. A substituted tile $7E triggered $B907 live. $B92C selects the secret map and $B961 restores the normal scene. |
| Extra lives and time pickups | traced | $9E33 consumes a tile and adds timer units. $9614 increments lives after five contacts with the $DB pickup. Its natural pickup locations remain open. |
| Score and timer in the playfield | confirmed | $8033 redraws score digits and $7FD4 redraws the timer digits in sprite memory. |
| Music and sound effects | traced | $CD8F and $CDD0 select and play music through three SID voices. Sound-effect selection remains open. |
