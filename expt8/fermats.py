import math

n = int(input("Enter n: "))

a = math.isqrt(n)

if a * a < n:
    a += 1

while True:

    b2 = a * a - n
    b = math.isqrt(b2)

    if b * b == b2:
        break

    a += 1

factor1 = a - b
factor2 = a + b

print("Factors:", factor1, factor2)