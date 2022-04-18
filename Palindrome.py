n=int(input("Enter a number"))
t=n
r=0
while n!=0:
    r=(r*10)+n%10
    n=n//10
if r==t:
    print("It is Palindrome")
else:
    print("Not a palindrome")