from Binary_search_recursive import binary_search_recursive

def exponential_search(arr, target):
    """
    Exponential search algorithm.
    :param arr: Sorted list of elements to search through.
    :param target: The element to search for.
    :return: The index of the element if found, else -1.
    """
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search_recursive(arr, target, i // 2, min(i, n - 1))

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = exponential_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

