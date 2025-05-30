def rail_fence_encrypt(plaintext, rails):
    rails = int(rails)
    if rails == 1:
        return plaintext
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i, char in enumerate(plaintext):
        fence[rail][i] = char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    cipher = ''.join([''.join(row) for row in fence])
    return cipher.replace('', '')

def rail_fence_decrypt(ciphertext, rails):
    rails = int(rails)
    if rails == 1:
        return ciphertext
    mark = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        mark[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if mark[r][c] == '*' and index < len(ciphertext):
                mark[r][c] = ciphertext[index]
                index += 1
    result = []
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        result.append(mark[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join(result)
