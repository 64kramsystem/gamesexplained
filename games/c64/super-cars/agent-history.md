# Super Cars agent history

The available VICE was already a v3.14.0 macOS arm64 headless build on the assigned ports. Its worktree wrapper supplied the dummy audio option. The emulator preflight counted 56 passes and two failures. The failures concerned host-key delivery and a missing checkpoint-list field late in the quirks probe.

The Airwolf intro advanced into a loop with the fire branch replaced by NOPs. A breakpoint on the joystick read showed why it stayed there. Setting PC to $0838 allowed the trainer to run without modifying the executable bytes. The final contact question uses Y to continue. The N branch led to a sample routine then hit the reset trampoline at $0400. The hand-over capture follows the Y path.

Typing into the KERNAL buffer during the game's name screen led to a black display. Restoring the name screen and using matrix keys reached the menu. Native monitor execution-map export and the frame-capture client lost their VICE connections. Restoring the race snapshot and taking narrower MCP checkpoints worked. The local kit census and string sweeps are in work/census.txt and work/strings.txt. The annotation scripts and all raw captures stay under work/.

A local comparison with the Silicon release established that its main image shares the compact hexadecimal font at $8008 but omits the Airwolf reset shim at $6E9F and the contact sample player at $80A4. The comparison snapshots and images stay in work/. The Airwolf image remains the listing source.
