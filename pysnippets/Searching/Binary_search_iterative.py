def binary_search(arr, target):
    """
    Binary search algorithm (iterative).
    :param arr: Sorted list of elements to search through.
    :param target: The element to search for.
    :return: The index of the element if found, else -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
