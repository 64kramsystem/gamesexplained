# Hunchback analysis history

The batch assigned VICE MCP port 23048, VICE monitor port 23049 and regenerator2000 port 23050. The installed VICE v3.14.0 macOS arm64 headless wrapper selected dummy audio on its command line. The emulator check's final quirks phase raised a checkpoint-list KeyError. The game's execute and store checkpoints worked afterward.

Autostart loaded the BASIC bootstrap, then dropped out of warp after the first file. Turning warp back on let HCODE finish loading. The hand-over breakpoint at $4000 caught the genuine tape entry. SPACE opens the control menu and J opens the port 2 prompt. The delay after the prompt made an early screenshot look stalled. A breakpoint on $4920 distinguished the steady first wall from the GET READY delay.

Regenerator2000's $4000 walk stopped at the title's wait loops. The local recursive trace seeded IRQ entries and all six targets from the indirect wall renderer. A VICE execution map around the first input sequence fell within the traced code. The listing preserves the overlapping BIT/LDA entry at $5887/$5888 and uses the entry snapshot so it shows the authored initial glyph and sprite bytes.

The first coverage export tracked the HCODE interval explicitly and identified three uncounted stretches. The bootstrap and its KERNAL display fell outside HCODE. The default vector table bytes at $FD30-$FD4F matched the installed KERNAL ROM. The live VIC screen is cleared and drawn by the game. The $77FF pointer seed is tracked because the HELP sprite animation reads that payload byte before toggling a pointer.

The fixed-seed listing sample and verdicts are in `work/reports/sample-1319/`. Targeted emulator scripts and logs are in `work/`. Step 65 was evaluated without a route recording. The tested claims are local instruction behavior and do not assert how to reach a novel state using player input.
