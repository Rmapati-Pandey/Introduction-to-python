name=input("please enter your name ")
#name.count("h"), name.count(name[0])
#name.count("a"), name.count(name[1])
#name.count("r"), name.count(name[2])
#name.count("s"), name.count(name[3])
#name.count("h"), name.count(name[4])
#name.count("i"), name.count(name[5])
#name.count("t"), name.count(name[6])


#counting each character frequency

i=0
temp_var=""
while i<len(name):
    if name[i] not in temp_var :
        temp_var+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1

