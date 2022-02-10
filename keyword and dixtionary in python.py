user_info={
'name':'rmapati',
'age':22,
'fav_movies':['A','B','C'],
'fav_tunes':['E','F','G']
}
#check if key is present in dictionary
# names key present
if 'name' in user_info:
    print('present')
else:
    print('Not present')


# names key not  present
if 'names' in user_info:
    print('present')
else:
    print('Not present')

#check if key is present in dictionary
#use values with dictionary name
if 'rmapati' in user_info.values():
    print('present')
else:
    print('Not present')

#check for 24
if 24 in user_info.values():
    print('present')
else:
    print('Not present')

#check for list
if ['E','F','G']  in user_info.values():
    print('present')
else:
    print('Not present')

print()
print()
#loops in dictionary
#for keys
for i in user_info:
    print(i)

#for values
print()
print()
for i in user_info.values():  
    print(i)

#directly print without looping
user_info_dictio=user_info.values()
print(user_info_dictio)
print(type(user_info_dictio)) #type id dict values

for i in user_info:  
    print(user_info[i])



#items method(most important)
# [(),(),(),(),()] tuple in list
# [('name', 'rmapati'), ('age', 22), ('fav_movies', ['A', 'B', 'C']), ('fav_tunes', ['E', 'F', 'G'])]
user_items=user_info.items()
print(user_items)
print(type(user_items))


print()
print()
print()
#tuple unpacking
for key,value in user_info.items():
    print(f"key  : {key} ,value : {value}")
