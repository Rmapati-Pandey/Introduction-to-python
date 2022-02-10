def odd_even(lst1,lst2):
    common=[]
    for i in lst1:
        if i in lst2:
                common.append(i)
    return common  
   
lst1=[1,2,5,8]
lst2=[1,2,7,6]
print(odd_even(lst1,lst2))