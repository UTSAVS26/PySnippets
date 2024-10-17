def bucket_sort(arr):
    bucket = [[] for _ in range(len(arr))]
    for num in arr:
        index = int(num * len(arr))
        bucket[index].append(num)
    for i in range(len(arr)):
        bucket[i].sort()
    result = []
    for sublist in bucket:
        result.extend(sublist)
    return result
