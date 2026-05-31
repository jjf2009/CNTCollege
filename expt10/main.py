import math
from string import ascii_uppercase

def shift_encrypt(text, key):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        else:
            result += ch

    return result


def shift_decrypt(text, key):
    return shift_encrypt(text, -key)

def mod_inverse(a, m):
    if math.gcd(a, m) != 1:
        return None

    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        return "Invalid multiplicative key"

    result = ""

    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - 65
            result += chr(((a * x + b) % 26) + 65)
        else:
            result += ch

    return result


def affine_decrypt(cipher, a, b):

    result = ""
    a_inv = mod_inverse(a, 26)

    if a_inv is None:
        return "Invalid multiplicative key"

    for ch in cipher.upper():
        if ch.isalpha():
            y = ord(ch) - 65
            result += chr((a_inv * (y - b)) % 26 + 65)
        else:
            result += ch

    return result

def generate_key(text, key):

    key = list(key.upper())

    if len(text) == len(key):
        return "".join(key)

    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])

    return "".join(key)


def vigenere_encrypt(text, key):

    text = text.upper()
    key = generate_key(text, key)

    cipher = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i]) + ord(key[i])) % 26
            x += 65
            cipher += chr(x)
        else:
            cipher += text[i]

    return cipher


def vigenere_decrypt(cipher, key):

    cipher = cipher.upper()
    key = generate_key(cipher, key)

    text = ""

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            x = (ord(cipher[i]) - ord(key[i]) + 26) % 26
            x += 65
            text += chr(x)
        else:
            text += cipher[i]

    return text

def playfair_matrix(key):

    key = key.upper().replace("J", "I")

    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            matrix.append(ch)

    for ch in ascii_uppercase:
        if ch not in used and ch != 'J':
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def playfair_positions(matrix):

    pos = {}

    for i in range(5):
        for j in range(5):
            pos[matrix[i][j]] = (i, j)

    return pos


def prepare_text(text):

    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))

    prepared = ""
    i = 0

    while i < len(text):

        a = text[i]
        b = 'X'

        if i + 1 < len(text):
            b = text[i + 1]

        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'

    return prepared


def playfair_encrypt(text, key):

    matrix = playfair_matrix(key)
    pos = playfair_positions(matrix)

    text = prepare_text(text)

    cipher = ""

    for i in range(0, len(text), 2):

        a, b = text[i], text[i + 1]

        r1, c1 = pos[a]
        r2, c2 = pos[b]

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

def adfgx_encrypt(text):

    matrix = {
        'A': 'AA', 'B': 'AD', 'C': 'AF', 'D': 'AG', 'E': 'AX',
        'F': 'DA', 'G': 'DD', 'H': 'DF', 'I': 'DG', 'J': 'DX',
        'K': 'FA', 'L': 'FD', 'M': 'FF', 'N': 'FG', 'O': 'FX',
        'P': 'GA', 'Q': 'GD', 'R': 'GF', 'S': 'GG', 'T': 'GX',
        'U': 'XA', 'V': 'XD', 'W': 'XF', 'X': 'XG', 'Y': 'XX',
        'Z': 'AX'
    }

    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += matrix[ch] + " "

    return result

while True:

    print("\n===== CLASSICAL CIPHERS =====")
    print("1. Shift Cipher")
    print("2. Affine Cipher")
    print("3. Vigenere Cipher")
    print("4. Playfair Cipher")
    print("5. ADFGX Cipher")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        text = input("Enter text: ")
        key = int(input("Enter key: "))

        enc = shift_encrypt(text, key)
        dec = shift_decrypt(enc, key)

        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == 2:

        text = input("Enter text: ")

        a = int(input("Enter multiplicative key: "))
        b = int(input("Enter additive key: "))

        enc = affine_encrypt(text, a, b)
        dec = affine_decrypt(enc, a, b)

        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == 3:

        text = input("Enter text: ")
        key = input("Enter keyword: ")

        enc = vigenere_encrypt(text, key)
        dec = vigenere_decrypt(enc, key)

        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == 4:

        text = input("Enter text: ")
        key = input("Enter key: ")

        enc = playfair_encrypt(text, key)

        print("Encrypted:", enc)

    elif choice == 5:

        text = input("Enter text: ")

        enc = adfgx_encrypt(text)

        print("Encrypted:", enc)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
