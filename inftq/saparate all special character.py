import re
input_str=input()
#digits=list(set(re.findall('\d',input_str)))
digits=[i for i in set(input_str) if i.isdigit()]
digits.sort()
digits.reverse()

Number=int("".join(digits))
if Number%2==0:
    print(Number)
else:
    length=len(digits)
    for i in range(length-1,0,-1):
        if int(digits[i])%2==0:
            a=digits[i]
            digits.remove(a)
            digits.insert(length-1,a)
            even=int("".join(digits))
            print(even)
            break
    else:
        print(-1)

