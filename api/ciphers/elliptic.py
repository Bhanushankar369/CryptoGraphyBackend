from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sympadding
import os, base64

# Generate ECC private and public keys
def generate_ecc_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem.decode(), public_pem.decode()

# Derive shared AES key using ECDH
def derive_shared_key(private_key_pem, peer_public_key_pem):
    private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None)
    peer_public_key = serialization.load_pem_public_key(peer_public_key_pem.encode())

    shared_key = private_key.exchange(ec.ECDH(), peer_public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ecc-encryption'
    ).derive(shared_key)

    return derived_key

# Encrypt using derived AES key
def ecc_encrypt(plaintext, aes_key):
    iv = os.urandom(16)
    padder = sympadding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(iv + encrypted).decode()

# Decrypt using derived AES key
def ecc_decrypt(ciphertext_b64, aes_key):
    try:
        data = base64.b64decode(ciphertext_b64)
        iv, encrypted = data[:16], data[16:]

        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(encrypted) + decryptor.finalize()

        unpadder = sympadding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext.decode()
    except Exception as e:
        return f"[DECRYPTION ERROR]: {str(e)}"

