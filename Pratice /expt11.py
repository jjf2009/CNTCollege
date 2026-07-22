from math import gcd


def text_to_number(text):
    number = " "

    for char in text.lower():
        if char.isalpha():
            number +=str(ord(char)-ord('a'))
    return int(number)

def rsa():
    p = int(input("Enter prime number p:"))
    q = int(input("Enter prime number q"))

    n = q*p
    phi = (q-1)*(p-1)

    e = int(input("Enter value of e:"))
    while gcd(e.phi)!=1:
        print("e should be coprime with phi")
        e = int(input("Enter value of e: "))
    
    d = pow(e,-1,phi)

    m = input("Enter message to be rsa used on")
    new_m = text_to_number(m)

    while m>=n:
        m=m%n

    encryod  = pow(m,e,n)



rsa()