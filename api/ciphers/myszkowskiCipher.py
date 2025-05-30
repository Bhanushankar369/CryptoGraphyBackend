import math

def myszkowski_encrypt(plaintext, key):
    from collections import defaultdict

    # Step 1: Format
    key = key.upper()
    plaintext = plaintext.replace(" ", "").upper()

    # Step 2: Build key index
    key_order = {}
    sorted_key = sorted(set(key))
    count = 1
    for ch in sorted_key:
        for idx, k in enumerate(key):
            if k == ch and idx not in key_order:
                key_order[idx] = count
                if key.count(k) == 1:
                    count += 1
        if key.count(ch) > 1:
            count += 1

    # Step 3: Fill matrix
    cols = len(key)
    rows = -(-len(plaintext) // cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    i = 0
    for r in range(rows):
        for c in range(cols):
            if i < len(plaintext):
                matrix[r][c] = plaintext[i]
                i += 1

    # Step 4: Read by group order
    cipher = ''
    sorted_items = sorted(key_order.items(), key=lambda x: (x[1], x[0]))
    groups = defaultdict(list)
    for idx, val in sorted_items:
        groups[val].append(idx)

    for group in sorted(groups):
        for idx in groups[group]:
            for r in range(rows):
                if matrix[r][idx]:
                    cipher += matrix[r][idx]
    return cipher


def myszkowski_decrypt(ciphertext, key):
    from collections import defaultdict

    key = key.upper()
    ciphertext = ciphertext.replace(" ", "").upper()

    key_order = {}
    sorted_key = sorted(set(key))
    count = 1
    for ch in sorted_key:
        for idx, k in enumerate(key):
            if k == ch and idx not in key_order:
                key_order[idx] = count
                if key.count(k) == 1:
                    count += 1
        if key.count(ch) > 1:
            count += 1

    cols = len(key)
    rows = -(-len(ciphertext) // cols)

    # Step 1: Determine reading order
    sorted_items = sorted(key_order.items(), key=lambda x: (x[1], x[0]))
    groups = defaultdict(list)
    for idx, val in sorted_items:
        groups[val].append(idx)

    # Step 2: Create empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    i = 0
    for group in sorted(groups):
        for idx in groups[group]:
            for r in range(rows):
                if i < len(ciphertext):
                    matrix[r][idx] = ciphertext[i]
                    i += 1

    # Step 3: Read row by row
    plaintext = ''
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c]:
                plaintext += matrix[r][c]
    return plaintext

