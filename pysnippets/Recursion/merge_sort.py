import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class MergeSort:
    array: list

    def sort(self) -> list:
        if len(self.array) > 1:
            mid = len(self.array) // 2
            left_half = self.array[:mid]
            right_half = self.array[mid:]

            left_sort = MergeSort(left_half).sort()
            right_sort = MergeSort(right_half).sort()

            return self._merge(left_sort, right_sort)
        else:
            return self.array

    def _merge(self, left, right):
        sorted_array = []
        while left and right:
            if left[0] < right[0]:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))
        sorted_array.extend(left or right)
        return sorted_array

# Sample usage
if __name__ == "__main__":
    ms_instance = MergeSort([34, 7, 23, 32, 5, 62])
    print(f"Sorted array: {ms_instance.sort()}")  # Output: [5, 7, 23, 32, 34, 62] 