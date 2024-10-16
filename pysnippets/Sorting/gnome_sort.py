def gnome_sort(arr):
    """
    Gnome Sort algorithm

    Time complexity: O(n^2) in the worst case
    Space complexity: O(1)

    :param arr: input array to be sorted
    :return: None
    """
    index = 0
    n = len(arr)

    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            # Swap the elements
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

