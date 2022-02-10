user_info={
'name':'rmapati',
'age':22,
'fav_movies':['A','B','C'],
'fav_tunes':['E','F','G']
}

more_info={'state':'haryana','hobbies':['coding','reading','guitar']}
user_info.update(more_info)
print(user_info)


print()
print()
more_info={'name':'amit', 'state':'haryana','hobbies':['coding','reading','guitar']}
user_info.update(more_info)
print(user_info)

# name will override in method by update 
