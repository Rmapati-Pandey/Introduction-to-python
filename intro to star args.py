# def total(a,b):
#     return a+b
# print(total(3,4))
# #print(total(3,4,10)#error typeerroe

# def all_total(*args):
#     print(args)
#     #args convert input to tuples and pass it to the inner function element

# all_total=(1,2,3,4,5,65)
 


def total(a,b):
    return a+b

def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total

print(all_total(1,2,3,4,5,6))



def multiply_nums(*args):
    multiply=1
    for i in args:
        multiply*=i

    return multiply
print(multiply_nums(1,2,3,4,5))


def multiply_nums(nums,*args):
    multiply=1
    for i in args:
        multiply*=i

    return multiply
print(multiply_nums(2,2,3))

#output =6 because 2 is not part of args


def multiply_nums(*args):
    multiply=1
    for i in args:
        multiply*=i

    return multiply
print(multiply_nums(2,2,3))


def multiply_nums(nums,*args):
    multiply=1
    for i in args:
        multiply*=i

    return multiply
print(multiply_nums())  # when nothing to pass ans num is in funciton call then there should be on value which has to be passed 

#always write num before *args else all element pass to args as a tuple ans type errror  genrated

def func(**kwargs): #kwargs converts input to dictionary
    for k,v in kwargs.items():
        print(f"{k} : {v}")
    print(kwargs)
   
func(first_name='Harshit',last_name='Vashishtha')














