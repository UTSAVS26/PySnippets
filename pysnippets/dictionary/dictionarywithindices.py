
def convert_list_to_dict_with_indices(lst):
    """
    Converts a list to a dictionary with list values as keys and their indices as values.
    Example:
        Input: ['a', 'b', 'c']
        Output: {'a': 0, 'b': 1, 'c': 2}
    """
    return {value: index for index, value in enumerate(lst)}
