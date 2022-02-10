winning_number=27
user_input=input("guess the number between 1 and 100 : ")
user_input=int(user_input)
if(user_input==winning_number):
    print("YOU WIN!!! \U0001f6002")
else:
    if(user_input<winning_number):
        print("too low")
    else:
        print("Too high")
