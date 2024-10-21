import unittest
from pysnippets.stats.mean_median_mode import mean, median, mode
from pysnippets.stats.standard_deviation import standard_deviation
from pysnippets.stats.variance import variance
from pysnippets.stats.iqr import calculate_iqr
from pysnippets.stats.skewness import calculate_skewness
from pysnippets.stats.kurtosis import calculate_kurtosis
from pysnippets.stats.correlation import calculate_correlation_coefficient

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


    def test_iqr(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_iqr = 5.0  # Q3 - Q1 = 8.5 - 3.5
        self.assertAlmostEqual(calculate_iqr(data), expected_iqr)

    def test_skewness(self):
        data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
        expected_skewness = 0.3397  # Expected skewness value
        self.assertAlmostEqual(calculate_skewness(data), expected_skewness, places=4)

    def test_kurtosis(self):
        data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
        expected_kurtosis = -1.211  # Expected kurtosis value
        self.assertAlmostEqual(calculate_kurtosis(data), expected_kurtosis, places=3)

    def test_correlation_coefficient(self):
        data1 = [1, 2, 3, 4, 5]
        data2 = [5, 4, 3, 2, 1]
        expected_correlation = -1.0  # Perfect negative correlation
        self.assertAlmostEqual(calculate_correlation_coefficient(data1, data2), expected_correlation)

        data3 = [1, 2, 3, 4, 5]
        data4 = [1, 2, 3, 4, 5]
        expected_correlation = 1.0  # Perfect positive correlation
        self.assertAlmostEqual(calculate_correlation_coefficient(data3, data4), expected_correlation)

if __name__ == '__main__':
    unittest.main()
