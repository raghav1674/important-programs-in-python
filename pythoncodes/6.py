input1="qwert@821142"
input1=list(input1)
disnum=list(map(int,set(filter(lambda x:x.isdigit(),input1))))
for i in disnum:
    m=0
    if i%2==0:
        m=1
        break
    else:
        m=0
if m==1:
    evens=[]
    for i in disnum:
        if int(i)%2==0:
            evens.append(i)
    mini=min(evens)
    disnum.remove(mini)
    disnum.sort(reverse=True)
    disnum.insert(len(disnum),mini)
    print(''.join(list(map(str,disnum))))
else:
    print("-1")

