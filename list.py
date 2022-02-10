number=[1,2,3,4]
print(number)
words=["amit","ankit","jyoti"]
print(words)

mixed=[1,2,3,4,"amit","rahul",None,2.3]
print(mixed)

print(mixed[::-1])
mixed[1]=4

print(mixed)

mixed[1:]='two' #devides the string character by character
print(mixed)

mixed[1:]=["amit","ankit","jyoti"]
print(mixed)