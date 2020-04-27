input="3,2,6,5,1,4,8,9".split(",")
num1=0
num2=""
index5=input.index("5")
index8=input.index("8")
for i in range(0,len(input)):
    if i<index5 or i>index8:
        num1+=int(input[i])
for i in range(index5,index8+1):
    num2+=input[i]
print(num1+int(num2))
