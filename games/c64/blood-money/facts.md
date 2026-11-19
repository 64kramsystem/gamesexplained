# Blood Money technical facts

## Disk loading and level selection

- The level number at `$0442` is ORed with `$30` at `$C8BF`. Four stores put the result into the filename templates at `$C9BD`, `$C9C3`, `$C9C9` and `$C9CE`. A store checkpoint on the first address and execution checkpoints at the four SETNAM calls fired during the level load.
- The Accept disk's level 4 load reaches the return at `$C9B6` with carry set. The intervening port restore changes A, so the KERNAL error number is unspecified at that stop. The same transition with the Syntax disk reached that return with carry clear and loaded the missing character and sprite data. See the disk identities and route in [orientation.md](orientation.md).
- After loading CHARS, `$C969` copies page `$5B00` to `$6F00`. The clear routine at `$CB40` later reuses `$5B00–$5FFF` for the scroll buffer.

## Graphics and timing

- The gameplay IRQ at `$2034` switches video settings and sets sprite pointers for the bottom panel. The captured level 1 frame shows writes to `$D011` and `$D018` on line 202, and writes to `$43FA–$43FF` on line 203. A non-stopping execution checkpoint at `$2034` fired 14 times across the 15-frame probe, which began partway through a frame.
- The title renderer reads display text as byte values. At `$C4F4`, space selects glyph 0, dollar selects 37, digits select 27–36, and letters select 1–26 by masking with `$1F`. The renderer uses two tile codes from `$1531` for the upper row and two from `$1581` for the lower row. The glyph sheet rendered from the character data at `$4800` is in `work/display-glyphs.png`.
- A load watchpoint in the first level's terrain glyph and staging range stopped after the load at `$DE31`. That instruction reads the scroll staging buffer at `$5B00`, and `$DE34` writes the byte to the first screen matrix. The alternate destination path starts at `$DEB2` for the second matrix.
- The four level parts have their source payloads captured at `$C9B6`. The graphics byte counts and observed consumers are in the part facts.

## Controls

A stopping load watchpoint on `$DC00` caught `$22BB` reading the port 2 joystick. The next instruction was `$22BE` with A equal to `$E7` while right and fire were held. Both input bits were low in that read. The engine then inverts the byte and tests bit 4 for fire.

## Coverage and evidence

The engine and overlay listings are partial. Scope and exact remaining ledger counts are recorded in [TODO.md](TODO.md). The 60-verify sample is pending completion of the Step 50 ledger.
