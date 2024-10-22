def linear_search(arr, target):
    """
    Linear search algorithm.
    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: The index of the element if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10

    # Function call
    result = linear_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)