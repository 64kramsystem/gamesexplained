# Street Sports Basketball boot and load notes

## Image and tools

The [XPB release](https://csdb.dk/release/?id=25791) was downloaded to `work/xpb.d64`. The kit disk reader sees a 683-sector D64 named `SCRATCH/TRIANGLE`, ID `35`. The boot file is `S.S.  BASKETBALL`, which loads at $0801. The disk has separate files for selection and match play.

VICE-MCP v3.14.0 ran headless on macOS arm64 with dummy audio and PAL timing. The assigned ports were 23028 for VICE and 23030 for regenerator2000. The emulator check reported 56 passes. Host-key input and the checkpoint-list response in the server quirks check failed. Joysticks, stopping watchpoints and instruction stepping passed. Frame capture aborted after VICE stopped answering during repeated instruction stepping. Single-address watchpoints worked after restart.

## Selection

1. Power-cycle and autostart the disk. Wait for the XPB scroller. Press fire on port 1 and release it. Allow the disk to finish loading. Warp can shorten the wait.
2. A KERNAL LOAD checkpoint at $FFD5 catches the XPB wrapper loading file M. An execution checkpoint catches the unpacked menu at $0800, with bytes `78 D8 A2 FF`. Save this as `parts/menu/work/entry.vsf`.
3. Run to the Epyx title screen. Press fire or wait for the timer to expire to get the court menu. Save `parts/menu/work/court-menu.vsf`. The listing uses the entry image because the title picture at $6000 and its colours at $5C00 are changed when the selection screen is drawn.
4. Observed KERNAL IRQ vector at $0314–$0315 was $08D8, and KERNAL NMI vector at $0318–$0319 was $08D7. The menu installs $08FB in the RAM hardware IRQ vector for use with the KERNAL banked out. Both IRQ paths call the music entry at $E000.

## Match

With School selected, press fire to accept. Choose Human, press fire on port 2 to claim green, then use fire to accept both default names. At the coin prompt make a call and press fire to toss. At the draft, press fire on the prompted side, alternating until six players are selected. Choose Play Game and wait for the load. At the score prompt, press fire to accept 20. The score bar shows both teams once play starts.

An execution checkpoint at $0835 records the match loader's KERNAL LOAD calls. For the school court the order is A, C, K, G, B. The other courts replace C/G with D/H, E/I and F/J. A checkpoint at $0E03 with bytes `4C BE 0E` captures the match hand-over. Use `parts/match/work/entry.vsf` for the listing. The score prompt and play snapshots are `work/school.vsf` and `work/playing-school.vsf`.

The match runs with the low banking bits of $01 equal to 5. Its hardware NMI vector points at $0E85. The game alternates the hardware IRQ vector between $575B and $56F8 when the sprite raster queue is active. The stores at $574B/$5750 and $5A78/$5A7D change the vector in opposite directions.

To check variant loads without repeating the draft, restore the saved pre-match menu, set $0394 to 0–3 and select Play Game. Both load tables and the resulting court screens were checked this way. Every variant uses the same B bytes and entry point.

## Disk-to-memory matches

| File | Observed use or placement |
| --- | --- |
| S.S.  BASKETBALL | XPB boot, scroller and loader at $0801. |
| A | KERNAL load requested on all four routes. The overlay loads A at $1000 and enters $1100. The relocation loop at $11C6 copies the shared poses and the six chosen overlay catalogues, adding the destination base to their pointer entries. The slot-pointer writes at $1299 and $129F fill $7002–$700D. Original and relocated record tails survive above $69FF after B loads. |
| B | Entire 23,552-byte payload matches $0E00–$69FF at all four hand-overs. |
| C–F | Each loads 6,144 bytes at $1800. The entire selected file then matches $D800–$EFFF at hand-over. |
| G–J | Each matches all 1,408 bytes at $C000–$C57F at its court hand-over. The 80-by-17 cell map starts at $C000. The final 47 bytes of each file match a slice of file B. Setup reuses several cells after the map for clamping, actor flags and a counter. |
| K | All 384 bytes match $FD80–$FEFF, where the match recolour routine reads them as six sprite templates. |
| L | One zero byte addressed to $03FF. The boot, four court load sequences and return request do not select it. The call-site inventory is in the match facts. |
| M | XPB loads the packed selection program at $0801. The unpacked menu starts at $0800. |

Seven decorative directory entries have type DEL and zero blocks. Their shared start points to the BAM at track 18 sector 0, then follows the directory sectors. The grouped entry is recorded as directory art in [media.json](media.json).

The LCX comparison disk has byte-identical A–L files and a different M. Its stripe loop polls CIA1 port A at $084E. In a controlled comparison, setting PC to $0855 took the input-accepted path. Execution stopped at the checksum comparison branch at $089D with Z set, at the unpacker entry $094A and at the menu hand-over $0800. All seven packed selection gaps and the parked overlay tail at $D16D–$D1FE match XPB byte for byte in that snapshot. The TBF disk contains a byte-identical M. Both preservation-archive retail G64 links returned HTTP 401. [LCX disk record](https://csdb.dk/release/?id=245631) · [TBF disk record](https://csdb.dk/release/?id=132763) · [Retail preservation record](https://preservation64.de/index.php?title=Street_Sports_Basketball)

The Dump Club comparison disk boots a differently packed BASKETBALL file and has byte-identical A–L files. A title snapshot matches each compared selection stretch except the 16 bytes at $FD30–$FD3F. The comparison uses a title snapshot, so a difference there can come from startup as well as the disk image. The parked overlay tail also matches. [Dump Club disk catalogue](https://www.dumpclub64.it/dumping/57-dumping-estate-2025/)
