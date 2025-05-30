from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

def aes_encrypt(plaintext, key):
    key = key.encode('utf-8')
    key = key[:32].ljust(32, b'\0')  # AES-256 requires 32-byte key

    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_text = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_text) + encryptor.finalize()

    return base64.b64encode(iv + ciphertext).decode()

def aes_decrypt(ciphertext, key):
    key = key.encode('utf-8')
    key = key[:32].ljust(32, b'\0')

    raw_data = base64.b64decode(ciphertext)
    iv = raw_data[:16]
    actual_cipher = raw_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_cipher) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()
