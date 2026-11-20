# Title and resident code

The title-entry snapshot stops at `$2E68`. The module header at `$2E64` contains the relocated entry and the size `$055A`. Entry code clears the input latch at `$46` and installs a title IRQ from the vector word at `$31D9`. The IRQ restores the processor port when returning to the interrupted code.

The first disk's named DM program loads at `$0800`. Its jump table provides services which also remain available to later modules. `$0800` resolves module IDs, `$0806` releases them, and `$081E` calls a module's relocated entry. The drive byte loop at `$0B6B` and the logical sector transfer at `$192B` are in the same resident body.

The music control entry at `$6400` and music tick at `$6403` dispatch into the same routine family. The title exit at `$31BC` queues the stop using Y equal to `$FF` and restores the prior interrupt vector. The register writes for the full tune are open.

## Startup modules and attract sequence

The resident records at $093C and $0943 identify TD at $2500 and UJ at $27F9. The first invokes the second with a resource ID and mode on the stack. After TM returns, TD walks the ID pairs at $27AA through the first zero ID byte and releases each item with $0806.

The title's attract sequence at $306F sets up the display before starting the S1 tune. A store checkpoint on $3080 stopped after the increment at $3083, with the immediate operand changed from zero to one. The operand belongs to the LDA at $307F. On a subsequent visit its nonzero value makes $3081 branch past the music setup. The sequence then presents the graphics and overlay, calls HS with A equal to zero, and presents a text panel. The timed input paths can leave the sequence early.

## Sampled title audio

TD loads $C2/$30 at $6A00 and $C2/$31 at $7564. All 2,916 and 4,889 bytes respectively match the private directory items. The two title call sites at $2F18 and $2F60 pass those IDs to DS. A CPU stop at $33D6 caught the first DS header load with the resource pointer at $6A00. The local trace is in `work/resume-title-samples.log` at the game root.

DS reads a little-endian length and an escape byte. It emits the low nibble of each packed byte first, then the high nibble. An escape reads a count and repeats the next packed nibble pair. The output loop polls CIA1 Timer A before writing each level to $D418. On return it restores the music player's volume register value and the processor port.

The title listing now uses `work/analysis.vsf` in this part, captured at the first DS header read after relocation. The call at $342A reaches $348B in this snapshot. The earlier hand-over image retains the module's original $20C9 operand and remains available in `work/entry.vsf`.

## Title artwork archive

Re-entering the title startup call at $25B4 and stopping at $2843 found the 7,030-byte side A archive $2A/$D4 at $887D–$A3F2. Every packed byte matched the disk extraction. A stop at the return site $25BB caught UJ after it had allocated and written its child objects. Following the linked resident directory pages located 21 objects. All 21 unpacked objects matched the saved title image byte for byte, with matching flags and lengths. The trace and address list are in `work/resume-title-archive-reentry.log` and `work/resume-title-assets.log`.

The children include GP bitmap streams, colour planes and uncompressed bitmap rectangles. Title uses $D4/$C2 and $5F/$42 in the attract screen call at $30AE, and draws the rectangle $D4/$42 at $30CC. The payload at $E9C7–$F051 is $C3/$D3, a GP bitmap stream. Some of its bytes remain at the same addresses in the selector and driving snapshots.

## Resident music driver

The PM disk items on sides A and B match exactly. The installation loop copies six pages starting with byte 53 of PM to $6400. The 1,393 bytes from the first jump through $6970 match the disk payload exactly in the relocated title capture. The remaining bytes through $69FF are zero-filled space beyond the disk item.

The title reached the music initializer at $68EE with the tune pointer in X and Y. A read watch on $683B–$68E8 stopped after the indexed load at $68F5, with X equal to zero and A equal to one. This is the first pointer-patch record. The stream ends at $68E8. The two preceding tables supply the bytes of the frequency word that the voice routines write to SID.

The second artwork archive has ID $2A/$CC. A CPU stop at $2843 during
startup's call from $25D3 showed the packed input beginning at $887D.
All 1,313 input bytes matched the side A catalogue. UJ returned at
$25D6. The five bitmap objects $CB/$31 through $CB/$35 and the five
packed colour objects $2D/$31 through $2D/$35 match the decoded input
byte for byte. The first resident directory page at $0900 holds eight of these entries.
The linked page at $BCCD holds the other two entries, whose payloads
start at $E807 and $E835. The trace is in the game's
`work/resume-title-cc-watch.log`.

The four pages at $2100–$24FF match side A track 3 sectors 0 through 3
byte for byte. During a reload of $2A/$CC, a CPU read watchpoint stopped
at $0CA8, just after the directory lookup read through $04 with the
pointer at $2100. The separate sector transfer buffer at $2000 matched
track 22 sector 6 in the title snapshot. Its read watchpoint stopped at
$0DDE when the transfer loop copied the start of the archive into its
allocated destination. See `work/resume-disk-cache-watch.log` at the game
root.

Cold-boot store watchpoints at $E500, $E600, $E700 and $E7FF
stopped immediately after the disk intro's indexed store at $082A.
The intro patches the destination page between copies. After the
intro settled, all 768 bytes matched the title snapshot before Space
was pressed. The traces are in `work/resume-intro-pages-watch.log`
and `work/resume-intro-final-watch.log` at the game root.

The disk DM payload covers $0800–$1EA1. Before the intro's handoff,
a store watchpoint at $1EA2 stopped immediately after the intro's
$0389 indexed store wrote $DD there. At this point all 94 bytes from
$1EA2 to $1EFF already matched the later title capture. The intro's
relocation tail persists immediately beyond the end of DM. See
`work/resume-serial-tail-watch.log` at the game root.

A store watchpoint on the two address bytes of the note-timing read at
$64D9 stopped at $692D after the installer wrote the low byte, $5F.
When execution later stopped at $64D9, the instruction bytes were
`B9 5F 39`, so the indexed load read the installed song table at $395F.
The analysis snapshot holds the pre-install operand $64D9. See
`work/resume-pm-operands-watch.log` at the game root.

All eleven bytes in the DOS file DRIVE match $03F5–$03FF in the
title snapshot. Starting a probe at $17CE stopped at $17D1 just
after reading the startup flag at $03F7. Its value was $FF in this
capture. The probe also confirmed that the title drawing loop reads
the tagged mask pointers beginning at $3314. See
`work/resume-title-resource-watch.log` at the game root.
