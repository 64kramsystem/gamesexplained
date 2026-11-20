# Test of Strength

- The selection around $0D8C reads the active-low left and right bits and uses the countdown in $1717 when direction changes. Timing and scoring across a complete strike remain open.
- $1358 copies the chamber bitmap from $2000 and the colours from $4000. The play snapshot uses hardware IRQ $143F.
- The routine at $C900 loaded file 4 when entered directly. The shared result border and apprentice records survived that hand-off.
