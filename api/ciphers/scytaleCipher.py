import math

def scytale_encrypt(plaintext, diameter):
    plaintext = plaintext.replace(" ", "").upper()
    rows = math.ceil(len(plaintext) / diameter)
    padded_len = rows * diameter
    plaintext += 'X' * (padded_len - len(plaintext))
    cipher = ''
    for i in range(diameter):
        for j in range(rows):
            cipher += plaintext[j * diameter + i]
    return cipher

def scytale_decrypt(ciphertext, diameter):
    ciphertext = ciphertext.replace(" ", "").upper()
    rows = math.ceil(len(ciphertext) / diameter)
    matrix = [['' for _ in range(diameter)] for _ in range(rows)]
    index = 0
    for i in range(diameter):
        for j in range(rows):
            if index < len(ciphertext):
                matrix[j][i] = ciphertext[index]
                index += 1
    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)
    return plaintext.rstrip('X')
