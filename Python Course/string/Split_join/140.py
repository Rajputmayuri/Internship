"""Q140. Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.

"""
my_string = "python is good"
words = my_string.split()

result = " ".join(i.capitalize() for i in words)
print(result)
