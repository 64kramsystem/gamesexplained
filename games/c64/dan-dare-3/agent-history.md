# Analysis history

The D64 was loaded in an existing headless VICE build on the batch's assigned ports. A first execution map mixed BASIC, the crack intro, decompression and game code. The committed map starts after clearing the access record in the opening cell. The first gameplay capture was still drawing the display, so the listing uses the later settled capture. The title snapshot retains title data overwritten by room setup.

A stopping range watch at the top of RAM was followed by a VICE exit. After restart, a stopping watch on the single address $FFFE reliably captured the IRQ sequence. Snapshot restores precede checkpoint creation.

Step 65 did not produce an input recording. The checks use individual inputs and stopping instruction or memory checkpoints from a local snapshot, with no route used as evidence.
