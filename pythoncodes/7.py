input="abcdabcde"
dislen=len(set(input))

output=""
for i in range(0,len(input)):
    str1=input[i]
    str2=str1
    for j in range(i+1,len(input)):
        str2+=input[j]
        if len(str2)>=3 and len(set(str2))==dislen and len(str2)==dislen:
            if len(output)<len(str2):
                output=str2
            break
        else:
            continue


if len(output)<3:
    print("-1")
else:
    print(output)
