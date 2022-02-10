
# to zip two list into one list 

l1=[1,2,3,4,5]
l2=[7,8,9,0,7]
my_l=list(zip(l1,l2))
print(my_l)




print()
print()
#to unpack the list (use * operator)



l3,l4=list(zip(*my_l)) #thos result in two tuple l3 and l4
print(list(l3)) #typecaste to list
print()
print(list(l4))








print()
print()
#maximum of two number from l1 and l2
new_list=[]
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)