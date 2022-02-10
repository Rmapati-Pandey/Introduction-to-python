def reverse_list(l):
    r_list=[]
    for i in range(1,len(l)+1):
        popped_item=l.pop()
        r_list.append(popped_item)
    return r_list

arr=list(range(1,11))
print(reverse_list(arr))