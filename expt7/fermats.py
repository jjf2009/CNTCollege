import math

n = int(input("Enter n: "))
a = int(input("Enter a: "))

if math.gcd(a, n) != 1:
    print("Composite")

elif pow(a, n - 1, n) == 1:
    print("Probably Prime")

else:
    print("Composite")