# Constants
PADDING_CHAR = 'X'
REPLACEMENT_CHAR = 'I'

def generate_key_table(key):
    """
    Generates a 5x5 key table for the Playfair cipher.
    
    Parameters:
    - key (str): The keyword to generate the table from.
    
    Returns:
    - list: A 5x5 matrix of characters as the key table.
    """
    # Remove duplicate characters in the key, preserving the order
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    # Fill the table with A-Z, excluding 'J' and already included key characters
    key += ''.join(chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != 'J')
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def preprocess_text(text):
    """
    Preprocesses the plaintext by converting to uppercase, replacing 'J' with 'I',
    and adding padding characters where needed.
    
    Parameters:
    - text (str): The plaintext message to preprocess.
    
    Returns:
    - str: The processed text with padding.
    """
    text = text.upper().replace('J', REPLACEMENT_CHAR)
    processed_text = ""
    i = 0
    while i < len(text):
        processed_text += text[i]
        # Add padding if two consecutive letters are the same
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += PADDING_CHAR
        elif i + 1 < len(text):
            processed_text += text[i + 1]
            i += 1
        i += 1
    # Append padding if the length is odd
    if len(processed_text) % 2 != 0:
        processed_text += PADDING_CHAR
    return processed_text

def find_position(char, key_table):
    """
    Finds the position of a character in the key table.
    
    Parameters:
    - char (str): The character to locate in the table.
    - key_table (list): The 5x5 matrix key table.
    
    Returns:
    - tuple: The row and column indices of the character.
    """
    for i, row in enumerate(key_table):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    """
    Encrypts the plaintext using the Playfair cipher with the provided key.
    
    Parameters:
    - plaintext (str): The text to encrypt.
    - key (str): The key for generating the cipher's key table.
    
    Returns:
    - str: The encrypted ciphertext.
    """
    key_table = generate_key_table(key)
    plaintext = preprocess_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(plaintext[i], key_table)
        row2, col2 = find_position(plaintext[i + 1], key_table)
        if row1 == row2:
            # Same row: shift right
            ciphertext += key_table[row1][(col1 + 1) % 5]
            ciphertext += key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Same column: shift down
            ciphertext += key_table[(row1 + 1) % 5][col1]
            ciphertext += key_table[(row2 + 1) % 5][col2]
        else:
            # Rectangle swap
            ciphertext += key_table[row1][col2]
            ciphertext += key_table[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using the Playfair cipher with the provided key.
    
    Parameters:
    - ciphertext (str): The text to decrypt.
    - key (str): The key for generating the cipher's key table.
    
    Returns:
    - str: The decrypted plaintext.
    """
    key_table = generate_key_table(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(ciphertext[i], key_table)
        row2, col2 = find_position(ciphertext[i + 1], key_table)
        if row1 == row2:
            # Same row: shift left
            plaintext += key_table[row1][(col1 - 1) % 5]
            plaintext += key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column: shift up
            plaintext += key_table[(row1 - 1) % 5][col1]
            plaintext += key_table[(row2 - 1) % 5][col2]
        else:
            # Rectangle swap
            plaintext += key_table[row1][col2]
            plaintext += key_table[row2][col1]
    return plaintext