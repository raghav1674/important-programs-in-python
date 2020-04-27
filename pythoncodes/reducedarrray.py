lis1=[10,20,20,50,40]
lis2=lis1.copy()
lis2.sort()
result=[]
for i in lis1:

    if lis2.index(i) in result:
        result.append(f"element present at {lis2.index(i)}")
    else:
        result.append(lis2.index(i))
print(result)
