def get_prime_factors(n):
    factors={}
    d=2
    while d*d<=n:
        while n%d==0:
            factors[d]=factors.get(d,0)+1
            n//=d
        d+=1
    if n>1:
        factors[n]=factors.get(n,0)+1
    return factors

def pohlig_hellman(g,h,p):
    n=p-1
    factors=get_prime_factors(n)

    congruences=[]

    print("\nCongruences obtained:")
    for q,e in factors.items():
        qe=q**e

        g1=pow(g,n//qe,p)
        h1=pow(h,n//qe,p)

        xq=next(x for x in range(qe) if pow(g1,x,p)==h1)

        print(f"x ≡ {xq} (mod {qe})")

        congruences.append((xq,qe))

    x,M=0,n

    print("\nCRT Computation:")
    for rem,mod in congruences:
        Mi=M//mod
        inv=pow(Mi,-1,mod)

        print(f"M{i if False else ''}")
        print(f"Mi = {Mi}")
        print(f"Inverse of {Mi} mod {mod} = {inv}")

        x+=rem*Mi*inv

    return x%M

g=int(input("Enter g: "))
h=int(input("Enter h: "))
p=int(input("Enter p: "))

x=pohlig_hellman(g,h,p)

print("\nFinal Answer")
print(f"x = {x}")