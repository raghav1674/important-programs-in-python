list1=[2,2,1,3,1]
inp=2
lis=list(set(list1))
listcount=[]
liscount1=[i for i in lis if list1.count(i)==inp]
# print(liscount1)
# for i in lis:
#     number=i
#     count=0
#     for j in list1:
#         if number==j:
#             count+=1
#     if count==inp:
#         listcount.append(i)
print(min(liscount1))


