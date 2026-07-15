# ---------------- DIFFIE HELLMAN ----------------

def diffie_hellman():
    print("\n===== DIFFIE-HELLMAN KEY EXCHANGE =====")

    p = int(input("Enter prime number q: "))
    g = int(input("Enter primitive root alpha: "))

    a = int(input("Enter private key for User A: "))
    b = int(input("Enter private key for User B: "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    print("\nPublic Key of A:", A)
    print("Public Key of B:", B)

    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("\nSecret Key computed by A:", key_A)
    print("Secret Key computed by B:", key_B)

    if key_A == key_B:
        print("Key Exchange Successful!")
    else:
        print("Key Exchange Failed!")


diffie_hellman()