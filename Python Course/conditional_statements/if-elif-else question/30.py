"""Q30. Write a program to check if the last digit of a number is divisible by 5
or not."""

num = int(input("Enter a number="))
num = num%10
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
