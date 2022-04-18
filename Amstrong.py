n=int(input("Enter number"))
temp1=n
order=0
while(temp1>0):
    order+=1
    temp1=temp1//10

temp2=n
s=0
while(temp2>0):
    r=temp2%10
    s+=pow(r,order)
    temp2=temp2//10

if(s==n):
    print("It is")
else:
    print("It is not")




