list=[1,2,3,4,5,6,7,8,9,10]
flen=int(input("enter a value"))
slen=int(input("enter a value"))
first=list[:flen]
second=list[flen:flen+slen]
third=list[flen+slen:]
print(first)
print(second)  
print(third)