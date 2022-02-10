name,age=input("Enter your name: ").split(",")
age=int(age)
if age>10 and (name[0]=='a'or name[0]=='A') :
    print("You can watch Coco Movie!!!")
else:
    print("You can not watch coco Movie")