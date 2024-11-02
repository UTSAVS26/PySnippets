def generate_key_table(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key += ''.join(chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != 'J')
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    processed_text = ""
    i = 0
    while i < len(text):
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += 'X'
        elif i + 1 < len(text):
            processed_text += text[i + 1]
            i += 1
        i += 1
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    return processed_text

def find_position(char, key_table):
    for i, row in enumerate(key_table):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    key_table = generate_key_table(key)
    plaintext = preprocess_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(plaintext[i], key_table)
        row2, col2 = find_position(plaintext[i + 1], key_table)
        if row1 == row2:
            ciphertext += key_table[row1][(col1 + 1) % 5]
            ciphertext += key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_table[(row1 + 1) % 5][col1]
            ciphertext += key_table[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_table[row1][col2]
            ciphertext += key_table[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    key_table = generate_key_table(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(ciphertext[i], key_table)
        row2, col2 = find_position(ciphertext[i + 1], key_table)
        if row1 == row2:
            plaintext += key_table[row1][(col1 - 1) % 5]
            plaintext += key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_table[(row1 - 1) % 5][col1]
            plaintext += key_table[(row2 - 1) % 5][col2]
        else:
            plaintext += key_table[row1][col2]
            plaintext += key_table[row2][col1]
    return plaintext