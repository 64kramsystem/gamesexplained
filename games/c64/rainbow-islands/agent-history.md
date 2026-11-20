# Analysis history

Booted the Powers of Pain D64 using the prepared headless VICE with
dummy audio. Autostart initially appeared to hang in KERNAL serial
transfer, but PC samples in the serial routine and the load's growing
RAM contents showed progress. Port 1 fire dismissed the crack intro.
F7 and F1 started the game through the keyboard matrix.

The Powers of Pain disk's directory lacked 11 and 21. Forced island
selection with the disk still mounted hit the retry loop while the
filename bytes read 31 31. Byte comparison established that all
thirteen common numbered files match the Saigon release, so the
numbered loads use it as the data disk. An early breakpoint fixture
called the loader alone and returned past the round setup. The
replacement fixture set the saved player record and entered at
$4037 so the native procedure handled both loading and round setup.

The ending was captured after a breakpoint at $0810. A frame capture
made during depacking showed flashing stripes, so the listing uses
the post-depack image.

The resident and ending sound drivers pair instruction for instruction
between $FA14–$FFF9 and $0E69–$144E, respectively. The pairing found
677 instructions on each side. Its branch-target and immediate-value
differences were inspected before carrying the shared notes. The
coverage pass treated the resident panel characters and sprites in
physical RAM under I/O as authored bytes.

An independent sample measured five wrong details in 95 comments.
Instruction stops confirmed the attract credit result, the cast
effect's spawn-record read, and the island height load and store.
The two ending pattern findings changed the whole comment template so
it describes inherited instrument state correctly. The later movement
control runs corrected the vertical and horizontal decode table names.
