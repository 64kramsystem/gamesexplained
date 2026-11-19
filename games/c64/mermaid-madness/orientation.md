# Orientation

The image is the 174,848-byte, 35-track D64 in the [C64.com Mermaid Madness download](https://www.c64.com/games/download.php?id=151). It has no GCR header or appended error map. The directory title is `WWW.C64HQ.COM`. The SHA-256 is in `media.json`. The image and both extracted programs are in ignored `work/`.

## Rebuild the snapshots

1. Start VICE x64sc with the kit launcher on the assigned port. The batch wrapper selects the macOS arm64 v3.14.0 headless build and `-sounddev dummy`. The companion monitor is on the next port.
2. Hard reset and autostart the directory entry `MERMAID MADNESS` by name, using `vice.autostart`. Allow the drive to finish loading. If the prompt reappears without running, enter `RUN` through the KERNAL keyboard buffer.
3. At the Kurt crack intro, hold the Space matrix key. For `entry.vsf`, arm an execute checkpoint at `$4000` first and save when it hits, after releasing Space. During the introduction the joystick fire button did not dismiss the crack screen.
4. Continue to the game's title and release all inputs. Save `title.vsf`. Hold port 2 fire to start, then release it once Myrtle and Gordon are on the promenade. The captured `room.vsf` is from the opening scene after a 90-frame fire hold and 10 frames with the port released. The title screen and the promenade captures are in `reference/`.
5. `room.vsf` is the disassembler and listing input and `entry.vsf` is the comparison image. `swim.vsf` is a local test fixture taken after holding right through the opening to reach swim mode. Snapshots omit ROM and disk state.

## Loader and banking

The selected PRG starts at `$0801` with a BASIC `SYS (2064)` stub. The startup code at `$0810` banks away I/O and ROM, relocates data and jumps into the stack page. It leaves the crack intro running with the KERNAL IRQ vector pointing to `$C360`. Space passes through a further stack-page stage with `$01 = $34` and reaches `$4000` with `$01 = $37`. The game entry clears bit 0 of `$01`. During play, `$2F/$36` at `$00/$01` leaves I/O and KERNAL visible and exposes RAM at `$A000`. The KERNAL IRQ vector `$0314` points to `$41E9`. That handler's self-modified JMP dispatches to `$421F`, `$42F2` and `$439E` at raster lines 0, 90 and 180, observed by execute checkpoint and single-step. The KERNAL NMI vector at `$0318` was `$FE47`.

| Directory item | Load and snapshot comparison |
|---|---|
| `MERMAID MADNESS` | 43,715 payload bytes at `$0801`. A 16-byte window sweep found matches at several offsets with no single contiguous mapping. The execute checkpoint establishes the unpacked hand-over at `$4000`. |
| `MERMAID M.+3/REM` | 27,539 payload bytes at `$0801`. No nontrivial aligned 16-byte payload windows matched either title or promenade RAM. This is a separate boot choice in the image. |
| `----------------` | Three DEL separators with zero blocks. Their track 18 pointer is reported by the ledger as a directory/BAM sector chain. |

The selected release has the room map in RAM at hand-over. Room redraws read that RAM. The decoded game paths contain no reference to the KERNAL LOAD vector at `$FFD5`. No overlay was identified in the selected release.

## Emulator checks

The kit's v3.14.0 probe passed 56 checks. `keys-host` failed, so the boot recipe uses a held matrix key. `no-exception` was a `KeyError('checkpoints')` in the server quirks phase. The instruction-step, execute-stop and load/store watch checks passed. The all-register frame recorder lost the process while handling many checkpoints. The three raster targets were verified with one execute checkpoint at a time instead.

## Comparison boot

The other entry shows the 1998 Remember intro. Space opens the included documents and RUN/STOP at matrix row 7, column 7 proceeds to the trainer. Three separate N presses decline the offers. Its title lists Soft Design and Richard Chappells, with a fire prompt in place of Kurt's credit. After starting, its KERNAL IRQ is also `$41E9`. Comparing both releases' title and promenade snapshots found identical terrain and much of the code. Differences that persist from title to promenade include the reset call operand at `$4004–$4005`, six bytes between `$5168` and `$51CE`, parts of the alphabet and text, and most RAM underneath I/O and the KERNAL. The comparison fixtures are in `work/`.
