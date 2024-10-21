import emoji

def emoji_to_text(text):
    """Converts emojis in a text string to corresponding words.

    Args:
        text (str): The input text string containing emojis.

    Returns:
        str: The text with emojis replaced by words.
    """

    emoji_dict = {
        "😀": "happy",
        "😢": "sad",
        "😠": "angry",
        "😂": "laughing",
        "❤️": "love",
        "🤗": "hug",
        "🐱": "cat",
        "👨🏻‍💻": "Ironman",
        "🐶": "dog",
        "⭐️": "star"
    }

    emojified_text = ""
    for char in text:
        if char in emoji_dict:
            word = emoji_dict.get(char, char)
            emojified_text += word + " "
        else:
            emojified_text += char + " "

    return emojified_text.strip()

# Example usage:
text = "I am 😀 cuz I am a ⭐️"
converted_text = emoji_to_text(text)
print(converted_text)