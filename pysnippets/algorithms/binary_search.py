from typing import List, Union

def binary_search(arr: List[Union[int, float]], target: Union[int, float]) -> int:
    """
    Performs binary search on a sorted array to find the target element.

    Args:
        arr (List[Union[int, float]]): A sorted list of elements to search through.
        target (Union[int, float]): The element to search for in the array.

    Returns:
        int: The index of the target if found, -1 if not found.

    Time Complexity:
        O(log n), where n is the number of elements in the array.

    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Safe calculation of mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
if __name__ == "__main__":
    result = binary_search([1, 2, 3, 4, 5], 3)
    print(result)  # Output: 2