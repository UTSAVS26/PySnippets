def ternary_search(arr, target, left=0, right=None):
    """
    Ternary search algorithm.
    :param arr: Sorted list of elements to search through.
    :param target: The element to search for.
    :param left: Left boundary for the search.
    :param right: Right boundary for the search.
    :return: The index of the element if found, else -1.
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = ternary_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

