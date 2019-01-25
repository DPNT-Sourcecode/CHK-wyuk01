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
        for remover_product, (quantity_needed, product_to_remove, quantity_to_remove) \
                in checkout_solution.REMOVERS.iteritems():
            input = remover_product * quantity_needed

        self.assertEqual(checkout_solution.checkout("EEB"), checkout_solution.checkout("EE"))