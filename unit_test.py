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
        with patch("builtins.input", return_value = ["Dungeon Crawler Carl",
                                                      "Matt Dinniman",
                                                      "2020"]):
            add_book()
        self.assertEqual(library, [{"title" : "Dungeon Crawler Carl",
                                    "author" : "Matt Dinniman",
                                    "year_published" : "2020"}])


if __name__ == "__main__":
    unittest.main()