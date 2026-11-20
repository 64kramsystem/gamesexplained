# Orientation

The input is the Airwolf-Team +7 release from [CSDb release 42330](https://csdb.dk/release/?id=42330). The 35-track D64 bears disk name DISK 32, ID 01, and SHA-256 e64fb83fe98ecc96e01d9ef0d62b0bc6f28a5eddd637e396ea8dd7ce48fe049e. Its packed program SUPER CARS+7/AWT has 44,571 payload bytes starting at $0801. The disk also has a scratched directory entry and eight allocated sectors without a live file.

## Boot recipe

1. Start VICE MCP v3.14.0 arm64 headless with dummy audio on the assigned port. Hard-reset and autostart SUPER CARS+7/AWT from work/super-cars.d64. Wait for the Airwolf text screen. Hold Space for 30 frames and advance 100 frames to reach the helicopter intro.
2. Stop before the intro joystick read at $082B. Its fire test at $0831 is followed by two NOPs and a jump back into the loop. Set PC to the loader's continuation at $0838.
3. Wait for the trainer. Leave its £20,000 default and press Return. Answer N to the seven race options, including race music. Answer Y to the contact prompt. The path at $46A5 takes Y to the game. N reaches a RAM-clear and reset path.
4. Arm an execute checkpoint at $0400 before the last answer. Save work/entry.vsf at $0400 with initial bytes 78 AD 11 D0 29 6F. This is the copied game launcher. Save snapshots without ROMs.
5. Disable warp, remove the stop and advance 120 frames. Save work/title.vsf at the name prompt. Enter S, A, V and Return through the key matrix, each held for seven frames with seven frames released between keys. Save work/menu.vsf.
6. On joystick port 2 hold left for 20 frames, release for three frames and hold fire for ten frames. Release and advance 95 frames to save work/play-round1.vsf during the starting sequence. The HUD shows position 4/4, lap 0/5, speed and four condition bars. Advance another 110 frames with no inputs for work/race-steady.vsf. An execute checkpoint at $2170 confirms active control processing there.

The initial BASIC stub calls $0810. Unpacking proceeds through the cracker screens and trainer. The final stage copies the launcher to $0400 and jumps to it. Comparing unique 16-byte PRG chunks every 16 bytes against both game snapshots gave scattered matches, with only five chunks at the most frequent common offset ($145C). The PRG is packed. The main code is shared between the sales offices and the first race, which rebuild display buffers in RAM. Entry preserves startup instructions and initial values and is the listing source.

In the race, $01 was $35 and the RAM IRQ vector at $FFFE was $06B6. The handler at $06B6 saves CPU state, exposes I/O and acknowledges $D019. A checkpoint there counted 45 hits over 15 frames and 75 over the next 25. A load watch at $DC00 counted 15 and 25 hits over the same windows. The KERNAL LOAD checkpoint at $FFD5 had zero hits from the initial boot through the first race. The analysed disk contains one named game payload, and all nine map and descriptor pairs are resident at hand-over. The resident code has no KERNAL disk calls and the CIA2 access at $0668 selects a VIC bank. Menu and race use the same program image, so there are no separate listing parts.

Regenerator2000 0.9.18 opened work/entry.vsf on the assigned port. The emulator check passed 56 checks. Host F1 injection failed, so use the key matrix. The later quirk probe raised a missing checkpoints field. The monitor execution-map dump and full-frame watch capture lost their connection, so the run used narrow checkpoints for live evidence.

## Reference captures

- reference/title.png shows the name prompt in the sales offices.
- reference/menu.png shows the track list, garage and current car.
- reference/race.png shows the first track and its initial HUD.
- reference/race-moving.png shows the first track after held acceleration.
