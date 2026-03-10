from prettytable import PrettyTable
a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))
c = int(input("Enter Constant:"))
print("Equation:")
if(b>0):
    print(f"{a} x + {b} y= {c} ")
else:
    print(f"{a} x {b} y= {c}")
myTable = PrettyTable(['q', 'r1', 'r2', 'r'])
def gcd(a, b):
    r1 = a
    if(b>0):
        r2=b
    else:
        r2 = -b
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        myTable.add_row([q, r1, r2, r])
        r1, r2 = r2, r
    return r1
result = gcd(a, b)
print(myTable)
print(f"GCD({a}, {b}) = {result}")
d = result
if d == 0:
    if c == 0:
        print("Infinite solutions (0x + 0y = 0).")
    else:
        print("The Equation does not have any Solution")
    exit()
if c % d != 0:
    print("The equation does not have any solution.")
    exit()
temp_a = int(a // d)
temp_b = int(b // d)
temp_c = int(c // d)
print("Temporary Equation:")
if temp_b > 0:
    print(f"{temp_a} s+{temp_b} t = 1")
else:
    print(f"{temp_a} s{temp_b} t = 1")
myTable2 = PrettyTable(['q', 'r1', 'r2', 'r', 's1', 's2', 's', 't1', 't2', 't'])
myTable2.align = 'c'
def extended_gcd(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2
        myTable2.add_row([q, r1, r2, r, s1, s2, s, t1, t2, t])
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    if r1 < 0:
        s1 = -s1
        t1 = -t1
    return s1, t1
s, t = extended_gcd(temp_a, temp_b)
print(myTable2)
print(f"s = {s}   t = {t}")
x_0 = int(temp_c * s)
y_0 = int(temp_c * t)
print("Particular Solution:")
print(f"x_0={x_0}   y_0={y_0}")
print("General Solution:")
if(b<0):
    print(f"x={x_0}{(int)(b/d)}k   y={y_0}-{(int)(a/d)}k  ")
else:
    print(f"x={x_0}+{(int)(b/d)}k   y={y_0}-{(int)(a/d)}k  ")

# Ask user to enter k values twice
b_over_d = int(b / d)
a_over_d = int(a / d)

for i in range(1, 3):
    k = int(input(f"\nEnter value of k (attempt {i}): "))
    x_k = x_0 + b_over_d * k
    y_k = y_0 - a_over_d * k
    print(f"For k={k}:  x = {x_k},  y = {y_k}")
    print(f"Verification: {a}*({x_k}) + {b}*({y_k}) = {a*x_k + b*y_k}  (should equal {c})")