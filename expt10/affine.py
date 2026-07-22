import math

text = input("Enter text: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) != 1:
    print("Invalid key")

else:
    encrypted = ""

    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - 65
            encrypted += chr((a * x + b) % 26 + 65)
        else:
            encrypted += ch

    print("Encrypted:", encrypted)

    # Modular inverse of a
    a_inv = pow(a, -1, 26)

    decrypted = ""

    for ch in encrypted:
        if ch.isalpha():
            y = ord(ch) - 65
            decrypted += chr((a_inv * (y - b)) % 26 + 65)
        else:
            decrypted += ch

    print("Decrypted:", decrypted)