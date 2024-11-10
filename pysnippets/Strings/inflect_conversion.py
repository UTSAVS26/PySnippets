import inflect

engine = inflect.engine()

def number_to_words_inflect(num: int) -> str:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    return engine.number_to_words(num)

def words_to_number_inflect(words: str) -> int:
    if not isinstance(words, str):
        raise ValueError("Input must be a string.")
    words = words.replace("-", " ").strip()
    word_to_num_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    total = 0
    for part in words.split():
        if part in word_to_num_map:
            total += word_to_num_map[part]
        else:
            return None  # return None if unknown word encountered
    return total
