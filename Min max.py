#=[6,60,2]
#print(max(numbers))
#print(min(numbers))

from re import L


def greatest_diff(l):
    return max(l)-min(l)

lst=[6,60,2]
print(greatest_diff(lst))