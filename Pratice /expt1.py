num1 = int(input("Enter Frist Number:"))
num2 = int(input("Enter Second Number:"))

print("Addition of x+y:",(num1+num2))


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

choice= int(input("1.Theorem 1 : a|b and b|c then a|c \n2.Theorem 2 : a|b and b|c then a|(mb + nc)\nEnter Choice:"))
if choice==1:
    if b==0 or c==0:
        print("Error")
    elif b%a==0 and b%c==0 and a%c==0:
        print("Proved")