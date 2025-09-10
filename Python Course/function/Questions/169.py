"""Q169. Write a function that takes an integer and
prints whether it is a prime number."""


def prime_number():
    factors = 0
    num = int(input("Enter number="))
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


prime_number()
