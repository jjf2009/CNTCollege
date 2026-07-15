a = int(input("Enter First Number:"))
b = int(input("Enter Second Number: "))

print("q r r1 r2")

# def gcd(a,b):
#     r1=a
#     r2=b
#     while r2 > 0:
#         q = r1 // r2
#         r = r1-q*r2
#         print(f"{q} {r} {r1} {r2}")
#         r1,r2=r2,r
#     return r1

# result = gcd(a,b)
# print(f"GCD({a},{b})= {result}")

def gcd(a,b):
    r1=a
    r2=b
    s1=1
    s2=0
    t1=0
    t2=1
    while r2 > 0:
        q = r1 // r2
        r = r1 -q * r2
        t = t1 - q * t2
        s = s1 - q * s2
        print(f"{q} {r} {r1} {r2} {s} {s1} {s2} {t} {t1} {t2}")
        r1,r2=r2,r
        t1,t2 = t2,t
        s1,s2 = s2,s
    gcd = r1
    s=s1
    t=t1
    return gcd ,s ,t

gcd , x,y = gcd(a,b)
print(f"{a} {x}+{b} {y}={gcd}")


