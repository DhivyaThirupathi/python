t=[(6,24,12),(60,12,6,-300),(12,-18,21)]
k=6
result=[]
# problem a
for i in t:
    count=0
    for j in i:
        if j%k==0:
            count=count+1
    if(count==len(i)):
        result.append(i)
print("All the tuples have elements divisible by k=6 : ",result)
#problem b
result1=[]
for i in t:
    count = 0
    for j in i:
        if j>0:
            count = count+1
    if count == len(i):
        result1.append(i)
print("all the tuples that have all positive elements",result1)

#problem c
for i in range(len(t)):
    for j in range(0,len(t)-i-1):
        if t[j][-1]>t[j+1][-1]:
            t[j],t[j+1]=t[j+1],t[j]
print("sort a list of tuples in increasing order by the last element in each tuple.",t)

#problem d

def count_digits(tup):
    count = 0
    for num in tup:
        count += len(str(abs(num)))
    return count
for i in range(len(t)):
    for j in range(len(t) - 1):
        if count_digits(t[j]) > count_digits(t[j + 1]):
            t[j], t[j + 1] = t[j + 1], t[j]

print("Sort the tuples on basis of total digits in tuple.",t)
