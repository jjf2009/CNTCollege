p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q

seed = int(input("Enter seed: "))
bits = int(input("Enter number of bits: "))

x = seed
result = ""

for i in range(bits):

    x = pow(x, 2, n)

    result += str(x % 2)

print("Generated bits:", result)