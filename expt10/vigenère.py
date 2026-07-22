text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

encrypted = ""

j = 0

for ch in text:
    if ch.isalpha():
        x = (ord(ch) - 65 + ord(key[j % len(key)]) - 65) % 26
        encrypted += chr(x + 65)
        j += 1
    else:
        encrypted += ch

print("Encrypted:", encrypted)

decrypted = ""

j = 0

for ch in encrypted:
    if ch.isalpha():
        x = (ord(ch) - 65 - (ord(key[j % len(key)]) - 65)) % 26
        decrypted += chr(x + 65)
        j += 1
    else:
        decrypted += ch

print("Decrypted:", decrypted)