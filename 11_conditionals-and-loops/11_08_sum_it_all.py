# Using a loop, sum all numbers from the `start` to the `stop` number.
# The sequence should consist only of integers from 1 to 100.
# The output of your calculation should look like this:
#
#      The sum is: 5050
start = 1
stop = 100
li=[]
for numbers in range(start-1, stop):
   numbers = numbers + 1
   li.append(numbers)
print(f"The sum is {sum(li)}") 



total = 0
for i in range(start,stop+1):
   total += i
print(total)



