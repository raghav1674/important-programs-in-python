list1=list(map(int,"1,9,3,5,8,7,13".split(",")))
totallist=[]
for i in range(0,len(list1)):
    first=list1[i]
    for j in range(i+1,len(list1)):
        second=list1[j]
        fablist=[]
        fablist.append(first)
        fablist.append(second)
        for k in range(j+1,len(list1)):
            third=list1[k]
            if first+second==third:
                fablist.append(third)
                first=second
                second=third

        print(fablist)
        if len(totallist)<len(fablist):
            totallist=fablist
print(totallist)
