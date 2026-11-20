# Dragon's Lair — agent history

The analysis used the alternate Software Projects disk with LA–LJ entries. A cracked build used to diagnose startup carried a third-party intro and differently named USR files. That comparison copy remained in ignored work storage. The final part captures use the alternate disk and the game's own loader.

The assigned VICE v3.14.0 headless build ran with dummy audio. The emulator qualification reported 56 passes and two failures. Host-key injection failed and its final monitor probe raised a checkpoint-list exception. The instruction-step, execution-stop and load/store-watch checks passed. Scene analysis used direct joystick input and instruction stops on the assigned VICE port. The installed Regenerator2000 0.9.18 responded on the assigned disassembler port. The kit exporter reads the local projects for the individual snapshots.

The first ledger covered the resident, title and nine scene images. The second platform descent initially appeared to own a different graphics bank. A checkpoint after its scene-local unpacking showed equality with the first bank through $7DFF and changes only in the final glyph pages. The second descent now inherits the shared region from the first one. The handoff includes both its entry and prepared snapshots.

The resumed step-50 pass stepped the dragon palette copy, bitmap strip copies and five self-modifying raster jumps, then used the jump destinations to recover the omitted code. The second-descent instruction probes stepped the matrix decoder and the collision read. Their logs and scripts are under the game's ignored work directory.

The staging audit matched decoded LH bytes against the post-LI snapshot and checked the patched source operands and their pointer tables. Four compressed-only ranges map to still-present unpacked bytes. The earlier staging, the raw image and palette spans and the compressed tail whose output LI overwrites remain in the part ledger.

The resident pass stepped the port 2 input tests for the initials editor, including the idle path. The trace is in the ignored work directory as `resume-score-editor.log`. The resident re-export also describes the score display and the SID voice-buffer dispatch.

The Ramps section trace entered the existing draw routine with section selectors 1 through 9 and stopped immediately after each decoder call. The ending source and destination pointers in `resume-ramp-records.log` establish the authored record boundaries.

The dragon variant probe stepped the patched bitmap and colour loads for selectors 1, 2 and 5 and compared the final bitmap strip at the destination. The source intervals in `resume-dragon-bitmap-variants.log` show where an operand spans the LI boundary or reads retained LH staging.

The resume traced the second descent overlay readers and matrix-cycle decrement, the Ramps up-input sprite write, the Burning Ropes template copy, the Phantom Knight glyph copy and the dragon raster pointer update and ending jump. The controlled probes and their results are in ignored work as `resume_descent_overlay_bounds.py` and `resume-descent-overlay-bounds.log`. The probes began from the saved scene snapshots and set the registers or flags needed for the tested instruction paths.

The Ramps state annotations initially reached into the retained Weapons Room region after the last known flag. Single-byte block boundaries now constrain those comments to their evidence. The first-descent sprite regions were split at the ledger's ownership limit. All eleven symbols files were exported from their local projects and the listings rebuilt from their saved snapshots.

A second Burning Ropes pass stepped the stores that install the next raster handler at $2C61, $2C91 and $2CA7. Those addresses seeded the recursive disassembly. The repaint destination and character tables were bounded by their indexed readers. A controlled run of the final packed token advanced the loader's pointers to $A7A2 and $7FFF, confirming the following literal is clipped. The rebuilt part ledger explains 20,964 of 20,964 tracked bytes.

The resident pass recovered the failure interstitial, alternate sprite setup and shared sprite mirroring. The probe stepped the final score reset store and the first mirrored sprite store. Rebuilding the listings after exporting the resident names refreshed the calls from its scene overlays.

The resumed coverage pass traced the raster vector stores in Weapons Room, Tentacle Room and Skull Hallway. In Skull Hallway the fifth handler pointed to $2C69, which replaced an earlier disassembly seed inside a store operand. The Weapons Room and Ramps sprite-builder test reached the pixel stores with index 5. A separate run checked the overlapping index-3 shape record in Weapons Room, Skull Hallway and Tentacle Room. Exact byte comparisons located the matching overlay data and retained instruction fragments in the resident image.

The title follow-up began from the pre-relocation snapshot and entered the relocation at $9F00. An execution stop at $45A0 confirmed the first story-row read, and the glyph copy at $2800 matched its source at $5000. The title ledger gained 3,035 tracked bytes. A standalone title ledger also exposed staging and other regions shared with later images. The title retains its resident inheritance. The full boot payload still needs an address-by-address ownership audit across the relocation.

Other focused probes stepped the first-descent fire branch and overlay read, the Weapons Room cell animation, the four Phantom Knight direction cases and both short dragon bitmap variants. Their scripts and results are in ignored work. All eleven local projects were exported and all listings rebuilt from their established snapshots.

The retained projectile instructions in the Ramps match the Weapons Room bytes from $2A35 onward. The first address is part of an overwritten store. The final pass separated that partial instruction from the complete retained routines and matched the $5D13 sprite fragment with the Weapons Room bank. The Phantom Knight target lookup verified the ten-byte row stride at $27B4. In the resident interstitial a load watch over $37FA–$39FF did not fire before the setup returned, so the range remains open.

The next pass decoded the resident block at $37FA as a zero-run stream and matched all 692 output cells to the first-descent ending matrix. The Weapons Room read at $26DE identified the retained screen patch at $31AB. Further VICE probes checked the title relocation store at $C071, first-descent matrix and vertical-offset branches and the Tentacle Room sprite instructions. The probe scripts, exports and full ledger queues remain in ignored work.


The final step-50 pass matched the retained Tentacle Room and Phantom Knight records against the source room bytes, measured the descent overlay boundaries, and decoded the packed dragon staging slices against their preserved output. VICE instruction probes identified the Ramps hazard hit frame and its divider, the descent transition writes, the raster and bitmap state bytes and the score-shift destination. The probes and output remain in ignored work.

Step 60 used an independent gpt-6.2-sol sample check. All five wrong details held against the code. The verification instructions and watchpoints are in `work/verify-handoff.log`. The code census of the numbered loader found the resident and Dragon calls. The Dragon ending probe reached the score path and the tested LJ header produced the first-scene fallback when forced into the numbered dispatcher.

Step 65 required no recording. The existing scene selections and controlled instruction probes support claims about what the code does when entered. They do not assert full-play reachability of a new route or serve as a replay for a port.
