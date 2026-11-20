# Orientation

The analyzed disk is the Ocean Rainbow Collection G64 from [C64Games.de](https://www.c64games.de/phpseiten/spieledetail.php?filnummer=120). Its first eight bytes are `GCR-1541`, and its SHA-256 is `341cb62e963b022fb7180791cc5cd3ed0bc74c617b4c0598faa446a40cfe1354`. It contains one disk and 18 directory files. The separate SID file supplied by the archive is outside the disk image.

## Boot and hand-over

1. Start the kit's headless macOS arm64 vice-mcp v3.14.0 in PAL with dummy audio. The emulator check passed 56 checks. Host-key delivery and the final compatibility probe failed. Joystick, matrix keys, exact instruction stops, watchpoints, and snapshots passed. The final probe raised `KeyError('checkpoints')`. The second tool was Regenerator2000 0.9.18.
2. Hard reset and autostart the G64. The KERNAL loads the first directory entry, LOADER, with `LOAD"*",8,1`. LOADER lands at $0316. Its indirect LOAD completion path enters $0363 and loads F to $4000. VICE's autostart may report that it left ROM at $0363. The game's boot continues.
3. Arm an execution stop at $0800 after autostart begins. If the loader continues at normal speed, enable warp after the initial LOAD begins. F uploads a 1541-side reader, copies its C64 receiver into the stack page and transfers NZS. The receiver selects $35 at $01 and jumps to $0800. Save `work/entry.vsf` at that stop, then disable warp and remove the checkpoint.
4. Resume through the title. With Start Game selected, hold port 2 fire until the game starts, then release it. The first round is Auckland 1-1. The title, play screen and screenshots are also in `work/`.

The resident listing uses the boot hand-over copied to `parts/resident/work/entry.vsf`. This preserves loaded bytes before the game clears work areas or alters instruction operands. Compare $0800 and $5B8F with the emulator's RAM to anchor the snapshot to the game. $01 is $35 in play. The software IRQ vector at $0314 reads $EA31 but the hardware IRQ uses RAM at $FFFE because the KERNAL is banked out. The title's handler is $9259. Play starts its raster IRQ at $4F37, which installs $5195. The latter dispatches more sprite phases through its patched jump at $51B4. A stop during live play saw $5195 in $FFFE and $20DB in the NMI vector.

## Disk packages

Each part's listing uses `parts/<id>/work/entry.vsf`. The paired `play.vsf` shows the same overlay after the display has started. For hand-off files and commands, see the local `work/parts.py`, `work/load-trace-final.txt`, and `work/observe.py`.

The direct route uses a stopped play snapshot and the game's own loader. Set $0624 to the zero-based world, $0625 to the zero-based round, $0629 to zero and SP to $FF. Enter at $0A21 and stop on $0819, after the load and before round initialization. Observe the file-name requests with a checkpoint on $5D51. Its pointer at $BB/$BC addresses two PETSCII bytes. These routes skip the prerequisite rounds.

| Part | Base snapshot | World, round | Files loaded | Overlaid ranges |
|---|---|---|---|---|
| World 1 | Round 1-1 in play | 0, 0 | M1, B1, DR | $9800–$CFFF and $6000–$637F |
| World 2 | Round 1-1 in play | 1, 0 | M2, B2, DR | $9800–$CFFF and $6000–$633F |
| World 3 | Round 1-1 in play | 2, 0 | M3, B3, DR | $9800–$CFFF and $6000–$623F |
| World 4 | World 3 in play | 3, 0 | M4, DR | $9800–$CFFF |
| World 4 boss | World 4 in play | 3, 3 | O4, C4, A4, DR | $B000–$BFFF, $C800–$CFFF and $9F00–$9FFF |
| World 5 | Round 1-1 in play | 4, 0 | M5, B5, DR | $9800–$CFFF and $6000–$647F |
| World 5 late | World 5 in play | 4, 2 | O5, DR | $B000–$BFFF |
| Ending | World 5 late in play | 4, 2 | GO | $A000–$A3D2 |

For the ending, set $0629 to one, enter at $4717 and stop at $A000. For each route the contents at the load addresses were compared with the extracted PRGs. The world packages reload an identical shared block at $9D0C–$9EFF. The ledger keeps that block with the resident engine. The identical B1 bytes already present in NZS are covered in World 1. DR restores $F800–$FFBF, which is shared by the worlds. The shared-sprites part uses the World 1 entry snapshot to list the three different bytes at $FF3A, $FFA3 and $FFA7. The resident listing keeps the boot values and counts the identical rest of DR once.

The boot and overlay receivers transfer directly into RAM, including underneath I/O and ROM. Each overlay uses the actual loader and drive; none of the listing snapshots was made by assembling files onto a memory dump.
