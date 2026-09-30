#!/usr/bin/env python3
"""Synthetic importer checks: occupants, gaps, labels and banked references."""
import json
from pathlib import Path
import tempfile
import unittest

from import_ghidra import parse, convert


class ImportTests(unittest.TestCase):
    def parse_text(self, text, space=''):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'export.txt'
            path.write_text(text)
            return parse(path, space)

    def test_selected_occupant_and_unknown_gaps(self):
        rows = self.parse_text("                ; Entry description.\nstart:\n2000 a901 LDA #1\n2002 60 RTS\n2003 ?? ??\nPHASE::2000 a902 LDA #2\n")
        self.assertEqual([r['b'] for r in rows], [[0xa9, 1], [0x60]])
        game = {'platform': 'c64', 'slug': 'fixture', 'build': 'synthetic'}
        sym = json.loads(convert(rows, game, 'synthetic'))
        self.assertEqual(sym['blocks'], [{'start': 0x2000, 'end': 0x2002, 'type': 'Code'}])
        self.assertEqual(sym['comments'][0]['text'], 'Entry description.')
        self.assertNotIn('records', sym)
        self.assertNotIn('spans', sym)

    def test_overlay_is_explicit(self):
        rows = self.parse_text('2000 01 byte 1\nPHASE::2000 02 byte 2\n', 'PHASE')
        self.assertEqual(rows[0]['b'], [2])

    def test_call_target_starts_a_routine(self):
        rows = self.parse_text('2000 201020 JSR sub\nsub:\n2010 60 RTS\n')
        game = {'platform': 'c64', 'slug': 'fixture', 'build': 'synthetic'}
        sym = json.loads(convert(rows, game, 'synthetic'))
        self.assertEqual(sym['symbols'][0]['type'], 'Subroutine')

    def test_overlap_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Overlapping'):
            self.parse_text('2000 a901 LDA #1\n2001 01 byte 1\n')

    def test_cli_writes_only_symbols(self):
        import subprocess, sys
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / 'game.json').write_text(json.dumps({'platform': 'c64', 'slug': 'fixture', 'build': 'synthetic'}))
            export = base / 'export.txt'
            export.write_text('start:\n2000 60 RTS\n')
            listing = base / 'listing.json'
            listing.write_text('existing listing')
            script = Path(__file__).with_name('import_ghidra.py')
            subprocess.run([sys.executable, str(script), str(base), str(export)], check=True, capture_output=True)
            self.assertEqual(listing.read_text(), 'existing listing')
            self.assertTrue((base / 'symbols.json').exists())


if __name__ == '__main__':
    unittest.main()
