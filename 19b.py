def findlen(s):
    counter = 0
    for i in s:
        counter += 1
    return counter

s = str(input())
print(findlen(s))
