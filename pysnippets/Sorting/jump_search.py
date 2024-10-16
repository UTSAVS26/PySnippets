import math

def jump_search(arr, x):
    """
    Jump Search algorithm

    Time complexity: O(sqrt(n))
    Space complexity: O(1)

    :paramarr: input array to be searched
    :param x: target element to be found
    :return: index of the target element if found, -1 otherwise
    """
    n = len(arr)
    step = math.sqrt(n)

    prev = 0
    while arr[min(int(step), n)-1] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1
        if int(prev) == min(int(step), n):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

    return -1

