def bucket_sort(arr):
    """
    Bucket sort algorithm

    Time complexity: O(n + k) where n is the length of the input array and k is the number of buckets
    Space complexity: O(n + k)

    :param arr: input array to be sorted
    :return: sorted array
    """
    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Insert elements into their corresponding buckets
    for elem in arr:
        index = int(elem * len(buckets))
        buckets[index].append(elem)

    # Sort each bucket individually
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr