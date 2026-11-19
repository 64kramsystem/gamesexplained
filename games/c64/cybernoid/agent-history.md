# Cybernoid analysis history

The archive disk autostart attempt left the PRG load area untouched. After waiting for BASIC to finish initializing, injecting the extracted PRG and setting PC to its SYS target reached the Beastie Boys intro. A clean boot with stopping checkpoints at $1900 and $0824 separated the first intro and final game handovers.

The headless build crashed during the frame recorder's frame advance. Direct execution stops let the analysis capture both handover and gameplay. Checkpoints on the three raster handlers and a store watch on the hardware IRQ vector established the interrupt chain. Holding the menu key before the release gate trapped the input test in that gate. Starting it at $8054 let it reach $2D0B and produce the first-room snapshot.

The live execute map combines the title, startup and first-room observations. Four addresses at $E5CD–$E5D4 in the startup map came from the ROM-marked monitor column while the KERNAL was still visible. The handover memory and the game's startup writes show graphics output at those addresses once the KERNAL is switched out. The working directory retains the three raw code maps and the annotation log.

The checkpoint tests required no route or replay, so step 65 did not apply. The independent sample used the specified model and remains under work/reports/sample-1848.
