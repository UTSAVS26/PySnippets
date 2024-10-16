def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i

    :param arr: input array
    :param n: size of the heap
    :param i: index of the root of the subtree
    :return: None
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Heap Sort algorithm

    Time complexity: O(n log n)
    Space complexity: O(1)

    :param arr: input array to be sorted
    :return: None
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
