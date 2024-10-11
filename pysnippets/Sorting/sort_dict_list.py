def sort_dict_list(dict_list, key, reverse=False):
    """
    Sorts a list of dictionary by a specified key.

    Args:
        dict_list (list): A list of dictionaries to be sorted.
        key (str): The dictionary key to sort by.
        reverse (bool, optional): If True sort in descending order. Default is False (ascending order)

    Returns:
        list: A new list of dictionaries sorted by the specified key.

    Raises:
        ValueError: if the list is empty or if the specified key is not present in all dictionaries

    Example:
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
        >>> sort_dict_list(data)
        [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
    """

    if not dict_list:
        raise ValueError("The list of dictionaries is empty.")

    if not all(key in d for d in dict_list):
        raise ValueError(f"The key {key} is not present in all dictionaries.")

    return sorted(dict_list, key=lambda x: x[key], reverse=reverse)


if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    sorted_data = sort_dict_list(data, key="age")
    print(sorted_data)
