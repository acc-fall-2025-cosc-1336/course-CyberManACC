import unittest
import sys, os
from pathlib import Path

# Make 'src' importable without __init__.py packages
SRC = Path(__file__).resolve().parents[3] / "src"
sys.path.insert(0, str(SRC))

from homework.c_decisions.decisions import (
    get_letter_grade_if,
    get_letter_grade_switch,
    get_letter_grade,
)

class TestDecisions(unittest.TestCase):
    def test_get_letter_grade_if(self):
        self.assertEqual(get_letter_grade_if(95), "A")
        self.assertEqual(get_letter_grade_if(85), "B")
        self.assertEqual(get_letter_grade_if(75), "C")
        self.assertEqual(get_letter_grade_if(65), "D")
        self.assertEqual(get_letter_grade_if(50), "F")

    def test_get_letter_grade_switch(self):
        self.assertEqual(get_letter_grade_switch(95), "A")
        self.assertEqual(get_letter_grade_switch(85), "B")
        self.assertEqual(get_letter_grade_switch(75), "C")
        self.assertEqual(get_letter_grade_switch(65), "D")
        self.assertEqual(get_letter_grade_switch(50), "F")

    def test_out_of_range_raises(self):
        for bad in (-1, 101, 1000):
            with self.assertRaises(ValueError):
                get_letter_grade_if(bad)
            with self.assertRaises(ValueError):
                get_letter_grade_switch(bad)
            with self.assertRaises(ValueError):
                get_letter_grade(bad)

if __name__ == "__main__":
    unittest.main()
