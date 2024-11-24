p=int(input("Enter the principal amount:"))
n=int(input("Enter the number of years:"))
r=int(input("Enter the rate of interest:"))
simple_interest=(p*n*r)/100
print("Simple interest",simple_interest)
compound_interest=p*((1+(r/100))**n-1)
print("Compound interest",compound_interest)
