def liner_search(arr, N, x):
    """
    Perform a linear search for a specified element in an array.

    Args:
        arr (list): A list of elements to search in.
        N (int): The number of elements in the array.
        x: The element to search for.

    Returns:
        int: The index of the element if found; otherwise, -1.

    Example:
        >>> search([2, 3, 4, 10, 40], 5, 10)
        3
    """
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = liner_search(arr, N, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)