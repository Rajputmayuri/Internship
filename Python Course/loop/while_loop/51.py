"""Calculate factorial of a number entered by user
Example :
Enter a number=5
5 factorial = 5*4*3*2*1
output=120"""

num = int(input("Enter a Number :"))
fact = 1
i = 1
while (i <= num):
    fact = num*fact
    num = num-1
i = i+1
print("Factorial =", fact)
