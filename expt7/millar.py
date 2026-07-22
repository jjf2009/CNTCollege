import math

n = int(input("Enter n: "))
a = int(input("Enter a: "))

# Write n - 1 = 2^k × m
m = n - 1
k = 0

while m % 2 == 0:
    m //= 2
    k += 1

print("k =", k)
print("m =", m)

b = pow(a, m, n)

if b == 1 or b == n - 1:
    print("Probably Prime")

else:

    for i in range(k - 1):

        b = pow(b, 2, n)

        if b == n - 1:
            break

    if b == n - 1:
        print("Probably Prime")
    else:
        print("Composite")