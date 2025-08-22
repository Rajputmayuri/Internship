"""Q64. Ask to numbers x and y from the user. If x<y then print all the
numbers from x to y, but if y<x then print all the numbers from y to x."""

x = int(input("Enter a value for x="))
y = int(input("Enter a value for y="))
if x < y:
    for i in range(x, y+1):
        print(i)
elif x>y:
    for i in range(x, y-1,-1):
        print(i)
else:
    print(x)
