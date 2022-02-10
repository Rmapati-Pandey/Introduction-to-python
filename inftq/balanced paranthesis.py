string=input()
stack=[]
counter=0
for a in string:
    if(a=='[' or a=='{' or a=='('):
        stack.append(a)
        counter+=1
        continue
    if(len(stack)==0):
        print(counter+1)
        exit()
    
    b=stack.pop()

    if(a==']' and b=='['):
        counter+=1
    elif(a=='}' and b=='{'):
        counter+=1
    elif(a==')' and b=='('):
        counter+=1
    
if(len(stack)==0):
    print(0)
else:
    print(counter+1)