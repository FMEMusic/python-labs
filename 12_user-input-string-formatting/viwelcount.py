script = input("Please input a string, I will count the vowels.>>>")
vowel_count = ''
vowel_list = ["a", "e", "i", "o","u"]
for vowels in script:
    if vowels in vowel_list:
        vowel_count += vowels
  

print(f"The vowel count in your input string is {len(vowel_count)}") 