def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
def reverse(l):
    l.reverse()
    return l

numbers=list(range(1,11))
#print(square_list(numbers))
print(reverse(numbers)) 