def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary search algorithm (recursive).
    :param arr: Sorted list of elements to search through.
    :param target: The element to search for.
    :param left: The left boundary for the search (default 0).
    :param right: The right boundary for the search (default None, which will be set to len(arr) - 1).
    :return: The index of the element if found, else -1.
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    
# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search_recursive(arr, target)
    
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
        
