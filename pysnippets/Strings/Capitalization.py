import random

def capitalize_each_word(text):
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def title_case(text):
    """Convert to title case following advanced grammar rules."""
    exclusions = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'by', 'with'}
    words = text.split()
    title_cased = [words[0].capitalize()]
    for word in words[1:]:
        if word.lower() in exclusions:
            title_cased.append(word.lower())
        else:
            title_cased.append(word.capitalize())
    return ' '.join(title_cased)

def alternate_capitalization(text):
    """Capitalize characters in an alternating pattern."""
    result = []
    upper = True
    for char in text:
        if char.isalpha():
            result.append(char.upper() if upper else char.lower())
            upper = not upper
        else:
            result.append(char)
    return ''.join(result)

def random_capitalization(text):
    """Randomly capitalize characters in a string."""
    return ''.join(char.upper() if random.choice([True, False]) else char.lower() for char in text)

if __name__ == "__main__":
    sample_text = "hello world, welcome to advanced string manipulation in python!"
    print("Capitalize Each Word:", capitalize_each_word(sample_text))
    print("Title Case:", title_case(sample_text))
    print("Alternate Capitalization:", alternate_capitalization(sample_text))
    print("Random Capitalization:", random_capitalization(sample_text))
