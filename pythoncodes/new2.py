# t=int(input())
missing=[]
# while(t!=0):
n=int(input())
list1=list(map(int,input().split(" ")))
lis2=range(1,n+1)
for i in lis2:

    number=i
    if number in list1:
        continue


    else:
        missing.append(str(i))


print(" ".join(missing))
print()
    # t-=1
