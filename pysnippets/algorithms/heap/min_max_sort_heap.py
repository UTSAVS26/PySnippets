def heap_sort_min(arr):
    min_heap = MinHeap()
    for num in arr:
        min_heap.insert(num)
    
    sorted_arr = []
    while len(min_heap.heap) > 0:
        sorted_arr.append(min_heap.extract_min())
    return sorted_arr

def heap_sort_max(arr):
    max_heap = MaxHeap()
    for num in arr:
        max_heap.insert(num)
    
    sorted_arr = []
    while len(max_heap.heap) > 0:
        sorted_arr.append(max_heap.extract_max())
    return sorted_arr[::-1]  # To get ascending order from max-heap
