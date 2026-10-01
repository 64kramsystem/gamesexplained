"""An imported map must not turn omitted runtime buffers into instructions."""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "kit_symbols_import", Path(__file__).resolve().parents[1] / "scripts" / "symbols_import.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
project_blocks = module.project_blocks


class ProjectBlocksTests(unittest.TestCase):
    def test_partial_map_keeps_code_and_words_and_fills_runtime_gaps(self):
        blocks = project_blocks([
            {"start": 0x1020, "end": 0x1021, "type": "Word"},
            {"start": 0x1000, "end": 0x1005, "type": "Code"},
        ])
        self.assertEqual([(b["start"], b["end"], b["type_"]) for b in blocks], [
            (0, 0x0FFF, "DataByte"),
            (0x1000, 0x1005, "Code"),
            (0x1006, 0x101F, "DataByte"),
            (0x1020, 0x1021, "DataWord"),
            (0x1022, 0xFFFF, "DataByte"),
        ])

    def test_complete_map_is_preserved(self):
        blocks = project_blocks([
            {"start": 0, "end": 0xFFFF, "type": "Byte"},
        ])
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["type_"], "DataByte")

    def test_overlapping_map_is_rejected(self):
        with self.assertRaises(ValueError):
            project_blocks([
                {"start": 0, "end": 10, "type": "Code"},
                {"start": 10, "end": 20, "type": "Byte"},
            ])


if __name__ == "__main__":
    unittest.main()
