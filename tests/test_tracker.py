import unittest
from unittest.mock import patch
from tracker import validate_title, search_issues
import tempfile
from pathlib import Path


class TestValidation(unittest.TestCase):

    def test_valid_title(self):
        result = validate_title("   Login broken    ")

        self.assertEqual(result, "Login broken")


    def test_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            validate_title("    ")

class TestSearch(unittest.TestCase):

    def test_search_finds_matching_issue(self):
        issues = [
            {
                "title": "Login broken",
                "status": "open"
            },
            {
                "title": "Search broken",
                "status": "open"
            }
        ]

        with patch("tracker.load_issues", return_value=issues):
            results = search_issues("LOGIN")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Login broken")

    def test_search_returns_empty_list_when_no_match(self):
        issues = [
            {
                "title": "Login broken",
                "status": "open"
            }
        ]
        with patch("tracker.load_issues", return_value=issues):
            results = search_issues("xyz")

        self.assertEqual(results, [])