import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        # Push item with negative value to simulate max-heap using heapq (which is a min-heap by default)
        heapq.heappush(self.heap, -item)

    def pop(self):
        # Pop the item with the maximum value
        return -heapq.heappop(self.heap)

    def peek(self):
        # Peek the maximum value without popping it
        return -self.heap[0]

    def heapify(self, arr):
        # Heapify the array (transform into a max-heap)
        self.heap = [-i for i in arr]
        heapq.heapify(self.heap)

    def get_heap(self):
        # Get the heap array in max-heap order
        return [-i for i in self.heap]

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        # Push item to the heap (min-heap is default in heapq)
        heapq.heappush(self.heap, item)

    def pop(self):
        # Pop the item with the minimum value
        return heapq.heappop(self.heap)

    def peek(self):
        # Peek the minimum value without popping it
        return self.heap[0]

    def heapify(self, arr):
        # Heapify the array (transform into a min-heap)
        self.heap = arr[:]
        heapq.heapify(self.heap)

    def get_heap(self):
        # Get the heap array in min-heap order
        return self.heap

# Heap Sort function using MaxHeap
def heap_sort(arr):
    """
    Heap Sort implementation using MaxHeap.
    Sorts the array in ascending order.
    """
    max_heap = MaxHeap()
    max_heap.heapify(arr)

    sorted_arr = []
    while max_heap.heap:
        sorted_arr.append(max_heap.pop())

    # The result is sorted in descending order, so reverse it to get ascending order
    return sorted_arr[::-1]

# Example usage for both MinHeap and MaxHeap with heap sort
if __name__ == "__main__":
    # MaxHeap Example
    max_heap = MaxHeap()
    max_heap.push(10)
    max_heap.push(20)
    max_heap.push(15)
    max_element = max_heap.peek()
    popped_max = max_heap.pop()
    max_heap_array = max_heap.get_heap()

    # MinHeap Example
    min_heap = MinHeap()
    min_heap.push(10)
    min_heap.push(20)
    min_heap.push(15)
    min_element = min_heap.peek()
    popped_min = min_heap.pop()
    min_heap_array = min_heap.get_heap()

    # Heap Sort Example
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(arr)
