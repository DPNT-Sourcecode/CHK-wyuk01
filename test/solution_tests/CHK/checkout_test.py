from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    def test_invalid_type_gives_minus_one(self):
        self.assertEqual(checkout_solution.checkout(1), -1)

    def test_invalid_sku_gives_minus_one(self):
        self.assertEqual(checkout_solution.checkout("F"), -1)

    def test_sum_correct(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)
        self.assertEqual(sum_solution.compute(0, 2), 2)
        self.assertEqual(sum_solution.compute(0, 100), 100)

    def test_sum_incorrect_type_raises_type_error(self):
        self.assertRaises(TypeError, sum_solution.compute, "2", 1)
        self.assertRaises(TypeError, sum_solution.compute, "2", "2")

    def test_sum_incorrect_value_raises_value_error(self):
        self.assertRaises(ValueError, sum_solution.compute, -1, -1)
        self.assertRaises(ValueError, sum_solution.compute, 20, -1)
        self.assertRaises(ValueError, sum_solution.compute, 100, 200)