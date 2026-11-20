# 720° orientation

The European C64 game by Chris Butler, from the C64 Comics Group release. The downloaded `work/comics.t64` has a C64S tape archive header. Its sole live directory entry is a PRG named 720, with payload at file offset $0400 and load addresses $0801–$BBA6. The kit has no T64 reader. The media ledger tracks the extracted `work/720-comics.prg`, consisting of the two-byte load address followed by that payload.

1. Cold start headless PAL x64sc v3.14.0 with dummy audio and autostart `work/comics.t64`. Wait for the C64 Comics Group intro. A trial reached the intro after approximately 6–15 seconds.
2. The intro writes zero to CIA1 port A at $1A9E and waits for a value other than $FF on port B at $1AA1. To exit reproducibly, set a stopping breakpoint at $1AA1, hold SPACE through the matrix, remove the breakpoint and step through $1AA1, $1AA4, $1AA5 and $1AAD. This enters the release's next unpacking stage at $3800. Release SPACE and resume.
3. The stage at $3800 eventually enters a final unpacker at $0811. Arm a breakpoint at $0850 after reaching $0811. The final unpacker jumps there from $011A, with the game decompressed. Save this handover as `work/entry.vsf`. At the breakpoint the 6510 port is $37. This is the listing source.
4. Resume until the title is visible and the CPU is waiting at $0E5A–$0E5F. Save `work/title.vsf`. Turn warp off. Hold port 2 fire and run 18 frames. Release fire, then save `work/play-first.vsf` showing the player at the opening Skate City map markers.
5. At the city snapshot the CPU is at $3915 and the banking bits are $05. The hardware NMI vector is $3A3A and the IRQ vector is $3A3B. The IRQ saves A, X and Y to $02–$04 and dispatches through $12–$13, which held $3A47. $0314 still held the KERNAL default $EA31, which the game bypasses with its hardware vector.

The loader unpacks the crack intro and later runs another depacker after the player exits it. The last stage at $0811 relocates itself into page one, expands the game from its packed RAM stream, restores the CPU port and jumps to $0850. The tape PRG therefore contains packed game bytes. It does not map into the game at a single offset. The captured game uses RAM beneath ROM, and the analysis uses the handover image to preserve initial bytes when play overwrites them.

The emulator self-check passed 56 probes, including hardware watchpoints and instruction stepping. Host-key delivery failed, so the route uses the keyboard matrix. The final quirk probe stopped on a missing checkpoint-list field. Whole-frame capture on this build disconnected the emulator. The IRQ addresses above come from live RAM and instruction inspection.

The Alpha Range 89, Fantastic 4 Cracking Group and The Goonies files were boot candidates. The analysed snapshots come from the C64 Comics Group file.

## Resident parts

This release has one resident game image. The shared tile map includes the city and the courses. Each park is entered through a branch from $1C9B into resident code, with its own entry and viewport coordinates. It does not require another media item or part folder for the captured release.
