import unittest
from snippets.statistics import mean, median, mode, variance, standard_deviation

class TestStatistics(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            mean([])

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        with self.assertRaises(ValueError):
            median([])

    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3, 4]), 2)
        with self.assertRaises(ValueError):
            mode([])

    def test_variance(self):
        self.assertEqual(variance([1, 2, 3, 4], population=True), 1.25)
        self.assertEqual(variance([1, 2, 3, 4], population=False), 1.6666666666666667)
        with self.assertRaises(ValueError):
            variance([])

    def test_standard_deviation(self):
        self.assertEqual(standard_deviation([1, 2, 3, 4], population=True), 1.118033988749895)
        self.assertEqual(standard_deviation([1, 2, 3, 4], population=False), 1.2909944487358056)
        with self.assertRaises(ValueError):
            standard_deviation([])

if __name__ == '__main__':
    unittest.main()
