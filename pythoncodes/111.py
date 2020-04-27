input1 = "1 1 1 1"
lis = list(map(int, input1.split(" ")))
ip = int(input())
dicti = {}
l = []
toberemoved = []

for i in range(0, len(lis)):
    count = 1
    num = lis[i]
    print(num)
    for j in range(i+1, len(lis)):
        if num == lis[j]:
            count += 1
    print(count)
    dicti.update({num: count})
print(dicti)
for i in dicti.values():
    l.append(i)
l.sort()
print(l)
length = len(l)

if l[0] > ip:
    length = "no distinct element"
else:
    for i in l:

        if i <= ip:
            ip -= i
            length -= 1
        else:
            break
print(length)


