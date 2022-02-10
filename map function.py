numbers=[1,2,3,4]

def square(a):
    return a**2

[square(1),square(2)]


squares=list(map(square,numbers))
print(squares)



squares=list(map(lambda a:a**2,numbers))
print(squares)


squares=[i**2 for i in numbers]
print(squares)

new_list=[]
for num in numbers:
    new_list.append(square(num))
print(new_list)


#note:- list and map shorts the code use list for len function pre defined list

names=['abc','abcd','abcde']
length=map(len,names)
for i in length:
    print(i,end=" ")
#for j in length:  #map object can use only one  time loop
    #print(j)
# if we convert it to the list then we can run the loop any number of time 



names=['abc','abcd','abcde']
length=list(map(len,names))
for i in length:
    print(i,end=" ")



for j in length:
    print(j)