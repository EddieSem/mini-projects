# Random password generator
# To create a program that takes a number and generate a random password length of that number.
# Topics: random module, joining strings, taking input
# Hint: Create a string with all characters, then take random characters from it and concatenate each char to make a
# big string.

import random
import string
from operator import itemgetter

all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
password = ''

password_length = int(input("Please enter your required password length......"))
password = ''.join(random.sample(all_characters, password_length))
# for i in random.sample(range(0, 94), password_length):
#     password += ''.join(itemgetter(i)(all_characters))
print(password)
