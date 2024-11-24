a=['apple','Bat','Ball','Ant','Elephant']
r={}
for i in a:
    if i:
        temp=i[0].lower()
        if temp not in r:
            r[temp]=[]
        r[temp].append(i)
print(r)
