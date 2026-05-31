import math
import time
from sympy import isprime

# ─── HELPERS ─────────────────────────────────────────────────────────────────

def get_number():
    while True:
        try:
            n = int(input("  Enter number to factor: "))
            if n < 4:
                print("  Please enter an integer >= 4.")
            elif isprime(n):
                print(f"  {n} is prime — nothing to factor.")
            else:
                return n
        except ValueError:
            print("  Invalid input.")

def show_result(n, x, y):
    print(f"\n  Number  : {n}")
    if x is None:
        print("  Result  : Could not find two factors.")
    else:
        print(f"  x       : {x}")
        print(f"  y       : {y}")
        print(f"  x * y   : {x} * {y} = {x * y}")
        print(f"  Verify  : {'CORRECT' if x * y == n else 'ERROR'}")

def sieve(limit):
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i*i, limit + 1, i):
                is_p[j] = False
    return [i for i in range(2, limit + 1) if is_p[i]]

def pollards_p1(n, B=200):
    """
    If factor p has (p-1) B-smooth:
      a = 2^(all prime powers <= B) mod n
      gcd(a-1, n) gives a factor.
    """
    prime_powers = []
    for p in sieve(B):
        q = p
        while q <= B:
            prime_powers.append(q)
            q *= p
    print(f"\n  B = {B}  |  Prime powers to process: {len(prime_powers)}")
    print(f"\n  {'Step':<6} {'Prime power q':<16} {'a mod n (last 8 digits)':<26} {'gcd(a-1, n)'}")
    print(f"  {'-'*65}")
    a = 2
    for i, q in enumerate(prime_powers):
        a = pow(a, q, n)
        d = math.gcd(a - 1, n)
        if i < 8 or d > 1:
            print(f"  {i+1:<6} {q:<16} ...{str(a)[-8:]:<26} {d}")
        if 1 < d < n:
            print("\n  Factor found!")
            return d, n // d
        if d == n:
            print("\n  d = n — failed. Try a larger B.")
            return None, None

    print(f"\n  No factor found with B = {B}. Try increasing B.")
    return None, None

# ─── 3. QUADRATIC SIEVE ──────────────────────────────────────────────────────

def quadratic_sieve(n):
    # 1. Setup
    B = 40  # Keep small for exam memory
    fb = [p for p in range(2, 200) if pow(n, (p - 1) // 2, p) in (0, 1)][:B]
    sqrtn = math.isqrt(n)
    smooth = [] # Stores (x, ft, bitmask)

    # 2. Find Smooth Numbers
    for t in range(1, 500):
        x = sqrtn + t
        ft = x*x - n
        rem, mask = ft, 0
        for i, p in enumerate(fb):
            while rem % p == 0:
                rem //= p
                mask ^= (1 << i)
        if rem == 1:
            smooth.append((x, ft, mask))
            if len(smooth) > B: break

    # 3. Solve Linear Dependency (Gaussian Elimination)
    basis = {} # {mask: product_of_x, product_of_ft}
    for x, ft, mask in smooth:
        orig_mask, orig_x, orig_ft = mask, x, ft
        for b in basis:
            if (mask ^ b) < mask:
                mask ^= b
                orig_x *= basis[b]
                orig_ft *= basis[b]
        
        if mask > 0:
            basis[mask] = (orig_x, orig_ft)
        else:
            # Dependency found!
            y = int(math.isqrt(orig_ft)) % n
            d = math.gcd(abs(orig_x - y), n)
            if 1 < d < n: return d, n // d
    return None

# ─── 4. POLLARD'S RHO ────────────────────────────────────────────────────────

def pollards_rho(n):
    if n % 2 == 0: return 2, n // 2
    x, y, d = 2, 2, 1
    f = lambda x: (x * x + 1) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
        
    return (d, n // d) if 1 < d < n else None
# ─── MENU ────────────────────────────────────────────────────────────────────

def menu():
    print("=" * 50)
    print("      INTEGER FACTORIZATION ALGORITHMS")
    print("=" * 50)

    while True:
        print("""
  1. Pollard's P-1 Algorithm
  2. Quadratic Sieve
  3. Pollard's Rho
  0. Exit""")

        choice = input("\n  Choice: ").strip()

        if choice == '0':
            print("\n  Goodbye!\n")
            break
        elif choice not in ('1', '2', '3', '4'):
            print("  Invalid choice. Enter 0-4.")
            continue

        n = get_number()

        if choice == '1':
            print("\n  [Pollard's P-1]")
            try:
                B = int(input("  Smoothness bound B (default 200): ") or 200)
            except ValueError:
                B = 200
            x, y = pollards_p1(n, B)

        elif choice == '2':
            print("\n  [Quadratic Sieve]")
            x, y = quadratic_sieve(n)

        elif choice == '3':
            print("\n  [Pollard's Rho]")
            x, y = pollards_rho(n)



        show_result(n, x, y)
        input("\n  Press Enter to continue...")

if __name__ == "__main__":
    menu()