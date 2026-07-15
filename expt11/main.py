from math import gcd

def text_to_number(text):
    text = text.lower()
    number = ""

    for char in text:
        if char.isalpha():
            value = ord(char) - ord('a')
            number += str(value)

    return int(number)

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa():
    print("\n===== RSA ALGORITHM =====")

    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input("Enter public key e: "))

    while gcd(e, phi) != 1:
        print("e must be coprime with phi.")
        e = int(input("Enter another e: "))

    d = mod_inverse(e, phi)

    print("\nPublic Key (e, n):", (e, n))
    print("Private Key (d, n):", (d, n))

    message = input("\nEnter message: ")


    m = text_to_number(message)

    if m >= n:
        m = m % n

    cipher = pow(m, e, n)
    print("Encrypted Message:", cipher)
    decrypted = pow(cipher, d, n)
    print("Decrypted Numeric Value:", decrypted)

rsa()