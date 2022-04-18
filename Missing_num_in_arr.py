def missingelement(a,n):
    expected_sum=n*(n+1)/2
    actual_sum=sum(a)
    return expected_sum-actual_sum

a=[]
n=int(input("enter size of an array "))
for i in range(0,n-1):
    e=int(input("Enter element"))
    a.append(e)

print(f"Missing element is {missingelement(a,n)}")
