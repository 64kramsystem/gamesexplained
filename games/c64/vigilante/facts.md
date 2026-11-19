# Vigilante — analysis facts

## Stage loads

The game loads five files per stage. The checkpoint at `$3C5B` counted five passes in each of the five stage loader runs. The stage number at `$0D16` is multiplied by five at `$3C40–$3C49`, and the result indexes the A–Y filename table through the resident entry `$0900`. Each row in the orientation table was matched to the corresponding loader-stop snapshot at `$0D98`.

## Display

- `$0E8D` selects VIC bank `$4000`, screen base `$5000` and multicolour characters.
- `$0F32` saves A, X and Y, checks and acknowledges raster IRQ on `$D019`, then calls the handler in the self-modified operand at `$0F46–$0F47`. Both raster handlers hit four times over four live frames. The handler at `$0F51` queues line `$FC` and sets playfield fine scroll from `$0D22`. The handler at `$0F90` queues line `$61` and selects the panel charset at `$4800`.
- `$C147` copies 40 columns from each of 19 256-byte rows, starting at stage tile map `$5400` and colour map `$6700` before scrolling. Destinations start at screen row 6 (`$50F0`) and colour row 6 (`$D8F0`).
- Sprite data is copied from RAM libraries at `$8000` and `$E000`. `$2707` and `$271B` select the source bank, and `$26D0` writes hardware sprite pointers at `$53F8` and above.

## Panel alphabet

The character set at `$4800` is indexed by custom codes. The name editor has an A–Z lookup table at `$C4AD`. Cross-checking that table against the rendered glyphs and screen text gives the alphabet below. The panel's number offset is `$05`, used when unpacking BCD at `$2997` and `$29A8`.

| Character | Code in character order |
|---|---|
| A–M | `55 68 01 59 04 5A 5B 5C 06 5D 5E 54 57` |
| N–Z | `58 05 53 5F 03 00 F8 60 F6 61 62 56 63` |
| 0–9 | `05 06 07 08 09 0A 0B 0C 0D 0E` |
| Alternate O and I | `02 64` |
| Plus, stops, space | `6F 69 6E 20` |

The message routine at `$39AA` consumes a mode byte, a row count, and 25 characters per row, including padding. Stage introduction records start at `$7A64`. Their text refers to the kidnapping, the van and junkyard, the bridge, downtown, and the final chance to save Madonna. The Hall of Fame uses separate fixed-length strings at `$C276`, `$C282` and `$C28E`.

## Joystick

`$16EF` inverts CIA1 port A and retains bits 0–4. If the facing flag at `$16EC` is set, it swaps the horizontal inputs before storing the result at `$16ED`. `$124C` indexes the common actor action table with the resulting mask. Over 20 frames from the same idle first-stage snapshot, the sampling instruction ran 10 times without input, nine with right, and ten each with left and fire. A store checkpoint saw the same counts at `$16ED`. Right left a decoded mask of `$08`. Holding left changed the facing byte and subsequently also produced normalised mask `$08`. Fire left mask `$10`.

## Live checks

| Check | Instruction and watchpoint evidence |
|---|---|
| Timer | With the prescaler at 100 and display at 99, `$0F90` and `$35D0` each executed 230 times over 230 PAL frames. The units byte at `$35CD` was written twice and the display ended at 97, with prescaler 70. An enabled timer unit lasts 100 frames, or 2 seconds at 50 Hz. |
| Up and up+fire | Over 12 frames the dispatch at `$124C` selected action headers `$2114` and `$2132` respectively. The writes to `$165C` left Y at `$D2` and `$D0`, compared with `$D8` for neutral input. |
| Down and attack inputs | Down selected `$2119`. Right+fire, down-right+fire and down-right selected `$2141`, `$2137`, and `$2128` respectively from the same starting snapshot. The dispatch executed once per attack case, and the animator at `$1371` executed 24 times over 12 frames. The exact strike attribution remains open. |
| Pause | RUN/STOP reached `$10DA` and the write clearing `$35CE`. In the pause loop a released matrix read at `$10F4` returned `$FF` and branched back to `$10F1`. A second RUN/STOP press returned `$7F` and fell through `$10FB`. The checkpoint at `$1101` then hit and the timer was enabled again. |

## Actors

The first sixteen bytes of each stage actor file are eight pointers to its five-byte actor headers. Each header gives an animation stream pointer in its first two bytes. The streams contain frame pointers, signed X/Y deltas and durations in five-byte steps. The update at `$15D6` advances five bytes, and the high byte of the next frame pointer determines whether it stops. The regular descriptors start with a count of hardware sprites, then indices and position fields as read at `$1371`. Stage 3 contains an animation step pointing at `$CB4B`, where the count byte would be `$25`. Its runtime effect remains open.

The files retain material beyond these streams. The tails of D, I, N and S are byte-identical to a corresponding range of stage 4's sprite library, with a fixed address delta of `$12E0`. File X first retains part of S's descriptor and animation region at the original addresses, then the same sprite bytes. These tails remain visible in the listings.

The game feeds the stage sprite library with the indices in descriptor bytes 1, 2, 3, 13 and 14, in that order, up to the descriptor's sprite count. Walking the valid frame descriptors from each overlay's directory yielded maximum indices of 100, 108, 100, 122 and 74. The trailing KERNAL-identical ranges start at slots 101, 110, 110, 123 and 123. Stage 3's malformed-looking descriptor stays open.

## Disk transfer

A stage 4 reload stopped at `$0D98` after hitting the load instruction at `$091A` five times. A non-stopping instruction checkpoint over `$7B00–$7BD5` counted 2,299,245 hits, with 3,968 hits at the CIA2 wait instruction at `$7B4E`. That copy of the host-side transfer routine remains resident after the stage data overwrites the original FAST image at `$7000`.

## Sound

`$37FA` sets the SID filter routing, cutoff high byte and mode/volume. The player at `$380F` gates voices 1 and 2 off before changing frequency and gates them on with pulse waveforms. The four byte planes at `$C700`, `$C7FB`, `$C8F6` and `$C9F1` supply low and high frequency bytes for the two voices. A first-plane byte of `$FF` invokes reset at `$387B`.

## Open

The exact chain pickup and the grab escape input remain open. The nearest code paths are the actor proximity test at `$3061`, the player input dispatch at `$11CA` and the damage routine at `$34F3`. The register census and live checkpoint measurements stay under `work/`.

## The listing's error rate

Seed 241119 drew 60 of 913 comments before verification edits. The independent `gpt-6.2-sol` checker found eight wrong, all confirmed against the code and corrected. The estimate was 13.3%, with a 95% Wilson interval of 6.9%–24.2% and a stratum-weighted estimate of 12.9%. The checker may have missed other errors. The fixes cover actor header selection and sprite colours, the embedded catalog, opponent and transition conditions, the serial-loader entry and a self-modified sprite operand. The sample also led to retyping the first stage-event callback at `$3B38`.
