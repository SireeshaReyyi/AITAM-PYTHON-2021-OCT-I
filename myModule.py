import random

def guessTheNumber():
    n = random.randint(1,10)

    while True:
        user_input = int(input())

        if user_input==n:
            print("you won!")
        else:
            print("try again :(")
            continue
    return