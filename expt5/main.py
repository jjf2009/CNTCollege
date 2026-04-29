

def extended_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def mod_inverse(a: int, m: int):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists.")
    return x % m

def gcd(a, b):
    r1 = a
    r2 = b
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r
    return r1

def are_pairwise_coprime(moduli):
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                return False
    return True


def chinese_remainder_theorem(remainders, moduli):
    if not are_pairwise_coprime(moduli):
        print("Moduli must be pairwise coprime.")
        return None, None

    M = 1
    for m in moduli:
        M *= m
    print(f"M = {M}\n")

    x = 0
    for idx, (ai, mi) in enumerate(zip(remainders, moduli), start=1):
        Mi = M // mi
        yi = mod_inverse(Mi, mi)
        contrib = ai * Mi * yi
        print(f"m{idx} = {mi}")
        print(f"M{idx} = M / m{idx} = {M} / {mi} = {Mi}")
        print(f"y{idx} = inverse of M{idx} mod m{idx} = inverse of {Mi} mod {mi} = {yi}")
        print(f"Contribution: a{idx} * M{idx} * y{idx} = {ai} * {Mi} * {yi} = {contrib}\n")
        x += contrib

    return x % M, M


def main():
    n = int(input("Enter number of congruences: "))
    remainders = []
    moduli = []

    for i in range(n):
        remainders.append(int(input(f"Enter remainder a{i + 1}: ")))
        moduli.append(int(input(f"Enter modulus m{i + 1}: ")))

    x, M = chinese_remainder_theorem(remainders, moduli)
    if x is not None:
        print(f"x = {x} (mod {M})")


if __name__ == "__main__":
    main()