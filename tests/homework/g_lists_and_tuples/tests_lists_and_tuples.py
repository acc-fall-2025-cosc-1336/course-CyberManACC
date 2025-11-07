import os, sys
_here = os.path.abspath(os.path.dirname(__file__))
_root = os.path.abspath(os.path.join(_here, "..", "..", ".."))
if _root not in sys.path:
    sys.path.insert(0, _root)

import unittest
from src.homework.g_lists_and_tuples.lists import (
    get_lowest_list_value,
    get_highest_list_value,
)

class Test_Config(unittest.TestCase):
    def test_get_lowest_list_value(self):
        data = [8, 10, 1, 50, 20]
        self.assertEqual(get_lowest_list_value(data), 1)

    def test_get_highest_list_value(self):
        data = [8, 10, 1, 50, 20]
        self.assertEqual(get_highest_list_value(data), 50)

if __name__ == "__main__":
    unittest.main(verbosity=2)
