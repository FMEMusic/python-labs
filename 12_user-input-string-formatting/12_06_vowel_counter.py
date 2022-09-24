# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

script = input("Please input a string, I will count the vowels.>>>")
vowel_count = ''
vowel_list = ["a", "e", "i", "o","u"]
for vowels in script:
    if vowels in vowel_list:
        vowel_count += vowels
  

print(f"The vowel count in your input string is {len(vowel_count)}") 

script = input("Please input a string, I will count the vowels.>>>")
vowel_count = ''
for vowels in script:
    if vowels == "a":
        vowel_count += vowels
    elif vowels == "o":
        vowel_count += vowels
    elif vowels == "i":
        vowel_count += vowels
    elif vowels == "u":
        vowel_count += vowels
    elif vowels == "e":
        vowel_count += vowels

print(f"The vowel count in your input string is {len(vowel_count)}") 

script = input("Please input a string, I will count the vowels.>>>")
vowel_count = ''
vowel = ["a", "e", "i", "o","u"]
for vowels in script:
    if vowels == vowel:
        vowel_count += vowels
  

print(f"The vowel count in your input string is {len(vowel_count)}") 
