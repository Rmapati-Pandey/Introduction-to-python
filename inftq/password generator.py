input_str=input()
list_input=[]
finalString=''
 
list_input=input_str.split(',')
 
for i in list_input:
    temp=i.split(':')
    name=temp[0]
    number=temp[1]
    length=len(name)
    mx=0
    for digit in number:
        if(int(digit)<=length):
            if(mx<int(digit)):
                mx=int(digit)
    if mx==0:
        finalString+='X'
    else:
        finalString+=name[mx-1]
 
print(finalString)