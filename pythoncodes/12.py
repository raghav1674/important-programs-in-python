list1=list("HeLloOWorlDd")

list2=list(set("HeLloOWorlDd".lower()))
print(list2)
charlist=[]
for i in range(0,len(list2)):
    elementgrp = list2[i]
    ele=""
    for j in range(0,len(list1)):
        if elementgrp.lower()==list1[j].lower():
                ele+=list1[j]


    charlist.append(ele)

for i in range(0,len(charlist)):
    for j in range(i+1,len(charlist)):
        if charlist[i].lower()>charlist[j].lower():
            charlist[i],charlist[j]=charlist[j],charlist[i]
print(charlist)
for i in range(0,len(charlist)//2):
    print(charlist[i]+charlist[len(charlist)-i-1],end="")
if(len(charlist)%2!=0):
    print(charlist[len(charlist)//2])
