import unittest
from main import bisection_method, f

class TestBisection(unittest.TestCase):
        
    def first_test_bisection(self):
        result = bisection_method(1, 2, f)
        self.assertAlmostEqual(f(result), 1.1542, places=4)