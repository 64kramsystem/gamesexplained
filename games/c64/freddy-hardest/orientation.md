# Orientation

The input is the [Fantastic 4 Cracking Group disk](https://csdb.dk/release/?id=164406)
downloaded on 19 November 2026. Local path `work/freddy-hardest.d64`.
The image has 174848 bytes, a standard 35-track 683-sector layout and a
readable BAM and directory at track 18. There is no container header or
error-byte tail. Its SHA-256 and file hashes are in `media.json`.

VICE release v3.14.0, macOS arm64 headless, ran in PAL with the preinstalled
dummy sound device. The kit's emulator check reported 56 passes. Host-name
key presses failed, so the run used keyboard matrix calls. The quirks phase
stopped on a missing `checkpoints` field. The required instruction steps,
execute checkpoints, store watchpoints, joystick and snapshot tests passed.
The assigned VICE, monitor and Regenerator2000 ports were 18508, 18509 and
18510 respectively. Regenerator2000 0.9.18 answered on each listing snapshot.

## Disk entries and boot routes

| Directory entry | Load address | Payload bytes | Route |
| --- | --- | ---: | --- |
| FREDDY HARDEST | $0801 | 12910 | Autostart the first file and let it decompress to the illustrated screen in `reference/loading-art.png`. Its BASIC entry is SYS 2065. |
| 1 FREDDY | $0801 | 26548 | Hard reset and autostart this exact name on unit 8. Press fire on the title. Wait through the spacecraft crash to reach surface play. |
| 2 FREDDY | $0801 | 35929 | Hard reset and autostart this exact name on unit 8. At ACCESS CODE press and release 2, 5, 4, 2, 5. Press fire on the title to enter base play. |

The direct gameplay files use BASIC SYS 2066. A stop at `$0812` catches
the packed entry. Its code copies the depacker to the stack and system
workspace and jumps to `$0100`. The first depacker jumps via `$03A2`
to the next stage at `$081B`. Run to `$04CD` to catch the final cleanup
before the game startup. Both stops were observed. The bytes of the packed
files principally belong to those load stages. The actual listings use the
decompressed game state.

Set an execute checkpoint at `$0812` before autostart. Once hit, replace
it with one at `$081B`, resume, then replace that with a checkpoint at
`$04CD`. Save without ROMs. After deleting that checkpoint, restore normal
speed and allow two seconds for the first game screen. The local files
`parts/*/work/entry.vsf` catch `$081B`, `handover.vsf` catches
`$04CD`, and `screen.vsf` is the first screen. The first part's screen is
the title and the second's is the code prompt.

On the surface title the run held fire on port 2 for 35 frames, released
it, then held it on port 1 for 35 frames and released it. After 240
frames it captured the crash sequence. It applied port-2 fire for four
frames and captured the surface after another 700 frames. Build the
surface listing from `parts/surface/work/surface-play.vsf`.

For the base, hold each of the five digits for eight frames and release
for eight. After another 20 frames, apply the same 35-frame fire holds,
then let the game run 240 frames. Build the base listing from
`parts/base/work/gameplay.vsf`. The published C64 access code was
used to reach this part directly. [Lemon64 C64 access code](https://www.lemon64.com/cheat/freddy-hardest/975)

Both listings use `--entry <part>/work/handover.vsf`. The port read
during the play captures was `$36` at `$01`, putting I/O and KERNAL
in CPU view and leaving RAM visible under BASIC. The observed KERNAL
IRQ vectors at `$0314` were `$B021`, `$CCA1`, `$A02C` for
the surface title, crash and play, and `$1055`, `$CBD0` for the
base prompt and play. The installers write those vectors at `$B017`,
`$CC97`, `$A022`, `$0F36` and `$CBC6` respectively.
Execution maps were captured independently for each part. The same
RAM addresses hold different code and data across the two boots, so the
kit lists each load separately.
