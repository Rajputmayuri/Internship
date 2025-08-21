"""Q38. Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are dierent."""

n1 = int(input("Enter 1st number="))
n2 = int(input("Enter 2nd number="))
n3 = int(input("Enter 3rd number="))
if n1 == n2 or n1 == n3 or n2 == n3:
    if n1 > n2 and n1 > n3:
        print(n1, "is large")
    elif n2 > n1 and n2 > n3:
        print(n2, "is large")
    else:
        print(n3, "is large")
else:
    print("Enter different number")
