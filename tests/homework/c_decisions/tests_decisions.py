import unittest
import sys
import os

# Add the folder that contains decisions.py to sys.path 
THIS_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(THIS_FILE_DIR, os.pardir, os.pardir, os.pardir))  # go up 3: c_decisions -> homework -> tests -> repo root
DECISIONS_DIR = os.path.join(REPO_ROOT, "src", "homework", "c_decisions")
if DECISIONS_DIR not in sys.path:
    sys.path.insert(0, DECISIONS_DIR)

from decisions import get_options_ratio, get_faculty_rating



class DecisionsTests(unittest.TestCase):
    def test_get_options_ratio_examples(self):
        self.assertAlmostEqual(get_options_ratio(9, 10), 0.90, places=4)
        self.assertAlmostEqual(get_options_ratio(17, 20), 0.85, places=4)
        self.assertAlmostEqual(get_options_ratio(3, 4), 0.75, places=4)
        self.assertAlmostEqual(get_options_ratio(13, 20), 0.65, places=4)
        self.assertAlmostEqual(get_options_ratio(59, 100), 0.59, places=4)

    def test_get_faculty_rating_table(self):
        # Per the assignment table
        self.assertEqual(get_faculty_rating(0.95), "Excellent")          # >= .9 and < 1
        self.assertEqual(get_faculty_rating(0.90), "Excellent")
        self.assertEqual(get_faculty_rating(0.85), "Very Good")          # > .8
        self.assertEqual(get_faculty_rating(0.80), "Good")               # > .7
        self.assertEqual(get_faculty_rating(0.75), "Good")
        self.assertEqual(get_faculty_rating(0.70), "Needs Improvement")  # > .6
        self.assertEqual(get_faculty_rating(0.65), "Needs Improvement")
        self.assertEqual(get_faculty_rating(0.60), "Unacceptable")       # 0 to .59
        self.assertEqual(get_faculty_rating(0.59), "Unacceptable")
        self.assertEqual(get_faculty_rating(0.00), "Unacceptable")


if __name__ == "__main__":
    unittest.main()
