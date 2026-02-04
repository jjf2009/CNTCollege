num1 = int(input("Enter x: "))
num2 = int(input("Enter y: "))
choice= int(input("1.Addition\n2.Subtraction\n3.Subtraction\n4.Division\n5.Modules \n6.Exponentiation\n7.Floor division\n8.Exit\nEnter Choice:"))

if(choice==1):
        print("\nAddition of Numbers:",(num1+num2))
elif(choice==2):
        print("\nSubtraction of Numbers:",(num1-num2))
elif(choice==3):
        print("\nMultiplication of Numbers:",(num1*num2))
elif(choice==4):
        print("\nDivision of Numbers: ",num1,"=",(num1//num2),"*",num2,"+",(num1%num2))
elif(choice==5):
        print("\nModules of Numbers:",(num1%num2))
elif(choice==6):
        print("\nExponentiation of Numbers:",(num1**num2))
elif(choice==7):
        print("\nFloor division of Numbers:",(num1//num2))


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter b:"))
choice= int(input("1.Thorem 1 \n2.Thorem 2\nEnter Choice:"))
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

