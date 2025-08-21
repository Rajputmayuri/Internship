"""Q.32. Ask 4 numbers from user. Make sure all the numbers entered by user
are dierent. Print which number is the smallest."""

n1 = int(input("Enter the first number="))
n2 = int(input("Ente the second number="))
n3 = int(input("Enter the third number="))
n4 = int(input("Enter the fourth number="))
if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print("Please enter unique numbers")
elif n1 < n2 and n1 < n3 and n1 < n4:
    print(f"{n1} is smaller")
elif n2 < n1 and n2 < n3 and n2 < n4:
    print(f"{n2} is smaller")
elif n3 < n1 and n3 < n2 and n3 < n4:
    print(f"{n3} is smaller")
else:
    print(f"{n4} is smaller")
