def odd_even(lst):
    even=[]
    odd=[]
    for i in lst:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    
    output=[odd,even]
    return output

   
lst=[1,2,3,4,5,6,7,8,9,10]
print(odd_even(lst))