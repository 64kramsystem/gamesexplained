# Freddy Hardest (C64) facts

Two separate packed disk programs implement the surface and the base.
The base's access-code form compares five digits at its own `$0FFE`.
The [base facts](parts/base/facts.md) give the comparison and its
instruction watchpoint. The [surface facts](parts/surface/facts.md)
give its scroll format, IRQ phases and input trace.

Both render the small title font as VIC character codes and maintain an
in-memory SID register shadow during gameplay. The surface writes the
shadow from `$3B50` at `$C3F6`. The base writes it from `$3A49`
at `$AFB8`. Each copy writes 25 consecutive registers from `$D400`.
Both loads contain their own glyph and sprite banks. Their bytes
differ across corresponding regions. The title and gameplay
screen matrices, map cursor and IRQ vector addresses are local to each
part. See the respective part for their meanings.

The retained asset loaders at surface `$09C4` and base `$0960`
call KERNAL SETNAM and LOAD for named resources, including C.B, C.A and
PIC. Those names are missing from this input disk's directory. The
disk's three actual entries are accounted for in `media.json`.
The packed route above reaches gameplay without using those directory
names. The original file-to-RAM mapping is open.

## Loading picture fragments

The standalone `FREDDY HARDEST` file displays the loading illustration
from VIC bank `$C000`. The stopped display had `$19` at `$D018`
and multicolour bitmap mode enabled. Rendering its RAM at
`$E000–$FF3F` as VIC bitmap cells recovers the title, faces and
credits. Rendering each gameplay hand-over at `$2000–$3F3F` shows
parts of the same composition between gameplay tables.

The base fragment at `$35B8–$3A1F` matches 1,110 of 1,128 bytes
at the corresponding offset in the standalone loader. The entire
`$3CAB–$3F3D` fragment matches between the surface and base, and 627
of its 659 bytes match the loader. In the base, the 63 bytes after
`$3B2D` and the 63 bytes after `$3C08` match the illustration exactly.
The individual workspace bytes at `$3B2D` and `$3C08` are updated by
the game. The listings identify these surviving picture fragments and
the gameplay variables between them.

## The listing's error rate

The independent gpt-6.2-sol sample drew 60 of 412 comments with seed
1987 and found 13 wrong (21.7%, with a Wilson 95% interval of 13.1% to
33.6%). The checker may have missed other errors. The run corrected all
13 findings, which concerned routine boundaries, branch conditions,
copy lengths, sprite axes, glyph ranges and a generated-value routine.
Related corrections cover the corresponding base panel copy and the
paired sprite paths. A full audit followed by a fresh sample is pending.
