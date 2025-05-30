from sympy import isprime, mod_inverse
import random

def generate_keys(p=None):
    if p is None:
        while True:
            p = random.randint(100, 200)
            if isprime(p):
                break
    g = random.randint(2, p - 1)
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return (p, g, y), x

def elgamal_encrypt(plaintext, public_key):
    p, g, y = public_key
    encrypted_pairs = []

    for char in plaintext:
        m = ord(char)
        k = random.randint(1, p - 2)
        a = pow(g, k, p)
        b = (pow(y, k, p) * m) % p
        encrypted_pairs.append((a, b))

    # Convert to string to send to frontend easily
    encrypted_string = ','.join(f"{a},{b}" for a, b in encrypted_pairs)
    return encrypted_string

def elgamal_decrypt(ciphertext, private_key, p):
    values = list(map(int, ciphertext.split(',')))
    if len(values) % 2 != 0:
        raise ValueError("Invalid ciphertext input.")

    pairs = [(values[i], values[i + 1]) for i in range(0, len(values), 2)]
    decrypted_text = ""

    for a, b in pairs:
        s = pow(a, private_key, p)
        s_inv = mod_inverse(s, p)
        m = (b * s_inv) % p
        decrypted_text += chr(m)

    return decrypted_text
