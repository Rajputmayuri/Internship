"""Q71. Ask N from user. N means number of lines.
Then print the follwing patter."""

n = int(input("Enter number="))
for i in range(1, n+1):
    for j in range(1, 6):
        print(i, end=" ")
    print()
