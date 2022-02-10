num=input()
length=len(num)
result=""
for i in range(1,length,2):
    result+=str(int(num[i])**2)

print(result[0:4])
    