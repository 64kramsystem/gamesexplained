# Pac-Land orientation

The input is the [Madonna Cracking Group disk listed by CSDb](https://csdb.dk/release/?id=75241), dated 24 March 1988. The 174,848-byte image is a 35-track sector D64 with 683 readable sectors. The directory header is DIGITAL DUNGEON, disk ID TD. SHA-256 is `8e0bcde5d3c760869eba445dec3eabf443f5bc8fc98d1ceec7f0f244de5458c3`.

1. Start a PAL C64 with VICE-MCP 3.14.0 headless and dummy audio. Hard reset, then autostart directory entry 2, `PAC-LAND   (MCG)`. The BASIC loader calls SYS 2072.
2. Wait for the MCG logo and scroll text. Its RAM IRQ vector is $1199. Press SPACE via the keyboard matrix for about 0.2 seconds. The intro gives way to a second unpack and then the game title.
3. For `work/entry.vsf`, arm an execute checkpoint at $033C before pressing SPACE. Save when PC is $033C and the bytes there are `78 A2 FF 9A`. The processor port is initially $37. The game's initialization switches it to $35 and configures the raster interrupt.
4. At the game title press F1 for a credit and F3 to start one player. Hold each for about 0.2 seconds with a short gap. After the ready screen, save once Pac is outside the house in Round 1. That image is `work/trip1.vsf`. Use `work/entry.vsf` for the listing to retain pre-initialization bytes.

## Interrupts

During play the port is $35, so the CPU reads the IRQ vector from RAM under the KERNAL at $FFFE/$FFFF. It points to $03D1. The startup writes $03D6 to the KERNAL's indirect IRQ vector at $0314/$0315 and $064B to both NMI vectors. The six raster positions are in $886C-$8871 and the low and high bytes of the dispatch targets minus one are at $8860 and $8866. A one-frame watch captured the VIC register changes in `work/trip1-frame.json`.

The headless build passed 56 emulator checks, including instruction stepping and load/store watchpoints. Host-key translation failed. The final quirks probe stopped on a checkpoint-list response missing its `checkpoints` key. Matrix input worked. The monitor answered disassembly requests, but `memmapzap` terminated the emulator after the gameplay frame capture.

## Disk files

| File | Bytes including load address | Match in entry and play snapshots |
| --- | ---: | --- |
| PAC-LAND   (PIC) | 8,683 | No aligned 16-byte chunks |
| PAC-LAND   (MCG) | 43,761 | No aligned 16-byte chunks. Packed boot and game |
| ^PAC LAND NOTE!^ | 1,450 | No aligned 16-byte chunks |
| PAC-LAND TUNES!! | 4,112 | Eleven chunks at displacement $ACDC in both snapshots |

The packed program first runs a low-memory unpacker and shows the MCG intro. SPACE releases it into the second unpack, which installs the game before entering $033C. The entry and play snapshots agree across large spans, with the largest differences in $A000-$AFFF and $C000-$CFFF.

## Program boundaries

The primary disk has one resident gameplay image. The picture, RADWAR note and tune rip are independently started disk entries. The picture entry shows the illustrated Pac-Land map. The note entry shows the credit and control instructions. The tune entry has small matching chunks in the resident music.

The engine loads sixteen round recipes from its own RAM. A breakpoint at the round initializer's exit reached all sixteen cases from $EBC2 without executing the KERNAL LOAD entry at $FFD5. Each initializer triggered its positive-control read watch in the resident terrain dictionary. The listing and symbol map therefore use the game folder directly.

The independently packed [Wanderer Group disk](https://csdb.dk/release/?id=56871) was used locally for comparison. Its game title snapshot matches the sampled entry code, the complete terrain strip bank and both retained regions at $3FEA-$3FFF and $BFEE-$BFFE. The MCG entry stays the source of the listing.
