import unittest
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.homework.b_in_proc_out.output import multiply_numbers, TAX_RATE, get_sales_tax_amount, get_tip_amount

class TestMultiplyNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_numbers(7, 7), 49)
        self.assertEqual(multiply_numbers(5, 5), 25)
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(-4, -5), 20)

    def test_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)
        self.assertEqual(multiply_numbers(10, 0), 0)
        self.assertEqual(multiply_numbers(0, 0), 0)

    def test_mixed_types(self):
        self.assertEqual(multiply_numbers(2.5, 4), 10.0)
        self.assertEqual(multiply_numbers(3, 2.5), 7.5)

class TestSalesTaxAndTip(unittest.TestCase):
    def test_get_sales_tax_amount_basic(self):
        self.assertAlmostEqual(get_sales_tax_amount(20.00), 1.35, places=2)

    def test_get_tip_amount_basic(self):
        self.assertAlmostEqual(get_tip_amount(20.00, 0.15), 3.00, places=2)

    def test_edges_zero(self):
        self.assertAlmostEqual(get_sales_tax_amount(0.0), 0.0)
        self.assertAlmostEqual(get_tip_amount(0.0, 0.20), 0.0)
        self.assertAlmostEqual(get_tip_amount(50.0, 0.0), 0.0)

    def test_tax_rate_constant_value(self):
        self.assertAlmostEqual(TAX_RATE, 0.0675)

if __name__ == '__main__':
    unittest.main()
