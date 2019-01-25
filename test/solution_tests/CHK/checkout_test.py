from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    def test_invalid_type_gives_minus_one(self):
        self.assertEqual(checkout_solution.checkout(1), -1)

    def test_invalid_sku_gives_minus_one(self):
        self.assertEqual(checkout_solution.checkout("F"), -1)

    def test_valid_sku_gives_correct_price(self):
        for product, price_quantities in checkout_solution.PRICES.iteritems():
            self.assertEqual(checkout_solution.checkout(product), price_quantities[1])