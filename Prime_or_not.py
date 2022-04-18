n=int(input("Enter a number to check "))

for i in range(2,n):
    if n%i==0:
        print("It is not prime")
        break
else:
    print("It is prime")