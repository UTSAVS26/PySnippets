import unittest

from pysnippets.maths.fibonacci_sequence import (
    fibonacci_sequence, fibonacci_recursive, fibonacci_memoized, 
    fibonacci_generator, fibonacci_negative, fibonacci_custom_start,
    fibonacci_ratio, fibonacci_list_or_tuple, fibonacci_sum,
    fibonacci_module, nth_fibonacci
)

class TestFibonacciSequence(unittest.TestCase):
    
    def test_fibonacci_sequence_count(self):
        self.assertEqual(fibonacci_sequence(count=10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_fibonacci_sequence_max_value(self):
        self.assertEqual(fibonacci_sequence(max_value=20), [0, 1, 1, 2, 3, 5, 8, 13])
    
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(10), 55)
    
    def test_fibonacci_memoized(self):
        self.assertEqual(fibonacci_memoized(10), 55)
    
    def test_fibonacci_generator(self):
        gen = list(fibonacci_generator(count=10))
        self.assertEqual(gen, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci_negative(-6), -8)
    
    def test_fibonacci_custom_start(self):
        self.assertEqual(fibonacci_custom_start(3, 5, count=5), [3, 5, 8, 13, 21])
    
    def test_fibonacci_ratio(self):
        ratios = fibonacci_ratio(10)
        self.assertAlmostEqual(ratios[-1], 1.619047619047619, places=5)
    
    def test_fibonacci_list_or_tuple_list(self):
        self.assertEqual(fibonacci_list_or_tuple(count=5, return_type="list"), [0, 1, 1, 2, 3])
    
    def test_fibonacci_list_or_tuple_tuple(self):
        self.assertEqual(fibonacci_list_or_tuple(count=5, return_type="tuple"), (0, 1, 1, 2, 3))
    
    def test_fibonacci_sum(self):
        self.assertEqual(fibonacci_sum(count=10), 88)
    
    def test_fibonacci_module(self):
        self.assertEqual(fibonacci_module(10, 3), [0, 1, 1, 2, 0, 2, 2, 1, 0, 1])
    
    def test_nth_fibonacci(self):
        self.assertEqual(nth_fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()
