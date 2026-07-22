import math

n = int(input("Enter n: "))

x = math.isqrt(n)

if x * x < n:
    x += 1

while True:

    y2 = (x * x) % n
    y = math.isqrt(y2)

    if y * y == y2:

        factor1 = math.gcd(x - y, n)
        factor2 = math.gcd(x + y, n)

        if factor1 != 1 and factor1 != n:
            print("Factors:", factor1, n // factor1)
            break

        if factor2 != 1 and factor2 != n:
            print("Factors:", factor2, n // factor2)
            break

    x += 1