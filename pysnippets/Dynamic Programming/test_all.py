import unittest
from edit_distance import edit_distance, EditDistanceInput
from longest_common_subsequence import longest_common_subsequence, LCSInput
from coin_change import coin_change, CoinChangeInput
from maximum_subarray_sum import max_subarray_sum, MaxSubarrayInput
from Longest_path_in_DAG import find_longest_path  # Assuming the function is correctly named
from unique_paths import unique_paths

class TestDynamicProgramming(unittest.TestCase):

    def test_edit_distance(self):
        test_cases = [
            (EditDistanceInput("horse", "ros"), 3),
            (EditDistanceInput("intention", "execution"), 5),
            (EditDistanceInput("", ""), 0),
            (EditDistanceInput("a", "b"), 1),
            (EditDistanceInput("abc", "yabd"), 2),
        ]
        
        for input_data, expected in test_cases:
            result = edit_distance(input_data)
            self.assertEqual(result, expected)

    def test_longest_common_subsequence(self):
        test_cases = [
            (LCSInput("AGGTAB", "GXTXAYB"), 4),
            (LCSInput("ABCBDAB", "BDCAB"), 4),
            (LCSInput("", ""), 0),
            (LCSInput("ABC", "AC"), 2),
        ]
        
        for input_data, expected in test_cases:
            result = longest_common_subsequence(input_data)
            self.assertEqual(result, expected)

    def test_coin_change(self):
        test_cases = [
            (CoinChangeInput([1, 2, 5], 11), (3, [5, 5, 1])),
            (CoinChangeInput([2], 3), -1),
            (CoinChangeInput([1], 0), (0, [])),
        ]
        
        for input_data, expected in test_cases:
            result = coin_change(input_data)
            self.assertEqual(result, expected)

    def test_max_subarray_sum(self):
        test_cases = [
            (MaxSubarrayInput([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6),
            (MaxSubarrayInput([1]), 1),
            (MaxSubarrayInput([0, -1, 2, -3, 4]), 4),
        ]
        
        for input_data, expected in test_cases:
            result = max_subarray_sum(input_data)
            self.assertEqual(result, expected)

    def test_unique_paths(self):
        test_cases = [
            (3, 7, 28),
            (3, 2, 3),
            (7, 3, 28)
        ]
        
        for m, n, expected in test_cases:
            result = unique_paths(m, n)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
