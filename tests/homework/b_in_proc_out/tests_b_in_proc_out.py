import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from src.homework.b_in_proc_out.output import multiply_numbers


class TestMultiplyNumbersSpecific(unittest.TestCase):
    def test_seven_times_seven(self):
        result = multiply_numbers(7, 7)
        self.assertEqual(result, 49)
        print(f"7 * 7 = {result}")  # This print is for demonstration when running tests manually

    def test_five_times_five(self):
        result = multiply_numbers(5, 5)
        self.assertEqual(result, 25)
        print(f"5 * 5 = {result}")  # This print is for demonstration when running tests manually

if __name__ == '__main__':
    unittest.main()