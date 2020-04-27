string=input()
half=len(string)//2
output=""
for i in range(0,half):
    prefix=string[0:half-i]
    print("prefix= ",prefix,end="  suffix=")
    suffix=string[len(string)-half+i:]
    print(suffix)
    if prefix==suffix:
        if len(output)<len(prefix):
            output=prefix
            print(output)
            break
print(len(output))
