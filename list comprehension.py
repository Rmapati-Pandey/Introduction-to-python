#list comprehension
#with the help of list comprehension we can create of list in one line
#create a list of squares from 1 to 10
#normal method
squares=[]
for i in range(1,11):
     squares.append(i**2)

print(squares)

# we can write it in one line
#list comprehension
square2=[]
squares2=[i**2 for i in range(1,11)]
#list comprehension
print(squares2)
negetive=[i**2*(-1) for i in range(1,11)]
print(negetive)

# negetive=[-i for i in range(1,11)]
# print(negetive)
#list comprehension
negetive=[i*(-1) for i in range(1,11)]
print(negetive)

names=['Harshit','Hohit','Rohit']

# new_list=['H','M','R']
#normal
newlist=[]
for name in names:
    newlist.append(name[0])

#list comprehension
new_list=[name[0] for name in names]
print(new_list)


#reverse word in list
list1=['abc','tuv','xyz']
newlist5=[string[::-1] for string in list1 ]
print(newlist5)


#list comprehensioin with if statement
numbers=list(range(1,11))
print(numbers)
even_num=[num for num in numbers if num%2==0]
print(even_num)
odd_nums=[num for num in numbers if num%2!=0]
print(odd_nums)


l=[1,3.4,4,6,7.9]
output1=[str(i) for i in l if(type(i)==int or type(i)==float)]
print(output1)


numlist1=[1,2,3,4,5,6]
new_num_list1=[i*2 if i%2==0 else -i for i in numlist1  ]
print(new_num_list1)

#nested list
# [[1,2,3][4,5,6][7,8,9]]
matrix=[[i for i in range(1,4)] for j in range(3)]






