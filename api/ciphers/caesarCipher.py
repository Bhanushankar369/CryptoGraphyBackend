import re

def is_alpha(s):
    return bool(re.match(r'^[A-Za-z]+$', s))

def caesar_encrypt(text, freq):
    text = text.strip()
    upper_case = [chr(65 + index) for index in range(26)]
    lower_case = [chr(97 + index) for index in range(26)]

    ans = ""
    shift = freq % 26

    for ch in text:
        code = ord(ch)
        if not is_alpha(ch):
            ans += ch
        elif ch in upper_case:
            ans += chr(((code - 65 + shift) % 26) + 65)
        elif ch in lower_case:
            ans += chr(((code - 97 + shift) % 26) + 97)

    return ans

def caesar_decrypt(text, freq):
    text = text.strip()
    upper_case = [chr(65 + index) for index in range(26)]
    lower_case = [chr(97 + index) for index in range(26)]

    ans = ""
    shift = freq % 26

    for ch in text:
        code = ord(ch)
        if not is_alpha(ch):
            ans += ch
        elif ch in upper_case:
            ans += chr(((code - 65 - shift) % 26) + 65)
        elif ch in lower_case:
            ans += chr(((code - 97 - shift) % 26) + 97)

    return ans

