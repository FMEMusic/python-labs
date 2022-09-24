guess =
num = None
while guess != num:
    guess =input("Guess a number between 1 & 10: ")
    guess = int(guess)
    if guess == num:
        print("Congratulations! You Won!")
        break
    else:
        print(f"Nope sorry try again, the number was {num}")