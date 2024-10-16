def counting_sort(arr):
    """
    Counting Sort algorithm

    Time complexity: O(n + k) where n is the length of the input array and k is the range of input
    Space complexity: O(n + k)

    :param arr: input array to be sorted
    :return: None
    """
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences of each element
    for num in arr:
        count[num] += 1

    # Calculate cumulative count
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Build the output array
    output = [0] * len(arr)
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1

    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

