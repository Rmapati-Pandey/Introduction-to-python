#first way
def check_palindrome(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return "Yes"
    else:
        return "false"

name=input()
print(check_palindrome(name))



#2nd way 
def check_palindrome(word):
    if word==word[::-1]:#for reversing the string
        return "Yes"
    return "false"

name=input()
print(check_palindrome(name))


