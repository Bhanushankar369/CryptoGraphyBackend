import numpy as np

# Helper: Convert letter to number and vice versa
def letter_to_num(c): return ord(c) - ord('A')
def num_to_letter(n): return chr(n + ord('A'))

# Mod inverse of determinant
def mod_inverse(a, m):
    if a<0:
        a *= -1
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for determinant {a} under mod {m}")

# Encryption function
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    s = key_matrix
    key_matrix = [
        [0, 0],
        [0, 0]
    ]
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = int(s[k])
            k+=1
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # pad if needed

    vectors = [ [letter_to_num(plaintext[i]), letter_to_num(plaintext[i+1])] for i in range(0, len(plaintext), 2) ]
    result = ""

    for vector in vectors:
        encrypted = np.dot(key_matrix, vector) % 26
        result += ''.join([num_to_letter(int(num)) for num in encrypted])

    return result

# Decryption function
def hill_decrypt(ciphertext, key_matrix):
    s = key_matrix
    key_matrix = [
        [0, 0],
        [0, 0]
    ]
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = int(s[k])
            k+=1
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)

    # Matrix inverse mod 26
    adjugate = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                         [-key_matrix[1][0], key_matrix[0][0]]])
    inv_matrix = (det_inv * adjugate) % 26
    inv_matrix = inv_matrix.astype(int)

    ciphertext = ciphertext.upper()
    vectors = [ [letter_to_num(ciphertext[i]), letter_to_num(ciphertext[i+1])] for i in range(0, len(ciphertext), 2) ]
    result = ""

    for vector in vectors:
        decrypted = np.dot(inv_matrix, vector) % 26
        result += ''.join([num_to_letter(int(num)) for num in decrypted])

    return result
