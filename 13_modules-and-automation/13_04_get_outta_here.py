# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import random
import sys
guess = input("Insert Negative number here")
while guess != random.randint(1,1000000):
    guess = input("Insert Negative number here")
    if guess == "quit":
        sys.exit()