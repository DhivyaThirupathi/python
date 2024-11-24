word1=str(input("enter a string 1:"))
word2=str(input("enter a string 2:"))
count1=0
count2=0
for i in word1:
    count1+=1
for j in word2:
    count2+=1
if(count1<count2):
    print("lager string is:")
    print(word2)
elif(count1==count2):
    print("both are equal")
else:
    print("larger string is:")
    print(word2)

            

