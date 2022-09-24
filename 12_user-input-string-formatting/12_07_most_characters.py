# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string1 = input("Please input your first string---->")
string2 = input("Please input your second string---->")
string3 = input("Please input your third string---->")

len1= len(string1)
len2= len(string2)
len3 = len(string3)
if string1 > string2 and string1 > string3:
    print(f"{len1},{string1}")
elif string2 > string3 and string2 > string1:
    print(f"{len2} , {string2}")
elif string3 > string2 and string3 > string1:
    print(f"{len3} , {string3}" )
