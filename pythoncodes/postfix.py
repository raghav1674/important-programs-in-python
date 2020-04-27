postfix="23-"
stack=[]
def operation(operator,rnum,lnum):
    if operator=="*":
        return lnum*rnum
    elif operator=="/":
        return lnum/rnum
    elif operator=="+":
        return lnum+rnum
    elif operator =="-":
        return lnum-rnum



for i in postfix:

    if i.isdigit():
        stack.append(int(i))
        continue
    if i in ["*","/","+","-"]:

        rnum=stack.pop()
        if len(stack)==0:
            break
        lnum=stack.pop()
        result=operation(i,float(rnum),float(lnum))
        stack.append(result)
if len(stack)==1:
    finalresult=stack.pop()
    print("result=",round(float(finalresult),2))
else:
    print("invalid postfix expression")