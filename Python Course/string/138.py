"""Q138. Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string."""


n = input("Enter string=")
alphabets = 0
digits = 0
spaces = 0
symbols = 0

for ch in n:
    if ch.isalpha():
        alphabets += 1
    elif ch.isalnum():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        symbols += 1
print("alphabets:", alphabets)
print("digits :", digits)
print("spaces :", spaces)
print("symbols :", symbols)
