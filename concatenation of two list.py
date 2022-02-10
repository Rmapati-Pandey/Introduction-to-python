fruits1=['grapes', 'apples']
#fruits1.insert(2,"grapes")
#print(fruits1)


fruits2=['mango','orange']
fruits=fruits1+fruits1
print(fruits)

#extend method extend whole list to the new 
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

#append extend list by addding whole new list
fruits1.append(fruits2)
print(fruits1)
print(fruits2)


#pop method delete from last element byu deafult else delete the postion we provide 
fruits1.pop()
print(fruits1)


#delete[1]

del fruits[1]
print(fruits1)


#remove deleted the perticular data if available in the list
fruits.remove('apples') 

if 'apples' in fruits:
    print("yes")

