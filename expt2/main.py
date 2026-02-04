from prettytable import PrettyTable


a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))

myTable = PrettyTable(['q', 'r1', 'r2', 'r'])


def gcd(a, b):
    r1 = a
    r2 = b
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        myTable.add_row([q, r1, r2, r])
        r1, r2 = r2, r
    return r1

result = gcd(a, b)
print(myTable)

print(f"GCD({a}, {b}) = {result}")
