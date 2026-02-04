"""
Testing personal library code
Tester: Luke Wieder
"""

import unittest
from unittest.mock import patch
from io import StringIO

from assignment_2 import (
    add_book,
    remove_book,
    update_book,
    list_all_books,
    search,
    show_stats
)

# Test class
class TestPersonalLibrary(unittest.TestCase):
    # Test case for add book function
    def test_add_book_normal_case(self):
        library = []
        with patch("builtins.input", return_value = "Dungeon Crawler Carl"):
            add_book(library)
        self.assertEqual(library, ["Dungeon Crawler Carl"])


if __name__ == "__main__":
    unittest.main()