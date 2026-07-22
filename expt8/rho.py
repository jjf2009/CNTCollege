import math

n = int(input("Enter n: "))

if n % 2 == 0:
    print("Factors:", 2, n // 2)

else:

    x = 2
    y = 2
    d = 1

    while d == 1:

        x = (x * x + 1) % n

        y = (y * y + 1) % n
        y = (y * y + 1) % n

        d = math.gcd(abs(x - y), n)

        print("x =", x)
        print("y =", y)
        print("gcd =", d)

    if d == n:
        print("Factor not found")

    else:
        print("Factors:", d, n // d)