from numpy import true_divide


def is_even(a):
    if a%2==0:
        return True
    else:
        return False

ans=lambda a : a%2==0
print(ans(4))

last_char=lambda s: s[-1]
print(last_char('akidjn'))

# lambda with if and else

def fun(s):
    if(len(s)>5):
        return True
    return False

func=lambda s: True if len(s)>5 else False
func=lambda s: len(s)>5 #its also same as above

print(func('absjndkjn'))