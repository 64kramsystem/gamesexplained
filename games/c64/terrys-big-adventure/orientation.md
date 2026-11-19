# Terry's Big Adventure orientation

## Image and tools

The New Fashion '77 release, [CSDb entry 152363](https://csdb.dk/release/?id=152363). The local file is `work/terry.d64`. It has the 174,848-byte layout of a 35-track D64 and one directory entry, `TERRYS B.ADV/TNF`, with a two-byte PRG start address of $0801 and 43,765 bytes of payload. SHA-256 is `e843a0f96c641aaacde46ebbe06872c7b3ccf457ff7e36191a10384f2c29951a`.

VICE v3.14.0 macOS arm64 headless ran a PAL C64SC with dummy audio. VICE MCP listened on 17420, the monitor on 17421 and regenerator2000 on 17422. The emulator check passed 56 checks. Host keys failed, so send SPACE by the C64 keyboard matrix. The final diagnostics raised `KeyError('checkpoints')` after the gameplay, stepping and watchpoint checks passed. The run restarted VICE and checked the instruction and watchpoint paths in the game itself.

## Reproduce the snapshots

1. Hard reset, wait one second, then autostart directory entry 1 on unit 8. Wait about 12 seconds for the TNF scrolls.
2. Arm a stopping execute checkpoint at $6D00. Hold SPACE by the keyboard matrix and let the unpacker finish. Warp shortens this wait. At the stop, verify PC=$6D00, A=$37, X=$00, Y=$01 and SP=$FF. Release SPACE, disable warp, remove the checkpoint while stopped, and save `work/entry.vsf`.
3. Run 60 frames. The logo and high score are drawn over the opening landscape. Save `work/title.vsf`.
4. Hold port 2 fire for 20 frames, release it, and run 233 frames. The Scene 01 interlude gives way to the first playable scene. `work/scene.vsf` was captured another 200 frames into this scene and supplies the verification baseline.
5. In play the CPU port reads $35, the KERNAL software vectors at $0314-$0319 contain zeros, and the RAM IRQ vector at $FFFE-$FFFF was $8ACB. The observed sequence of vector writes in one PAL frame is $8ACB → $8EC5 → $797C → $8ACB. The three entry addresses were counted separately.

## Loader and engine

The disk program first runs the TNF intro. SPACE exits to the unpacker, which runs in low RAM with ROMs banked out. At the handoff the engine begins with a jump at $6D00 to $75F9. The file carries packed data. Matching unique 16-byte windows against RAM found nine matches at the leading offset ($A202 bytes lower than the file position), and four isolated matches at other offsets in the entry snapshot. No unique chunks from the packed PRG matched the play snapshot. The source listing uses `work/entry.vsf` because it preserves the start-up data, raw HUD seeds and initial operands. Comparing it with `work/scene.vsf` found 1,943 changed RAM bytes.

This release uses resident compressed map streams and a shared map buffer at $1000-$1BFF. The original disk's [preservation image](https://preservation64.de/index.php?title=Terry%27s_Big_Adventure) returned HTTP 401 when fetching it for comparison. The findings apply to the TNF image.

The resident decoder was instrumented for all twelve scene indices and both alternate selectors. Each used its own source stream and wrote the same map buffer. The KERNAL LOAD call at $B61E was also watched during these probes and was not hit. See [facts.md](facts.md) for the trace evidence. The shared engine and all fourteen resident streams use one symbol map and listing.
