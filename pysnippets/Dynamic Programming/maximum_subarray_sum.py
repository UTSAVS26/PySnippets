from dataclasses import dataclass
import logging

@dataclass
class MaxSubarrayInput:
    nums: list

def max_subarray_sum(input_data: MaxSubarrayInput):
    nums = input_data.nums
    try:
        if not isinstance(nums, list) or not nums:
            raise ValueError("Input must be a non-empty list of numbers.")
        
        max_so_far = max_ending_here = nums[0]

        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
    except Exception as e:
        logging.error(f"Error in max_subarray_sum function: {e}")
        return None

# Test cases
def test_max_subarray_sum():
    test_cases = [
        (MaxSubarrayInput([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6),
        (MaxSubarrayInput([1]), 1),
        (MaxSubarrayInput([0, -1, 2, -3, 4]), 4),
    ]
    
    for input_data, expected in test_cases:
        result = max_subarray_sum(input_data)
        assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_max_subarray_sum()