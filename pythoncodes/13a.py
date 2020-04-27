lis1="abcdef#123ret@56"

spcl=0
evens=[]
odd=[]
for i in lis1:
    if str(i).isalnum() == False:
        spcl+=1
    elif(i.isdigit()):
        if int(i)%2==0:
            evens.append(i)
        else:
            odd.append(i)
if spcl%2==0:
    evens,odd=odd,evens
for i in range(max(len(evens),len(odd))):
    if i!=len(odd):
        print(odd[i],end="")
    if i!=len(evens):
        print(evens[i],end="")



