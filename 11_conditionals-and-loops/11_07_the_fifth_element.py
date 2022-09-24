# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...
lst=[]
for numbers in range(1,1000):
    if numbers % 5 == 0:
        lst.append(numbers)
print(lst)