# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random

num = int(input("Insert your guess here >>>"))

while num != random.randint(1,10):
    print("Guess again")
    int(input("Insert your guess here >>>"))
else:
    print("Congrats you won!")