import unittest
from euler import euler_totient_function, visualize_coprimes

class TestEulerFunction(unittest.TestCase):
    
    def test_phi_value(self):
        # Test the Euler's Totient function value
        self.assertEqual(euler_totient_function(1)[0], 1)
        self.assertEqual(euler_totient_function(6)[0], 2)
        self.assertEqual(euler_totient_function(9)[0], 6)
        self.assertEqual(euler_totient_function(10)[0], 4)

    def test_coprimes_list(self):
        # Test the list of coprimes
        self.assertEqual(euler_totient_function(9)[1], [1, 2, 4, 5, 7, 8])
        self.assertEqual(euler_totient_function(10)[1], [1, 3, 7, 9])
        self.assertEqual(euler_totient_function(6)[1], [1, 5])
        self.assertEqual(euler_totient_function(1)[1], [1])

    def test_invalid_input(self):
        # Test invalid input
        with self.assertRaises(ValueError):
            euler_totient_function(0)
        with self.assertRaises(ValueError):
            euler_totient_function(-5)

    def test_visualize_coprimes(self):
        # Test the visualize_coprimes function 
        try:
            visualize_coprimes(10, [1, 3, 7, 9])
        except Exception as e:
            self.fail(f"visualize_coprimes raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()