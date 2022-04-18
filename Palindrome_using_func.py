n=int(input("enter a number "))

def rev(num):
    r = 0
    while num>0:
        r = (r * 10) + num % 10
        num = num // 10
    return r

if n==rev(n):
    print("Palindrome")
else:
    print("not a palindrome")



