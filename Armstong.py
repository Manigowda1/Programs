n=int(input("Enter a number to check "))
t1=n
sum=0
while n!=0:
    t=n%10
    sum=sum+t**3
    n=n//10

if sum==t1:
    print("It is Amrstrong number")
else:
    print("Not an armstrong number")



