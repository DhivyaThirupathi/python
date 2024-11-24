A=int(input("Enter any number: "))
temp = 0
s=0
while(a>0):
    r=a%10
    s=s*10+r
    a=a//10
if s==temp:
    print("It is palindrome")
else:
    print("Not a palindrome")
