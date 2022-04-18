def CI(P,T,R):
    ci_amount=p*(pow(1+(R/100),T))
    return ci_amount

p=int(input("Enter Priciple "))
t=int(input("\nEnter time in year "))
r=int(input("\nEnter rate of interest"))
print(CI(p,t,r))