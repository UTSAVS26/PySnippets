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
        >>> perform_iterative_binary_search([2, 3, 4, 10, 40], 10)
        3
    """
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
    arr = [2, 3, 4, 10, 40]
    target = 10

    # Function call
    result = binary_search_iterative(arr, target)
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in array")