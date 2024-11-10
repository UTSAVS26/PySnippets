import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class BinarySearch:
    array: list
    target: int

    def search(self) -> int:
        return self._binary_search_recursive(self.array, self.target, 0, len(self.array) - 1)

    def _binary_search_recursive(self, array, target, left, right):
        if right >= left:
            mid = left + (right - left) // 2
            if array[mid] == target:
                logging.info(f"Target {target} found at index {mid}")
                return mid
            elif array[mid] > target:
                return self._binary_search_recursive(array, target, left, mid - 1)
            else:
                return self._binary_search_recursive(array, target, mid + 1, right)
        else:
            logging.info(f"Target {target} not found")
            return -1

# Sample usage
if __name__ == "__main__":
    bs_instance = BinarySearch([1, 2, 3, 4, 5], 3)
    print(f"Index of 3 is {bs_instance.search()}")  # Output: 2 