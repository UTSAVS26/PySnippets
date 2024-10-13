import emoji

# Sample text with emojis
text_with_emojis = 'I love Python! 😊🐍'

# Convert emojis to text
def emoji_to_text(text_with_emojis):
    text_with_text = emoji.demojize(text_with_emojis)
    return text_with_text

text_with_text = emoji_to_text(text_with_emojis)

print('Original Text:', text_with_emojis)
print('Text with Emojis Converted to Text:', text_with_text)