def prime_factors(n):

    factors = {}
    d = 2

    while d * d <= n:

        while n % d == 0:
            if d not in factors:
                 factors[d] = 0
            else:
                 factors[d] += 1
            n //= d

        d += 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


def pohlig_hellman(g, h, p):

    n = p - 1
    factors = prime_factors(n)

    congruences = []

    print("\nCongruences obtained:")

    for q, e in factors.items():

        mod = q ** e

        g1 = pow(g, n // mod, p)
        h1 = pow(h, n // mod, p)

        for x in range(mod):

            if pow(g1, x, p) == h1:
                break

        print("x =", x, "mod", mod)

        congruences.append((x, mod))


    # CRT
    answer = 0

    print("\nCRT Computation:")

    for rem, mod in congruences:

        M = n // mod
        inverse = pow(M, -1, mod)

        print("M =", M)
        print("Inverse =", inverse)

        answer += rem * M * inverse


    return answer % n


g = int(input("Enter g: "))
h = int(input("Enter h: "))
p = int(input("Enter p: "))

x = pohlig_hellman(g, h, p)

print("\nFinal Answer")
print("x =", x)