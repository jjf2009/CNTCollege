
from prettytable import PrettyTable
def extended_gcd(a, b):
    myTable = PrettyTable(['q', 'r1', 'r2', 'r', 's1', 's2', 's', 't1', 't2', 't'])
    myTable.align = 'c'  
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        r  = r1 - q * r2
        s  = s1 - q * s2
        t  = t1 - q * t2
        myTable.add_row([q, r1, r2, r, s1, s2, s, t1, t2, t])
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    print("\n" + str(myTable))
    return r1, s1, t1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def euler_totient(m):
    count = 0
    for k in range(1, m + 1):
        if gcd(k, m) == 1:
            count += 1
    return count


def modular_exponentiation(base, exp, mod):
    base = base % mod
    result = 1
    while exp > 0:
        if exp % 2 == 1:                  
            result = (result * base) % mod
        base = (base * base) % mod        
        exp //= 2                          
    return result

# ─────────────────────────────────────────────
#  METHOD A — EUCLID'S METHOD (EEA)
# ─────────────────────────────────────────────

def euclids_method(a, b, m):
    """
    Solve ax ≡ b (mod m) using the Extended Euclidean Algorithm.
    """
    print(f"  Equation : {a}x ≡ {b} (mod {m})")

    d, s, t = extended_gcd(a, m)

    print(f"\n Result   : gcd({a}, {m}) = {d}")
    print(f"   Bézout   : {a}·({s}) + {m}·({t}) = {d}")

    if b % d != 0:
        print(f"\n  ✗ No solution: gcd({a},{m}) = {d} does not divide {b}")
        return None
    s0 = (s * (b // d)) % m
    solutions = [(s0 + i * (m // d)) % m for i in range(d)]
    solutions.sort()

    print(f"\n  x₀ = s · (b/d) mod m  =  {s} · {b//d} mod {m}  =  {s0}")
    print(f"  Number of solutions: {d}")
    print(f"\n  Solutions modulo {m}: {solutions}")
    return solutions


# ─────────────────────────────────────────────
#  METHOD B — MODULAR EXPONENTIATION + TOTIENT
# ─────────────────────────────────────────────

def totient_method(a_t, b_t, m_t):

    print(f"  Equation : {a_t}x ≡ {b_t} (mod {m_t})")
    d = gcd(a_t, m_t)
    a=int(a_t/d);
    b=int(b_t/d);
    m=int(m_t/d);
    d = gcd(a, m)
    if d != 1:
        print(f"\n  ✗ Method requires gcd(a,m) = 1, but gcd({a},{m}) = {d}")
        print(f"  ✗ Euler's theorem is not directly applicable.")
        return None

    phi= euler_totient(m)
    print(f"\n  φ({m}) = {phi}")
    print(f"\n  By Euler's Theorem: {a}^φ({m}) ≡ 1 (mod {m})")
    print(f"  So inverse of {a} = {a}^(φ({m})-1) = {a}^{phi-1} (mod {m})")

    inv_a = modular_exponentiation(a, phi - 1, m)
    print(f"\n  a⁻¹ = {a}^{phi-1} mod {m} = {inv_a}")

    x = (inv_a * b) % m
    print(f"  x   = a⁻¹ · b mod m = {inv_a} · {b} mod {m} = {x}")
    print(f"\n  Solution: x ≡ {x} (mod {m})")
    return [x]


# ─────────────────────────────────────────────
#  METHOD C — MULTIPLICATIVE INVERSE METHOD
# ─────────────────────────────────────────────

def multiplicative_inverse_method(a, b, m):
    print("  METHOD C: MULTIPLICATIVE INVERSE METHOD")
    print(f"  Equation : {a}x ≡ {b} (mod {m})")

    d = gcd(a, m)
    if d != 1:
        print(f"\n  ✗ Inverse does not exist: gcd({a},{m}) = {d} ≠ 1")
        return None

    # Use EEA silently to find inverse
    r1, r2 = a, m
    s1, s2 = 1, 0

    while r2 > 0:
        q  = r1 // r2
        r1, r2 = r2, r1 - q * r2
        s1, s2 = s2, s1 - q * s2

    inv_a = s1 % m

    print(f"\n  Finding a⁻¹ such that {a} · a⁻¹ ≡ 1 (mod {m})")
    print(f"  Using EEA  →  {a}⁻¹ ≡ {inv_a} (mod {m})")
    print(f"  Verify     :  {a} × {inv_a} = {a * inv_a} ≡ {(a * inv_a) % m} (mod {m})  ✓")

    x = (inv_a * b) % m
    print(f"\n  x = a⁻¹ · b mod m  =  {inv_a} · {b} mod {m}  =  {x}")
    print(f"\n  Solution: x ≡ {x} (mod {m})")
    return [x]



def main():
    print("LINEAR CONGRUENCE EQUATION SOLVER")
    print("         ax ≡ b  (mod m)")
 

    print("\nEnter the values for ax ≡ b (mod m):")
    a = int(input("  a = "))
    b = int(input("  b = "))
    m = int(input("  m = "))

    print(f"\n  Solving: {a}x ≡ {b} (mod {m})")
    d = gcd(a, m)
    print(f"  gcd({a}, {m}) = {d}")
    if b % d != 0:
        print(f"  ✗ No solution exists since {d} ∤ {b}\n")
        return

    # Run all three methods
    sol_a = euclids_method(a, b, m)
    sol_b = totient_method(a, b, m)
    sol_c = multiplicative_inverse_method(a, b, m)

    # Summary
    print("\n" + "═"*55)
    print("  SUMMARY")
    print("═"*55)
    print(f"  Equation            :  {a}x ≡ {b} (mod {m})")
    print(f"  Method A (Euclid)   :  {sol_a}")
    print(f"  Method B (Totient)  :  {sol_b}")
    print(f"  Method C (Inv)      :  {sol_c}")
    print("═"*55)


if __name__ == "__main__":
    main()
