"""Q24. Write a program that takes a character as input and prints whether
it's a vowel or a consonant. (Multiple OR will be used)"""

char = str(input("Enter a character="))
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"{char} is a Vowels")
else:
    print(f"{char} is a Consonant")
