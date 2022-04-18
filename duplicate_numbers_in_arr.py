arr,uniq,dup=[],[],[]
n=int(input("Enter size of the array "))

for i in range(n):

    ele=int(input(f"Enter array elements between 0 to {n-1} "))
    arr.append(ele)

for i in range(n):
    if arr[i] not in uniq:
        uniq.append(arr[i])
    else:
        dup.append(arr[i])


print(dup)


