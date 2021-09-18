# Dice roll simulator
# The goal is to create a program that will simulate the roll of dice.
# Topics: random module, looping, and if-else
# Hint: Using a random module generate a random number between the range from 1 to 6 when the user wants.

import random

while True:
    print("""1. Roll Dice               2. Exit  """)
    user = int(input("What would you like to do? \nType [1] to roll dice \nType [2] to exit...."))
    if user==1:
        number = random.randint(1,6)
        print("the dice shows................................... " + str(number))
    else:
        break




