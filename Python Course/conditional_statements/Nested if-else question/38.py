"""Q38. Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are dierent."""

n1 = float(input("Enter first number ="))
n2= float(input("Enter second number ="))
n3= float (input("Enter third number="))

if a==b or b==c or a==c:
    print("Error : All three numbers must be different.")
else:
    if a>b:
        if a>c:
            largest=a
        else:
            largest=c
    else:
        if b>c:
            largest=b
        else:
            largest=c
    print(f"The largest number is :{largest}")
