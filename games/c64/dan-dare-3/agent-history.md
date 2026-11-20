# Analysis history

The D64 was loaded in an existing headless VICE build on the batch's assigned ports. A first execution map mixed BASIC, the crack intro, decompression and game code. The committed map starts after clearing the access record in the opening cell. The first gameplay capture was still drawing the display, so the listing uses the later settled capture. The title snapshot retains title data overwritten by room setup.

A stopping range watch at the top of RAM was followed by a VICE exit. After restart, a stopping watch on the single address $FFFE reliably captured the IRQ sequence. Snapshot restores precede checkpoint creation.

Step 65 did not produce an input recording. The checks use individual inputs and stopping instruction or memory checkpoints from a local snapshot, with no route used as evidence.

The restored worktree had the committed symbol map, listing and reference captures. Its ignored media, snapshots and annotation log were missing. The D64 was recovered by hash and the play snapshot rebuilt. The previous listing and the recovered snapshot agreed except for 22 runtime records, including a patched rifle dispatch operand.

A breakpoint before the loader's final RTI at $01E4 and a one-instruction step identified $0600 as the game entry. A subsequent stopping checkpoint at $0600 gave a snapshot that reloaded at that PC. Saving immediately after the single step had instead resumed briefly and captured PC $48E1. The checkpoint-based capture is the hand-over used by the listing's loaded-data audit.

The resumed work stayed in step 50. Targeted execution and store checkpoints distinguished the startup colour plane from the machine code already at $0200 on hand-over, established the metatile descriptor read and located the VIC sprite images beneath I/O. The two snapshots preserve the transient startup code and the later state of the resident game.

A further coverage pass typed the entity dispatch tables and their callbacks, the coordinate probes, and the equipment and panel graphics. The controlled VICE probes stopped after the equipment bitmap store and at the callback selected by a patched jump. A cold RAM read at $A200 showed only the power-on pattern. In two boots a store watch caught the first unpacker's store at $012B and a later copy at $081E. The final $BC fill has a different value from either observed store, so the range remains unclassified.

The assigned ports in the restored launcher were 23072 for VICE and 23074 for regenerator2000. The older regenerator2000 session on 17418 was preserved. The assigned disassembler was rebuilt from the existing exported map and play snapshot. Re-export retained every committed address that held a user label or a line comment. The project rebuilt from the new export is `work/play-handoff.regen2000proj`. The separate hand-over candidate in `work/entry-analysis/` is reproducible with `work/make-entry-candidate.py` and the kit import, export and listing commands.

The main play listing reached equality in the exported byte ledger after the room, sound and raster tables, generated workspace and operand aliases were described. A printed 100.0% still left twelve one-byte descriptors bare before the last export. The listing’s uncounted section was empty. Earlier annotations remain in the original play address space.

The two saved program states reuse several CPU addresses. In the hand-over image $0200 contains a CIA 2 monitor and the $0400 matrix contains a P. D. Systems copyright line. Startup replaces these bytes with terrain colours. The keyboard setup and title SID player also occupy RAM that play repurposes. `work/handover-overlay/` holds the supplementary symbol export, listing and ledger for these ranges and the original packed terrain and effects source, reproducible with `work/build-handover-overlay.py`, `symbols_import.py`, `symbols_export.py --project` and `listing.py` on `work/entry.vsf`. The disk has one resident program load, so these alternate address meanings do not get separate media parts.

The verification sample on the expanded play export used seed 191136. All seven findings held when read against the code. The evidence for the mechanic checks is in `work/verify-local-mechanics.log`. The inputs were isolated control samples or injected test state, so step 65 did not require a recorded route.
