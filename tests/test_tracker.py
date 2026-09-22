import unittest
from unittest.mock import patch
from tracker import validate_title, search_issues, close_issue, update_issue
import tempfile
from pathlib import Path
from unittest.mock import patch


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


    def test_close_matching_issue(self):
        issues = [
            {
                "title": "Login broken",
                "status": "open"
            }
        ]
        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                result = close_issue("Login broken")

            self.assertEqual(result["status"], "closed")
            mock_save.assert_called_once_with(issues)


    def test_close_missing_issue_raises_error(self):
        issues = [
        {
            "title": "Login broken",
            "status": "open"
        }
    ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    close_issue("Database broken")

        mock_save.assert_not_called()



    def test_close_duplicate_titles_raises_error(self):
        issues = [
            {
                "title": "Login broken",
                "status": "open"
            },
            {
                "title": "Login broken",
                "status": "open"
            }
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    close_issue("Login broken")

        mock_save.assert_not_called()


    def test_close_already_closed_raises_error(self):
        issues = [
            {
                "title": "Login broken",
                "status": "closed"
            }
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    close_issue("Login broken")

        mock_save.assert_not_called()




class TestUpdateIssue(unittest.TestCase):

    def test_update_matching_issue(self):
        issues = [
            {"title": "Login broken", "status": "open"}
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                result = update_issue(
                    "Login broken",
                    "Login page broken"
                )

        self.assertEqual(result["title"], "Login page broken")
        self.assertEqual(result["status"], "open")
        mock_save.assert_called_once_with(issues)


    def test_update_missing_issue_raises_error(self):
        issues = [
            {"title": "Login broken", "status": "open"}
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    update_issue(
                        "Does not exist",
                        "New title"
                    )

        mock_save.assert_not_called()


    def test_update_duplicate_titles_raises_error(self):
        issues = [
            {"title": "Login broken", "status": "open"},
            {"title": "Login broken", "status": "closed"}
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    update_issue(
                        "Login broken",
                        "New title"
                    )

        mock_save.assert_not_called()


    def test_update_empty_new_title_raises_error(self):
        issues = [
            {"title": "Login broken", "status": "open"}
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    update_issue(
                        "Login broken",
                        "     "
                    )

        mock_save.assert_not_called()


    def test_update_same_title_raises_error(self):
        issues = [
            {"title": "Login broken", "status": "open"}
        ]

        with patch("tracker.load_issues", return_value=issues):
            with patch("tracker.save_issues") as mock_save:
                with self.assertRaises(ValueError):
                    update_issue(
                        "Login broken",
                        "LOGIN BROKEN"
                    )

        mock_save.assert_not_called()