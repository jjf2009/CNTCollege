

def get_prime_factors(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def pohlig_hellman(g, h, p):
    n = p - 1
    factors = get_prime_factors(n)
    
    congruences = []
    for q, e in factors.items():
        qe = q**e
        g1, h1 = pow(g, n // qe, p), pow(h, n // qe, p)
        xq = next(x for x in range(qe) if pow(g1, x, p) == h1)
        congruences.append((xq, qe))
    
    x, M = 0, n
    for rem, mod in congruences:
        Mi = M // mod
        x += rem * Mi * pow(Mi, -1, mod)
    return x % M

# Example usage:
# print(pohlig_hellman(2, 3, 19))