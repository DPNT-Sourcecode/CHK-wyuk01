from solutions.SUM import sum_solution
import unittest

class TestSum(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)

    def test_sum_incorrect_type(self):
        self.assertRaises(TypeError, sum_solution.compute, "2", 1)
        self.assertRaises(TypeError, sum_solution.compute, "2", "2")


