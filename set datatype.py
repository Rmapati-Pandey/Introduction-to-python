#set data type
#unordered collection of unique items


s={1,2,3}
#print(s[1])# no indexing in sets

#removing duplicated
l=[1,2,3,4,3,4,5,6,74,4,6,7,4,4,6,6,7,8,8]
s2=set(l)
print(s2)


print()
print()


s1={1,2,3,4}
s1.add(4)
s1.add(5)
s1.add(4)
print(s1)
s1.remove(3)
print(s1)
# if element which is to be removed is not present 
# it showk key error
#example: s1.remove(10)
s2={1,2,3,4,5}
s2.discard(3)
print(s2)
s2.discard(10)
print(s2)# if element which is to be removed is not present then discard does not affect and does not shows error 



print()
print()


s3={1,2,3,4,5}
print(s3)
s3.clear()
print(s3) #set()

print()
print()

s4={1,2,3,4,5}
s5=s4.copy()
print(s5)

for items in s4:
    print(items)

s1={1,2,3,4}
s2={3,4,5,6}
#union
#intersection(|)
#{1,2,3,4,5,6}

union_set=s1 | s2
print(union_set)

intersection_set=s1 & s2
print(intersection_set)


