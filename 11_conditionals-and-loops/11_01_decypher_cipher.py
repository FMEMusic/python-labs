# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

from curses.ascii import isalpha


secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ''

for character in secret:
    if character.isalpha():
     solution += character
print(solution)