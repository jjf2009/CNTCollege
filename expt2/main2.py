from prettytable import PrettyTable


a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

myTable = PrettyTable(['q', 'r1', 'r2', 'r','s1','s2','s','t1','t2','t'])


def gcd(a, b):
    r1 = a
    r2 = b
    s1=1
    s2=0
    t1=0
    t2=1
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2
        myTable.add_row([q, r1, r2, r,s1,s2,s,t1,t2,t])
        r1, r2 = r2, r
        s1,s2=s2,s
        t1,t2=t2,t
    gcd=r1
    s=s1
    t=t1
    return gcd,s,t

result,x,y = gcd(a, b)
print(myTable)

print(f"{a} {x}+{b} {y} = {result}")
