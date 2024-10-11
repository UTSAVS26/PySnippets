
import unittest
from percentage_format import percentage_format

class TestPercentageFormat(unittest.TestCase):
    def test_percentage_format(self):
        self.assertEqual(percentage_format(50, 200), "25.00%")
        self.assertEqual(percentage_format(25, 50, 1), "50.0%")
        with self.assertRaises(ValueError):
            percentage_format(50, 0)

if __name__ == '__main__':
    unittest.main()
