import random

num = random.randint(1,10)
guess = None
while guess != num:
    guess = input("Guess the number between 1 & 10:")
    guess = int(guess)
    if guess == num:
        print("Congrats you Won!")
        break
    else: print("sorry try again")

