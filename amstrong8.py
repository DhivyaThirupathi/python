for i in range(100,400):
    temp=i
    s=0
    while(temp!=0):
        r=temp%10
        s=s+(r*r*r)
        temp=temp//10
    if(s==i):
        print(i)
