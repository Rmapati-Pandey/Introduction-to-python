def nextPalindrome(num):
    numlen=len(str(num))
    isEven=numlen%2==0
    numleft=str(num)[:int(numlen/2)]
    if isEven:
        nextpd=numleft+numleft[::-1]
    else:
        nextpd=numleft+str(num)[int(numlen/2)]+numleft[::-1]

    print(nextpd)

n=input()
nextPalindrome(n)

