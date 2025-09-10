"""Q168. Write a function that takes three numbers
as parameters and prints the largest among them."""


def large_number(a, b, c):
    if a > b and a > c:
        print(f"{a} is largest number")
    elif b > a and b > c:
        print(f"{b} is largest number")
    else:
        print((f"{c} is largest number"))


large_number(1, 2, 3)
