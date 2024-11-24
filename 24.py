import numpy as np
arr = np.array([1, 2, 3, 4, 5,6,2])
max1=0
for i in arr:
 if(i>max1):
   max1=i
print("Maximum element from the array:",max1)
sum=0
for i in arr:
 sum=sum+i
avg=sum/len(arr)
print("Average of array is:",avg)
arr_unique=np.unique(arr)
print(arr_unique)
np.sort(arr_unique)
print("The second smallest element in array:",arr[1])
position=int(input("Enter the position:"))
y=np.concatenate((arr_unique[-position:],arr_unique[:-position]))
print(y)