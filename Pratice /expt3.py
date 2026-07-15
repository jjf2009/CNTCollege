a = int(input("Enter value of a :"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

print("Equation:")
if(b>0) :
   print(f"{a}x + {b}y = {c}")
else:
   print(f"{a}x+{b}y = {c}")

def gcd(a,b):
   r1=a
   if(b>0):
      r2=b
   else:
      r2=-b
   while(r2>0):
      q = r1 // r2
      r = r1-q*r2
      r1,r2=r2,r
   return r1

result = gcd(a,b)
d  = result
if d ==0:
   if c==0:
      print("Infinite Solutions")
   else:
      print("No Solution")
elif c%d!=0:
   print("No Solution") 
   exit()

temp_a = int(a//d)
temp_b = int(b//d)
temp_c = int(c//d)

print("Tempory Equation")
if(b>0) :
   print(f"{temp_a}x + {temp_b}y = {temp_c}")
else:
   print(f"{temp_a}x+{temp_b}y = {temp_c}")

def extended_gcd(a,b):
    r1=a
    s1=1
    s2=0
    t1=0
    t2=1
    if(b>0):
      r2=b
    else:
      r2=-b
    while(r2>0):
      q = r1 // r2
      r = r1-q*r2
      s= s1-q*s2
      t=t1-q*t2
      r1,r2=r2,r
      t1,t2=t2.t
      s1,s2=s2,s
    return r1,s1,t1


s, t = extended_gcd(temp_a, temp_b)
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


b_over_d = int(b//d)
a_over_d =int(a//d)

for i in range(1,3):
   k = int(input(f"Enter Value of k (attempt {i}):"));
   x_k = x_0 + b_over_d*d
   y_k = y_k+a_over_d*d
   print(f"for {k}: x={x_k} and y={y_k}")



