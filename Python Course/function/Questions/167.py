"""Q167. Write a function that accepts an integer
and print whether it is odd or even."""


def even_odd():
    num = int(input("Enter a number="))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_odd()
