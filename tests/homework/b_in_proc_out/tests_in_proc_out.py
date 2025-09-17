import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

import unittest
from homework.b_in_proc_out.output import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_7x7(self):
        self.assertEqual(multiply_numbers(7, 7), 49)

    def test_5x5(self):
        self.assertEqual(multiply_numbers(5, 5), 25)

    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertEqual(multiply_numbers(5, 0), 0)

    def test_negative(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(2, -3), -6)
        self.assertEqual(multiply_numbers(-2, -3), 6)

if __name__ == "__main__":
    unittest.main()