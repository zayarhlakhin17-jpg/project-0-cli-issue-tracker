import unittest
import tempfile

from pathlib import Path
from unittest.mock import patch
from storage import load_issues, save_issues
from tracker import search_issues

class TestStorage(unittest.TestCase):

    def test_save_them_load(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "issues.json"

            issues = [
                {
                    "title": "Login broken",
                    "status": "open"
                }
            ]

            save_issues(issues, file_path)

            loaded = load_issues(file_path)

            self.assertEqual(loaded, issues)


    def test_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "missing.json"

            loaded = load_issues(file_path)

            self.assertEqual(loaded, [])
            
    def test_broken_json_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "issues.json"

            file_path.write_text('{ "title": "Login broken", }')

            loaded = load_issues(file_path)

            self.assertEqual(loaded, [])

    def test_search_is_case_insensitive(self):
        issues = [
            {
                "title": "Login broken",
                "status": "open"
            }
        ]

        with patch("tracker.load_issues", return_value=issues):
            results = search_issues("LOGIN")

        self.assertEqual(len(results), 1)