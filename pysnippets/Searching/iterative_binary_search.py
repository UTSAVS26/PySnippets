def binarySearchiterative(arr, low, high, x):
    """
    Perform binary search for a specified element in a sorted array.

    Args:
        arr (list): A sorted list of elements to search in.
        low (int): The starting index of the subarray to search.
        high (int): The ending index of the subarray to search.
        x: The element to search for.

    Returns:
        int: The index of the element if found; otherwise, -1.

    Example:
        >>> binarySearch([2, 3, 4, 10, 40], 0, 4, 10)
        3
    """
    while low <= high:
        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element was not present
    return -1

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearchiterative(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")