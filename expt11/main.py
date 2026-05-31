

def mod_inverse(a, m):

    for x in range(1, m):
        if (a * x) % m == 1:
            return x

    return None


def rsa():

    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input("Enter public key e: "))

    d = mod_inverse(e, phi)

    print("\nPublic Key =", (e, n))
    print("Private Key =", (d, n))

    msg = int(input("\nEnter message(integer): "))

    cipher = pow(msg, e, n)

    print("Encrypted Message =", cipher)

    plain = pow(cipher, d, n)

    print("Decrypted Message =", plain)



def diffie_hellman():

    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))

    a = int(input("Enter Alice private key: "))
    b = int(input("Enter Bob private key: "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    print("\nAlice Public Key =", A)
    print("Bob Public Key =", B)

    keyA = pow(B, a, p)
    keyB = pow(A, b, p)

    print("\nShared Secret Key for Alice =", keyA)
    print("Shared Secret Key for Bob =", keyB)



while True:

    print("\n===== MENU =====")
    print("1. RSA Algorithm")
    print("2. Diffie Hellman Key Exchange")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        rsa()

    elif choice == 2:
        diffie_hellman()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")