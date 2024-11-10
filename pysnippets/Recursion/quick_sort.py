import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class QuickSort:
    array: list

    def sort(self) -> list:
        return self._quick_sort_recursive(self.array, 0, len(self.array) - 1)

    def _quick_sort_recursive(self, array, low, high):
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort_recursive(array, low, pi - 1)
            self._quick_sort_recursive(array, pi + 1, high)
        return array

    def _partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

# Sample usage
if __name__ == "__main__":
    qs_instance = QuickSort([10, 80, 30, 90, 40, 50, 70])
    print(f"Sorted array: {qs_instance.sort()}")  # Output: [10, 30, 40, 50, 70, 80, 90] 