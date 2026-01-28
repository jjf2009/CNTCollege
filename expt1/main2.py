a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))
c = int(input("Enter Number3:"))

if b == 0 or c == 0:
    print("ERROR: division by zero")
elif b%a == 0 and c%b == 0 and c%a == 0:
    print("TRUE")
else:
    print("FALSE")


if b == 0 or c == 0:
    print("ERROR: division by zero")
elif b%a == 0 and c%b == 0 :
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    val = m * b + n * c
    print("TRUE" if val %  a  == 0 else "FALSE")
else:
    print("Cannot prove: require a|b and b|c")