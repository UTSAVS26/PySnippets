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

        Args:
            lst (List[Any]): A list from which to remove duplicates.

        Returns:
            List[Any]: A list without duplicates.
        """
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]

    @staticmethod
    def flatten_nested_list(nested_list: List[List[Any]]) -> List[Any]:
        """
        Flattens a nested list into a single list.

        Args:
            nested_list (List[List[Any]]): A nested list to flatten.

        Returns:
            List[Any]: A flattened list.
        """
        return [item for sublist in nested_list for item in sublist]

    @staticmethod
    def list_intersection(lst1: List[Any], lst2: List[Any]) -> List[Any]:
        """
        Finds the intersection of two lists.

        Args:
            lst1 (List[Any]): The first list.
            lst2 (List[Any]): The second list.

        Returns:
            List[Any]: The intersection of the two lists.
        """
        return list(set(lst1) & set(lst2))

    @staticmethod
    def random_shuffle(lst: List[Any]) -> List[Any]:
        """
        Randomly shuffles the elements of the list.

        Args:
            lst (List[Any]): A list to shuffle.

        Returns:
            List[Any]: A shuffled list (order will vary).
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

