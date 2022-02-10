#why use dictionary?
#because of limitation of list ,list are not enough to represent real data


#dictionaries are unordered collection of data in key:value pair 


# how to create dictionary
user={'name':'harshit','age':24}
print(user)
print(type(user))

print()
print()
# second method to create the dictionary

user1=dict(name='harshit',age=24)
print(user1)


# no indexing in dictionaries
# we use keys to access the dictionary values
# acessing
print(user1['name'])
print(user1['age'])


# anything can be stored in the dictionary

user_info={
'name':'rmapati',
'age':22,
'fav_movies':['A','B','C'],
'fav_tunes':['E','F','G']
}

print(user_info)

# dictionary into dictionary



# how to add data to empty dictionary

user_info2={}
user_info2['name']='pandey'
user_info2['age']=23



print(user_info2)