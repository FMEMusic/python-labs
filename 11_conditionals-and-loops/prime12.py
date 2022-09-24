prime = []
for numbers in range(0,1001):
        for i in range (2, numbers):
            if (numbers % i) == 0:
                break
        else:
            prime.append(numbers)
print(prime)


