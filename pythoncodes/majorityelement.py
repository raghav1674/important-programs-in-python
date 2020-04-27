
list1=[2,3,3,3,2,2]
list2=list(set(list1))
length=len(list1)
hlf=length/2


result=[]
for i in list2:
    count=0
    number=i
    for j in list1:
        if number==j:
            count+=1
    if count>=hlf:

        result.append(str(i))
print(result)
if len(result)==0:
    print("-1")
else:
    print(" ".join(result))
