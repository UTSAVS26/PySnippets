import unittest
from lcs import LCSSolver

class TestLCSSolver(unittest.TestCase):
    
    def test_lcs_standard_case(self):
        self.assertEqual(LCSSolver.lcs("AGGTAB", "GXTXAYB", 6, 7), 4)
    
    def test_lcs_no_common_subsequence(self):
        self.assertEqual(LCSSolver.lcs("ABC", "DEF", 3, 3), 0)
    
    def test_lcs_empty_string(self):
        self.assertEqual(LCSSolver.lcs("", "ABC", 0, 3), 0)
        self.assertEqual(LCSSolver.lcs("ABC", "", 3, 0), 0)
    
    def test_lcs_complete_overlap(self):
        self.assertEqual(LCSSolver.lcs("ABC", "ABC", 3, 3), 3)

if __name__ == "__main__":
    unittest.main() 