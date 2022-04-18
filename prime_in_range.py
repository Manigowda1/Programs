S=int(input("Enter range start value"))
E=int(input("\nEnter range End value"))

for i in range(S,E+1):
        for j in range(2, i):
            if (i % j == 0):
                break
            else:
                print(i)
                break




