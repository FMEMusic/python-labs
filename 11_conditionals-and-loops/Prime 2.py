# Print out every prime number between 1 and 1000.
numero = range(1,1000)
prime_list = []
for number in numero:
    
    rango=range(2,number) #From where to where should be iterating???
    
    for i in rango:       # print(rango)
        if number % i == 0:
            print("It is not prime")
            break
        else:
            print("It is prime")
            prime_list.append(number)
            break
       