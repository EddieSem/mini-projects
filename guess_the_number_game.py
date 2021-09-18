# Guess the number game
# The main goal of the project is to create a program that randomly select a number in a range then the user has to guess the number.
# user has three chances to guess the number if he guess correct then a message print saying “you guess right “otherwise a negative message prints.
# Topics: random module, for loop, f strings

import random

lower_limit = 1
upper_limit = 10
user_guess = int

while True:
    print("""\n1. Start the game \n2. Close the game""")
    number = random.randint(lower_limit,upper_limit)
    user_play = int(input("1\nWhat would you like to do? \n\nType [1] to start \nType [2] to close\n"))
    if user_play == 1:
        print("Loading...")
        for i in range(0, 3):
            user_guess = int(input(f"""Guess the number chosen between {lower_limit} and {upper_limit}.........."""))
            if user_guess == number:
                print(f"you guessed right, it's {number}")
                break
        if user_guess != number:
            print(f"Your guess is incorrect the number is {number} \nYou lost the game...... Goodbye!")
            break
    else:
        print("\nClosing... \n\nClosed")
        break
