"""Q117. Make a program that takes a list of 
integers and returns the product
of all the elements."""

my_list = [1, 2, 3, 4, 5]
prod = 1

for i in my_list:
    prod *= i
print(prod)
