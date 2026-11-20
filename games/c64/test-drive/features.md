# Test Drive features

## Sources

- [Accolade's Test Drive manual](https://www.retrogames.cz/manualy/DOS/Test_Drive_-_Manual.pdf), read 20 November 2026. The loading and control sections identify the C64-specific instructions.
- [Test Drive — C64-Wiki](https://www.c64-wiki.com/wiki/Test_Drive), read 20 November 2026. The directions given for car selection differ from the manual.

| Feature | Status | What to check |
|---|---|---|
| Title and car selection | traced | VICE showed the title, attract scores and side B Lotus screen. The selector reads CIA1 port A and wraps the selection within five entries. The direction mapping still needs an input trace. |
| Five cars | traced | The Lotus Esprit Turbo, Lamborghini Countach, Porsche 911 Turbo and Ferrari Testarossa use needle sprites. The Chevrolet Corvette uses rising or widening bars and numeric glyphs. Each cockpit supplies its own driving parameter pointers. A complete performance comparison remains open. |
| Driving controls | traced | A trace of port 2 with up and fire held reached the store of gear 1 at $8EF4. Throttle, braking, steering and the alternate shift pattern still need separate traces. |
| Dashboard | traced | Gauge updates read road speed at $41 and engine speed at $42. The Corvette sprite table reads and other cars’ needle endpoint reads have VICE watchpoint evidence. The visibility conditions for the shifter remain open. |
| Keyboard controls | traced | Store watchpoints verified the dispatch for D, V, M, S, P and O. The end-of-drive key codes at $6D7B–$6D85 are traced. Their keyboard-matrix mappings remain open. |
| Mountain road | open | Locate the curves, cliff and ravine boundaries, potholes, slicks and traffic. Check whether traffic follows fixed placements. |
| Radar and police | open | Check warning LEDs, beeps, the speed measurement point, pursuit, forced stops and what happens after colliding with a patrol car. |
| Crashes and retries | open | The manual gives five chances and says to press fire after a mishap. Check chance accounting and restart state. |
| Stages and interludes | traced | The driving engine loads R1 through R5 according to $52, and calls GS through its road-completion path. Controlled loads captured all five stages. The scoring formulas remain open. |
| Music and effects | open | Identify which states play music and what produces the engine and radar sounds. |
