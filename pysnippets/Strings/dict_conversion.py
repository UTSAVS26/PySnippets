def number_to_words_advanced(num: int) -> str:
    if not isinstance(num, int) or num < 0 or num > 99:
        raise ValueError("Input must be an integer between 0 and 99.")
    under_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if num < 20:
        return under_20[num]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else '-' + under_20[num % 10])
    return str(num)  # Return as is for numbers outside range

def words_to_number_advanced(words: str) -> int:
    if not isinstance(words, str):
        raise ValueError("Input must be a string.")
    words_to_num = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    words = words.split('-')
    if len(words) > 2:
        raise ValueError("Input must be a valid number in words (up to 99).")
    return words_to_num.get(words[0]) + words_to_num.get(words[1], 0)
