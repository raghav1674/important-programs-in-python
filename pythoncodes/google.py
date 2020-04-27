n=2
output=[]

for i in range(1,n+1):
    i=str(i)
    if len(i)==1:
        output.append(i)
    else:

        for j in range(0,len(i)-1):
            m=0
            ano=int(i[j])

            bno = int(i[j+1])
            if abs(ano-bno)==1:

                m=1
            else:
                break
        if m==1:
            output.append(i)

print(output)


