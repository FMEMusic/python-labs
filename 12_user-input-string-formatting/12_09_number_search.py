# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user_input= int(input("Input a number between 0 and 1,000,000-->>"))

while user_input not in range (0,1000000):
    user_input= int(input("Input a number between 0 and 1,000,000-->>"))        
    if user_input in range(0,1000000):
        break
print(f"Hey you gave a good number! {user_input}")



