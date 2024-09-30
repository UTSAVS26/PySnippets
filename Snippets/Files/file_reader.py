# file_reader.py


def read_file(file_path):
    """
    Read the contents of a text file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file as a string.

    Example:
        >>> read_file('example.txt')
        'File contents here...'
    """
    with open(file_path, "r") as file:
        return file.read()


# Example usage
if __name__ == "__main__":
    content = read_file("example.txt")
    print(content)
