print("Welcome to CNT Lab")

while(1):
    choice= int(input("1.Addition\n2.Subtraction\n3.Subtraction\n4.Division\n5.Modules \n6.Exponentiation\n7.Floor division\n8.Exit\nEnter Choice:"))
    if(choice==8):
        break
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter second Number: "))
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
    else:
        break

