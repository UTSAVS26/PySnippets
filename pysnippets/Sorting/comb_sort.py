def comb_sort(arr):
    """
    Comb Sort algorithm

    Time complexity: O(n log n) on average, O(n^2) in the worst case
    Space complexity : O(1)

    :param arr: input array to be sorted
    :return: None
    """
    def get_next_gap(gap):
        """
        Calculate the next gap value

        :param gap: current gap value
        :return: next gap value
        """
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True