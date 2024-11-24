a=int(input("Enter a number:"))
count=0
while(a>0):
    r=a%10
    count+=1
    a=a//10
print("Count:",count)
