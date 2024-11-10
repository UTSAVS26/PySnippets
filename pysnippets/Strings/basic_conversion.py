def number_to_words_basic(num_str: str) -> str:
    if not isinstance(num_str, str) or not num_str.isdigit():
        raise ValueError("Input must be a string of digits.")
    num_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    return ' '.join(num_map.get(digit, digit) for digit in num_str)

def words_to_number_basic(words_str: str) -> str:
    if not isinstance(words_str, str):
        raise ValueError("Input must be a string.")
    word_map = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return ''.join(word_map.get(word, word) for word in words_str.split())
