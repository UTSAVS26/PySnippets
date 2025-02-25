import logging
from collections import Counter
from dataclasses import dataclass
from typing import List, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

@dataclass
class ListManipulator:
    """Class for manipulating lists with various operations."""

    @staticmethod
    def remove_duplicates(lst: List[Any]) -> List[Any]:
        """
        Removes duplicate elements from the list while maintaining the original order.
        """
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]

    @staticmethod
    def flatten_nested_list(nested_list: List[List[Any]]) -> List[Any]:
        """
        Flattens a nested list into a single list.
        """
        return [item for sublist in nested_list for item in sublist]

    @staticmethod
    def list_intersection(lst1: List[Any], lst2: List[Any]) -> List[Any]:
        """
        Finds the intersection of two lists.
        """
        return list(set(lst1) & set(lst2))

    @staticmethod
    def random_shuffle(lst: List[Any]) -> List[Any]:
        """
        Randomly shuffles the elements of the list.
        """
        import random
        random.shuffle(lst)
        return lst

    @staticmethod
    def sort_by_frequency(lst: List[Any]) -> List[Any]:
        """
        Sorts the list based on the frequency of elements in descending order.

        Args:
            lst (List[Any]): A list to sort by frequency.

        Returns:
            List[Any]: The sorted list by frequency.
        """
        frequency = Counter(lst)
        return sorted(lst, key=lambda x: frequency[x], reverse=True)

    @staticmethod
    def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
        """
        Splits a list into smaller chunks of a given size.
        """
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    @staticmethod
    def most_frequent_element(lst: List[Any]) -> Any:
        """
        Identifies the most frequently occurring element in a list.
        """
        if not lst:
            return None
        return Counter(lst).most_common(1)[0][0]

    @staticmethod
    def rotate_list(lst: List[Any], positions: int) -> List[Any]:
        """
        Rotates the list by a given number of positions.
        """
        positions %= len(lst)
        return lst[-positions:] + lst[:-positions]

    @staticmethod
    def unique_elements(lst: List[Any]) -> List[Any]:
        """
        Gets elements that appear exactly once in the list.
        """
        frequency = Counter(lst)
        return [x for x in lst if frequency[x] == 1]

    @staticmethod
    def find_pairs_with_sum(lst: List[int], target: int) -> List[tuple]:
        """
        Finds all pairs of numbers that sum to a specific target.
        """
        seen = set()
        pairs = []
        for num in lst:
            complement = target - num
            if complement in seen:
                pairs.append((complement, num))
            seen.add(num)
        return pairs

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    nested_list = [[1, 2], [3, 4], [5]]

    logging.info("Original List: %s", sample_list)
    logging.info("Without Duplicates: %s", ListManipulator.remove_duplicates(sample_list))
    logging.info("Flattened Nested List: %s", ListManipulator.flatten_nested_list(nested_list))
    logging.info("List Intersection: %s", ListManipulator.list_intersection([1, 2, 3], [2, 3, 4]))
    logging.info("Shuffled List: %s", ListManipulator.random_shuffle(sample_list.copy()))  # Using copy to keep original
    logging.info("Sorted by Frequency: %s", ListManipulator.sort_by_frequency(sample_list))
    logging.info("Chunked List: %s", ListManipulator.chunk_list(sample_list, 2))
    logging.info("Most Frequent Element: %s", ListManipulator.most_frequent_element(sample_list))
    logging.info("Rotated List: %s", ListManipulator.rotate_list(sample_list, 2))
    logging.info("Unique Elements: %s", ListManipulator.unique_elements(sample_list))
    logging.info("Pairs with Sum 6: %s", ListManipulator.find_pairs_with_sum(sample_list, 6))
