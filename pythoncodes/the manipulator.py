string=list("E#R##C")
for i in range(0,len(string)):
    if string[i] =="#":
        for j in range(i-1,-1,-1):
            if string[j].isalpha():
                string[j]=chr(ord(string[j])+1)
                break


print("".join(string))