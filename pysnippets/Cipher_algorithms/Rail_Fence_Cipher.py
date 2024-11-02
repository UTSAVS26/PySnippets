def rail_fence_cipher_encrypt(text, key):
    if not isinstance(text, str) or not isinstance(key, int):
        raise ValueError("Invalid input types. 'text' must be a string and 'key' must be an integer.")
    if key <= 0:
        raise ValueError("Key must be a positive integer.")

    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        row += 1 if dir_down else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def rail_fence_cipher_decrypt(cipher, key):
    if not isinstance(cipher, str) or not isinstance(key, int):
        raise ValueError("Invalid input types. 'cipher' must be a string and 'key' must be an integer.")
    if key <= 0:
        raise ValueError("Key must be a positive integer.")

    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
    return "".join(result)
