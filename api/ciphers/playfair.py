import string

def generate_key_square(key):
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I')))  # Remove duplicates, replace J with I
    alphabet = string.ascii_uppercase.replace('J', '')  # A-Z without J
    key_square = []

    for char in key:
        if char not in key_square:
            key_square.append(char)

    for char in alphabet:
        if char not in key_square:
            key_square.append(char)

    matrix = [key_square[i:i + 5] for i in range(0, 25, 5)]
    return matrix

def prepare_text(text, pad_char='X'):
    text = text.upper().replace('J', 'I')
    prepared = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else pad_char

        if a == b:
            prepared += a + pad_char
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += pad_char
    return prepared

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    matrix = generate_key_square(key)
    text = prepare_text(plaintext)
    ciphertext = ''

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_key_square(key)
    plaintext = ''

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext
