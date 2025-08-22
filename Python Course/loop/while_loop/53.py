"""Q53. Ask two numbers x and y from user.
if x<y then print all the numbers from x to y,
but if y<x then print all the numbers from y to x"""

x = int(input("Enter a 1st number :"))
y = int(input("Enter a 2nd number :"))
i = x

if (x < y):
    while i <= y:
        print(i, end=' ')
        i = i+1

elif x > y:
    while (i >= y):
        print(i, end=" ")
        i = i-1
else:
    print(x)
