"""Q132. Ask a string from user. Count how many alphabets are there in that
string."""

a = input("Enter a string=")
count = 0
for ch in a:
    if a.isalpha():
        count += 1
print("Number of alphabets in string :", count)
