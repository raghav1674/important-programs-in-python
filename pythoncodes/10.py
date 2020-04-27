list1="1 1 2 2 2 2 2".split()
lis=list(set(list1))
lis.sort()
inp=1
listcount=[]
for i in range(0,len(lis)):

    first=lis[i]
    count=0
    for j in range(0,len(list1)):
        if first==list1[j]:
            count+=1

    listcount.append(count)
print(listcount)
listcount.sort()
for i in listcount:
    if int(i)<=inp:
        inp-=int(i)
        listcount.remove(i)
print(len(listcount))



