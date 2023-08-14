import unittest
from mhristev03_L8_L1 import bisection, f, f2

class TestBisectionMethod(unittest.TestCase):

    def test_zero_width_interval(self):
        with self.assertRaises(ValueError):
            bisection(10, 10, f)
            
    def test_same_sign_within_interval(self):
        with self.assertRaises(ValueError):
            bisection(10, 20, f)
            
    def test_max_iterations(self):
        with self.assertRaises(ValueError):
            bisection(1, 2, f, max_iterations=5)

    def test_function_f(self):
        root, iterations = bisection(1, 2, f)
        self.assertAlmostEqual(f(root), 8.77253711223602E-4, places=8)
        self.assertEqual(iterations, 9)

        root, iterations = bisection(10, -10, f)
        self.assertAlmostEqual(f(root), -0.004245794189046137, places=8)
        self.assertEqual(iterations, 14)
        
    def test_function_f_with_different_tol(self):
        root, iterations = bisection(10, -10, f, tol=0.0001)
        self.assertAlmostEqual(f(root), -0.00104432450896752, places=8)
        self.assertEqual(iterations, 17)
    
    def test_function_f2(self):
        root, iterations = bisection(1, 2, f2)
        self.assertAlmostEqual(f2(root), -0.002055356167718169, places=8)
        self.assertEqual(iterations, 9)

        root, iterations = bisection(1, -3, f2)
        self.assertAlmostEqual(f2(root), -7.07962920470696E-4, places=8)
        self.assertEqual(iterations, 11)
        
    def test_function_f2_with_different_tol(self):
        root, iterations = bisection(1, -10, f2, tol=0.0001)
        self.assertAlmostEqual(f2(root), -1.68919495379966E-4, places=8)
        self.assertEqual(iterations, 16)
        
