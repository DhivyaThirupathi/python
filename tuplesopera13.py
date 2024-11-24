#a. Compare two tuples
tuple1=tuple(map(int,input("Enter tuple 1:").split(" ")))
tuple2=tuple(map(int,input("Enter tuple 2:").split(" ")))
print("Comparing Two Tuples")
if(tuple1==tuple2):
    print("True")
else:
    print("False")

# problem b
if len(tuple1) != len(tuple2):
    print("Tuples must have the same length")
    exit()
tuple1, tuple2 = tuple2, tuple1
print("After Swapping")
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# problem cTo concatenate two tuples
tuple3=tuple1+tuple2
print("The concat of tuple1 and tuple2 is ",tuple3)

# problem dTo find the length of a tuple
len=len(tuple3)
print("The length of tuple3 is",len)

# problem eTo find maximum and minimum element of a tuple

print("The minimum element in tuple",min(tuple3))
print("The maximum element in tuple",max(tuple3))

# problem f To reverse the elements of a tuple

print("Reverse of Tuple is ")
tuple4=tuple3[::-1]
print(tuple4)
