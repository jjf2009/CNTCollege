from math import gcd, prod
def crt(a,m):
    M = prod(m)
    x=0
    for i in range(len(m)):
        m1 = M//m[i]
        y1 = pow(m1,-1,m[i])
        x += a[i]*m1*y1
    
    print(f"X = {x%M} mod {M}")


n = int(input("Enter the number of Equations"))
a =[]
m =[]

for i in range(i,n+1):
    a.append(int(input(f"{a}{i} = ")))
    m.append(int(input(f"{m}{i} = ")))

for i in range(1,len(m)):
    for j in range(i+1,len(m)):
        if(gcd(m[i],m[j])!=1):
            print("Modulei are not coprime")
            exit()
crt(a,m)