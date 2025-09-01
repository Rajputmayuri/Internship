"""Q137. Count the number of spaces in a string entered by user."""

n = input("Enter string=")
count_space = 0

for ch in n:
    if ch.isspace():
        count_space += 1
print(count_space)
