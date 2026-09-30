"""The Firefox launcher confines its profile and writable paths."""
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import tools

class BrowserTests(unittest.TestCase):
    def test_profile_and_environment_are_local(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(tools, 'TOOLS', folder), patch.object(tools, 'LOGS', folder), patch.object(tools.shutil, 'which', return_value='/usr/bin/firefox'), patch.object(tools, 'up', return_value=False), patch.object(tools, 'start') as start:
                tools.browser()
                args, kw = start.call_args
                command = args[0]
                self.assertEqual(command[command.index('--profile') + 1], str(Path(folder)/'firefox/profile'))
                for name in ['XDG_CONFIG_HOME', 'XDG_STATE_HOME', 'XDG_CACHE_HOME', 'XDG_DATA_HOME', 'TMPDIR']:
                    self.assertTrue(Path(kw['env'][name]).is_relative_to(folder))
                self.assertIn('--no-remote', command)
                self.assertEqual(kw['env']['MOZ_CRASHREPORTER_DISABLE'], '1')

    def test_occupied_port_does_not_start_another_browser(self):
        with patch.object(tools.shutil, 'which', return_value='/usr/bin/firefox'), patch.object(tools, 'up', return_value=True), patch.object(tools, 'start') as start:
            with self.assertRaises(SystemExit): tools.browser()
            start.assert_not_called()

if __name__ == '__main__': unittest.main()
