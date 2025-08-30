"""Q120. Write a program that swaps the first 
and last elements of a given list."""

my_list = [89, 43, 12, 54, 80, 40, 67]

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
