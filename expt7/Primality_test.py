import math

def calculate_jacobi(a, n):
    assert n > a > 0 and n % 2 == 1
    a = a % n
    jacobi = 1
    while a != 0:
        while a % 2 == 0:
            a = a // 2
           
            if n % 8 == 3 or n % 8 == 5:
                jacobi = -jacobi
        a, n = n, a
        
        if a % 4 == 3 and n % 4 == 3:
            jacobi = -jacobi
        a = a % n
    if n == 1:
        return jacobi
    else:
        return 0

def get_a_from_user(limit, check_gcd=False, n=None):

    while True:
        try:
            prompt_msg = f"   Enter value for 'a' (2 <= a <= {limit - 1})"
            if check_gcd:
                prompt_msg += f" such that gcd(a, {n}) = 1"
            prompt_msg += ": "
            
            a = int(input(prompt_msg))
            
            if not (1 < a < limit):
                print(f"   [Error] 'a' must be between 2 and {limit - 1}.")
                continue
                
            if check_gcd:
                g = math.gcd(a, n)
                if g != 1:
                    print(f"   [Error] gcd({a}, {n}) is {g}, not 1. Try a different 'a'.")
                    continue
                
            return a
        except ValueError:
            print("   [Error] Invalid input. Please enter an integer.")

def fermat_test(p):
    print("\nFermat's Primality Testing")
    if p <= 1:
        return "Composite"
    if p == 2 or p == 3:
        return "Prime"
        
    print("1) Choose a < p:")
    a = get_a_from_user(p)
    print(f"   Let a = {a}")
    
    g = math.gcd(a, p)
    print(f"2) Compute gcd(a, p) -> gcd({a}, {p}) = {g}")

    if g > 1:
        print(f"3) If gcd(a, p) > 1 -> {g} > 1")
        print(f"   then return '{p} is composite'")
        return "Composite"
        
    print(f"4) If gcd(a, p) = 1")
    y = pow(a, p - 1, p)
    print(f"   y <- a^(p-1) (mod p) -> {a}^({p}-1) (mod {p}) = {y}")
    
    if y != 1:
        print(f"   If (y != 1 (mod p)) -> ({y} != 1)")
        print(f"   then {p} is composite")
        return "Composite"
    else:
        print(f"   else {p} is Prime")
        return "Prime"


def miller_rabin_test(p):
    print("\nMiller Rabin Test")
    if p <= 1 or p % 2 == 0:
        if p == 2: return "Prime"
        return "Composite (Input must be odd > 2)"

    m = p - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    print(f"1. {p}-1 = 2^k * m -> 2^{k} * {m}. So k={k}, m={m} (m is odd).")
    
    print("   choose a such that gcd(a,p)=1:")
    a = get_a_from_user(p, check_gcd=True, n=p)
    print(f"   Let a = {a}")
    
    b = pow(a, m, p)
    print(f"2. b <- a^m (mod p) -> {a}^{m} (mod {p}) = {b}")
    
    if b == 1:
        print(f"3. If b = 1 (mod p) -> {b} = 1")
        print(f"   then return '{p} is a Prime'")
        return "Prime"
    else:
        print(f"3. b is not 1. Moving to loop.")

    print(f"4. For i <- 1 to (k-1) [where k={k}]")
    
    if b == p - 1:
        print(f"5.   [Initial] If b == -1 (mod p) -> b is {p-1}")
        print(f"     then return '{p} is Prime'")
        return "Prime"
        
    for i in range(1, k):
        print(f"     [Loop i={i}]")
        b = pow(b, 2, p)
        print(f"     else b <- b^2 (mod p) -> {b}")
        
        if b == p - 1:
            print(f"5.   If b == -1 (mod p) -> b is {p-1}")
            print(f"     then return '{p} is Prime'")
            return "Prime"

    # Step 6
    print(f"6. return '{p} is composite'")
    return "Composite"


def solovay_strassen_test(n):
    print("\nSolovay Strassen Test")
    if n <= 2 or n % 2 == 0:
        return "Composite (Input must be an odd positive integer)"
        
    # Step 1
    print("1. Choose a random integer a such that 2 <= a <= (n-1) and gcd(a,n)=1:")
    a = get_a_from_user(n, check_gcd=True, n=n)
    print(f"   Let a = {a}")
    
    # Step 2
    x = calculate_jacobi(a, n)
    print(f"2. Compute Jacobi Symbol x <- (a/n) -> ({a}/{n}) = {x}")
    
    # Step 3
    if x == 0:
        print(f"3. If x=0 then return '{n} is composite'")
        return "Composite"
    else:
        y = pow(a, (n - 1) // 2, n)
        print(f"3. else compute y <- a^((n-1)/2) mod n -> {a}^({(n-1)//2}) mod {n} = {y}")
        
    # Step 4
    x_mod_n = x % n 
    print(f"4. If x == y mod n -> (Checking if {x_mod_n} == {y})")
    if x_mod_n == y:
        print(f"   then return '{n} is Prime'")
        return "Prime"
    else:
        print(f"   else return '{n} is composite'")
        return "Composite"


def main():
    while True:
        try:
            user_input = input("Enter an Input Number (Modulus) to test, or 'q' to quit: ").strip()
            
            if user_input.lower() == 'q':
                print("Exiting Program. Goodbye!")
                break
                
            number = int(user_input)
            
            print("\nSelect the Primality Test to use:")
            print("1. Fermat Primality Testing")
            print("2. Miller Rabin Test")
            print("3. Solovay Strassen Test")
            
            choice = input("Enter your choice (1/2/3): ").strip()
            
            if choice == '1':
                result = fermat_test(number)
                print(f"\nFINAL RESULT: {number} is {result} (using Fermat Primality Testing)\n")
            elif choice == '2':
                result = miller_rabin_test(number)
                print(f"\nFINAL RESULT: {number} is {result} (using Miller Rabin Test)\n")
            elif choice == '3':
                result = solovay_strassen_test(number)
                print(f"\nFINAL RESULT: {number} is {result} (using Solovay Strassen Test)\n")
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()