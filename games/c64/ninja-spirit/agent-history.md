# Analysis record

## 19 November 2026

The DCS loader reached real play under the installed headless vice-mcp
build. An exact breakpoint at the shared handover, and register reads at
the two decoder boundaries, identified the four overlay loads and their
two respective ranges. A high-volume frame capture lost the emulator
while deleting breakpoints. The same executable and ports worked after
restart for individual CPU breakpoints, instruction steps and memory
watches.

The disassembler’s export guard detected shorter spans after stage
dispatch tables were typed. The earlier exports were retained in local
work while those tables and their readers were reannotated. The lasting
part listings use the appropriate live gameplay snapshots.
