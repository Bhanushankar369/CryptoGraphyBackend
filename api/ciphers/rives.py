def rc4(key, text):
    S = list(range(256))
    j = 0
    out = bytearray()

    # Ensure key is a string before converting with ord()
    if isinstance(key, str):
        key = [ord(c) for c in key]
    elif isinstance(key, (bytes, bytearray)):
        key = list(key)  # treat bytes directly
    else:
        raise TypeError("Key must be a string or bytes")

    # Convert text to bytes if it's a string
    if isinstance(text, str):
        text = text.encode()

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(char ^ K)

    return out
