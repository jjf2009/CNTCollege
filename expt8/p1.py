import math

n = int(input("Enter n: "))
B = int(input("Enter B: "))
a = int(input("Enter a: "))

for e in range(2, B + 1):

    a = pow(a, e, n)

    d = math.gcd(a - 1, n)

    print("e =", e)
    print("a =", a)
    print("gcd =", d)

    if d != 1 and d != n:
        print("Factors:", d, n // d)
        break