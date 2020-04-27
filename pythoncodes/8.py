lis1="abcd:1234,bcdgfhf:127836".split(',')
for i in lis1:
    word,number=i.split(":")[0],i.split(":")[1]
    l=len(word)
    number=list(map(int,number))
    sumofdigits=sum(list(map(lambda x:x*x,number)))
    if sumofdigits%2==0:
        s=word[l-2:]
        print(s+word[0:l-2])
    else:
        print(word[1:]+word[0])

