"""Q172. Write a function that takes a string and
prints whether it is a palindrome."""


def palindrome():
    my_string = input("Enter a string=")
    reversed_string = my_string[::-1]
    # reversed_string = "".join(reversed(my_string))
    if my_string == reversed_string:
        print("Palindrome string")
    else:
        print("Not palindrome string")


palindrome()
