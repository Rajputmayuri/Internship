"""Q133. Ask a string from user. Count the number of uppercase and
lowercase characters in that String."""

n = input("Enter string=")
uppercase = 0
lowercase = 0

for ch in n:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
print("Number of uppercase in string :", uppercase)
print("Number of lowercase in string :", lowercase)
