key = input("Enter key: ").upper().replace("J", "I")

matrix = []
used = set()

for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in used:
        used.add(ch)
        matrix.append(ch)

matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

print("\nMatrix:")

for row in matrix:
    print(row)




text = input("Enter plaintext: ").upper().replace("J", "I")



prepared = ""
i = 0

while i < len(text):

    a = text[i]

    if i + 1 < len(text):
        b = text[i + 1]
    else:
        b = "X"

    if a == b:
        prepared += a + "X"
        i += 1
    else:
        prepared += a + b
        i += 2

if len(prepared) % 2 != 0:
    prepared += "X"


cipher = ""

for i in range(0, len(prepared), 2):

    a = prepared[i]
    b = prepared[i + 1]

    for r in range(5):
        for c in range(5):

            if matrix[r][c] == a:
                r1, c1 = r, c

            if matrix[r][c] == b:
                r2, c2 = r, c


    if r1 == r2:

        cipher += matrix[r1][(c1 + 1) % 5]
        cipher += matrix[r2][(c2 + 1) % 5]

    elif c1 == c2:

        cipher += matrix[(r1 + 1) % 5][c1]
        cipher += matrix[(r2 + 1) % 5][c2]

    else:

        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]


print("Encrypted:", cipher)


    # # Same row → move LEFT
    # if r1 == r2:

    #     decrypted += matrix[r1][(c1 - 1) % 5]
    #     decrypted += matrix[r2][(c2 - 1) % 5]


    # # Same column → move UP
    # elif c1 == c2:

    #     decrypted += matrix[(r1 - 1) % 5][c1]
    #     decrypted += matrix[(r2 - 1) % 5][c2]
