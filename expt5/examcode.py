from math import gcd, prod

def crt(a, m):
    M = prod(m)
    x = 0

    for i in range(len(m)):
        Mi = M // m[i]
        yi = pow(Mi, -1, m[i])

        print(f"M{i+1} = {Mi}")
        print(f"y{i+1} = {yi}\n")

        x += a[i] * Mi * yi

    print(f"x = {x % M} (mod {M})")

n = int(input("Enter number of congruences: "))
a = []
m = []

for i in range(n):
    a.append(int(input(f"a{i+1} = ")))
    m.append(int(input(f"m{i+1} = ")))

# Pairwise coprime check
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if gcd(m[i], m[j]) != 1:
            print("Moduli are not pairwise coprime.")
            exit()

crt(a, m)