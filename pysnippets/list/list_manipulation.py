def remove_duplicates(lst: list) -> list:
    """
    Removes duplicate elements from the list while maintaining the original order.

    Example usage:
    remove_duplicates([1, 2, 2, 3, 4, 4]) -> [1, 2, 3, 4]
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def flatten_nested_list(nested_list: list) -> list:
    """
    Flattens a nested list into a single list.

    Example usage:
    flatten_nested_list([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    """
    return [item for sublist in nested_list for item in sublist]

def list_intersection(lst1: list, lst2: list) -> list:
    """
    Finds the intersection of two lists.

    Example usage:
    list_intersection([1, 2, 3], [2, 3, 4]) -> [2, 3]
    """
    return list(set(lst1) & set(lst2))

def random_shuffle(lst: list) -> list:
    """
    Randomly shuffles the elements of the list.

    Example usage:
    random_shuffle([1, 2, 3, 4]) -> [3, 1, 4, 2] (order will vary)
    """
    import random
    random.shuffle(lst)
    return lst

def sort_by_frequency(lst: list) -> list:
    """
    Sorts the list based on the frequency of elements in descending order.

    Example usage:
    sort_by_frequency([4, 5, 6, 4, 5, 4]) -> [4, 4, 4, 5, 5, 6]
    """
    from collections import Counter
    frequency = Counter(lst)
    return sorted(lst, key=lambda x: frequency[x], reverse=True)

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    nested_list = [[1, 2], [3, 4], [5]]

    print("Original List:", sample_list)
    print("Without Duplicates:", remove_duplicates(sample_list))
    print("Flattened Nested List:", flatten_nested_list(nested_list))
    print("List Intersection:", list_intersection([1, 2, 3], [2, 3, 4]))
    print("Shuffled List:", random_shuffle(sample_list.copy()))  # Using copy to keep original
    print("Sorted by Frequency:", sort_by_frequency(sample_list))

