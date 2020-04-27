lis="12345678".split()
list1=[]
for i in range(0,len(lis)):
    i=int(i)
    if int(i)%2!=0:
        list1.append(int(lis[i]))
list1=list(map(str,list(map(lambda x:x*x,list1))))


print("".join(list1[0:4]))













