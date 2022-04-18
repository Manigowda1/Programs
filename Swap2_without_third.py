# n1,n2=input("Enter two numbers").split()
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print("first number before swap ",n1)
print("second number before swap ",n2)
print()
n1=n1-n2
n2=n1+n2
n1=n2-n1
print("first number after swap",n1)
print("second number after swap",n2)