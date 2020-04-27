stri=input()
dicti={}
string=[]
for i in range(0,len(stri)):
    if stri[i].isalpha():
        string.append(stri[i])
    else:
        dicti.update(({i:stri[i]}))

string.reverse()
for i,j in dicti.items():
    string.insert(int(i),stri[i])

print(''.join(string))
