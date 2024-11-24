def factors(a):
 for i in range(1,a+1):
    if(a%i==0):
        print(i)
num=int(input("enter a integer: "))
factors(num)
