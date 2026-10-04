#!/usr/bin/env python3
"""The narration rule reads the agent's words, not the text the game prints (#145)."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_docs  # noqa: E402


def narrations(line):
    """How many lines of a facts.md holding this one line check_docs.py fails."""
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / 'facts.md'
        f.write_text(line + '\n', encoding='utf-8')
        with contextlib.redirect_stdout(io.StringIO()):
            return check_docs.scan(str(f), check_docs.NARRATION, 'narration', blank=check_docs.GAME_TEXT)


class GameText(unittest.TestCase):
    def test_quoted_as_the_game_prints_it(self):
        for line in ('The terminal prints "ORIENTATION CORRECTED" after the puzzle.',
                     'The terminal prints ORIENTATION CORRECTED after the puzzle.',
                     'The terminal prints “Orientation corrected” after the puzzle.',
                     'The variable `corrected` holds it.'):
            self.assertEqual(narrations(line), 0, line)

    def test_the_agents_own_words_still_fail(self):
        for line in ('The label was corrected after the trace.',
                     'We corrected the "ROOM" name after the trace.',
                     'A 5.25" disk; the earlier reading was wrong.',
                     'This was wrong: "OK" is printed twice.'):
            self.assertEqual(narrations(line), 1, line)


if __name__ == '__main__':
    unittest.main()
