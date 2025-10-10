import unittest
import sys
import os

# Add the folder that contains value_return_functions.py to sys.path
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(THIS_DIR, os.pardir, os.pardir, os.pardir))
EFUNC_DIR = os.path.join(REPO_ROOT, "src", "homework", "e_functions")
if EFUNC_DIR not in sys.path:
    sys.path.insert(0, EFUNC_DIR)

from value_return import (
    get_gross_pay,
    get_fica_tax,
    get_federal_tax,
    FICA_RATE,
    FEDERAL_RATE,
)

class Test_Config(unittest.TestCase):
    def test_gross_pay_regular(self):
        self.assertAlmostEqual(get_gross_pay(30, 10), 300.00, places=2)
        self.assertAlmostEqual(get_gross_pay(40, 10), 400.00, places=2)

    def test_gross_pay_overtime(self):
        # 45 hours @ $10 => 40*10 + 5*15 = 400 + 75 = 475
        self.assertAlmostEqual(get_gross_pay(45, 10), 475.00, places=2)
        # another case
        self.assertAlmostEqual(get_gross_pay(41, 20), 40*20 + 1*30, places=2)

    def test_fica_tax(self):
        # Example row: gross 400 -> FICA 400*0.0765 = 30.6
        self.assertAlmostEqual(get_fica_tax(400), 30.60, places=2)
        self.assertAlmostEqual(get_fica_tax(475), 475 * FICA_RATE, places=2)
        self.assertAlmostEqual(get_fica_tax(300), 22.95, places=2)

    def test_federal_tax(self):
        # Example row: gross 400 -> Federal 400*0.08 = 32
        self.assertAlmostEqual(get_federal_tax(400), 32.00, places=2)
        self.assertAlmostEqual(get_federal_tax(475), 475 * FEDERAL_RATE, places=2)
        self.assertAlmostEqual(get_federal_tax(300), 24.00, places=2)

if __name__ == "__main__":
    unittest.main()
