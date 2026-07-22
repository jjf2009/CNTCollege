print("Program")

q = int(input("Enter the prime number  q:"))
al = int(input("Enter the number alpha :"))

a = int(input("Enter the pritive key for user A :"))
b = int(input("Enter the pritive key for User B :"))

A = pow(al,a,q)
B = pow(al,b,q)

print("Public Key of User A",A)
print("Public Key of User B",B)

shar_A= pow(A,b,q)
shar_B= pow(B,a,q)

print("Shared Key of User A:",shar_A)
print("Shared Key of User B:",shar_B)

