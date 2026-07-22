key = input("Enter key: ").upper()

letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

matrix = []

for ch in key + letters:
    if ch == "J":
        ch = "I"

    if ch not in matrix:
        matrix.append(ch)


symbols = "ADFGX"

text = input("Enter text: ").upper()

result = ""

for ch in text:

    if ch == "J":
        ch = "I"

    if ch.isalpha():

        index = matrix.index(ch)

        row = index // 5
        col = index % 5

        result += symbols[row] + symbols[col]


print("Encrypted:", result)

cipher = result

decrypted = ""

for i in range(0, len(cipher), 2):

    row = symbols.index(cipher[i])
    col = symbols.index(cipher[i + 1])

    index = row * 5 + col

    decrypted += matrix[index]


print("Decrypted:", decrypted)