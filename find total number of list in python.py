from numpy import integer


def countlist(lst):
    count=0
    for i in lst:
        if type(i)==list:
            count+=1
    return count
lst=[1,2,3,[1,2],[3,4]]

print(countlist(lst))