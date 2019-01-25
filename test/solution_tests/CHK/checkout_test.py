from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    def test_invalid_type_gives_minus_one(self):
        self.assertEqual(checkout_solution.checkout(1), -1)

    def test_invalid_sku_gives_minus_one(self):
        self.assertEqual(checkout_solution.checkout("G"), -1)

    def test_valid_sku_gives_correct_price(self):
        for product, price_quantities in checkout_solution.PRICES.iteritems():
            self.assertEqual(checkout_solution.checkout(product), price_quantities[1])

    def test_valid_remover_correctly_removes(self):
        self.assertEqual(checkout_solution.checkout("EEB"), checkout_solution.checkout("EE"))
        self.assertEqual(checkout_solution.checkout("FFF"), checkout_solution.checkout("FF"))