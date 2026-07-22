import math
def jacobi(a, n):
    result = 1
    a = a % n

    while a != 0:

        while a % 2 == 0:

            a //= 2

            if n % 8 == 3 or n % 8 == 5:
                result = -result

        a, n = n, a

        if a % 4 == 3 and n % 4 == 3:
            result = -result

        a %= n

    if n == 1:
        return result

    return 0


n = int(input("Enter n: "))
a = int(input("Enter a: "))

if math.gcd(a, n) != 1:

    print("Composite")

else:

    j = jacobi(a, n)

    x = pow(a, (n - 1) // 2, n)

    print("Jacobi Symbol:", j)
    print("a^((n-1)/2) mod n:", x)

    if x == j % n:
        print("Probably Prime")
    else:
        print("Composite")