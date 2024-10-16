def shell_sort(arr):
    """
    Shell Sort algorithm

    Time complexity: O(n log n) in the best case, O(n^2) in the worst case
 Space complexity: O(1)

    :param arr: input array to be sorted
    :return: None
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

