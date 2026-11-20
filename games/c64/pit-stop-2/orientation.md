# Pitstop II — orientation

## Image and tools

The [Commodore 64 Boxed Sets tape image](https://www.c64sets.com/pitstop2/pitstop2.t64)
is a C64S T64 container with one occupied entry, `FILE`, loaded at
`$0801–$AF7E`. The BASIC stub calls `SYS 2087` and carries an
“ULB PRODUCTION” credit. The title credits Stephen H. Landrum with Dennis
Caswell. No trainer prompt appeared along the boot route.

VICE is the installed v3.14.0 macOS arm64 headless release, with the
dummy sound device and PAL timing. The emulator check passed 56 checks.
Host-key injection failed, so the route uses the keyboard matrix.
A transport quirks phase ended at `clear_checkpoints` with a
`KeyError('checkpoints')`. Regenerator2000 0.9.18 answered on port 23130.

## From power-on to play

1. Hard-reset VICE. Add a stopping execution checkpoint at `$C000`.
   Autostart `work/pitstop2.t64`. Save `work/entry.vsf` at the stop,
   without ROMs. Remove the checkpoint and resume.
2. The title screen requests no input on screen. Press Space for about
   half a second to enter the setup menu. Leave the defaults of two
   drivers, Brands Hatch, three laps and Rookie.
3. Press down on joystick port 2 four times, releasing between presses,
   then press fire on that port while Start the Race is selected.
4. Press Return twice to accept the default driver names. The game draws
   the starting grid and asks each driver to press fire. Hold fire on port 1 for about two seconds, release it, then hold fire on
   port 2 for about two seconds. After the countdown, hold up and fire on
   port 2 briefly to start driving. `work/play-round1.vsf` is the grid
   prompt and `work/actual-race.vsf` is the running race. Both omit ROMs.

## Handoff and banking

The tape entry's bootstrap copies its decoder to `$0100`, relocates
42,596 compressed bytes from `$08BE–$AF21` to `$599C–$FFFF`, then
expands them forward. A local reconstruction of the literal and run
commands produced exactly 57,344 bytes, matching `$1000–$EFFF` in
`work/entry.vsf` byte for byte. The final 93 bytes of the tape entry
lie beyond the decoder's input window. The entry snapshot preserves the
initial data before the game starts changing it.

Race setup starts with `$01 = $25` and the live race uses `$01 = $35` and the IRQ vector in RAM under the
KERNAL. The frame capture observed vector stores to `$3672`, `$36B8`,
`$371A`, `$3ECD` and `$4008`. The RAM vector at `$0314` retained
its KERNAL default `$EA31` in the race. The tape has one program entry.
The title, menu and race were reached with the same resident image.
