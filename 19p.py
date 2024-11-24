def check(s1,s2): 
    s1 = s1.lower()
    s2 = s2.lower()
    if(sorted(s1)==sorted(s2)):
        print("it is a anagram")
    else:
        print("not a anagarm")
s1=str(input())
s2=str(input())
check(s1,s2)
