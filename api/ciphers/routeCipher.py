import math

def route_encrypt(plaintext, key):
    rows, cols = map(int, key.split(','))
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    padded_len = rows * cols
    plaintext += '_' * (padded_len - len(plaintext))
    index = 0
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = plaintext[index]
            index += 1

    top, bottom, left, right = 0, rows-1, 0, cols-1
    cipher = ''
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            cipher += matrix[top][i]
        top += 1
        for i in range(top, bottom + 1):
            cipher += matrix[i][right]
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                cipher += matrix[bottom][i]
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                cipher += matrix[i][left]
            left += 1
    return cipher

def route_decrypt(ciphertext, key):
    rows, cols = map(int, key.split(','))
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    top, bottom, left, right = 0, rows-1, 0, cols-1
    index = 0
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = ciphertext[index]
            index += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = ciphertext[index]
            index += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = ciphertext[index]
                index += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = ciphertext[index]
                index += 1
            left += 1
    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)
    return plaintext.rstrip('_')