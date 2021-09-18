# Binary search
# The goal of binary search is to search whether a given number is present in the string or not.
# Topics: list,sorting,searching
# Hint: First Check whether it is present in the middle or not then check for front and rear.

import string
import numpy as np

string_length = int(input("enter the required string length....."))
all_characters = string.digits + string.ascii_lowercase
random_string = ''.join(np.random.choice([char for char in all_characters], string_length, True))
print(random_string)

contains_digit = any(map(str.isdigit, random_string))

print(contains_digit)
