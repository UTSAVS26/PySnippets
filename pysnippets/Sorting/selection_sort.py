def selection_sort(arr):
    """
    Selection Sort algorithm

    Time complexity: O(n^2)
    Space complexity: O(1)

    :param arr: input array to be sorted
    :return: None
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


