"""Q38. Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are dierent."""

a = float(input("Enter first number ="))
b = float(input("Enter second number ="))
c = float (input("Enter third number="))

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

