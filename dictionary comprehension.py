# dictionary comprehension
square1={k:k**2 for k in range(1,11)}
print(square1)

# count word
stri="harshit"
word_count={char: stri.count(char) for char in stri}
print(word_count)

#dictionary if else
odd_even={i: ('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)