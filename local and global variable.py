x=5
def fun():
    #global x
    x=7 #local before the globla declaaration
    return x

print(x)
print(fun())
print(x)