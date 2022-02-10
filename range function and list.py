#range method 
numbers=list(range(1,11))
print(numbers)
numbers.pop() #stored the poped values
print(numbers.pop())
print(numbers)

#index method

print(numbers.index(1))

#xyz.index(element,from,till)
print(numbers.index(1,3)) #lelement =1 start finding from=3
print(numbers.index(1,11,14))
