# Print the total number of vowels that are used in the lorem ipsum text.

from operator import contains


lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""
characters = ''
for letters in lorem_ipsum:
    if letters == "a":
        characters += letters
    elif letters == "i":
        characters += letters
    elif letters == "o":
        characters += letters 
    elif letters == "e":
        characters += letters
    elif letters == "u":
        characters += letters

        
print(len(characters))
characters = ''
for letters in lorem_ipsum:
    if letters == "a"== "i" :
        characters+=letters
print(len(characters))