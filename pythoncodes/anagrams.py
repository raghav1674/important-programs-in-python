def count_occureneces_alpha(string1):
    need={}

    for i in range(65,122):
        need[chr(i)]=0

    for i in range(0,len(string1)):
        string=string1[i]
        count=0
        for j in range(0,len(string1)):
            if string==string1[j]:
                count+=1
        need[string]+=1
    return need

s1=input()
s2=input()
s1count=count_occureneces_alpha(s1)
s2count=count_occureneces_alpha(s2)
delteions=0
for i in range(65,122):
    delteions+=abs(s1count[chr(i)]-s2count[chr(i)])
print(delteions)
