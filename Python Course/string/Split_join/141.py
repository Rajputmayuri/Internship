"""Q141. Write a program that reverses each word in a sentence while
maintaining the word order. For example, "Hello World" should become
"olleH dlroW"""

my_string = "Hello World"
words = my_string.split()
result = " ".join(i[::-1] for i in words)
print(result)
