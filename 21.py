import math
def binom(n,k):
    if n<k or n<0:
        print("invalid number")
        return 0
    binomial_coefficient=(math.factorial(n)/math.factorial(k)*math.factorial(n-k))
    print("binomial_coefficient:",binomial_coefficient)
n=int(input("enter a number:"))
k=int(input("enter a number:"))
binom(n,k)