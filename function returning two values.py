def fun(int1,int2):
    add=int1+int2
    multiply=int1*int2
    return add,multiply
#function returning two values always stored in the tuples 
a=10
b=30
print(fun(10,20))

#so avoid to store the returning values in the tuple always use two variable assignment art function call
def fun(int1,int2):
    add=int1+int2
    multiply=int1*int2
    return add,multiply

a=10
b=30
add,multiply=fun(10,20)
print(add,multiply)





#printing all the tuple values ranging from 1 to 11
nums=tuple(range(1,11))
print(nums)
print(type(nums))
print()
print()

#converting tuple to the list data  type
nums=list(tuple(range(1,11)))
print(nums)
print(type(nums))
print()
print()

#converting tuple to string
nums=str(tuple(range(1,11)))
print(nums)
print(type(nums))








