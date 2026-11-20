# Analysis history

- Booted the original cassette with the installed headless VICE and dummy audio. The first game snapshot and raster frame identified the IRQ chain. A second boot with a stopping checkpoint at `$4000` preserved the full handover.
- Decoded the loader's two short/long pulse streams per tape recording in `work/decode.py`. Checked their XORs and compared the payloads with RAM. This established one resident analysis image and a 48,896-byte starting scope for the ledger.
- Seeded Regenerator with VICE's executed-address map. Recovered the remainder of the code with a recursive walk that included the object, map command and IRQ dispatch targets. Counted the complete tape payload including fill-dominated gaps. Traced the relocated KERNAL vector bytes outside the payload to the ROM mirror.
- Completed the exact byte ledger before verification. Drew sample 1985 and corrected the seven held findings. Instruction probes and checkpoint counts are in `work/probe.txt` and `work/verify.txt` and summarized in [facts](facts.md).
