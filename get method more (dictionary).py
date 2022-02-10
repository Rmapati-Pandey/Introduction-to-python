user={'name':'amit','age':24}
print(user.get('college'))

#by default when key not found in dictionary then key return the none value 

# if we want get method to return somthing else
print(user.get('college','not found'))


# more than one keys in dictionary
user1={'name':'amit','age':24,'age':34}
#34 will override the age 24 key in dictionary
print(user1)

user1={'name':'amit','age':34,'age':24}
#24 will override the age 34 key in dictionary
print(user1)
