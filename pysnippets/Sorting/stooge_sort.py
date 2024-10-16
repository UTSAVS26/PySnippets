def stooge_sort(arr, i, j):
    """
    Stooge Sort algorithm

    Time complexity: O(n^2.7095) in the worst case
    Space complexity: O(n)

    :param arr: input array to be sorted
    :param i: starting index
    :param j: ending index
    :return: None
    """
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stooge_sort(arr, i, j - t)
        stooge_sort(arr, i + t, j)
        stooge_sort(arr, i, j - t)


