import emoji

def text_to_emoji(text):
  """Converts text to emojis.

  Args:
    text: The text to convert.

  Returns:
    The text converted to emojis.
  """

  emoji_dict = {
      "happy": "😀",
      "sad": "😢",
      "angry": "😠",
      "laughing": "😂",
      "love": "❤️",
      "hug": "🤗",
      "cat": "🐱",
      "dog": "🐶",
      "star": "⭐️"
  }

  emojified_text = ""
  words = text.split()
  for word in words:
    if word.lower() in emoji_dict:
      emojified_text += emoji_dict[word.lower()] + " "
    else:
      emojified_text += word + " "

  return emojified_text.strip()

# Example usage:
text = "I am happy and love my cat"
emojified_text = text_to_emoji(text)
print(emojified_text)