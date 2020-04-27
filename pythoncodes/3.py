stack=[]
br=input()
open=["[","{","("]
count=0
for i in br:
    if i in open:
        stack.append(i)
        count+=1

    continue
    if len(stack)==0:
        print(f"mismatch occured at {count+1}")
        break
    last=stack.pop()
    if (i == "}" and last == "{"):
        count+=1
    elif (i == "]" and last == "["):
        count+=1
    elif (i == ")" and last == "("):
        count+=1
    else:
        print(f"mismatch occured at {count + 1}")
        break
if len(stack)!=0:
    print(f"mismatch occured at {count+1}")
else:
    print("no mismatch")

