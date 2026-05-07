def blum_blum_shub(n, seed, num_bits):
    if n <= 1:
        raise ValueError("n must be greater than 1")
    if seed <= 0 or seed >= n:
        raise ValueError("seed must be greater than 0 and less than n")
    if num_bits < 0:
        raise ValueError("num_bits must be non-negative")

    state = seed
    bits = []
    for _ in range(num_bits):
        state = pow(state, 2, n)
        bits.append(str(state % 2))
    return "".join(bits)


def linear_congruential_generator(m, a, c, seed, num_iterations):
    if m <= 0:
        raise ValueError("m must be greater than 0")
    if a <= 0 or a >= m:
        raise ValueError("a must be between 0 and m")
    if c < 0 or c >= m:
        raise ValueError("c must be between 0 and m")
    if seed < 0 or seed >= m:
        raise ValueError("seed must be between 0 and m")
    if num_iterations < 0:
        raise ValueError("num_iterations must be non-negative")

    results = []
    state = seed
    for _ in range(num_iterations):
        state = (a * state + c) % m
        results.append(str(state))
    return results


def run_bbs():
    print("\n--- Blum Blum Shub Generator ---")
    try:
        p = int(input("Enter prime p: "))
        q = int(input("Enter prime q: "))
        n = p * q
        print(f"Computed n = p * q = {n}")
        seed = int(input("Enter seed (must be > 0 and < n): "))
        num_bits = int(input("Enter number of bits to generate: "))
        result = blum_blum_shub(n, seed, num_bits)
        print(f"Generated bits: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def run_lcg():
    print("\n--- Linear Congruential Generator (LCG) ---")
    try:
        m = int(input("Enter modulus m (e.g. 16): "))
        a = int(input("Enter multiplier a (e.g. 5): "))
        c = int(input("Enter increment c (e.g. 3): "))
        seed = int(input("Enter seed X0 (e.g. 7): "))
        num_iterations = int(input("Enter number of values to generate: "))
        
        result = linear_congruential_generator(m, a, c, seed, num_iterations)
        print(f"Generated values: {', '.join(result)}")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n========== PRNG Menu ==========")
        print("1. Blum Blum Shub (BBS)")
        print("2. Linear Congruential Generator (LCG)")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            run_bbs()
        elif choice == "2":
            run_lcg()
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()