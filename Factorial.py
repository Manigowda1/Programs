def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        f=1
        while(n>1):
            f=f*n
            n=n-1
        return f

       

num=int(input("Enter number"))
print(fact(num))




