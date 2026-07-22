def shift(text, key):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        else:
            result += ch

    return result


text = input("Enter text: ")
key = int(input("Enter key: "))

encrypted = shift(text, key)
decrypted = shift(encrypted, -key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)