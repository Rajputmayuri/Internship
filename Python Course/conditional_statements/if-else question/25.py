"""Q25. Write a program that takes two numbers as input and checks if the
first number is divisible by the second"""

n1 = int(input("Enter a 1st number="))
n2 = int(input("Enter a 2nd number="))
if n1 % n2 == 0:
    print(f"{n1} is divisible by {n2}")
else:
    print(f"{n1} is not divisible by {n2}")
    