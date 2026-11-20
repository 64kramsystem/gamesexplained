# Orientation

The input is the Five Immortals disk, labelled `STRIDER NTSC"` in its BAM. It is a 174,848-byte D64 with 683 sectors. SHA-256 is `6988c9131db3d7f50c6ddc917e10ba0118f48854b74cf47bccdc790908e7fd1c`. The local file is `work/T8I.d64`. The image is catalogued at [CSDb](https://csdb.dk/release/?id=187649).

The VICE build is release v3.14.0, v3.14.0-macos-arm64-headless.zip, with dummy audio. It ran in PAL with MCP on port 23100. The emulator check reported 55 passes and three failed rows (`keys-host`, `unpaced-calls` and `no-exception` after a checkpoint-list reply lacked the checkpoint array). Exact execute stops, load/store watchpoints and matrix input passed.

1. Hard-reset VICE. Autostart directory entry 2 (`STRIDER`), leaving the image in drive 8. This entry loads from $0100 and arranges for the LOAD return to land in its code at $0203. It names `STLO DISK2` in its call to the KERNAL. The disk's first entry is `STRIDER DEMO`; selecting entry 2 bypasses it.
2. Let the disk run until the menu offering MUSIC, SOUND FX and START GAME appears. The disk first shows the large logo over a black background. The initial file series and the first stage take time to load even in warp. Disable warp once the menu is visible. Save `work/title.vsf`.
3. Hold port 2 fire on START GAME for roughly one second. Release it and confirm a playfield and the TIME and SCORE display. Save `work/play-stage1.vsf`.

The hardware IRQ vector in the captured title is $B5B3. In the stage 1 capture it is $8269. The KERNAL RAM IRQ vector $0314 was $EA31 at the menu. The game reached $8100 once on its way from the stage load to the menu, as counted by an execute checkpoint. The title snapshot preserves the first-stage disk bytes more closely than the play snapshot.

## Disk and RAM

The KERNAL LOAD checkpoint at $FFD5 caught files H, I, J, K, L and M from caller $041F. The loader at $0400 selects one character from its file-name table at $0423 and passes it to SETNAM before calling LOAD. The following load addresses come from the PRG headers. Exact byte matches are measured at those addresses in the title snapshot.

| Files | Destination | Matches in title |
|---|---|---|
| A, B | $2000–$471F, $4000–$4FFF | 2,445 / 10,016 and 1,316 / 4,096. Later loads overlap both. |
| C, D, E | $E000–$FFDF, $1200–$15FF, $4B40–$6BFF | 6,261 / 8,160, 1,024 / 1,024 and 8,222 / 8,384. |
| F, G, H, I | $6C00–$80FE, $8100–$BEFF, $C000–$CFFF, $0B00–$11BF | 5,334 / 5,375, 15,870 / 15,872, 4,026 / 4,096 and 1,728 / 1,728. |
| J, K, L, M | $1600–$47FF, $5A00–$67FF, $F500–$F6FF, $E400–$E7FF | All 17,920 payload bytes match. |
| N–Q, R–U, V–Y, Z–2 | Same four start addresses as J–M | Later-stage loads. See the exact route below. |

## Exact hand-over and later stages

The resident listing uses `parts/resident/work/entry.vsf`, captured at $0840 after initial load and before the first stage replaces three resident data windows. The loader's first file can be captured separately by stopping at $0812. All 10,016 bytes of A matched that earlier snapshot. File B matched all 4,096 bytes at the relocated address $D000. Files C and E matched all 8,160 and 8,384 bytes respectively at $0840. File C's original $E400–$E7FF equals the stage 2 metatile file Q.

The first engine hand-over is `work/entry.vsf`, saved exactly at $8100. Each stage part holds a copy of its own $8100 entry as `work/entry.vsf` and a running-state capture as `work/play.vsf`. The engine stage number is one-based at $8101 and is copied to $5B. The disk loader's selector in $FF is zero-based.

For stages 2–5, load the first engine hand-over while stopped with the D64 attached. Write 0 to $0200 to bypass the title, write 1 through 4 to $FF for the desired stage, and set PC to $0840. Resume in warp with an execute stop at $8100. The loader at $093C makes four calls through $041F before hitting $8100. The load count was four for every later stage, and the full payloads matched their PRG files. Disable warp and advance 35 frames to see the stage. This direct route leaves initial score bytes that the title normally clears.

| Stage | Files in loading order | Payload bytes |
|---|---|---:|
| 1 | J, K, L, M | 17,920 |
| 2 | N, O, P, Q | 17,920 |
| 3 | R, S, T, U | 17,919 |
| 4 | V, W, X, Y | 17,918 |
| 5 | Z, 0, 1, 2 | 17,918 |

The four window starts are $1600, $5A00, $F500 and $E400. Some files stop a byte short of a window's maximum, so each stage owns its measured payload length. The loader route uses an execute stop and a stage selector write. Its proof is the four LOAD calls and the exact payload match at the next $8100 entry.
