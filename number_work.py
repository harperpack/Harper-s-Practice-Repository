# This is a program built to help me practice representing numbers in Python

# Explore different arithmetic in Python

import time

print(5 + 3)
print(4.0 * 2)
print(2 ** 3)
print(24 / 3)
print(9.0 - 1)

favorite_number = 8.0

print("Can you guess which is my favorite number?")
# Allow the user time to "catch up" with the program output
time.sleep(2)
# Explore arithmetic within a string output
print("\nI'll give you a hint: I've already printed it " + str(favorite_number - 3) + " times!")
time.sleep(2)
print("Time's up!  My favorite number is " + str(favorite_number) + "!")
print("Disclaimer: I am not particularly partial to any number.")
