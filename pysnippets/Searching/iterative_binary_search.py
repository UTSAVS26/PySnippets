from typing import List

def binary_search_iterative(arr: List[int], target: int) -> int:
    """
    Executes an iterative binary search on a sorted array to find a target element.

    Args:
        arr (List[int]): A sorted list of integers to search within.
        target (int): The element to search for within the array.

    Returns:
        int: The index of the target element if found; otherwise, -1.

    Example:
        >>> binary_search_iterative([2, 3, 4, 10, 40], 10)
        3
    """
    if not arr:  # Edge case for empty array
        print("The array is empty.")
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the target is present at the mid index
        if arr[mid] == target:
            return mid
        # If the target is greater, adjust the search range to the right half
        elif arr[mid] < target:
            low = mid + 1
        # If the target is smaller, adjust the search range to the left half
        else:
            high = mid - 1

    # If the loop completes without finding the target, return -1
    return -1

# Driver Code
if __name__ == '__main__':
    test_cases = [
        ([2, 3, 4, 10, 40], 10, 3),   # Standard case
        ([2, 3, 4, 10, 40], 5, -1),   # Target not in array
        ([], 5, -1),                  # Empty array
        ([10], 10, 0),                # Single-element array, found
        ([10], 20, -1)                # Single-element array, not found
    ]

    for arr, target, expected in test_cases:
        result = binary_search_iterative(arr, target)
        print(f"Searching for {target} in {arr}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
        assert result == expected, f"Test failed for array: {arr} and target: {target}"