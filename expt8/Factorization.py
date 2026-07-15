import math

# ---------------- BASIC FUNCTIONS ----------------

def gcd(a, b):
    return math.gcd(a, b)

def is_square(n):
    root = math.isqrt(n)
    return root * root == n

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False

    return True


# ---------------- 1. FERMAT FACTORIZATION ----------------

def fermat_factorization(n):

    a = math.isqrt(n)

    if a * a < n:
        a += 1

    print("\nFermat Factorization Steps:")

    while True:

        b2 = a * a - n

        print(f"a = {a}")
        print(f"a^2 - n = {a*a} - {n} = {b2}")

        if is_square(b2):

            b = math.isqrt(b2)

            print(f"\nPerfect square found: {b2}")
            print(f"b = sqrt({b2}) = {b}")

            print("\nUsing:")
            print("n = a^2 - b^2")
            print("n = (a-b)(a+b)")

            factor1 = a - b
            factor2 = a + b

            return factor1, factor2

        a += 1


# ---------------- 2. POLLARD p - 1 FACTORIZATION ----------------

def pollard_p_minus_1(n, B, a):

    print("\nPollard p - 1 Steps:")

    for j in range(2, B + 1):

        if not is_prime(j):
            continue

        power = j

        while power * j <= B:
            power *= j

        a = pow(a, power, n)

        d = gcd(a - 1, n)

        print(f"\nj = {j}")
        print(f"largest power of {j} <= {B} is {power}")
        print(f"a = a^{power} mod n = {a}")
        print(f"gcd(a - 1, n) = gcd({a-1}, {n}) = {d}")

        if d != 1 and d != n:
            return d, n // d

    return None


# ---------------- 3. POLLARD RHO FACTORIZATION ----------------

def pollard_rho(n):

    if n % 2 == 0:
        return 2, n // 2

    def g(x):
        return (x * x + 1) % n

    x = 2
    y = 2
    d = 1

    print("\nPollard Rho Steps:")
    print("Using g(x) = x^2 + 1")

    while d == 1:

        x = g(x)          # x = g(x)
        y = g(g(y))       # y = g(g(y))

        diff = abs(x - y)
        d = gcd(diff, n)

        print(f"\nx = {x}")
        print(f"y = {y}")
        print(f"|x - y| = {diff}")
        print(f"gcd({diff}, {n}) = {d}")

    if d == n:
        return None

    return d, n // d


# ---------------- 4. BASIC QUADRATIC SIEVE ----------------

def quadratic_sieve_basic(n):

    x = math.isqrt(n)

    if x * x < n:
        x += 1

    print("\nQuadratic Sieve Steps:")
    print(f"Starting x = ceil(sqrt({n})) = {x}")

    while True:

        y2 = (x * x) % n

        print(f"\n{x}^2 mod {n} = {y2}")

        if is_square(y2):

            y = math.isqrt(y2)

            print(f"\nPerfect square found:")
            print(f"{y2} = {y}^2")

            print("\nTherefore:")
            print(f"{x}^2 ≡ {y}^2 mod {n}")

            factor1 = gcd(x - y, n)
            factor2 = gcd(x + y, n)

            print(f"\ngcd({x} - {y}, {n}) = {factor1}")
            print(f"gcd({x} + {y}, {n}) = {factor2}")

            if factor1 != 1 and factor1 != n:
                return factor1, n // factor1

            if factor2 != 1 and factor2 != n:
                return factor2, n // factor2

        x += 1


# ---------------- MENU ----------------

while True:

    print("\n==============================")
    print(" FACTORIZATION METHODS")
    print("==============================")
    print("1. Fermat Factorization")
    print("2. Pollard p - 1 Factorization")
    print("3. Pollard Rho Method")
    print("4. Quadratic Sieve Method")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        n = int(input("Enter odd composite number n: "))

        factors = fermat_factorization(n)

        print("\nFactors are:")
        print(f"{n} = {factors[0]} × {factors[1]}")

    elif choice == 2:

        n = int(input("Enter composite number n: "))
        B = int(input("Enter bound B: "))
        a = int(input("Enter base a: "))

        result = pollard_p_minus_1(n, B, a)

        print("\nUsing Pollard p - 1:")

        if result is None:
            print("No factor found.")
        else:
            print(f"Factors are: {result[0]} and {result[1]}")

    elif choice == 3:

        n = int(input("Enter composite number n: "))

        result = pollard_rho(n)

        print("\nUsing Pollard Rho:")

        if result is None:
            print("No factor found.")
        else:
            print(f"Factors are: {result[0]} and {result[1]}")

    elif choice == 4:

        n = int(input("Enter composite number n: "))

        result = quadratic_sieve_basic(n)

        print("\nUsing Quadratic Sieve:")

        if result is None:
            print("No factor found.")
        else:
            print(f"Factors are: {result[0]} and {result[1]}")

    elif choice == 5:

        print("Program ended.")
        break

    else:
        print("Invalid choice.")