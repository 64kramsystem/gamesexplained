# Analysis history

On 19 November 2026 the two packed gameplay entries booted separately
on the assigned headless C64 tools. The analyzed RAM states were saved
without ROMs. Executed-address maps seeded Regenerator2000. Each listing
was generated from the same snapshot used by its disassembler.

The core coverage loop identified the main video, input, map and sound
paths and the large authored graphics banks. Targeted instruction and
memory watch tests pinned down the base access-code accept store and
the surface port-2 poll. The disk inventory is closed against the
three PRGs in the input release.
