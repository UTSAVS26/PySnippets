import unittest
import numpy as np
import scipy.stats as stats
from probability import (
    correlation_coefficient, poisson_probability, normal_distribution_pdf,
    normal_distribution_cdf, log_normal_distribution_pdf, gamma_distribution_pdf,
    z_value, binomial_probability, exponential_probability
)

class TestProbabilityFunctions(unittest.TestCase):
    
    def test_correlation_coefficient(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        self.assertAlmostEqual(correlation_coefficient(x, y), 1.0, places=4)
    
    def test_poisson_probability(self):
        self.assertAlmostEqual(poisson_probability(3, 2), stats.poisson.pmf(2, 3), places=4)
    
    def test_normal_distribution_pdf(self):
        self.assertAlmostEqual(normal_distribution_pdf(0, 0, 1), stats.norm.pdf(0, 0, 1), places=4)
    
    def test_normal_distribution_cdf(self):
        self.assertAlmostEqual(normal_distribution_cdf(0, 0, 1), stats.norm.cdf(0, 0, 1), places=4)
    
    def test_log_normal_distribution_pdf(self):
        self.assertAlmostEqual(log_normal_distribution_pdf(1, 0, 1), stats.lognorm.pdf(1, 1, scale=np.exp(0)), places=4)
    
    def test_gamma_distribution_pdf(self):
        self.assertAlmostEqual(gamma_distribution_pdf(2, 3, 2), stats.gamma.pdf(2, 3, scale=1/2), places=4)
    
    def test_z_value(self):
        self.assertAlmostEqual(z_value(5, 2, 1), 3.0, places=4)
    
    def test_binomial_probability(self):
        self.assertAlmostEqual(binomial_probability(10, 0.5, 5), stats.binom.pmf(5, 10, 0.5), places=4)
    
    def test_exponential_probability(self):
        self.assertAlmostEqual(exponential_probability(2, 3), stats.expon.pdf(3, scale=1/2), places=4)

if __name__ == "__main__":
    unittest.main()