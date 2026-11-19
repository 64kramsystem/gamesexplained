# Analysis history

- Captured the unpacker's final stream at `$01B9`, the clean trainer hand-over at `$11C0`, the title and four driving states. Raw image, snapshots, annotation inputs and traces remain in ignored `work/`.
- The first screenshots during road initialization still showed GET READY and a dashboard without the road. Continued to the valid play milestone, where the object script at `$1445` stores one to `$19D7`.
- After a full-frame capture stopped VICE at an instruction-step call, restarted the installed headless build and used targeted execution checkpoints.
- Rebuilt the disassembler from the committed symbols and verified the hand-over listing reproduced byte for byte. Narrow watches separated the title frame and row-helper accesses from their adjacent retained bytes. Traced the final depacker's store at the remaining range boundaries and kept those bytes in the ledger. The paused-snapshot probes capture the character and dashboard bounds and the SID effect path in `work/resume-verify.txt`.
