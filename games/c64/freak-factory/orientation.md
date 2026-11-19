# Orientation

Freak Factory, Firebird, 1986. The analysed image is the [Doughnut Cracking Service release](https://csdb.dk/release/?id=23733). Keep the downloaded container as `work/freak.t64`. Its header starts with `C64 tape image file`, with one occupied directory entry named `FREAK-FACT/DCS`. The payload starts at file offset $60 and loads at $0801. The extracted payload, with its two-byte PRG load address restored, is `work/FREAK-FACT-DCS.prg`.

1. Cold reset PAL x64sc and autostart the T64. Wait for the brick wall, scrolling caption and EXIT sign. This is the DCS intro.
2. Hold port 2 left until the agent reaches the exit and the lift appears. Release the stick.
3. Let the lift arrive. Save `work/play-round1.vsf` on the two-floor room with an energy bar and the stationary agent. The active KERNAL IRQ vector at $0314 was $C01C in this snapshot, and the underlying RAM word at $FFFE was $4000, beneath the visible KERNAL.
4. For `work/entry.vsf`, arm a stopping execute checkpoint at $4000 after the intro appears and before walking left. Save on the first hit, with PC=$4000. The KERNAL IRQ vector was $CC91 in the intro. The entry instruction disables interrupts before replacing the intro's handler. Use the entry image to preserve bytes the game modifies during startup.

The wrapper starts with a BASIC SYS 2064 and relocates the program and its own intro. The intro samples port 2 at $C9D1. Execute checkpoints at $CA82 and $4000 each counted one hit on exit. Across 16-byte payload chunks, there is no single relocation offset that accounts for the whole file. The payload includes code and graphics in packed or rearranged form. The play snapshot changes large parts of $0400–$07FF and $3800–$3FFF during startup. The boot payload is the only entry on the selected tape.

VICE v3.14.0 macOS arm64 headless ran on port 17400 with dummy audio. The emulator probe passed 56 checks, including instruction stops, memory watchpoints, frame stepping and snapshots. Host key names failed, and the final quirks phase ended with a missing checkpoint-list field. Instruction and joystick checks passed on this build. Regenerator2000 answers on port 17402.

The observed laboratory transitions swap graphics in RAM and dispatch code already resident at $8000. The five selections share this image. The listing uses `work/entry.vsf` and does not require part folders.
