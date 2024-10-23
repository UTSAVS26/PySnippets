import math

def jump_search(arr, target):
    """
    Jump search algorithm.
    :param arr: Sorted list of elements to search through.
    :param target: The element to search for.
    :return: The index of the element if found, else -1.
    """
    if not arr:  # Check for empty array
        return -1
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = jump_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)



