dict={}
input_string="Abhishek:34848,Mayur:4739,Friend:2949,Yeah:98893"
z=[]
finalstr=""
z=input_string.split(",")
for l in z:
    name,code=l.split(":")[0],l.split(":")[1]
    code=set(code)
    # name=k[0]
    # code=k[1]
    listupdated = []
    for i in code:
        i=int(i)
        if i<=len(name):
            listupdated.append(i)
    if(len(listupdated)==0):
        finalstr+="X"
    else:
        m = max(listupdated)
        finalstr += name[m - 1]
print(finalstr)





