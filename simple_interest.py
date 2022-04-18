def SI(P,T,R):
    si_amount=(P*T*R)/100
    return si_amount

p=int(input("Enter Priciple "))
t=int(input("\nEnter time in year "))
r=int(input("\nEnter rate of interest"))
print(SI(p,t,r))