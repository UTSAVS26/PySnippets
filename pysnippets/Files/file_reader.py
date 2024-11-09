# file_reader.py


def read_file(file_path):
    """
    Read the contents of a text file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file as a string, or None if an error occurred.

    Example:
        >>> read_file('example.txt')
        'File contents here...'
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

# Example usage
if __name__ == "__main__":
    content = read_file("example.txt")
    if content is not None:
        print(content)