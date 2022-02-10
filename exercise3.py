name,char=input().split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")#case sensitive means during input if we make space after comma then it will not be acceptable
