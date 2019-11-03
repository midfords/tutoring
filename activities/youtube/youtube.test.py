import unittest
from youtube import find_added_items
from youtube import find_missing_items
from youtube import find_renamed_items

class TestYoutubeDiff(unittest.TestCase):

    def setUp(self):
        self.old_items = [
            ["", "00000000000", "Item 0"],
            ["", "00000000001", "Item 1"],
            ["", "00000000002", "Item 2"],
            ["", "00000000003", "Item 3"],
            ["!", "00000000004", "Item 4"]
        ]
        self.new_items = {
            "00000000000": "Item 0 (New)",
            "00000000001": "Item 1",
            "00000000002": "Item 2",
            "00000000005": "Item 5"
        }

    def test_added_items(self):
        expected_result = [
            ("00000000005", "Item 5")
        ]
        expected_old = [
            ["", "00000000005", "Item 5"],
            ["", "00000000000", "Item 0"],
            ["", "00000000001", "Item 1"],
            ["", "00000000002", "Item 2"],
            ["", "00000000003", "Item 3"],
            ["!", "00000000004", "Item 4"]
        ]
        actual = find_added_items(self.old_items, self.new_items)

        self.assertEqual(expected_result, actual)
        self.assertEqual(expected_old, self.old_items)

    def test_added_items_empty(self):
        expected_result = [
            ("00000000000", "Item 0 (New)"),
            ("00000000001", "Item 1"),
            ("00000000002", "Item 2"),
            ("00000000005", "Item 5")
        ]
        expected_old = [
            ["", "00000000000", "Item 0 (New)"],
            ["", "00000000001", "Item 1"],
            ["", "00000000002", "Item 2"],
            ["", "00000000005", "Item 5"]
        ]
        self.old_items = []
        actual = find_added_items(self.old_items, self.new_items)

        self.assertEqual(expected_result, actual)
        self.assertEqual(expected_old, self.old_items)

    def test_missing_items(self):
        expected_result = [
            ("00000000003", "Item 3")
        ]
        expected_old = [
            ["", "00000000000", "Item 0"],
            ["", "00000000001", "Item 1"],
            ["", "00000000002", "Item 2"],
            ["!", "00000000003", "Item 3"],
            ["!", "00000000004", "Item 4"]
        ]
        actual = find_missing_items(self.old_items, self.new_items)

        self.assertEqual(expected_result, actual)
        self.assertEqual(expected_old, self.old_items)

    def test_missing_items_empty(self):
        expected_result = []
        expected_old = []
        self.old_items = []
        actual = find_missing_items(self.old_items, self.new_items)

        self.assertEqual(expected_result, actual)
        self.assertEqual(expected_old, self.old_items)

    def test_renamed_items(self):
        expected_result = [
            ("00000000000", "Item 0", "Item 0 (New)"),
        ]
        expected_old = [
            ["", "00000000000", "Item 0"],
            ["", "00000000001", "Item 1"],
            ["", "00000000002", "Item 2"],
            ["", "00000000003", "Item 3"],
            ["!", "00000000004", "Item 4"]
        ]
        actual = find_renamed_items(self.old_items, self.new_items)

        self.assertEqual(expected_result, actual)
        self.assertEqual(expected_old, self.old_items)

    def test_renamed_items_empty(self):
        expected_result = []
        expected_old = []
        self.old_items = []
        actual = find_renamed_items(self.old_items, self.new_items)

        self.assertEqual(expected_result, actual)
        self.assertEqual(expected_old, self.old_items)

if __name__=='__main__':
    unittest.main()
