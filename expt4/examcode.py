def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

def phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count

a = int(input("a = "))
b = int(input("b = "))
m = int(input("m = "))

d = gcd(a, m)

if b % d != 0:
    print("No Solution")
else:
    print("\nMethod 1: Extended Euclid")
    d, x, y = extended_gcd(a, m)
    x = (x * (b // d)) % m
    print("x =", x)

    print("\nMethod 2: Euler Totient")
    a1, b1, m1 = a // d, b // d, m // d
    p = phi(m1)
    inv = pow(a1, p - 1, m1)
    x = (inv * b1) % m1
    print("x =", x)

    print("\nMethod 3: Multiplicative Inverse")
    d, inv, _ = extended_gcd(a1, m1)
    inv %= m1
    x = (inv * b1) % m1
    print("x =", x)