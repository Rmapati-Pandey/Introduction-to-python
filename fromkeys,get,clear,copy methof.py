#fromkeys
#d={'name':'unknown','age':'unknown'}
# list
d=dict.fromkeys(['name','age','height'],'unknown')
print(d)
print()
print()
# tuple
d=dict.fromkeys(('name','age','height'),'unknown')
print(d)
print()
print()

# string
d=dict.fromkeys("abc",'unknown') # {a:'',b:''}
print(d)
print()
print()

d=dict.fromkeys(range(1,6),'unknown')
print(d)
print()
print()


d=dict.fromkeys(['name','age'],['unknown','unknown'])
print(d)
print()
print()



#get method

di={'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}
#print(di['names']) #shows error when key is not present 

print(di.get('college'))#when college not pesent in dictionary then return none
print()
print()

# one way
if 'names' in di:
    print("Yes")
else:
    print("no")

print()
print()

# second way
if d.get('names'):
    print('presengt')

else:
    print("Not present")

print()
print()


#clear method

#di.clear()
#print(di)

#copy method

# deep copy
d1=di.copy()
print(d1.popitem())
print(di)
print(d1)

# shallow copy
d1=di  #it means both di and d1 are same so whatever operation performed on d1 will reflect on di also  
print(d1.popitem())
print(di)
print(d1)
print()
print()

