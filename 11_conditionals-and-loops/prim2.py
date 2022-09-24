prime = []
for number in range (1,1001):  
      
    for i in range (2, number):  
        if (number % i) == 0:  
            break  
    else:  
        prime.append(number) 
print(prime)
