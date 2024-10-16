def pigeonhole_sort(arr):
    """
    Pigeonhole Sort algorithm

    Time complexity: O(n + range) where range is the range of the input data
    Space complexity: O(n + range)

    :param arr: input array to be sorted
    :return: None
    """
    my_min = min(arr)
    my_max = max(arr)
    size = my_max - my_min + 1

    holes = [0] * size

    for x in arr:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + my_min
            i += 1


