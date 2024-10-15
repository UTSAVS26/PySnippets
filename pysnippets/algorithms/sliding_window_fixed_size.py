def sliding_window_max_sum(arr, k):
    """
    Finds the maximum sum of a subarray of size k using the sliding window technique.

    Args:
        arr (list): A list of numbers.
        k (int): The size of the window.

    Returns:
        int: The maximum sum of any subarray of size k.

    Example:
        >>> sliding_window_max_sum([2, 1, 5, 1, 3, 2], 3)
        9
    """
    # Handle edge cases
    if len(arr) < k or k <= 0:
        return 0

    # Initialize the sum of the first window
    max_sum = current_sum = sum(arr[:k])

    # Slide the window across the array
    for i in range(k, len(arr)):
        # Slide the window: subtract the element that's leaving, add the new element
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
if __name__ == "__main__":
    result = sliding_window_max_sum([2, 1, 5, 1, 3, 2], 3)
    print(result)  # Output: 9
