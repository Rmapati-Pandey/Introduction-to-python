def func(**kwargs): #kwargs converts input to dictionary
    for k,v in kwargs.items():
        print(f"{k} : {v}")
         #print(kwargs)
   
func(first_name='Harshit',last_name='Vashishtha')


#dictionary unpacking
d={'name':'harshit','age':24}
func(**d)

#padk(parameter,args,default parameter,kwargs)