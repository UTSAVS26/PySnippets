import random

def generate_text(text: str, n: int = 3) -> str:
    words = text.split()
    index = random.randint(0, len(words) - n)
    return ' '.join(words[index:index+n]) 