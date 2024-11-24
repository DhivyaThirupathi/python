list1=[5,3,7,8,9,2,3,4,5,3]
list1[0]=~list1[0]
print("Negation of the value",list1)
list1.append(10)
print("Adding value 10 in the list",list1)
list1.insert(2,22)
print("Insert the value 22 at position 2 in data",list1)
del list1[1]
print("Remove the value at position 1 in the data",list1)
list1.extend([8,9,10])
print("Add value at the end of the list",list1)
print("Locate the index value of 7:",list1.index(7))
list1.sort()
print("Sort the values in data",list1)
