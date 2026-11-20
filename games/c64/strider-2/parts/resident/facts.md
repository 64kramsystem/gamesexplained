# Resident engine and title

- `$8000` configures raster interrupts and ports. Its first instruction's operand at `$8001` is mutable. The stage transition uses the value at `$FF` to construct the next disk name.
- `$9389` and `$9680` are two handlers observed in the hardware IRQ vector during the captured forest frame. The latter uses the current logical sprite index in `$13` modulo eight to select a VIC slot, rewrites coordinates and sprite pointers, and arranges another interrupt or returns to the normal split.
- `$851D` subtracts one across three packed decimal bytes at `$89–$8B`. `$8532` clears decimal mode and sets `$64` when the result is zero. The status panel shows time during forest play. The initial timer bytes are set by $80A0–$80B5. The normal timing measurement is below.
- At the serial read call at `$CC66`, the CPU port read `$37`. Single-stepping the JSR entered `$EE13`. CPU-view bytes there matched the KERNAL ROM and differed from RAM beneath it. The resident listing classifies the RAM bytes there as part of the sprite storage.
- At `$8334`, stepping the input read traversed `$862F`, `$8631`, `$8634` and `$8637`, returning to `$8337` with A = `$FF` idle, `$F7` for right and `$FE` for up on port 2. The input latch uses active-low joystick bits. This trace establishes the sampled values, while the subsequent player behavior is still being annotated.
- The selected object animation in `$0538` indexes the pointer table at `$C6AA/$C6AB`. Frame index `$0460` selects a four-byte header. The builder reads the parts through a patched operand. Each part has a colour, sprite pointer, signed horizontal displacement and vertical displacement. It mirrors the horizontal displacement according to facing when building the logical sprite queue.


## Live tests

- **Timer.** From the forest play snapshot, 120 advanced PAL frames hit the primary IRQ at `$9389` 120 times and the timer guard at `$8532` 14 times. The subtract routine at `$851D` and the store watch at `$89` also counted 14. Packed decimal time changed from 003846 to 003832.
- **Fire.** Three 12-frame trials started from the same snapshot. Idle reached the port 2 reader three times and neither attack entry. Fire alone reached the projectile activation at `$A1C2` once and never the sword enable at `$BF53`. Right plus fire reached the sword enable once and never the projectile activation. The port reader counted four times in the latter trial.
- **RUN/STOP.** With the matrix key released, the test at `$8572` reached the return at `$8585`. Holding row 7, column 7 reached the wait at `$8574` with X = `$7F`. Releasing the key reached the transition at `$843D` with file pattern `A*`. This is the X-Ray release's stage skip.

The checks used execution breakpoints and a store watch. The original scripts and results are kept in ignored `work/`.
