def min_size_subarray_sum(arr, target):
    """
    Finds the length of the smallest subarray whose sum is greater than or equal to the target.
    
    Args:
        arr (list): A list of positive numbers.
        target (int/float): The target sum to achieve.
    
    Returns:
        int: The length of the smallest subarray with sum >= target. 
             Returns 0 if no such subarray exists.
    
    Example:
        >>> min_size_subarray_sum([2, 1, 5, 2, 3, 2], 7)
        2
    """
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    # Iterate over the array
    for end in range(n):
        current_sum += arr[end]
        
        # Shrink the window from the left as long as the sum >= target
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1
    
    # If no valid subarray found, return 0
    return min_length if min_length != float('inf') else 0

# Example usage
if __name__ == "__main__":
    result = min_size_subarray_sum([2, 1, 5, 2, 3, 2], 7)
    print(result)  # Output: 2
