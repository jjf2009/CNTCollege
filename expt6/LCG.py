m = int(input("Enter modulus m: "))
a = int(input("Enter multiplier a: "))
c = int(input("Enter increment c: "))
x = int(input("Enter seed X0: "))

iterations = int(input("Enter number of values: "))

for i in range(iterations):

    x = (a * x + c) % m

    print(x)