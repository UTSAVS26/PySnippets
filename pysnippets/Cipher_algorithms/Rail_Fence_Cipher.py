# Constants for placeholder characters
EMPTY_CHAR = '\n'  # Used in encryption matrix
MARKER_CHAR = '*'  # Used in decryption matrix

def toggle_direction(row, key, dir_down):
    """
    Helper function to toggle direction in the rail matrix.
    
    Parameters:
    - row (int): Current row index.
    - key (int): Total number of rails (key).
    - dir_down (bool): Current direction.
    
    Returns:
    - tuple: Updated row and direction.
    """
    if row == 0:
        dir_down = True
    elif row == key - 1:
        dir_down = False
    return row + (1 if dir_down else -1), dir_down

def rail_fence_cipher_encrypt(text, key):
    """
    Encrypts the given text using the Rail Fence Cipher method.
    
    Parameters:
    - text (str): The text to encrypt.
    - key (int): The number of rails to use in the cipher.

    Returns:
    - str: The encrypted text.
    """
    if not isinstance(text, str) or not isinstance(key, int):
        raise ValueError("Invalid input types. 'text' must be a string and 'key' must be an integer.")
    if key <= 0:
        raise ValueError("Key must be a positive integer.")
    
    # Initialize the rail matrix
    rail = [[EMPTY_CHAR for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    # Fill the rail matrix with characters in zig-zag fashion
    for char in text:
        rail[row][col] = char
        col += 1
        row, dir_down = toggle_direction(row, key, dir_down)

    # Collect the encrypted text
    result = [rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != EMPTY_CHAR]
    return "".join(result)


def rail_fence_cipher_decrypt(cipher, key):
    """
    Decrypts the given cipher text using the Rail Fence Cipher method.
    
    Parameters:
    - cipher (str): The encrypted text to decrypt.
    - key (int): The number of rails to use in the cipher.

    Returns:
    - str: The decrypted text.
    """
    if not isinstance(cipher, str) or not isinstance(key, int):
        raise ValueError("Invalid input types. 'cipher' must be a string and 'key' must be an integer.")
    if key <= 0:
        raise ValueError("Key must be a positive integer.")
    
    # Initialize the rail matrix
    rail = [[EMPTY_CHAR for _ in range(len(cipher))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    # Mark the pattern path in the rail matrix
    for _ in range(len(cipher)):
        rail[row][col] = MARKER_CHAR
        col += 1
        row, dir_down = toggle_direction(row, key, dir_down)

    # Place characters in the marked positions
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == MARKER_CHAR and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the matrix in zig-zag fashion to decrypt
    result = []
    row, col = 0, 0
    for _ in range(len(cipher)):
        if rail[row][col] != MARKER_CHAR:
            result.append(rail[row][col])
            col += 1
        row, dir_down = toggle_direction(row, key, dir_down)

    return "".join(result)