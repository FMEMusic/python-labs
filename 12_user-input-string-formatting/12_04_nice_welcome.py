
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

# Ask the user to input their name. Then print a nice welcome message
name = input("Please enter your name!:")
split_name = name.split()
first_name = split_name[0]
countOfWords = len(name.split())

if countOfWords > 1:
    print(f"Welcome to my script {first_name}, your name is really cool")
else:
    print(f"Welcome to my script {name}, thanks for joining")


