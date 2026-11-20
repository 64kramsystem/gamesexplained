# 720° analysis history

The batch worktree started from its prepared main checkout. The analysis branch is `game/c64/720`. VICE used the installed v3.14.0 macOS arm64 headless build with dummy sound at the assigned MCP port 23160 and monitor port 23161. The disassembler used port 23162.

The first archive tested was Alpha Range 89. It ceased answering after entering its depacker. The Fantastic 4 and Goonies trials did not yield a usable gameplay image. The C64 Comics Group T64 reached its intro, and tracing its keyboard loop and three transfers established the $0850 handover. Its sole record was extracted as the standard PRG that the media ledger can read. The T64, PRG and release candidates remain in ignored work.

The whole-frame capture disconnected VICE on this headless build. The recorded city raster evidence comes from exact instruction stops on its chain and a stepped load and store in the viewport loop. The code map combines the game entry and opening city, and the remaining code was reached through explicit dispatch targets from the RAM image.

The final unpacker starts at $0400 and leaves the destination pointer at $FFFF when it jumps to $0850. Memory above $0400 is accounted for including the retained loader regions and the sprite data under I/O. Below $0400 are transient processor, stack, firmware and game workspace. The initial and play snapshots are kept for rebuilding and checking the extent. Handwritten and generated annotation batches, the glyph and map renderings, and control and event traces are in `work/`.

The verification sample used one independent gpt-6.2-sol checker. Step 65 did not require a recording for this scope. Verification used instruction traces, watchpoints and supplied states, and no replay or reachability claim depends on an input recording.
