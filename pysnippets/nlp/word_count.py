#word_count.py

def word_count(text):
    """
    Count the number of words in a given text.

    Args:
        text (str): The text for which word count is to be calculated.

    Returns:
        int: The number of words in the text.

    Example:
        >>> word_count("Hello world")
        2
    """
    return len(text.split())

# Example usage
if __name__ == "__main__":
    text = "Welcome to the world of Python"
    count = word_count(text)
    print("Word Count:", count)
