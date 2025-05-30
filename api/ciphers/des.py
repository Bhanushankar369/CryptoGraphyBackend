from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def des_encrypt(plaintext, key):
    key = key.encode('utf-8')[:8].ljust(8, b'\0')  # DES key must be 8 bytes
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode()

def des_decrypt(ciphertext, key):
    key = key.encode('utf-8')[:8].ljust(8, b'\0')
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return unpad(decrypted, DES.block_size).decode()
