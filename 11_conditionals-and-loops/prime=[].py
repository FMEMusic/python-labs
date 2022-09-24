prime=[]
for numbers in range(1,1000):
    for i in range(2,numbers):
        if numbers % i == 0:
            break
    else:
        prime.append(numbers)
print(prime)