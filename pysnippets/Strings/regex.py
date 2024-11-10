import re

def number_to_words_regex(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    num_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return re.sub(r'\d', lambda x: num_map[x.group()], text)

def words_to_number_regex(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    word_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return re.sub(r'\b(' + '|'.join(word_map.keys()) + r')\b', 
                  lambda x: word_map[x.group()], text)
