# list_to_comma_string.py

def list_to_comma_string(items):
    """
    Convert a list of strings into a comma-separated string.

    Args:
        items (list of str): List of strings to convert.

    Returns:
        str: A single comma-separated string.

    Example:
        >>> list_to_comma_string(['apple', 'banana', 'cherry'])
        'apple, banana, cherry'
    """
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All elements of the list must be strings")
    return ", ".join(items)


# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    result = list_to_comma_string(my_list)
    print(result)
