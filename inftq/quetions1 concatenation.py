p=str(input()).replace(',',"")
num1=""
num2=0
res=0
flag=0
for i in range(0,len(p)):
    if p[i]=='5':
        flag=1
    if flag==0:
        num2=num2+int(p[i])
    else:
        num1=num1+p[i]

    if p[i]=='8':
        flag=0

res=int(num1)+num2
print(res)
