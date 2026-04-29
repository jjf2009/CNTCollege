
def blum_blum_random(n, seed, num_bits):
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


def main():
    s = int(input("Enter value of s: "))
    n = int(input("Enter value of n: "))
    num = int(input("Enter number of iterations: "))

    key = blum_blum_random(n, s, num)
    print(f"Random Number Generated: {key}")


if __name__ == "__main__":
    main()