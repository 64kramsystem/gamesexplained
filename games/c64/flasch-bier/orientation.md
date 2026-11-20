# Orientation

The [c64g archive](https://legacy.c64g.com/1829-flasch-bier.c64g) contains `FLSCHBIR.T64` and an archival text note that gives the copy's origin as unknown. The image begins with `C64 tape image file`. It has one active directory entry, `FLASCHBIER`, with payload at file offset $60 and load addresses $0801–$6380 inclusive. The extracted PRG represents that same payload. The TSI disk was inspected as an alternate release and was outside the analysis.

Use VICE-MCP v3.14.0 macOS arm64 headless with dummy audio on port 23188. Hard reset, arm a stopping execute checkpoint at $0840, then autostart `work/FLSCHBIR.T64`. The BASIC stub runs SYS 2112. Save `work/entry.vsf` with ROMs omitted at $0840, remove the checkpoint and resume. Allow the title animation to reach the sprites and hold port 2 fire until the score and lives screen appears. Release fire and allow the first cave to appear. Save `work/play-round1.vsf` with ROMs omitted. The first successful run used 160 frames of fire followed by 340 frames with the stick released.

At $0840 the game begins with the NMI vector setup. The title capture had the KERNAL IRQ vector at $EA31. The first cave capture had the vector at $2727, the NMI vector at $084A and the PC at $2030. The processor port data direction and pins read $2F/$07 at that stop. regenerator2000 on port 23190 opened the hand-over snapshot and reported 65536 bytes of C64 memory.

The emulator check passed 55 checks. Host key delivery failed. The unpaced transport test and the incomplete quirks phase overlapped with an early boot attempt. The successful boot followed the checks with serial calls. Port 2 and exact instruction stops worked on this build.
