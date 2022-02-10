def is_even(a):
    return a%2==0

numbers=[3,4,2,1,5,6,9,8,10]
# even=[]  ????????????????
print()
print()

even=tuple(filter(is_even,numbers))
print(even,end="\n")


even=tuple(filter(lambda a: a%2==0,numbers))
for i in even:
    print(i, end=" ")



#print(tuple(filter(lambda a: a%2==0,numbers)))