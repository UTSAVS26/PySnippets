import math

def jump_sort(arr):
    def jump_search(val):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while arr[min(step, n)-1] < val:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return None
        for i in range(prev, min(step, n)):
            if arr[i] == val:
                return i
        return None
    return sorted(arr)
