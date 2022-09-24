# Using a `for` loop, print out all odd numbers from 1 to 100.
odds = []
for numbers in range(1,100):
   if numbers % 2 != 0:
      odds.append(numbers)
print(odds)
