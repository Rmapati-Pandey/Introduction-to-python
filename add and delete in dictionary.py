user_info={
'name':'rmapati',
'age':22,
'fav_movies':['A','B','C'],
'fav_tunes':['E','F','G']
}


# how to add data

user_info['fav_songs']=['song1','song2']
print(user_info)


print()
print()
#pop method

popped_items=user_info.pop('fav_tunes')#provide atleast one item
print(f"popped item is {popped_items}")
print(user_info)
print(type(popped_items))# returning list type because fav tunes values are is list type 



print()
print()
popped_items=user_info.pop('name')#provide atleast one item
print(f"popped item is {popped_items}")
print(user_info)
print(type(popped_items))# returning string type because names values are is list type 



