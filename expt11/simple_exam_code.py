from math import gcd

def text_to_number(text):
    number = ""

    for char in text.lower():
        if char.isalpha():
            number += str(ord(char) - ord('a'))

    return int(number)


def rsa():
    print("\n===== RSA ALGORITHM =====")

    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input("Enter public key e: "))

    while gcd(e, phi) != 1:
        print("e must be coprime with phi")
        e = int(input("Enter another e: "))

    d = pow(e, -1, phi)

    print("Public Key:", (e, n))
    print("Private Key:", (d, n))

    message = input("Enter message: ")

    m = text_to_number(message)

    if m >= n:
        m = m % n

    cipher = pow(m, e, n)
    print("Encrypted Message:", cipher)

    decrypted = pow(cipher, d, n)
    print("Decrypted Numeric Value:", decrypted)


rsa()