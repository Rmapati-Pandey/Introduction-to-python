n=input()
o=""
for i in n:
    if i not in o:
        o+=i
print(o[::-1])



string=input()
d=list(dict.fromkeys(string))
d.reverse()
print(d)
print("".join(d))