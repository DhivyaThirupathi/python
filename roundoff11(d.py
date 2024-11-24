x=[2.0,3.4,4.4,5,6,5.5,7,7,8,9]
num=list(map(round,x))
print(min(num))
print(max(num))
n=len(num)
n1=n*(n+1)/2
print(n1)
unique=sorted(set(x))  
print(*unique,sep=" ")
