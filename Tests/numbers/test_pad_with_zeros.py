
import unittest
from pad_with_zeros import pad_with_zeros

class TestPadWithZeros(unittest.TestCase):
    def test_pad_with_zeros(self):
        self.assertEqual(pad_with_zeros(123, 6), "000123")
        self.assertEqual(pad_with_zeros(1, 3), "001")
        self.assertEqual(pad_with_zeros(0, 5), "00000")

if __name__ == '__main__':
    unittest.main()
