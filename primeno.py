num = int(input("Enter a number:"))

if num<=1:
    print("Enter a number which is greater than 1")

else:
    prime=0
    for i in range(2,num+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count=count+1
        if count == 2:
            prime+=1
    print("The count of prime numbers are:",prime)
