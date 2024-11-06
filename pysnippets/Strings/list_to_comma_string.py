# list_to_comma_string.py

from typing import List

def list_to_comma_string(items: List[str]) -> str:
    """
    Convert a list of strings into a comma-separated string.

    Args:
        items (list of str): List of strings to convert.

    Returns:
        str: A single comma-separated string.

    Raises:
        ValueError: If any element in the list is not a string.

    Example:
        >>> list_to_comma_string(['apple', 'banana', 'cherry'])
        'apple, banana, cherry'
    """
    if not all(isinstance(item, str) for item in items):
        invalid_items = [item for item in items if not isinstance(item, str)]
        raise ValueError(f"All elements of the list must be strings. Invalid items: {invalid_items}")
    
    return ", ".join(items)


# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    result = list_to_comma_string(my_list)
    print(result)
