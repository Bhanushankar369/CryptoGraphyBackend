import random
import string

# Convert letter to number and back
def letter_to_num(c): return ord(c.upper()) - ord('A')
def num_to_letter(n): return chr((n % 26) + ord('A'))

# Generate a random key of same length as plaintext
def generate_random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Encrypt
def otp_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    if len(key) != len(plaintext):
        raise ValueError("Key must be the same length as plaintext.")

    cipher = ''
    for p, k in zip(plaintext, key):
        cipher += num_to_letter((letter_to_num(p) + letter_to_num(k)) % 26)
    return cipher

# Decrypt
def otp_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    if len(key) != len(ciphertext):
        raise ValueError("Key must be the same length as ciphertext.")

    plain = ''
    for c, k in zip(ciphertext, key):
        plain += num_to_letter((letter_to_num(c) - letter_to_num(k)) % 26)
    return plain
