prime_list = []

for numbers in range(1,1001): # for tested numbers between 1 to 1001 do the following:
    for i in range(2, numbers): # for the tested numbers, iterate  between 2 and the value of the number
        if numbers % i == 0: # if a tested number is divided by iterated 
            break
    else:
        prime_list.append(numbers) # append the list with the numbers that dont have a modulo of 0

print(prime_list) # print the list 