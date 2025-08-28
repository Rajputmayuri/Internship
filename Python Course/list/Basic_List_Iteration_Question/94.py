"""Q94. Print all the odd numbers present in the list."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_list:
    if i % 2 != 0:
        print(i, end=" ")
