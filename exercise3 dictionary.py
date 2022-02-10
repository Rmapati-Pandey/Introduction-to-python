# user input ans store in dictionary

user={}
name=input('what is your name: ')
age=int(input('what is your age: '))
fav_movies=input('your fav movies saparated by : ').split(',')
fav_song=input('your fav song saparated by : ').split(',')

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_song']=fav_song
print()
print()
print(user)


print()
print()
print()
print()


# or

for key,value in user.items():
    print(f"{key}:{value}")






