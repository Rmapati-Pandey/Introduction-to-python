#for removing spaces  we use strip method

name="     Har  shit       "
dots=".............."
print(name+dots)# prints spaces also
print(end="\n")
print(end="\n")
#lstrip remove left spaces
print(name.lstrip()+dots) 
print(end="\n")
print(end="\n")
#rstrip removes right spaces
print(name.rstrip()+dots)
print(end="\n")
print(end="\n")
 #remove all the spaces at both the end
print(name.strip()+dots)
print(end="\n")
print(end="\n")


#remove all the spaces at both the end along with in between
print(name.replace(" ","")+dots)