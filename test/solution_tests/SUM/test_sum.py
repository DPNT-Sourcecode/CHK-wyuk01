from solutions.SUM import sum_solution
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        self.assertRaises(TypeError, sum_solution.compute("2", 1))

