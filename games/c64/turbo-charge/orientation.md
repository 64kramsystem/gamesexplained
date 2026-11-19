# Turbo Charge — orientation

## Image and emulator

Nostalgia release 277, dated 6 March 2023. The two work images are
`277A_Turbo_Charge_1991_System3.d64` (SHA-256
`50ae94696cc55701930de5a840eaa8c82aa52a22db073de7fafce0cab360da31`)
and `277B_Turbo_Charge_1991_System3.d64` (SHA-256
`9550a476cb4666677487af8976379191eb60416f5defdc37b2d31b5d60477e1f`).
The archive also includes an EasyFlash build. These snapshots use the
disk build. The release reports PAL/NTSC and other patches, so code and
address claims here describe this particular disk build.
[Release notes and archive](https://csdb.dk/release/?id=230212&show=notes)

The installed VICE v3.14.0 macOS arm64 headless build ran with dummy
audio, MCP port 17484, monitor port 17485 and PAL video. regenerator2000
0.9.18 answered on 17486. The kit capability report recorded 56 passes,
`keys-host` and `no-exception`. The latter ended the check during a
checkpoint-list call. The matrix, joystick, snapshot, stop, step and
memory-watch tests passed. Some restore-and-resume sequences dropped the
VICE process. A clean start through the kit and reattaching the image
before restoring the snapshot recovered play.

## From power-on to the first drive

1. Start VICE through the kit and autostart side A's first PRG,
   `TCHARGE+10  [N0]`. The intro shows a pixel-art face and scrolling
   text. Hold Space on the keyboard matrix for about two seconds.
2. The trainer starts with **Start game** selected. Leave the gameplay
   options off, starting stage 01 and **Skip intros faster** at its
   default Yes. Press joystick port 2 fire for about a third of a
   second, release it and wait for the title car and logo. The loader
   produces white streaks while it runs. Use warp during loading if
   needed and turn it off before measuring gameplay.
3. At the title, press and release port 2 fire to start. To capture the
   hand-over, arm a stopping execute checkpoint at `$0801` while still
   at the title. The stop has X=1 after the controller has selected the
   first stage. Save without ROMs as `parts/round-01/work/entry.vsf`.
   Release the stop and let the road and dashboard appear. Store the
   steady image as `parts/round-01/work/play.vsf`. The listing uses the
   hand-over for the transient start-up code and compares it
   against this play snapshot. The first load also stops at
   `$AC00` before that code runs in `parts/round-01/work/startup.vsf`.
4. In steady play, CPU port `$00/$01` is `$2F/$35`. The IRQ and NMI
   hardware vectors in RAM are `$9392` and `$9365`. The ROM's
   default indirect IRQ pointer at `$0314` remains `$EA31`.
   The register trace in `work/play-frame.json` has 116 VIC and
   pointer writes. See [round 1](reference/round-01.png).

## Parts and debugger routes

The first driving payload contains both stage 1 and the shared engine.
At `$A85B` the controller calls `$0801` in each driving image. The
first byte executed in each later stage is again at `$0801`. Record
the loaded state there and the steady display after the first `$9392`
IRQ. The hand-over is the source for the later driving listings.

| Transition | Files | Snapshot route |
|---|---|---|
| Title and high scores | Side A `00-N0S` | Title reload enters at `$0F00`. From driving, call the existing title-reload path at `$A89C` and stop at `$0F00`, then continue until the title loop. |
| Opening cutscenes | Side A `0D-N0S` and `0E-N0S` | From a title snapshot, enter `$0433` with A=$0D, Y=2 and a synthetic return to `$3000`. If the retry stripes appear, press port 2 fire. The first cutscene hands off at `$315F` with A=$0E and Y=2. Stop at `$3000` in both images. |
| Round 1 | Side A `01-N0S` | Port 2 fire from the title. |
| Rounds 2–4 | Side A `02-N0S` through `04-N0S` | Restore the relevant preceding image, set `$0432` to 2–4 and enter the controller's load path at `$A8DC`. |
| Rounds 5–10 | Side B `05-N0S` through `0A-N0S` | Same route, with side B on unit 8. If the load pauses on blue stripes after a disk change, press port 2 fire. |
| Car destroyed / out of fuel | Side A `0B-N0S` / `0C-N0S` | From driving set PC to `$A868` or `$A885`. Stop at `$A6CF` for the image input and at `$A878` or `$A895` for the display. |
| Round completion cards | Side A `0F-N0S`–`12-N0S`, side B `13-N0S`–`18-N0S` | Set `$0432` to the round just finished and PC to `$A8B7`. Stop at `$A6CF` and then `$A8CB`. The controller adds `$0E` to the round number before loading. |
| Ending | Side B `19-N0S` | Enter the ending dispatch at `$A8EA`. The load completes at `$3000`. |

For odd rounds 3, 5, 7 and 9 the first driving snapshot can serve as
the source for the debugger route. Even rounds inherit the previous
odd round's music and were recaptured from that odd round. The odd
loads rewrite `$B000–$CCFF`. Their even partners write `$C000–$CCFF`
and one byte at `$B7B0`. The $0F and $15 images expand to identical
bytes at `$0800–$2F3F`, as do the $11 and $17 images. Each pair shares
a picture part.

## Loader and file cross-check

The release's boot screen identifies the fast loader as NOSDOS F128.
The game passes an index in A and a block count in Y to `$0433`. The
loader calls `$0646`, exchanges bytes with the drive via CIA2 and
unpacks backwards through `$05BC`. Its failure path shows blue
stripes and polls the fire input. The packed files' PRG addresses are
listed in [the media ledger](media.json).

A 16-byte window search against the trainer, title and first-driving
snapshots found two windows of `1A-N0S` at `$0405` after boot and
13 windows of compressed `00-N0S` near `$D33E` in the title
snapshots. The main stage files had no comparable aligned runs.
Part ownership uses loader entry and return checkpoints, physical
RAM differences, and store maps from snapshots taken across the
load. The `$F002–$F0FF` traffic reflects the loader input buffer
written at `$072C`. The opening files also load through this route. The regular trainer-to-title route in this build entered driving directly. See the separate opening snapshot route.

The simulation of the original backwards depacker gives the first
driving file ranges `$0801–$EFFF` and `$F300–$FFF7`. Those
bytes match the VICE hand-over apart from the opcode at `$6900`
and the stage continuation operand at `$A9F0`. A store watch
on `$6900` stopped at `$AC4C`, immediately after the routine
wrote `$2C` over the initial JSR opcode.
