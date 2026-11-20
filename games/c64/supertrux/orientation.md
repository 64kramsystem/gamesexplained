# Supertrux — orientation

## Image and tools

The analysis uses the Elite C64 tape archived as `Supertrux (1989)(Elite).tap` at [Planet Emulation](https://www.planetemu.net/en/rom/commodore-c64-games-racing-tap/supertrux-1989-elite). The header is `C64-TAPE-RAW`, version 0, with 712,798 pulse bytes. SHA-256 is recorded in `media.json`. The preliminary Action disk boot was discarded in favor of this tape.

VICE v3.14.0 macOS arm64 headless, C64SC in PAL mode, with dummy audio. The emulator check reported 56 passes, with failures in `keys-host` and `no-exception`. The host key F1 did not arrive. Matrix F1, joystick port 2, precise stopping checkpoints, watchpoints, frame stepping, and snapshot restore passed. The final quirks probe raised a missing `checkpoints` response. Regenerator2000 reads the raw C64 RAM from the entry snapshot.

## Rebuild the snapshots

1. Hard reset, let BASIC start, and autostart the TAP. Leave warp on while the tape plays. The Elite loading picture appears with changing border stripes.
2. Arm a stopping execution checkpoint at `$080D` once the loading picture is on screen. Wait for it to fire. The PC is `$080D`, and the jump there enters `$1461`. Save without ROMs or media as `work/entry.vsf`. The listing uses this image because the title and race replace parts of the loaded image.
3. Continue past the checkpoint, turn warp off, and run 120 PAL frames to the map and title. Save `work/title.vsf`.
4. From that state hold port 2 fire for 25 frames, release it, and run another 60 frames. The screen shows the London start gantry with the player truck and the race HUD. Save `work/play-round1.vsf`.

The loader hands over with the KERNAL software IRQ vector at `$EA31`. In play the hardware IRQ vector points to `$0B7F`, which had 20 execution-checkpoint hits in five video frames. The CPU port read back `$25` with direction register `$2F`, which exposes I/O while the CPU reads RAM at the BASIC and KERNAL addresses.

## Tape blocks and their RAM destinations

The offsets below were found by matching unique 16-byte pieces and checking the resulting full ranges against the emulator snapshots.

| Tape item | Destination and evidence |
|---|---|
| KERNAL file `SUPERTRUX` | `$02A7`. 348 of 512 extracted bytes match during loading and at handoff. |
| First `NOVA` | `$1293`. 173 of 177 bytes match during loading. |
| Second `NOVA` | `$0400`. 207 of 208 bytes match during loading and at handoff. |
| `1` | `$0C00–$0FFF`. 1,024 of 1,024 bytes match during loading. |
| `2` | `$2000–$3FFF`. 8,192 of 8,192 bytes match during loading. |
| `3` | Loads at `$4000`. The loader copies it in full to RAM under I/O at `$D000–$DFFF`. All 4,096 bytes match there at handoff. |
| `4` | `$4000–$CFFF`. 36,864 of 36,864 bytes match at handoff. |
| `5` | `$E000–$FEFF`. 7,936 of 7,936 bytes match at handoff. |
| `6` | `$1000–$1FFF`. 4,096 of 4,096 bytes match at handoff. |
| `7` | `$0800–$0FFF`. 2,048 of 2,048 bytes match at handoff, including the entry jump. |
| `8` | `$2000–$3FFF`. 8,192 of 8,192 bytes match at handoff. |

The loader at `$0400` calls `LOAD` with the eight single-character names in order. It selects bitmap mode after the first two blocks. It moves block 3 under I/O before block 4 reuses the original space, blanks the display before blocks 7 and 8, and jumps to `$080D` after the last call returns. The tape presents one loading sequence before the title and race.

The ten pulse ranges the tape scanner reports between or after the turbo blocks each start with the previous block checksum shifted left in successive bytes. Each has a run of at least 1,975 short pilot pulses. The boot chain names the numbered loads and the game listing has no direct or indexed reference to the KERNAL LOAD entry. Title, start and running play use the same resident program, with generated screen and glyph buffers.
