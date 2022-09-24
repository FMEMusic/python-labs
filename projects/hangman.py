# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
print("Guess the secret word. Put one letter at a time. It is the name of a hugging saint. ")
secret_word = "tree"

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
spaces = len(secret_word) * "_ "
print(spaces)

letter = (input("Input one letter at a time. >>>")) 





output_list = list(spaces)
secret_word_list = list(secret_word) 

# Print an explanation to the user

for letter in  secret_word_list:
    #look for letter in secret word, then we subsitute in the right place
    output_index = secret_word_list.index(letter)
    print(output_index)
    output_list[output_index] = letter
    new_word  = " ".join(output_list)
    print(new_word)
    continue

else:
    print("Try again!")




# Allow only single-character alphabetic input

# while True:
#     
#     if len(letter) >= 2:
#         continue
#     else:
#         break
# if letter not in secret_word:
#     print("Try again.")
letter = (input("Input one letter at a time. >>>")) 
if letter in secret_word_list:
    print()
 
# else:
#     print ("a _ _ a")
#     print( "_ m m _")

# Ask for user inputa
# if letter in secret_word:
#     print(f"{letter}")

# else:
#     print("try again")
# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it
