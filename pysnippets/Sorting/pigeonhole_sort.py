def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1
    holes = [[] for _ in range(size)]
    for num in arr:
        holes[num - min_val].append(num)
    result = []
    for hole in holes:
        result.extend(hole)
    return result
