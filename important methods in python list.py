
#count method
fruits=['orange','apple','pear','banana','kiwi','apple','banana','apple']
print(fruits.count('apple'))
print(fruits.count('banana'))
print(fruits.count('orange'))

#sort method
fruits.sort()
print(fruits)

number=[3,5,1,9,10]
#number.sort() #it sort the original list 
print(number)


#sorted method

print(sorted(number))
print(sorted(fruits))
print(number)


#copy method 

numbers_copy=number.copy()
print(numbers_copy)


#list comparison

fruits2=fruits=['orange','apple','pear','banana','kiwi','apple','banana','apple']
fruits3=['orange','apple','banana','kiwi','banana','apple']
print(fruits2==fruits3)
print(fruits2 is fruits3)