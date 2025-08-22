"""Q63. Calculate factorial of a number entered by user.
Example:
Enter a number = 5
Factorial of a number means product of all the numbers from 1 to that
number.
5 factorial = 5 x 4 x 3 x 2 x 1
Output = 120"""

fact = 1
num = int(input("Enter a number="))

for i in range(num, 1, -1):
    fact = fact*num
    num = num-1
print("Factorial is=", fact)
