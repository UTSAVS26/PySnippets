#text_tokenization.py

def text_tokenization(text):
    """
    Tokenize a given text into individual words.

    Args:
        text (str): The text to be tokenized.

    Returns:
        list: A list of words in the text.

    Example:
        >>> text_tokenization("This is an example.")
        ['This', 'is', 'an', 'example']
    """
    return text.split()

# Example usage
if __name__ == "__main__":
    text = "Natural Language Processing with Python"
    tokens = text_tokenization(text)
    print("Tokens:", tokens)
