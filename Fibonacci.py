n=int(input("Enter a number"))
f,s=0,1
for i in range(0,n):
    if i<=1:
        print(i)
    else:
        r = f + s
        f = s
        s = r
        print(r)

