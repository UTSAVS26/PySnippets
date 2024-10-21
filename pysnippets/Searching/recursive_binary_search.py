def binarySearchRecursive(arr, low, high, x):
    """
    Perform binary search for a specified element in a sorted array recursively.

    Args:
        arr (list): A sorted list of elements to search in.
        low (int): The starting index of the subarray to search.
        high (int): The ending index of the subarray to search.
        x: The element to search for.

    Returns:
        int: The index of the element if found; otherwise, -1.

    Example:
        >>> binarySearchRecursive([2, 3, 4, 10, 40], 0, 4, 10)
        3
    """
    # Check base case
    if high >= low:
        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, search left subarray
        elif arr[mid] > x:
            return binarySearchRecursive(arr, low, mid-1, x)
        # Else search right subarray
        else:
            return binarySearchRecursive(arr, mid + 1, high, x)

    # Element is not present in the array
    return -1

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearchRecursive(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")