prime= []
for numbers in range(1,1000): # iterate for numbers between 1 and 1000
    for i in range(2,numbers): #iterate over the range 
        if (numbers % i) == 0:
            break
    else:
         prime.append(numbers)
print(prime)