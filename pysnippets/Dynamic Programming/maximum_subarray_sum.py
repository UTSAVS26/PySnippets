def max_subarray_sum(nums):
    # Input validation
    if not isinstance(nums, list) or len(nums) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")
    
    max_so_far = max_ending_here = nums[0]

    for x in nums[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(nums)  # Output: 6
    print(f"The maximum sum of a contiguous subarray is: {max_sum}")