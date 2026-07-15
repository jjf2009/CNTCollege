def extended_gcd(a, b): 
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        r  = r1 - q * r2
        s  = s1 - q * s2
        t  = t1 - q * t2
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    return r1, s1, t1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(m):
    count = 0
    for k in range(1,m+1):
        if gcd(k,m)==1:
            count+=1
    return count

def modular_exponentiation(base, exp, mod):
    base = base % mod 
    results = 1
    if exp % 2 ==1 :
        results = (results*base)%mod
        base = (base*base)%mod
        exp //= 2
    return results


a = int(input("Enter a:"))
b = int(input("Enter b:"))
m = int(input("Enter c:"))

d = gcd(a,m)

if b % d !=0:
    print("Enter No Solution")
else:
    print("\nMethod 1: Extended Euclid")
    d,x,y = extended_gcd(a,m)
    x = (x*(b//d))%m
    print("x = {x}")
   
    print("\nMethod 2: Euler Totient")
    a1 ,b1,m1 = a//d , b//d,m//d
    p = euler_totient(m1)
    inv = pow(a,pow-1,m1)
    x = (inv *b1)% m1
    print("x = {x}")

    print("\nMethod 3: Multiplicative Inverse")
    d, inv, _ = extended_gcd(a1, m1)
    inv %= m1
    x = (inv * b1) % m1
    print("x =", x)

   
