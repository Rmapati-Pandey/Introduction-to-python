#looping in tuples
#tuples in one Element
#tuple without paranthesis
#tuple unpacking
#list inside the tuples
#some functions that you can use with tuples
mixed=(1,2,3,4,5)
for i in mixed:
    print(i,end=" ")
print()
#tuples in one Element use comma(,) else it will be of integer type
#nums1=(1) its shows type integer
nums1=(1,)
words1=('word',) 
print(type(nums1))
print(type(words1))


guitars='yamaha','baton rough','taylor' #its also an tuple
print(type(guitars))
 
#tuple unpacking
#tuples values assigned the the values gui1,gui2,gui3 called upacking

guitarists=('amit','ankit','vivek')
guitar1,guitar2,guitar3=(guitarists)
#guitar1,guitar2=(guitarists) #this shows error too many values to unpack
print(guitar1)
print(guitar2)
print(guitar3)

#list inside tuple

favourite=('sm',['tk','lc'])
favourite[1].pop() #delete the lc
print(favourite)
favourite[1].append('kl')#adds the kl in the list
print(favourite)

#min function
#max function
#sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))



















