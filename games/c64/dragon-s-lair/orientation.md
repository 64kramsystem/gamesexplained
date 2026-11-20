# Dragon's Lair — orientation

Software Projects, 1986. The image used for the captures is the alternate D64 with the following SHA-256.

```text
c3a3270636a1831d9fd0dd40c89a4c5e55400452e264de1fcb0a73aaebaaca78
```

The disk is catalogued by Planet Emulation as [Dragon's Lair (1986)(Software Projects) [a]](https://www.planetemu.net/en/rom/commodore-c64-games-arcade-d64/dragon-s-lair-1986-software-projects-a).

## Boot and capture

1. Use PAL C64SC, drive 8 and a hard reset. Autostart the first directory entry, `DRAGON'S LAIR`. Wait for the castle title picture.
2. Press fire on joystick port 1 to leave the title. The title polls `$DC01` for exactly `$EF` at `$C053`. The subsequent game prompt at `$0CF2` polls joystick port 2 fire at `$DC00`.
3. The resident code calls the scene entry at `$1E01`. For the first descent, the source begins at RAM `$D010`. The first-descent frame at 75 frames from entry shows Dirk beside the green platform.
4. For numbered scenes, stop in resident play, write the desired index 1 through 8 to `$26`, and set PC to `$0CD1`. The game's disk loader at `$0334` sets the filename and calls KERNAL LOAD. Break on `$FFD5` to inspect the name through `$BB/$BC` and count at `$B7`. Continue to the fire prompt at `$0CF2`, hold port 2 fire, break at `$1E01`, and release fire. Legal progress through the intervening scenes remains open.
5. For scene 8, the additional break at `$FFD5` after entry sees `LI`. The post-load snapshot stops at `$1E12`. The play snapshot advances another 150 frames.

The boot picture uses a multicolour bitmap in VIC bank `$C000`. Its exit at `$9F00` copies `$6000–$9FFF` to RAM at `$C000–$FFFF` with `$01=$34` and jumps to `$4401`. At scene entry the hardware NMI and IRQ vectors in RAM point to `$1566` and `$1647` respectively. The game writes `$05` to the processor port at `$0C1F` to bank the ROMs out while retaining I/O.

Part `work/entry.vsf` holds the stopped instruction at `$1E01` except for the title picture, which holds its title state, and the dragon part, which holds the stop immediately after `LI`. The corresponding `work/play.vsf` files hold scene frames from the same emulator. The scene captures follow the loader's return and raster synchronization. The disk was attached throughout. VICE v3.14.0 ran headless with dummy audio. The disassembler answered on the batch port and each part has a local Regenerator2000 project.

## Media and locations

| File | Disk load address | Run-time destination |
|---|---|---|
| `DRAGON'S LAIR` | `$0801` | Boot package containing the title, resident code and embedded first scene |
| `LA` | `$8010` | Skull Hallway, copied to `$1E00` through `$31B3` |
| `LB` | `$8010` | Burning Ropes, copied to `$1E00` through `$2F76` |
| `LC` | `$8010` | Weapons Room, copied to `$1E00` through `$31DF` |
| `LD` | `$8010` | The Ramps, copied to `$1E00` through `$31DF` |
| `LE` | `$8010` | Tentacle Room, copied to `$1E00` through `$305F` |
| `LF` | `$8010` | Second falling platform, copied to `$1E00` through `$2F84`. Its entry decodes the embedded picture at `$E200` again. |
| `LG` | `$8010` | Phantom Knight, copied to `$1E00` through `$2EBD` |
| `LH` | `$8010` | The Dragon, copied to `$1E00` through `$31E5` |
| `LI` | `$9A00` | Additional dragon scene bytes at `$9A00–$A1ED` |
| `LJ` | `$8010` | One byte, zero. The normal gameplay path to this request remains open. |

The directory accounts for all allocated sectors. The shared loader copies the scene record, then reads run-length-coded graphics from the page after `END OF CODE` into the bank beginning at `$4000`. For `LA`, `LB`, `LC`, `LE` and `LG`, decoding the disk stream reproduces all 16,383 destination bytes at the scene entry. `LD` matches 16,378, with five cells changed before entry. `LH` reproduces 23,154 bytes through the end of the file. This decode continues into RAM past the file, and its later request for `LI` changes part of that destination. `LF` has 16 bytes after its marker page, and the scene reinitializes its graphics from the embedded source.

| Source | First graphics byte | Last source byte required for the measured output |
|---|---|---|
| Embedded first descent | `$E200` | `$FD3A` |
| `LA` | `$9400` | `$BD20` |
| `LB` | `$9200` | `$A7A1` |
| `LC` | `$9400` | `$B611` |
| `LD` | `$9400` | `$AA44` |
| `LE` | `$9300` | `$B7B3` |
| `LG` | `$9100` | `$A373` |
| `LH` | `$9400` | `$BF0F` through the end of the file |

The second descent listing uses its `work/prepared.vsf`, captured at `$1E72` after it transforms the last two graphics pages. Its original entry snapshot remains available. All other part listings were built from their `work/entry.vsf`. The game ledger aggregates the per-part symbol maps. The kit rejects a competing symbol map or listing at the game root for a multipart game.
