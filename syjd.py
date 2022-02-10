def nextpos(arr, k):
    m = arr[k]+1
    sub = arr[k+1:k+m]
    if sub==[]:
        return -1
    elif k+max(sub)+2 == len(arr):
        final.append(max(sub))
        return len(arr)
    else:
        final.append(max(sub))
        return k+sub.index(max(sub))+1
n = input().split(',')
out = []
final = []
j = 0
for i in range(0,len(n)):
    n[i] = int(n[i])
final.append(n[0])
while j != len(n):
    j = nextpos(n,j)
    if j==-1:
        break
if j<len(n):
    print('-1')
else:
    out.append(sum(final)+n[-1])
    out.append(len(final))
    print(out)